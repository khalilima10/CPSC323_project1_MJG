# Name: Mohammad Khalil, Jayden Garcia, Gage Ashbaugh
# CPSC 323 Project Assignment 1
# Miss Susmitha Padda
# Date: 4/2/2023

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
            lexemes.append(code[a])
        else:
            current = current + code[a] # done by char and char so just holds char(s) until lexeme is finished
    
    tokens = [] # holds the token types
    
    for x in lexemes: # calls all lexmes in the lexemes array
        token = tokenind(x) # calles function to determine type of token
        tokens.append(token) # addes it to the tokens array
    # creates/opens output.txt file and writes to it
    outfile = open("output.txt", "w")
    outfile.write("token              lexeme\n")
    outfile.write("-------------------------\n")
    
    length = "token              lexeme" 
    l = len(length) # length of the line on file
    
    # loop to determine write to the file for the number of lexemes and tokens
    for c in range(len(lexemes)):
        # determines the number spaces need for each line of the file
        s = l - (len(tokens[c]) +  len(lexemes[c]))
        #creates a string that is the number of spaces 
        space = ""
        for i in range(s):
            space = space + " "
            
        # one line of the code
        line = tokens[c] + space + lexemes[c]
        
        # writes that line to the file
        outfile.write(line)
        outfile.write("\n")
        
    # closes both input and output files
    outfile.close()
    infile.close()
           
 
file = "input_scode.txt" # filename with code
lexer(file) # calls function with filename input_scode.txt