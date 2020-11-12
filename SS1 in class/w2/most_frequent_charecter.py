def split(word):
    return [char for char in word]
    
def most_frequent(String):
    counter = 0
    li = split(String)
    num = li[0]
    for i in li:
        current_frequency = li.count(i)
        if(current_frequency > counter):
            counter = current_frequency
            num = i
    if num == ' ':
        return 'space'
    else:
        return num
def main():
    inp = input("Enter whatever String: \n")
    print("The most frequently charater is: " + most_frequent(inp))
main()