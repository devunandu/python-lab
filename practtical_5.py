def frequency(string,char):
    return string.count(char)
def replace_char(string,old_char,new_char):
    return string.replace(old_char,new_char)
def remove_first_occurrence(string,char):
    return string.replace(char,'',1)
def remove_all_occurrence(string,char):
    return string.replace(char,'')

while True:
    print("\n menu:")
    print("a.find the frequency of a character in a string")
    print("b.replace a character by another character in a string")
    print("c.remove the first occurence of a character from a string")
    print("d.remove all occurrence of a character from a string")
    print("e.exit")
    choice=input("enter your choice: ").lower()
    if choice=='e':
        print("exiting the program")
        break
    string=input("enter the string: ")
    if choice=='a':
        char=input("enter tha character to find frequency: ")
        print("frequency of ",char," in the string is: ",frequency(string,char))
    elif choice=='b':
        old_char=input("enter the character to be replaced: ")
        new_char=input("enter the new  character: ")
        print("modified string: ",replace_char(string,old_char,new_char))
    elif choice=='c':
        char=input("enter the character to remove first occurrence: ")
        print("modified string: ",remove_first_occurrence(string,char))
    elif choice=='d':
        char=input("enter the character to remove all occurrence: ")
        print("modified string: ",remove_all_occurrence(string,char))
    else:
        print("invalid choice")
