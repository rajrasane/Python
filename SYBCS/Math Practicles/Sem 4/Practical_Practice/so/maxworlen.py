words = ["apple", "banana", "strawberry", "kiwi"]

def m(words):
    return max(len(word) for word in words)

print(m(words))