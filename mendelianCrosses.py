def addAlleles() -> dict:
    trait:str = input("Trait: ")
    A:str = input("Allele label for dominant phenotype: ")
    A_pheno:str = input("Associated dominant phenotype: ")
    a: str = input("Allele label for recessive phenotype: ")
    a_pheno: str = input("Associated recessive phenotype: ")
    return ({trait: {1: {"label": A,
                         "pheno": A_pheno}},
                    {0: {"label": a,
                         "pheno": a_pheno}}})

def main():
    alleles1:list = list()
    genotype1:list = list()
    alleles2: list = list()
    genotype2: list = list()
    while True:
        print("\nPARENT 1 ALLELES AND TRAITS")
        for allele_pair in alleles1:
            for allele in allele_pair:
                for k, v in allele.items():
                    print(f"{v['label']}: {v['trait']}, {v['pheno']} ({'dominant' if k else 'recessive'})")
        print(genotype1)
        print("\nPARENT 2 ALLELES AND TRAITS")
        for allele_pair in alleles2:
            for allele in allele_pair:
                for k, v in allele.items():
                    print(f"{v['label']}: {v['trait']}, {v['pheno']} ({'dominant' if k else 'recessive'})")
        print(genotype2)
        while True:
            choice = input("{} {} {} {} {}"
                           .format("\n\n1: add allele pair for parent 1",
                                   "\n2: add allele pair for parent 2",
                                   "\n3: calculate all F1 offspring allele combinations sorted by phenotype",
                                   "\n4: calculate specific F1 offspring allele combinations sorted by phenotype",
                                   "\n\nEnter number or X for exit: "))
            if choice == "X" or choice == "x":
                quit()
            else:
                try:
                    number = int(choice)
                    if number == 1:
                        allele_pair:tuple = addAlleles()
                        alleles1.append(allele_pair)
                        genotype1.append((allele_pair[0][1]["label"], allele_pair[1][0]["label"]))
                        break
                    if number == 2:
                        while True:
                            choice:str = input("\nCopy alleles and traits from parent 1? (Y/N) ")
                            if choice in ("Y", "y", "N", "n"): break
                            else: print("\nEnter a valid choice.")
                        if choice.lower() == 'y':
                            alleles2 = alleles1
                            genotype2 = genotype1
                            break
                        else:
                            allele_pair:tuple = addAlleles()
                            alleles2.append(allele_pair)
                            genotype2.append((allele_pair[0][1]["label"], allele_pair[1][0]["label"]))
                            break
                    if number == 3:
                        combinations:list = list()
                        for allele_pair in alleles1:
                            for allele in allele_pair:
                                key:int = list(allele.keys())[0]
                                combination = [allele[key]["label"]]
                                for allele_pair in alleles2:
                                    for allele in allele_pair:
                                        key:int = list(allele.keys())[0]
                                        combination.append(allele[key]["label"])
                                combinations.append(combination)
                        print(combinations)
                        break
                    else:
                        print("\nEnter a valid number.")
                except ValueError:
                    print("\nEnter a valid choice.")
if __name__ == "__main__": main()