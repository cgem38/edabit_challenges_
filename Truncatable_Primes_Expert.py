import numpy as np

def truncatable(n):

    narray = np.array([int(x) for x in str(n)])
    
    #First check for zeros
    for ii in range(len(narray)):
       
        if narray[ii] == 0:
            return False
            break
        else:
            continue

 #left-truncatable prime check function:
    def leftcheck(narray):
        
        leftint = narray

        for ii in range(len(leftint)):
            
            leftstring = str(leftint)
            test = isprime(int(''.join(map(str, leftint))))
            
            if test == False:

                return False 
                break

            else:
                
                leftint = leftint[1:]
                continue
        return True
    
    #right-truncatable prime check function:
    def rightcheck(narray):

        rightint = narray

        for ii in range(len(rightint)):
            
            rightstring = str(rightint)
            test = isprime(int(''.join(map(str, rightint))))

            if test == False:

                return False 
                break
            else:
                
                rightint = rightint[:-1]
                continue
        return True

    #prime check function

    def isprime(num):
        ii = 2

        if num == 1:
            return False

        while ii <= num / 2:

            if num % ii == 0:
                return False
            else: 
                ii = ii + 1
                continue
                
        return True

    #Assess left and right truncatable primes

    left = leftcheck(narray)
    right = rightcheck(narray)
    
    #Conditions to determine what to return
    
    if left == True and right == True:

        result = "both"

    elif left == True and right == False:

        result = "left"

    elif right == True and left == False:
        
        result = "right"
    else:
        
        result = False
    
    return result
    


print(truncatable(347))
