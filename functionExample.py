#Declare a function

def countSeconds(hours, minutes, seconds):
  hrs=3600*hours
  mts=60*minutes
  scds=seconds
  return hrs+mts+scds
  
  
#Call a function with values

a = countSeconds(2,30,0)
b = countSeconds(0,45,15)


#Print the outcome of calculation

print("First seconds are " + str(a))
print("Second seconds are " + str(b))

print("Total seconds are " + str(a+b))



