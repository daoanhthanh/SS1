#dictionary
months={1:"January", 2:"February ", 3:"March ", 4: "April ",\
        5: "May ", 6: "June ", 7:"July ", 8: "August ", \
        9: "September ", 10: "October ", 11: "November ", 12: "December "}

# check whether input is valid or not
def check(input):
    if (int(input[0]) >0 and int(input[0]) <= 12) and (int(input[1]) > 0 and int(input[1]) <=31):
        return True    
    else:
        return False

# format output
def show_date(date_show):
    txt=date_show.split("/")
    month=""
    if check(txt) == True:
        month = months[int(txt[0])] + txt[1] + ", " + txt[2]
        return month
    else:
        return "Format of input is invalid."

def main():
    type_in=input("Enter date following this format: mm/dd/yyyy ")
    print(show_date(type_in))
main()