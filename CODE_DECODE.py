import random
import string

characters = string.ascii_letters + string.digits

choice = input("Enter C for Coding or D for Decoding: ").upper()

text = input("Enter the message: ")

words = text.split()

result = []

if choice == "C":

    for word in words:

        if len(word) >= 3:
            r1 = ''.join(random.choices(characters, k=3))
            r2 = ''.join(random.choices(characters, k=3))

            newWord = r1 + word[1:] + word[0] + r2
            result.append(newWord)

        else:
            result.append(word[::-1])

    print("Encoded Message:")
    print(" ".join(result))

elif choice == "D":

    for word in words:

        if len(word) >= 9:

            word = word[3:-3]          # Remove random characters
            word = word[-1] + word[:-1]  # Move last letter to front

            result.append(word)

        else:
            result.append(word[::-1])

    print("Decoded Message:")
    print(" ".join(result))

else:
    print("Invalid Choice")
