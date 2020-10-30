units=["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín", "mười"]
big_units=["nghìn", "triệu", "tỷ", "nghìn tỷ", "triệu tỷ", "tỷ tỷ"]


def from_1_to_999(n):
    # t(trăm) c(chục) d(đơn vị)
    # convert to int since default data type is float 
    d = int(n%10)                        # đơn vị
    c = int((n%100 - d)/10)              # chục
    t = int(((n%1000) - 10*c -d)/100)    # trăm
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

def main():
    print(from_1_to_999(21))
if __name__ == "__main__":
    main()

