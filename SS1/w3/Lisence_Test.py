key =[]

with open("dapan.txt", "r") as dap_an:
    key = dap_an.readlines()

key = [ x.strip() for x in key]  
key = [x[-1:] for x in key]


lln = len(key)
question = []
answer = []
in_ = ['1', '2', '3']
# Read question and answer that provided  in advance
try:
    with open("Question.txt", "r" , encoding="utf-8") as ques:
        question = ques.readlines()

except FileNotFoundError:
    print("There is no file named Question.txt")
question = [a.strip() for a in question]

w = 0
r = 0

for i in range(len(question)):
    
    if question[i] != '':
       
        print(question[i])
        

    else:
        while True:
            user_ans = input("Your answer is: ")
            if not user_ans in in_:
                print("Please enter 1, 2 or 3.")
                continue
            elif user_ans.isalpha() == True:
                print("Please enter 1, 2 or 3.")
                continue
            else:
                answer.append(user_ans)
                break
        print("\n")
        
for i in range(len(answer)):
    if answer[i] == key[i][-1:]:
        r += 1
    else:
        w += 1
print("You got", str(r), "correct answer.")


