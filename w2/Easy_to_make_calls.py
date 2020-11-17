

#   m="323-sth-abcd"
#   tx=m.split(sep="-", maxsplit=1)
#   print(tx)    ['323', 'sth-abcd']

def num(user_input):
    numeric_phone_number =""
    right_char = True
    count = 0
    while right_char == True and count < 3:
        for ch in user_input[count]:
            if ch.isdigit():
                numeric_phone_number += ch
            elif ch.lower() in 'abc':
                numeric_phone_number += "2"
            elif ch.lower() in 'def':
                numeric_phone_number += "3"
            elif ch.lower() in 'ghi':
                numeric_phone_number += '4'
            elif ch.lower() in 'jkl':
                numeric_phone_number += "5"
            elif ch.lower() in 'mno':
                numeric_phone_number += '6'
            elif ch.lower() in 'pqrs':
                numeric_phone_number += '7'
            elif ch.lower() in "tuv":
                numeric_phone_number += '8'
            elif ch.lower() in 'wxyz':
                numeric_phone_number += '9'
            else:
                right_char = False
        if count != 2:
            numeric_phone_number += '-'
        count +=1
    return numeric_phone_number

def main():
    phone_number = input ("Enter using format: XXX-XXX-XXXX ")
    split_number = phone_number.split("-")
    tx=num(split_number)
    print(tx)
main()