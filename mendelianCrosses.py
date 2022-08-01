def addAlleles() -> tuple:
    trait:str = input("\nTrait: ")
    a_all:str = input("Allele 1 label: ")
    a_pheno:str = input("Phenotype 1: ")
    while True:
        a_dom:str = input("Phenotype 1 dominant? (Y/N) ")
        if a_dom in ("Y", "y", "N", "n"): break
        else: print("\nEnter a valid choice.")
    while True:
        choice:str = input("Alleles homozygous? (Y/N) ")
        if a_dom in ("Y", "y", "N", "n"): break
        else: print("\nEnter a valid choice.")
    if choice.lower() == 'y':
        b_all:str = a_all
        b_pheno:str = a_pheno
        b_dom:str = a_dom
    else:
        b_all:str = input("Allele 2 label: ")
        b_pheno:str = input("Phenotype 2: ")
        if a_dom.lower() == 'y': b_dom:str = 'n'
        else: b_dom:str = 'y'
    return ({"label": a_all,
             "pheno": a_pheno,
             "dominant": 1 if a_dom.lower() == "y" else 0,
             "trait": trait},
            {"label": b_all,
             "pheno": b_pheno,
             "dominant": 1 if b_dom.lower() == "y" else 0,
             "trait": trait})

def addAllelesGenotypes() -> tuple:
    allele_pair:tuple = addAlleles()
    alleles:tuple = (allele_pair[0], allele_pair[1])
    genotype:tuple = (alleles[0]["label"], alleles[1]["label"])
    return (alleles, genotype)

def main():
    alleles_pairs1:list = list()
    genotype1:list = list()
    alleles_pairs2:list = list()
    genotype2:list = list()
    while True:
        print("\nPARENT 1 TRAITS & ALLELES")
        for allele_pair in alleles_pairs1:
            for allele in allele_pair: print(f"{allele['label']}: {allele['trait']}, {allele['pheno']} ({'dominant' if allele['dominant'] else 'recessive'})")
        print(genotype1)
        print("\nPARENT 2 TRAITS & ALLELES")
        for allele_pair in alleles_pairs2:
            for allele in allele_pair: print(f"{allele['label']}: {allele['trait']}, {allele['pheno']} ({'dominant' if allele['dominant'] else 'recessive'})")
        print(genotype2)
        while True:
            choice = input("{} {} {} {} {}"
                           .format("\n\n1: add allele pair for parent 1",
                                   "\n2: add allele pair for parent 2",
                                   "\n3: calculate all F1 offspring allele combinations sorted by phenotype",
                                   "\n4: calculate specific F1 offspring allele combinations sorted by phenotype",
                                   "\n\nEnter number or X for exit: "))
            if choice == "X" or choice == "x": quit()
            else:
                try:
                    number = int(choice)
                    if number == 1:
                        allele_pair, genotype = addAllelesGenotypes()
                        alleles_pairs1.append(allele_pair)
                        genotype1.append(genotype)
                        break
                    if number == 2:
                        while True:
                            choice:str = input("\nCopy alleles and traits from parent 1? (Y/N) ")
                            if choice in ("Y", "y", "N", "n"): break
                            else: print("\nEnter a valid choice.")
                        if choice.lower() == 'y':
                            alleles_pairs2 = alleles_pairs1
                            genotype2 = genotype1
                            break
                        else:
                            allele_pair, genotype = addAllelesGenotypes()
                            alleles_pairs2.append(allele_pair)
                            genotype2.append(genotype)
                            break
                    if number == 3:
                        combinations:list = list()
                        for allele_pair1 in alleles_pairs1:
                            for allele1 in allele_pair1:
                                combination = [allele1["label"]]
                                for allele_pair2 in alleles_pairs2:
                                    for allele2 in allele_pair2:
                                        if allele1["trait"] == allele2["trait"]: # traits must match to combine
                                            combination.append(allele["label"])
                            combinations.append(combination)
                        print(combinations)
                        break
                    else:
                        print("\nEnter a valid number.")
                except ValueError:
                    print("\nEnter a valid choice.")
if __name__ == "__main__": main()