def getSample(n, file):
    """
    Returns a random sample of size n from items in file.
    :param n: int; sample size
    :param file: str; filename of items to be processed (requires a list of rows)
    :return: str; a sample of n random items from file, formatted as a string
    """
    from random import sample
    return "".join(sample(open(file).readlines(), n))

def main():
    while True:
        try:
            sample_size = int(input("Enter sample size: "))
            break
        except: print("Sample size must be an integer.")
    fh = open("random_sample.txt", "w")
    fh.write(getSample(sample_size, "input.txt"))
    fh.close()
    print("\nGenerated random sample of size {} saved to file random_sample.txt.".format(sample_size))

if __name__ == "__main__":
    main()
