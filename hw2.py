name = 'pinksentor'

name_underscores = ''.join([i + '_' for i in name])
name_underscores_upper = name_underscores.upper()
ASCII_upper = [ord(i) for i in name_underscores_upper]

name_underscores = ''.join([i + '_' for i in name])
name_underscores_lower = name_underscores.lower()
ASCII_lower = [ord(i) for i in name_underscores_lower]

all_ASCII = ASCII_lower + ASCII_upper

print(max(all_ASCII))
print(min(all_ASCII))