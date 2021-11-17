from typing import Any

def getDBConnectionData() -> None:
    databases:enumerate = enumerate(("PROD19c", "SIMU19c", "TEST19c"))
    for i, d in databases: print(f"{i + 1} {d}")

def connectDB(database:str, username:str, password:str) -> Any:
    import cx_Oracle as cxO # type: ignore
    if not username.startswith("r_"): username = "r_" + username
    databases:dict = {
        "test19c": {
            "HOST"        : "tvrtvitaora01",
            "PORT"        : 1521,
            "SERVICE_NAME": "igastest"
        },
        "simu19c": {
            "HOST"        : "tvrtvitaora01",
            "PORT"        : 1521,
            "SERVICE_NAME": "igassimu"
        },
        "prod19c": {
            "HOST"        : "csmavitaora01.nlb.si",
            "PORT"        : 1521,
            "SERVICE_NAME": "igasprod_dg"
        }
    }
    try: return cxO.connect(f"{username}/{password}@{databases[database.lower()]['HOST']}:{databases[database.lower()]['PORT']}/{databases[database.lower()]['SERVICE_NAME']}", encoding="UTF-8")
    except cxO.DatabaseError: return "Invalid username and/or password."
    except KeyError: return "Invalid database name."

def importSQL(fileSQL:str, selectors:tuple=None) -> tuple:
    """
    Parses and fetches SQL queries from a given file.
    :param fileSQL: .sql file; file containing SQL queries to parse
    :param selectors: tuple; optional tuple of selectors which SQL queries must contain in description comment in order to be fetched
    :return: tuple; parsed SQL queries as strings
    """
    from re import sub
    fh = open(fileSQL, encoding="utf-8", errors="ignore")
    queries:list = list()
    query:str = f""""""
    selected:bool = False
    finished = False
    for line in fh.readlines():
        if line.startswith("/* SELECT"):
            if selectors:
                selector_found:bool = False
                for selector in selectors:
                    if selector in line:
                        selector_found = True
                        break
                if selector_found:
                    selected = True
                    query += line
                else: selected = False
            else:
                selected = True
                query += line
        elif line.rstrip().endswith(";"):
            if selected:
                query += line
                finished = True
                selected = False
            else: finished = True
        else:
            if line.rstrip() and not line.rstrip().startswith("*") and selected:
                query += line

        if finished:
            if query: queries.append(sub(r"'?&(\w+)'?", r":\1", query.rstrip()[:-1]))
            query = f""""""
            finished = False
    return tuple(queries)

def getQueryResults(db:str, username:str, password:str, query:str, variables:dict=None, expressions:dict=None) -> tuple:
    """
    Returns results of an SQL query.
    :param db: str; database name
    :param username: str; username for database access
    :param password: str; password for database access
    :param query: str; an SQL query
    :param variables: dict; an optional map of replacements (to_replace -> replacement) to plug into query
    :param expressions: dict; and optional array of expressions (to_replace -> replacement) to plug into query
    :return: tuple; array of header and array of results
    """
    from cx_Oracle import Error as cxOE
    conn:Any = connectDB(db, username, password)
    if type(conn) == str:
        print(conn)
        exit()
    cursor = conn.cursor()
    try:
        query_to_run:str = query
        results:list = list()
        if expressions:
            header:list = list()
            result:list = list()
            for key, value in expressions.items():
                if key in query_to_run:
                    for v in value:
                        replacement:str = ",".join([str(item) for item in v])
                        query_to_run = query_to_run.replace(key, replacement)
                        if variables: query_result = cursor.execute(query_to_run, variables)
                        else: query_result = cursor.execute(query_to_run)
                        if not header: header = [str(item[0]) for item in query_result.description]
                        result.extend(query_result.fetchall())
                        query_to_run = query # resets modified query to original after every loop
            results.append(tuple(header))
            results.append(result)
        else:
            if variables: query_result = cursor.execute(query_to_run, variables)
            else: query_result = cursor.execute(query_to_run)
            header:list = [str(item[0]) for item in query_result.description]
            results.append(tuple(header))
            results.append(query_result.fetchall())
        return tuple(results)
    except cxOE as e1:
        print(e1)
        cursor.close()
        conn.close()
        exit()
    except Exception as e2:
        print("A non-database error occurred.", e2)
        cursor.close()
        conn.close()
        exit()
    finally:
        cursor.close()
        conn.close()