import string

text = "The quick brown fox jumps over the lazy dog"

a = set(string.ascii_lowercase)

b = set(text.lower())

if(a<=b):
    print("Pangram")
else:
    print("Not Pangram")