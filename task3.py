a = '\u265E'
print(a)

a = '\N{ROMAN NUMERAL NINE}'
print(a)

a = '\N{ROMAN NUMERAL TEN}'
print(a)

a = r'\u265E'
print(a)

a = 'adfdFFFFSSgrwif'
print(a.capitalize())
print(a.lower())
print(a.upper())
print(a.title())
print(a.swapcase())

# check methods
print(a.startswith('ad'))
print(a.endswith('ad'))
print(a.isalnum())
print(a.isalpha())
print(a.isdigit())
print(a.isspace())

# changes
print(a.replace('grw', '123'))