#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Letters/starting_letter.txt") as file:
    letter_content = file.read()

with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()


for name in names:
    file_name = "letter_for_" + name.strip() + ".txt"
    print(file_name)
    path = "./Output/ReadyToSend/" + file_name
    with open(path, mode="+w") as output_file:
        output_file.write(letter_content.replace("[name]", name.strip()))
    
# with open("./Output/ReadyToSend/letter_for_Aang.txt", mode="+w") as output_file:
#     output_file.write(letter_content.replace("[name]","Aang"))