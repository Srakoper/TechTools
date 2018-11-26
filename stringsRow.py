def stringsRow():
    """
    Reads data from file and encloses every line in single quotation marks, adds comma at the EOL if not present, then joins lines into a single row.
    Requires input data as a list of rows.
    Writes stringified data to file stringsList.txt.
    """
    fh = open("input.txt")
    lines = fh.readlines()
    fh.close()
    lines_quotes = list()
    for i in range(len(lines)):
        if lines[i] != "\n":
            if i == len(lines) - 1:
                if lines[i][-2] == ",":
                    line_quotes = "'" + lines[i].strip()[:-1] + "' "
                else:
                    line_quotes = "'" + lines[i].strip() + "'"
            else:
                if lines[i][-2] == ",":
                    line_quotes = "'" + lines[i].strip()[:-1] + "', "
                else:
                    line_quotes = "'" + lines[i].strip() + "', "
        if (i + 1) % 1000 == 0:
            lines_quotes.append(line_quotes[:-2] + "\n\n{} VNOSOV\n\n".format(i + 1))
        else:
            lines_quotes.append(line_quotes)
    fh = open("stringsRow.txt", "w")
    for line in lines_quotes: fh.write(line)
    fh.close()
    print("Stringified data saved to file stringsRow.txt.")

def main():
    stringsRow()

if __name__ == "__main__":
    main()
