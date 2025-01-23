
while(True):
    string = input("Enter an String: ")
    if string == "":
        print("You wanna enter an String")
        continue
    lower_letters = ''
    upper_letters = ''
    special_char = ''
    for i in string:
        if i.islower():
            lower_letters += i
        elif (i.isupper()):
            upper_letters += i
        else:
            special_char += i
    print(f"The lower case letters are {lower_letters}")
    print(f"The upper case letters are {upper_letters}")
    if special_char == '':
        print()
    else:
        print(f"The special characters are {special_char}")
    wc = input("Do you want to continue? Enter y/n: ")
    if wc == 'y':
        continue
    else:
        break
