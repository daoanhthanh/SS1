def cap(text):
    li = text.split('. ')
    for i in li:
        print(i.capitalize(),end='. ')
    # replace ' '' ' by ' '
    # replace ' .'and '. ' by '.'
    # replace '.' by '. '
def main():
    text = input("Enter a String: \n")
    cap(text)
main()