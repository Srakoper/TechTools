def wordNumGenerator():
    """
    Generates a (pseudo)random string of length 8 composed of a word of length 6 with 3 capital characters, and a 2-digit number
    :return: str; random alphanumeric string of length 8
    """
    from random import choice, sample
    random_chars = tuple(sorted(sample(range(6), 3)))
    random_word = choice(open("words.txt").readlines())[:-1]
    random_word_case = ""
    for i in range(len(random_word)):
        if i in random_chars: random_word_case += random_word[i].upper()
        else: random_word_case += random_word[i]
    return random_word_case + str(choice(range(11,99)))

def main():
    from datetime import datetime
    fh = open("random_string.txt", "a")
    fh.write(str(datetime.now()) + " " + wordNumGenerator() + "\n")
    fh.close()
    print("\nGenerated random string saved to file random_string.txt.")

if __name__ == "__main__":
    main()
