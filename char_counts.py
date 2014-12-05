#return counts for each letter in a string
#1-Hello World
#2-For a better tomorrow
 
#required for OrderedDict
import collections

#function definitions 
def printCharCounts(s):

  #ordered Dict to store character-Number of occurrences in str
  dict = collections.OrderedDict()

  #using for loop to iterate over all char in the str ( c-character)
  for c in s:
  #skip whitespaces  
     if c == ' ':
        continue
        
  #get count for current char 
     count = dict.get(c)
    
  #if char count is not found in the dict then insert current char with count = 1    
     if count is None:
        dict[c] = 1
        
  #else increment count for current char by 1        
     else:
        count = count + 1
        dict[c] = count

  #iterate dict keys and print the count      
  for c in dict.keys():
     print(c + " = " + str(dict.get(c)))
     
#program starts here
s1 = "Hello World"
s2 = "For a better tomorrow"

printCharCounts(s1)
print
printCharCounts(s2)
 