#Dik Üçgen1:
for i in range(5, -1, -1):
  for j in range(0, i): 
    print("*", end=" ") 
  print ()

#Dik Üçgen2:
for i in range(5, 1, -1):
  print(" "*(6-i)+"*"*i) 

#Dik Üçgen3:
for i in range(1,6):
  print(" "*(6-i)+"*"*i) 

#İkizkenar Üçgen:
for i in range(1,6):
  print(" "*(6-i)+"*"*(2*i-1)) 

#Ters İkizkenar Üçgen:
for i in range(5,0,-1):
  print(" "*(6-i)+"*"*(2*i-1))

#İkili üçgen 
for i in range(1,6):
  print("*"*i+" "*(5-i)*2+"*"*i )