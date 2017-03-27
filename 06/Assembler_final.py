import re

#Handling symbols in the assembly code

def number(x):
    try:
        x = int(x)
        return True
    except ValueError or TypeError:
        return False

def remove_inline_comment(line):
    arr = line.split("//");
    line = arr[0]
    return line


def symbols(inst_file):
    d = {'R0':0,'R1':1,'R2':2,'R3':3,'R4':4,'R5':5,'R6':6,'R7':7,'R8':8,'R9':9,'R10':10,
         'R11':11,'R12':12,'R13':13,'R14':14,'R15':15,'SP':0,'LCL':1,'ARG':2,'THIS':3,
        'THAT':4}
    i = 16
    line_no = 0
    final = ""
    binary_code = open('rect\output_RectL.txt','w')
    fp = open(inst_file,'r')
    label = {}
    for line in fp:
        line = line.strip()
          
        if line == "" or line[0:2] == "//":
            continue
        else:
            line = remove_inline_comment(line)

            if line[0] == '(':
                label[line[1:(len(line)-1)]] = line_no
                
            else:
                line_no = line_no + 1

    fp = open(inst_file,'r')
    for line in fp:
        line = line.strip()
        if line == "" or line[0:2] == "//" or line[0] == "(":
            continue
        else:
        
            line = remove_inline_comment(line)
            
            if line[0] == '@':
                if line[1:] in d.keys():
                    line = line.replace(line[1:],str(d[line[1:]]))
                elif line[1:] in label.keys():
                    line = line.replace(line[1:],str(label[line[1:]]))
                elif not(number(line[1:])):
                    if d[line[1:]] in d:
                        line = line.replace(line[1:],str(d[line[1:]]))
                    else:
                        d[line[1:]] = i
                        i = i + 1
                        line = line.replace(line[1:],str(d[line[1:]]))
                
                    
                final = final + a_instruction(line) + "\n"
            else:
                final = final + c_instruction(line)+ "\n"
            print line
    binary_code.write(final)

    binary_code.close()
    return final


#Generates the equivalent 15-bit binary constant of the instruction

def a_instruction(inst):
    x = inst[0]
    y = int(inst[1:])
    s = "0"
    binary = ""
    while y > 0 :
        binary = binary + str(y%2)
        y = y/2
    binary = rev(binary)
    zeros = "000000000000000"
    s = s + zeros[:(15-(len(binary)))] + binary
    return s

def rev(s): return s[::-1]


#Converting the c_instruction into the equivalent 15-bit binary constant

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
    return s
    
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
        b = "1110010"
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


if (__name__== "__main__"):
    final = symbols("rect\RectL.txt")
    print final
        
