#range
#output for each number

for value in range (1, 101):
  if value % 3 == 0 and value % 5 == 0:
     print value, "Ping Pong"
  elif value % 3 == 0:
     print  value, "Ping"
  elif value % 5 == 0:
     print value, "Pong"
  elif value % 2 == 0:
     print value, "PingPongPing"
  else:
     print value
  