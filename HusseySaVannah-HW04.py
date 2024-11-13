#SaVannah Hussey
# 11/12/2024
#Lab Section: 14
# HW04
#Sources: Textbook 8,10, COSC1010_lec13-FilesAndExceptions.pptx.pdf, COSC1010_lec7-IfStatements.pptx.pdf
#help given to/received from: https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository
#https://documentation.sas.com/doc/en/lecompobjref/9.4/n0zvtjw02x6kkgn1s4vip8o7qxq4.htm#:~:text=The%20INFILE%20method%20reads%20Python,the%20Python%20function%20definition%20statement.
# (The URL above told me how to use the infile method)
#https://www.pythonclassroom.com/files
#ChatGPT "" 11/10/2024
# This code works because I was able to add the prompt.txt to my
# Github repostiory; I couldn't remember how you did in on class on Monday, but
# hopefully the code still works the same!

#The program reads key-value pairs from `prompt.txt`, 
# generates corresponding ASCII art, and writes the result to `out.txt`.

def process_file():
    with open('prompt.txt', 'r') as infile:
        lines = infile.readlines()

    
    with open('out.txt', 'w') as outfile:
        # Iterate through each line in prompt.txt
        for line in lines:
            # Remove any whitespace from the line
            line = line.strip()

            # Split the line into key-value pairs 
            pairs = line.split("\t")
            
            result = ""

            # Iterate through the pairs and process them
            for pair in pairs:
                # Before splitting strip any extra spaces around the key-value pair
                pair = pair.strip()
                
                print(f"Processing pair: '{pair}'")

                # Split each pair into key and value
                if ':' in pair:
                    key, value = pair.split(":")
                else:
                    # If ':' is missing, print a message and skip the pair
                    print(f"Skipping malformed pair: {pair}")
                    continue
                
                # Convert the value (which is a string) to an integer
                try:
                    num = int(value)
                except ValueError:
                    print(f"Error: Invalid number format in pair {pair}")
                    continue

                # Append the corresponding character (' ' for 'w' and '*' for '*') 
                # repeated 'num' times
                # Adding spaces and asterisks
                if key == 'w':
                    result += ' ' * num  
                elif key == '*':
                    result += '*' * num  
                else:
                    print(f"Skipping unrecognized key: {key}")
            
            outfile.write(result + '\n')

process_file()


