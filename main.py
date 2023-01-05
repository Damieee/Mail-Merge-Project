# convert names in names file to list
with open("./Input/Names/invited_names.txt", "r") as letter_name:
    letter_names=letter_name.readlines()
    

name="[name]"
#read letter in starting letter
with open("./Input/Letters/starting_letter.txt", "r") as letter:
    letters=letter.read()

#modify letters    
for names in letter_names:
    modified_letters=letters.replace(name, names.strip())
    with open(f"./Output/ReadyToSend/letter_to_{names.strip()}", "w") as files:
        files.write(modified_letters)
