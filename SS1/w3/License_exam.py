key = {1: "A", 2: "C", 3: "A"}

bank = {1: "Khái niệm đường bộ được hiểu như thế nào?" ,\
        2: "Vạch kẻ đường hiểu như thế nào là đúng?", \
        3: "Vừa đi xa máy vừa mang theo vật cản như ô dù sẽ bị phạt ntn?" }
ans_bank={1: "A B C D", \
        2: "A B C D ", \
        3: "A B C D"}

def answer():
    right = 0
    wrong = 0
    for i in range(len(key)):
        print(str(bank[i +1]) + "\n" + str(ans_bank[i +1]))
        ans = input("Your answer: ")
        if key[i+1] != ans.upper():
            wrong += 1
        else:
            right += 1
    print("Number of right answer " + str(right))
    print("Number of wrong answer " + str(wrong))
answer()