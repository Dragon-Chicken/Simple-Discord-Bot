import os

filename = 'joke_list.txt'
new_filename = 'formatted_jokes.txt'

with open(filename, 'r') as file:
    lines = file.readlines()

with open(new_filename, 'w') as new_file:
    for line in lines:
        new_file.write(line.rstrip() + ',\n')

print('Commas added and saved to', new_filename)
