def compareValues(file1, file2):
    """
    Compares values from two lists and returns possible missing values in either list.
    :param file1: str; filename of values from list 1, requires values as list of rows
    :param file2: str; filename of values from list 2, requires values as list of rows
    """
    lines1 = open(file1).readlines()
    lines2 = open(file2).readlines()
    missing1 = list()
    missing2 = list()
    for line in lines1:
        if line not in lines2: missing2.append(line.rstrip())
    for line in lines2:
        if line not in lines1: missing1.append(line.rstrip())
    print("{} values found in input 1 but missing in input 2: \n".format(len(missing2)))
    for missing in missing2: print(missing)
    print("\n{} values found in input 2 but missing in input 1: \n".format(len(missing1)))
    for missing in missing1: print(missing)

def main():
    compareValues("input.txt", "compareWith.txt")

if __name__ == "__main__":
    main()