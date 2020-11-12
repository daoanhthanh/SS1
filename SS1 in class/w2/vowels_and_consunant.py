#this will split a string in to character
def split(word): 
    return [char for char in word]

def count(input):
    li = split(input)
    vow = 0
    con = 0
    for i in li:
        if i in "ueoai":
            vow += 1
        else:
            con += 1
    print("Number of vowel(s): " + str(vow) + \
           " and number of consunant(s): " + str(con))

def main():
    inp = input("Enter any String: \n")
    count(inp)
main()