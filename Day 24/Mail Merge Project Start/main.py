#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
    
    

PLACEHOLDER = "[name]"
with open("/home/amul/Documents/anjela python/Day 24/Mail Merge Project Start/Input/Names/invited_names.txt",'r') as names_file:
    names = (names_file.readlines())
    
with open("/home/amul/Documents/anjela python/Day 24/Mail Merge Project Start/Input/Letters/starting_letter.txt",'r') as letter:
    letter_content = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER,name)
        with open(f"/home/amul/Documents/anjela python/Day 24/Mail Merge Project Start/Output/{stripped_name}.txt",'w') as completed_letter:
            completed_letter.write(new_letter)