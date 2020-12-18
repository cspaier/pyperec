import csv
import unidecode

LEXIQUE = "lexique-grammalecte-fr-v7.txt"
NUMBER_LETTER = 5

def read_grammalecte_lexique(file):
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='\t')
        words_list = []
        for row in reader:
            word = row['Flexion']
            if len(word) == NUMBER_LETTER and not word.isupper() and word.isalpha():
                word = unidecode.unidecode(word)
                if word not in words_list:
                    words_list.append(word)
        with open('liste_french.2.txt', 'w') as f:
            for word in words_list:
                f.write("%s\n" % word)


read_grammalecte_lexique(LEXIQUE)
