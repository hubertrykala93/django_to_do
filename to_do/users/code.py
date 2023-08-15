from string import ascii_lowercase, ascii_letters, ascii_uppercase, digits

print(ascii_letters)
print(digits)

for digit in digits:
    print(digit, type(digit))

lst = ','.join([ascii_letters + digits])
print(lst)
