cipher = 'ynkooejcpdanqxeykjrbdofgkq'
plain = ''

# test case k = 1
# for k in range(26):
k = 2
for k in range(26):
    for i in cipher:
        char = chr((ord(i) + k) % 123) 
        # check if char has looped past 'z'
        if ord(char) < 97:
            char = chr((ord(char) + 97 ))
        plain += char
    # print & reset plaintext
    print(f'k = {k}: {plain}')
    plain = ''
