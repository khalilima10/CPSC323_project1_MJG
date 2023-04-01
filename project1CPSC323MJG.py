# Name: Mohammad Khalil, Jayden Garcia, Gage Ashbaugh
# CPSC 323 Project Assignment 1
# Miss Susmitha Padda
# Date: 4/2/2023

# defination of one states
class State:
    def __init__(self, lexeme ,token):
        self.lexeme = lexeme
        self.token = token
        self.zero = None
        self.one = None

# This function sends the lexeme and token of the State to the file output.txt
def writeto(self):
    if self:
        length = "token              lexeme" 
        l = len(length) # length of the line on file
        s = l - (len(self.token) +  len(self.lexeme))
        #creates a string that is the number of spaces 
        space = ""
        for i in range(s):
             space = space + " "
        line = self.token + space + self.lexeme
        # opens file to add to it
        filewrite = open("output.txt", "a")
        filewrite.write(line)
        filewrite.write("\n")
        filewrite.close()
    if self.one != None: # see if it is the final state
        writeto(self.one) # if not goes to next state
    else:
        return # if yes then leaves function

# The tokenind function takes in a lexeme and determines which type of token it is
def tokenind(lexeme):
    if (lexeme[0] == "1"    or lexeme[0] == "2" or lexeme[0] == "3" # checks if it is a number
        or lexeme[0] == "4" or lexeme[0] == "5" or lexeme[0] == "6"
        or lexeme[0] == "7" or lexeme[0] == "8" or lexeme[0] == "9" 
        or lexeme[0] == "0"): 
        return "real"
    elif(len(lexeme) > 1) : # see if the # of char of the lexeme is greater than one 
        if (lexeme == "while"   or lexeme == "for"  or lexeme == "if"    # sees if the lexeme is a keyword
            or lexeme == "elif" or lexeme == "else" or lexeme == "do"):
            return "keyword" # returns token type keyword
        else:
            return "identifier" # returns identifier token type if not keyword
    elif(lexeme == "(" or lexeme == ")" or lexeme == ";" ): # checks if lexeme is a seprater
        return "separator"
    elif(lexeme == "+"     or lexeme == "-"  or lexeme == "*" # see if the lexeme is a operator
         or lexeme == "/"  or lexeme == "="  or lexeme == ">"
         or lexeme == "<"  or lexeme == ">=" or lexeme == "<=" 
         or lexeme == "=="):
        return "operator"
    else:
        return "identifier" # returns identifier if none of the conditions are valid

# The lexer function takes a file name with code in then identify the lexmes and determines
# the token type of each lexmes in the code
def lexer(filename):
    # opens and reads the file 
    infile = open(filename, "r")
    code = infile.read() # saves it to a variable
    
    l = len(code)
    lexemes = [] # holds all the lexemes 
    current = "" # holds lexemes before placed in array
    
    # loop to run through all the code in file
    for a in range(l):
        if code[a] == " ": # removes white space from code
            if current != "":
             lexemes.append(current)
             current = ""
        elif code[a] == ";": # adds ; and previous lexeme to lexemes
            lexemes.append(current)
            lexemes.append(code[a])
        elif code[a] == "(" or code[a] == ")" or code[a] == "<" or code[a] == ">":
            if current != "":
                 lexemes.append(current)
                 current = ""
            lexemes.append(code[a])
        else:
            current = current + code[a] # done by char and char so just holds char(s) until lexeme is finished
    
    tokens = [] # holds the token types
    
    for x in lexemes: # calls all lexmes in the lexemes array
         token = tokenind(x) # calles function to determine type of token
         tokens.append(token) # addes it to the tokens array
    
    # FSA implementation
    q0 = State(lexemes[0], tokens[0]) # initial state
    q0.zero = q0
    q1 = State(lexemes[1], tokens[1])
    q1.zero = q0
    q0.one = q1
    q2 = State(lexemes[2], tokens[2])
    q2.zero = q0
    q1.one = q2
    q3 = State(lexemes[3], tokens[3])
    q3.zero = q0
    q2.one = q3
    q4 = State(lexemes[4], tokens[4])
    q4.zero = q0
    q3.one = q4
    q5 = State(lexemes[5], tokens[5])
    q5.zero = q0
    q4.one = q5
    q6 = State(lexemes[6], tokens[6])
    q6.zero = q0
    q5.one = q6
    q7 = State(lexemes[7], tokens[7])
    q7.zero = q0
    q6.one = q7
    q8 = State(lexemes[8], tokens[8])
    q8.zero = q0
    q7.one = q8
    q9 = State(lexemes[9], tokens[9]) 
    q8.one = q9
    
    # set up the labels of the table
    outfile = open("output.txt", "w")
    outfile.write("token              lexeme\n")
    outfile.write("-------------------------\n")
    outfile.close()
    
    # writes each lexeme and token from FSA to output.txt
    writeto(q0)
    
    infile.close() # closes input file
           
 
file = "input_scode.txt" # filename with code
lexer(file) # calls function with filename input_scode.txt
