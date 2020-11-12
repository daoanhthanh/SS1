units=["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín", "mười"]
big_units=["nghìn", "triệu", "tỷ", "nghìn tỷ", "triệu tỷ", "tỷ tỷ"]

def main():
    num = input("Enter an amount ")
    abc = from_1_to_999(num)
    print(abc)

def from_1_to_999(n):
    # t(trăm) c(chục) d(đơn vị)
    # convert to int since default data type is float 
    d = n%10                        # đơn vị
    c = (n%100 - d)/10              # chục
    t = ((n%1000) - 10*c -d)/100    # trăm
    hundered = ""
    if t !=0 and c == 0 and d == 0:         #  eg: 400
        hundered = units[t] + " trăm "
    elif t!=0  and c == 0 and d != 0:       #  eg: 405
        hundered = units[t] + " trăm linh " + units[d]
    elif t != 0 and c > 1 and d==0:         #  eg: 450
        hundered = units[t] + " trăm " + units[c] + " mươi"
    elif t!=0 and c==1:                     #  eg: 130
        hundered = units[t] + " trăm mười " + units[d] 
    elif t == 0 and c>1:                    #  eg: 45
        hundered = units[c] + " mươi " + units[d]
    elif t == 0 and c==1:                   #  eg: 19
        hundered = "mười " + units[d] 
    elif t!=0 and c!=0 and d!=0:            #  eg: 119
        hundered = units[t] + " trăm " + units[c] + " mươi " + units[d]
    else:                                   #  eg: 6
        hundered = units[d]
    return hundered




if __name__ == '__main__':
    money = input('Enter the money: ')
    
    #Divide money number into parts and use def from_1_to_999() for each
    #Each part has maximum 3 digits
    if len(str(money)) < 4:
        part1 = int(money)
        print(from_1_to_999(part1))
    elif (str(money)) > 3 and len(str(money)) < 7  :
        part1 = int(money) // 1000
        part2 = int(money) % 1000
        print(from_1_to_999(part1) , 'nghin' , from_1_to_999(part2), "dong")

    elif len(str(money)) < 10:
        part1 = int(money) // 1000000
        part2 = (int(money) % 1000000) // 1000
        part3 = int(money) % 1000
        print(from_1_to_999(part1), 'trieu', from_1_to_999(part2), 'nghin', from_1_to_999(part3), 'dong')

    elif len(str(money)) < 13:
        part1 = int(money) // 1000000000
        part2 = (int(money) % 1000000000) // 1000000
        part3 = (int(money) % 1000000) // 1000
        part4 = int(money) % 1000
        print(from_1_to_999(part1), 'ti', from_1_to_999(part2), 'trieu', from_1_to_999(part3), 'nghin', from_1_to_999(part4),
              'dong')