import csv

current_address = "michel.martin@gmail.com"

def generate_combinations(word):
    if len(word) == 1:
        return [word]

    combinations = []
    # Ajouter un point entre chaque lettre
    for i in range(1, len(word)):
        prefix = word[:i]
        suffix = word[i:]
        for suffix_combination in generate_combinations(suffix):
            combinations.append(prefix + '.' + suffix_combination)

    # Ne pas ajouter de point
    for suffix_combination in generate_combinations(word[1:]):
        combinations.append(word[0] + suffix_combination)

    return combinations

def write_combinations_to_csv(combinations, filename):
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for combination in combinations:
            csvwriter.writerow([combination + "@gmail.com"])

def main():
    word = current_address.replace('.', '').split('@')[0]
    combinations = generate_combinations(word)
    print("Nombre total de combinaisons:", len(combinations))
    write_combinations_to_csv(combinations, "combinations.csv")

if __name__ == "__main__":
    main()
