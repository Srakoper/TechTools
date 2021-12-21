import DButil as DBu
from datetime import datetime, timedelta
from GeneralUtil import generateFile, getColumnData, isDateInLeapYear
from XLSXutil import saveToXLSX

def main():
    db:str = "PROD19c"
    username:str = "r_MihelicD"
    password:str = "Laskolasko!2"
    claim:str = input("Zahtevek: ")
    today:str = datetime.today().strftime('%Y-%m-%d')
    if not claim.startswith("#"): claim = "#" + claim
    path_SQL:str = "D:\SQL Commands\SELECT\Police NLB Vita Nezgoda Junior z napačnim datumom konca zavarovanja.sql"
    path_file:str = "D:\Scripts"
    queries:tuple = DBu.importSQL(path_SQL)
    incorrect_policies:tuple = DBu.getQueryResults(db, username, password, queries[0])
    if not incorrect_policies[1]:
        print("\nNo viable NLB Vita Nezgoda Junior policies with incorrect end dates found.")
        exit()
    policy_nos:tuple = tuple(f"'{p}'" for p in getColumnData(incorrect_policies[1], 4))
    pol_ref_nos:tuple = getColumnData(incorrect_policies[1], 1)
    incorrect_proposals:tuple = DBu.getQueryResults(db, username, password, queries[1], None, {"/* policy_nos */": (policy_nos,)})
    incorrect_pol_benfs:tuple = DBu.getQueryResults(db, username, password, queries[2], None, {"/* pol_ref_nos */": (pol_ref_nos,)})
    updates:list = list()
    print("Police NLB Vita Nezgoda Junior z napačnim datumom konca zavarovanja:\n")
    for i in range(len(incorrect_policies)):
        if i == 0: print(f"{incorrect_policies[i][4]} {incorrect_policies[i][1]} {incorrect_policies[i][6]} {incorrect_policies[i][10]} {incorrect_policies[i][11]} {incorrect_policies[i][12]:>10} {incorrect_policies[i][31]:>4}")
        else:
            for row in incorrect_policies[i]:
                print(f"{row[4]:>9} {row[1]:>10} {row[6]:>6} {row[10]:>8} {row[11].strftime('%d.%m.%Y'):>10} {row[12].strftime('%d.%m.%Y')} {row[31]:>4}")
                if row[10].upper() in ('A', 'P', 'U'):
                    if isDateInLeapYear(row[11], True): correct_date:datetime = row[11] + timedelta(days=365)
                    else: correct_date:datetime = row[11] + timedelta(days=364)
                    if row[31] == 12:
                        updates.append(f"UPDATE policy\n   SET END_DATE = '{correct_date.strftime('%d.%m.%Y')}'\n WHERE POLICY_NO = '{row[4]}';")
                        updates.append(f"UPDATE pol_benf\n   SET END_DATE = '{correct_date.strftime('%d.%m.%Y')}'\n WHERE POL_REF_NO = {row[1]};")
                    else:
                        updates.append(f"UPDATE policy\n   SET END_DATE = '{correct_date.strftime('%d.%m.%Y')}',\n       TERM = 12\n WHERE POLICY_NO = '{row[4]}';")
                        updates.append(f"UPDATE pol_benf\n   SET END_DATE = '{correct_date.strftime('%d.%m.%Y')}',\n       TERM = 12\n WHERE POL_REF_NO = {row[1]};")
                    updates.append(f"UPDATE e2_ponudba\n   SET DATUM_KONCA_ZAVAROVANJA = '{correct_date.strftime('%d.%m.%Y')}'\n WHERE SIFRA_PONUDBE = '{row[4]}';")
    if updates:
        if generateFile(path_file, f"{claim} SQL NLB Vita Nezgoda Junior popravek datumov konca zavarovanja {today}.txt", updates, "\n\n"): print(f"\nCorrections saved as SQL UPDATE commands to file '{claim} SQL NLB Vita Nezgoda Junior popravek datumov konca zavarovanja {today}.txt'")
        else: print("\nError when saving corrections to file")
        print(saveToXLSX(path_file, f"{claim} backup {today}.xlsx", (incorrect_policies, incorrect_proposals, incorrect_pol_benfs), ("policy", "e2_ponudba", "pol_benf")))
    else: print("\nNo viable NLB Vita Nezgoda Junior policies with incorrect end dates found")
if __name__ == "__main__": main()