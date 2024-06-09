file = open('youtube.txt', 'w')

try:
    file.write('First Python Error handling program')
finally:
    file.close()

with open('youtube.txt', 'w') as file:
    file.write('First Python Error handling program 2')