#Converting the c_instruction into the equivalent 15-bit binary constant

import re

def c_instruction(inst):
    s = "111"
    
    x = inst.strip()
    dest = "";
    comp = "";
    jump = "";
    x = x.strip()
    y = re.split('=+',x)
    if len(y) == 1 :
        dest = "";
        comp = y[0]
    else:
        dest = y[0]
        comp = y[1]
 
    z = re.split(';+',comp)

    if (len(z) == 1):
        comp = z[0]
        jump = ""
    else:
        comp = z[0]
        jump = z[1]

    dest = dest.strip()
    comp = comp.strip()
    jump = jump.strip()

    comp_c = comp_code(comp)
    dest_c = dest_code(dest)
    jump_c = jump_code(jump)
    s = s + comp_c + dest_c + jump_c
    print s
    
def comp_code(comp):
    b = "";
    if comp == "0":
        b = "0101010"
    elif (comp == "1"):
        b = "0111111"
    elif (comp == "-1"):
        b  = "0111010"
    elif (comp == "D"):
        b = "0001100"
    elif (comp == "A"):
        b = "0110000"
    elif (comp == "!D"):
        b = "0001101"
    elif (comp == "!A"):
        b = "0110001"
    elif (comp == "-D"):
        b = "0001111"
    elif (comp == "-A"):
        b = "0110011"
    elif (comp == "D+1"):
        b = "0011111"
    elif (comp == "A+1"):
        b = "0110111"
    elif (comp == "D-1"):
        b = "0001110"
    elif (comp == "A-1"):
        b = "0110010"
    elif (comp == "D+A"):
        b = "0000010"
    elif (comp == "D-A"):
        b = "0010011"
    elif (comp == "A-D"):
        b = "0000111"
    elif (comp == "D&A"):
        b = "0000000"
    elif (comp == "D|A"):
        b = "0010101"
    elif (comp == "M"):
        b = "1110000"
    elif (comp == "!M"):
        b = "1110001"
    elif (comp == "-M"):
        b = "1110011"
    elif (comp == "M+1"):
        b = "1110111"
    elif (comp == "M-1"):
        b = "1110111"
    elif (comp == "D+M"):
        b = "1000010"
    elif (comp == "D-M"):
        b = "1010011"
    elif (comp == "M-D"):
        b = "1000111"
    elif (comp == "D&M"):
        b = "1000000"
    elif (comp == "D|M"):
        b = "1010101"
    else:
          print "Invalid Option"
    return b

          
def dest_code(dest):
    b = ""
    if dest == "":
        b = "000"
    elif dest == "M":
        b = "001"
    elif dest == "D":
        b = "010"
    elif dest == "MD":
        b = "011"
    elif dest == "A":
        b = "100"
    elif dest == "AM":
        b = "101"
    elif dest == "AD":
        b = "110"
    elif dest == "AMD":
        b = "111"
    else:
         print "Invalid option"
    return b


def jump_code(jump):
    b = ""

    if jump == "":
        b = "000"
    elif jump == "JGT":
        b = "001"
    elif jump == "JEQ":
        b = "010"
    elif jump == "JGE":
        b = "011"
    elif jump == "JLT":
        b = "100"
    elif jump == "JNE":
        b = "101"
    elif jump == "JLE":
        b = "110"
    elif jump == "JMP":
        b = "111"
    else:
        print "Invalid option"

    return b


if __name__ == "__main__":

    final = raw_input("Enter a C-instruction: ")
    c_instruction(final)

