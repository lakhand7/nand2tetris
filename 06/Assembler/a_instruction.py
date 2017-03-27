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
#Checking the working of a_instruction

if __name__ == "__main__":
    s = raw_input("Enter the A-instruction: ")
    final = a_instruction(s)
    print final

