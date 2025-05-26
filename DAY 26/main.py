import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

dict_data = {row.letter: row.code for (index, row) in data.iterrows()}

user_word = input("Enter a word: ").upper()

words = [dict_data[letter] for letter in user_word]

print(words)
