#deduplicate letters from string
#1-Hello World
#2-For a better tomorrow

#function definitions
#creating dedup string function    
def dedupStr(str):

#variable to store dedup string (initialization)
    dedupStr = ''

#using for loop to iterate over all char in the str ( c-character)
    for c in str:
#append current char to dedup str if current char is not found in dedup str or current char is white space 
        if (not c in dedupStr) or (c == ' '):
            dedupStr += c
    return dedupStr
    
#program starts here  
  
string1 = "Hello World"
string2 = "For a better tomorrow"
        
print(dedupStr(string1))
print(dedupStr(string2))
    