#range
#output for each number
#no ping pong ping


 
#iterate over values from 1 to 101
for value in range (1, 101):
#just do it with 2 comparasing  (not 3)
#if value % 3 == 0 and value % 5 == 0:

#if value devisable by 3 and 5 print ping pong
  if value % 15 == 0:
     print value, "Ping Pong"
     
#if value devisable by 3 print ping     
  elif value % 3 == 0:
     print  value, "Ping"
     
#if value devisable by 5 print pong          
  elif value % 5 == 0:
     print value, "Pong"
     
#if value is not devisable by 3 or 5 print value     
  else:
     print value
  