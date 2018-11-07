def stringsColumn():
    """
    Reads data from file and encloses every line in single quotation marks, adds comma at the EOL if not present.
    Writes stringified data to file stringsColumn.txt.
    """
    fh = open("input.txt")
    lines = fh.readlines()
    fh.close()
    lines_quotes = list()
    for i in range(len(lines)):
        if lines[i]:
            if i == len(lines) - 1:
                if lines[i][-2] == ",": line_quotes = "'" + lines[i].strip()[:-1] + "'\n"
                else: line_quotes = "'" + lines[i].strip() + "'"
            else:
                if lines[i][-2] == ",": line_quotes = "'" + lines[i].strip()[:-1] + "',\n"
                else: line_quotes = "'" + lines[i].strip() + "',\n"
        lines_quotes.append(line_quotes)
    fh = open("stringsColumn.txt", "w")
    for line in lines_quotes: fh.write(line)
    fh.close()
    print("Stringified data saved to file stringsColumn.txt.")
        
def main():
    stringsColumn()

if __name__ == "__main__":
    main()
