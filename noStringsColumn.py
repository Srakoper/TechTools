def noStringsColumn():
    """
    Reads data from file and adds comma at the EOL if not present.
    Requires input data as a list of lines.
    Writes data to file noStringsColumn.txt.
    """
    fh = open("input.txt")
    lines = fh.readlines()
    fh.close()
    lines_no_quotes = list()
    for i in range(len(lines)):
        if lines[i] != "\n":
            if i != len(lines) - 1:
                if lines[i][-2:] != ",\n": lines_no_quotes.append(lines[i][:-1] + ",\n")
                else: lines_no_quotes.append(lines[i])
            else:
                if lines[i][-2:] == ",\n": lines_no_quotes.append(lines[i][:-2] + ",\n")
                else: lines_no_quotes.append(lines[i])
        if (i + 1) % 1000 == 0: lines_no_quotes.append("\n\n{} VNOSOV\n\n".format(i + 1))
    fh = open("noStringsColumn.txt", "w")
    for line in lines_no_quotes: fh.write(line)
    fh.close()
    print("Data saved to file noStringsColumn.txt.")
        
def main():
    noStringsColumn()

if __name__ == "__main__":
    main()
