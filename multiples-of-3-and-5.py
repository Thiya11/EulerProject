
#Initializing array for add multiples of 3 and 5.
x = []

#method to sum up all the multiples of 3 and 5

def reducing():
    total = 0
    for k in x:
       total= total + k
    print(total)
    
#method to push all the multiples of 3 and 5 into the array x

def adding(numrange):
    total = 1
    for i in range(int(numrange)):
       if(((i%3 == 0) or (i%5 == 0)) and i != 0):
          x.append(i)
    reducing()
          
#apply the range as a parameter to sumup numbers.
adding(1000)

