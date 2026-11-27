word = input("Palabra: ").lower()
vowels = 0

for letter in word:
    if letter in "aeiou":
        vowels += 1

print("Vocales:", vowels)