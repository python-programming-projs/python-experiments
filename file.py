# trying to read file first time
# thanks waheguru

import sys

file = open("text.txt", "r")
file_text = file.read()
file.close()
print(file_text)
