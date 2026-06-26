# python program to translate a message into the secret code language .use the rules to transate the normal English into secert code language


word =input("enter the text you want to convert into screte code:  ")

for i in range(len(word)):

    if word[i].upper() == 'A':
        print('Q', end="")
    elif word[i].upper() == 'B':
        print('W', end="")
    elif word[i].upper() == 'C':
        print('E', end="")
    elif word[i].upper() == 'D':
        print('R', end="")
    elif word[i].upper() == 'E':
        print('T', end="")
    elif word[i].upper() == 'F':
        print('Y', end="")
    elif word[i].upper() == 'G':
        print('U', end="")
    elif word[i].upper() == 'H':
        print('I', end="")
    elif word[i].upper() == 'I':
        print('O', end="")
    elif word[i].upper() == 'J':
        print('P', end="")
    elif word[i].upper() == 'K':
        print('A', end="")
    elif word[i].upper() == 'L':
        print('S', end="")
    elif word[i].upper() == 'M':
        print('D', end="")
    elif word[i].upper() == 'N':
        print('F', end="")
    elif word[i].upper() == 'O':
        print('G', end="")
    elif word[i].upper() == 'P':
        print('H', end="")
    elif word[i].upper() == 'Q':
        print('J', end="")
    elif word[i].upper() == 'R':
        print('K', end="")
    elif word[i].upper() == 'S':
        print('L', end="")
    elif word[i].upper() == 'T':
        print('Z', end="")
    elif word[i].upper() == 'U':
        print('X', end="")
    elif word[i].upper() == 'V':
        print('C', end="")
    elif word[i].upper() == 'W':
        print('V', end="")
    elif word[i].upper() == 'X':
        print('B', end="")
    elif word[i].upper() == 'Y':
        print('N', end="")
    elif word[i].upper() == 'Z':
        print('M', end="")


      