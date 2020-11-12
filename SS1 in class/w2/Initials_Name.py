def printInitials(name):  
    list=[]
    list=name.split()
    iname=""
    for i in range(len(list)-1):
        s=list[i]                   #['abc', 'def', 'ghi', 'jKO']
        iname=iname + s[0].upper() + "." #print the first letter, except the last one

    #Add the last 
    list2=[]
    list2=list[len(list)-1]
    t=list2[0].upper()
    iname=iname+t
    print(iname)

def main(): 
    name = "abc def ghi jKO mnOP"
    printInitials(name) 
if __name__=="__main__": 
 main()  
# The end of the code.  


