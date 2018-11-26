def stringsColumn():
    """
    Reads data from file and encloses every line in single quotation marks, adds comma at the EOL if not present.
    Requires input data as a list of lines.
    Writes stringified data to file stringsColumn.txt.
    """
    fh = open("input.txt")
    lines = fh.readlines()
    fh.close()
    lines_quotes = list()
    for i in range(len(lines)):
        if lines[i] != "\n":
            if i == len(lines) - 1:
                if lines[i][-2] == ",": line_quotes = "'" + lines[i].strip()[:-1] + "'\n"
                else: line_quotes = "'" + lines[i].strip() + "'"
            else:
                if lines[i][-2] == ",": line_quotes = "'" + lines[i].strip()[:-1] + "',\n"
                else: line_quotes = "'" + lines[i].strip() + "',\n"
        if (i + 1) % 1000 == 0: lines_quotes.append(line_quotes[:-2] + "\n\n{} VNOSOV\n\n".format(i + 1))
        else: lines_quotes.append(line_quotes)
    fh = open("stringsColumn.txt", "w")
    for line in lines_quotes: fh.write(line)
    fh.close()
    print("Stringified data saved to file stringsColumn.txt.")
        
def main():
    stringsColumn()

if __name__ == "__main__":
    main()
