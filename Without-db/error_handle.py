file = open('youtube.txt', 'w')

try:
    file.write('poxy')
finally:
    file.close()

with open('youtube.txt', 'w') as file:
    file.write('poxy')