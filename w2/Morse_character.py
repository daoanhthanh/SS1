# Programming Morse Code

def main():
    # Local variables
    morse_string = ''
   
    
    # List of Morse codes
    morse_list =  {" ": ", ", ",": "--..--", ".": ".-.-.-",
             "?": "..--..", "0": "-----", "1": ".----",
             "2": "..---", "3": "...--", "4": "....-",
             "5": ".....", "6": "-....", "7": "--...",
             "8": "---..", "9": "----.", "A": ".-",
             "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
             "F": "..-.", "G": "--.", "H": "....", "I": "..",
             "J": ".---", "K": "-.-", "L": ".-..", "M": "--",
             "N": "-.", "O": "---", "P": ".--.", "Q": "--.-",
             "R": ".-.", "S": "...", "T": "-", "U": "..-",
             "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
             "Z": "--.."}
    
    # Get the string as input from the user.
    morse_string = input('Enter the string to be ' \
                         'converted to Morse code: ')
    
    convert =''
    for i in morse_string:
        i=i.upper()
        convert = convert + morse_list[i]
    
    print(convert)
main()
        
     
