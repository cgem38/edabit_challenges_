import math as math
import numpy as np
import matplotlib as plot
import socket

def longest_substring(digits):
    integer = np.array([int(x) for x in digits])
    length = len(digits)
    even1 = np.zeros(length)
    substrings = np.array([0])
    ministrings = np.array([0])
    
    for ii in range(length): 
        
        if integer[ii] % 2 == 0: 
            even1[ii] = 1
        else:
            even1[ii] = -1

        if ii == 0:
            ministrings[0] = integer[ii]
            continue

        else: 
            pass
        
        altcheck = even1[ii] * even1[ii-1] #checks for alternating even/odd

        if altcheck < 0:
            ministrings = np.append(ministrings, integer[ii])

        elif altcheck > 0 and len(ministrings) >= 2:
            substrings =  np.append(substrings, int(''.join(map(str, ministrings))))
            ministrings = np.array([integer[ii]])
        elif altcheck > 0 and len(ministrings) < 2:
            ministrings = np.array([integer[ii]])
            
    substrings =  np.append(substrings, int(''.join(map(str, ministrings))))
    print(substrings[1:])
    substringarray = max(np.array([str(x) for x in substrings[1:]]), key = len)
    return substringarray

print(longest_substring("844929328912985315632725682153"))
