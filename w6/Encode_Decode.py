from mylibs import find_congruence

# create a list that contain original message
li = []
original = input("Enter you signature: ")
for i in original:
    li.append(ord(i))
print("*****************")
print("Below is your original signature")
print(li)
print("*****************")

'''
  This step will encode 
'''
for i in li:
    