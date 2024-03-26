# A simple script for searching how many times a string is found in a file
# and in which lines the string is found
file_name = 'String Hunter'
ver = '1.0'
signature = 'Leo Veloso'

# Print information about this script
print(file_name, '\nver:', ver)

while True:
    # Asks user for file's path
    f_name = input('\nEnter file path: ')

    # Tries to open the file
    try:
        f_hand = open(f_name)
    # Shows error message if file cannot be open
    except:
        print(f_name, 'can not be found')
        # Restarts loop if file couldn't be open
        continue

    # Opens counters and lists
    counter = 0
    s_string = input('What are you looking for? ')
    f_lines = []

    # Iterates upon lines in the file
    for line_num, line in enumerate(f_hand, start = 1): 
        # Searches for the string in line
        if s_string in line:
            # Counts the string and adds lines to the list
            counter += line.count(s_string)
            f_lines.append(str(line_num))

    # Verify if the string was found
    if counter == 0:
        print('Nothing found.')
    else:
        # Prints how many times the string was found and in which lines
        print(f"\nThere {'is' if counter == 1 else 'are'} {counter} {s_string}{'\'s' if counter > 1 else ''} found in the {'line' if counter == 1 else 'lines'} {', '.join(f_lines)}")
    # Asks user if a new string search is wanted
    choice = input('\nSearch again? (yes/no): ')
    # If string is different from 'yes', then break the loop
    if choice.lower() != 'yes':
        break

#Self explanatory :p
print('\n' + file_name, '\nver:', ver, '\nby', signature)

# Pauses before exiting
input('\nPress enter to exit..')