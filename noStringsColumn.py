def stringsColumn():
    """
    Reads data from file and adds comma at the EOL if not present.
    Writes data to file noStringsColumn.txt.
    """
    fh = open("input.txt")
    lines = fh.readlines()
    fh.close()
    lines_no_quotes = list()
    for i in range(len(lines)):
        if lines[i]:
            if i != len(lines) - 1:
                if lines[i][-2:] != ",\n": lines_no_quotes.append(lines[i][:-1] + ",\n")
                else: lines_no_quotes.append(lines[i])
            else:
                if lines[i][-2:] == ",\n": lines_no_quotes.append(lines[i][:-2] + ",\n")
                else: lines_no_quotes.append(lines[i])
    fh = open("noStringsColumn.txt", "w")
    for line in lines_no_quotes: fh.write(line)
    fh.close()
    print("Data saved to file noStringsColumn.txt.")
        
def main():
    stringsColumn()

if __name__ == "__main__":
    main()
