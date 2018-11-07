def randomStringGenerator(l):
    """
    Generates a (pseudo)random alphanumeric string of length l.
    @param l: int; lenth of random string to generate
    @return: str, random alphanumeric string of length l
    """
    from random import choice
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    randomString = ""
    for i in range(l):
        randomString += choice(chars)
    return randomString

def main():
    from datetime import datetime
    while True:
        length = input("Enter length of random string: ")
        if length.isdigit(): break
        else: print("Enter a valid number.\n")
    fh = open("random_string.txt", "a")
    fh.write(str(datetime.now()) + " " + randomStringGenerator(int(length)) + "\n")
    fh.close()
    print("\nGenerated random string saved to file random_string.txt.")
    
if __name__ == "__main__":
    main()
