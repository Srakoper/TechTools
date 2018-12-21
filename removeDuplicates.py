def removeDuplicates(file):
    """
    Sorts input items, removes duplicates and returns a list of sorted unique items, formatted as a string.
    :param file: str; filename of items to be processed (requires a list of rows)
    :return: str; a list of sorted unique items from file, formatted as a string
    """
    uniques = list()
    lines = open(file).readlines()
    for line in lines:
       if line not in uniques: uniques.append(line)
    return "".join(uniques)

def main():
    fh = open("removed_duplicates.txt", "w")
    fh.write(removeDuplicates("input.txt"))
    fh.close()
    print("\nUnique items saved to file removed_duplicates.txt.")

if __name__ == "__main__":
    main()