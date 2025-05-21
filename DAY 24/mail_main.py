# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

letters = []
with open("input/letters/starting_letter.txt") as letter:
    letter_template = letter.read()

with open("input/names/invited_names.txt") as names:
    names_template = names.read().split("\n")

for name in names_template:
    letter = letter_template.replace("[name]", name)
    letters.append(letter)

with open("output/readyToSend/final_letters.txt", "w") as output_file:
    for final_letter in letters:
        output_file.write(final_letter + "\n")
