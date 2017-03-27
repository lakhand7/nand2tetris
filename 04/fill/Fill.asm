// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

// Put your code here.
  
  
  
(LOOP)
  
  @SCREEN
  D=A
  @output2
  M=D
  
  
  @SCREEN
  D=A
  @output1
  M=D
  
  @KBD
  D=A
  @input
  M=D
  
  @input
  A=M
  D=M
  @STOP
  D;JEQ

(LOOP1)
    
  @24576
  D=A
  @output1
  D=D-M
  @LOOP
  D;JEQ
    
  @output1
  A=M
  M=-1
  
  @1
  D=M
  @output1
  M=M+1
  
  @input
  A=M
  D=M
  @LOOP
  D;JEQ

  @LOOP1
  0;JMP
  
(STOP)
  
  @24576
  D=A
  @output2
  D=D-M
  @LOOP
  D;JEQ
    
  @output2
  A=M
  M=0
  
  @1
  D=M
  @output2
  M=M+1
  
  @input
  A=M
  D=M
  @LOOP
  D;JNE

  @STOP
  0;JMP
 
  
(END)
  @END
  0;JMP
  