  
alphabet = []
# fill in alphabet: alphabet[0] = 'A' .....alphabet[25] = 'Z'
for i in range(26):
    alphabet.append(chr(ord('A') + i))

the_numbers1 = [16, 9, 3, 15, 3, 20, 6]
the_numbers2 = [20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]
message = ''

for i in the_numbers1:
    message += alphabet[i - 1]

# insert open curly brace
message += '{'

for i in the_numbers2:
    message += alphabet[i -1]
    
# insert closed curly brace
message += '}'

# print the result
print(message)
