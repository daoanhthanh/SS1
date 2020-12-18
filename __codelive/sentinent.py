import string
import re

def remove_dup(x):
    return list(dict.fromkeys(x))

 
def get_score(file, word):
    file_striped = []
    count = 0
    row_number=[]
    for i in file:
        file_striped.append(i.strip())

    for j in file_striped:
        if word in j:
            row_number.append(int(j[0]))

    for t in row_number:
        count = count + t
    if len(row_number) == 0:
        return count/1
    return count/(len(row_number))
    
def average_score(file1, file2):
    li = []
    # Create a translation table, where all digits are mapped to None
    translation_table = str.maketrans('', '', string.digits)
    # replace characters in string based on translation table, so it will
    # delete all numbers / digits from the string
    file1 = file1.translate(translation_table)
    res = re.sub('['+string.punctuation+']', '', file1).split() 
    for i in res:
        li.append(i.lower())
    li = remove_dup(li)
    _all = len(li)
    count = 0
    mark = []
    for word in li:
        m = get_score(file2, word)
        mark.append(m)
    for i in mark:
        count = count + i
    print(count/_all)
    


    

        



if __name__ == '__main__':
    ask = input('Learning data file name:')
    print('What would you like to do?')
    print('1: Get the score of a words in a file ')
    print('3: Get the average score of words in a file')
    print('4: Sort the words into positive.txt and negative.txt')
    print('5: Exit the program')
    ans = input('Enter a number 1 – 5: ')
    if ans == '1':
        word = input('Which word?')
        with open(ask) as op:
            file = op.readlines()
            a = get_score(file, word)
            print(a)

    elif ans == '2':
        with open(ask) as op:
            file2 = op.readlines()
            op.seek(0)
            file1 = op.read()
            average_score(file1, file2)
            
            

