PLACEHOLDER = "[name]"


with open("./Mail_Merge_Demo/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Mail_Merge_Demo/Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"./Mail_Merge_Demo/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as complete_letter:
            complete_letter.write(new_letter)

