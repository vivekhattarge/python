file = open('Newfile.txt', 'w')

try:
    file.write('First Python Error handling program')
finally:
    file.close()

with open('Newfile.txt', 'w') as file:
    file.write('First Python Error handling program 2')