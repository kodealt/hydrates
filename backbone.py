# helper file for the necissary changes

import math
import numpy

import elements

elements = elements.Elements()

def splitElements(compound): # return a list
    soloElements = []
    tmp = ""
    for i, j in enumerate(compound):
        if j.isupper():
            tmp += j
            try:
                if compound[i+1].isupper():
                    soloElements.append(tmp)
                    tmp = ""
            except:
                continue
        else:
            if isInt(j): 
                continue
            k = i
            tmp += j
            try:
                while isInt(compound[k]):
                    tmp += compound[k]
                    k+=1
            except:
                continue
            soloElements.append(tmp)
            tmp = ""

    if len(tmp) != 0:
        soloElements.append(tmp)
        
    print(soloElements)
    return soloElements
        


def isInt(char):
    try:
        k = int(char)
        return True
    except:
        return False

def countElements(compound):
    counts = {}
    tmp = ""
    scalar = 1
    k = splitElements(compound)
    for u in k:
        c = 0
        try:
            while isInt(u[c]) == False:
                c+=1
        except:
            continue

        counts[u[:c]] = int(u[c:]) if len(u[c:]) != 0 else 0


        # if isInt(u[-1*c:]):
        #     counts[u[:-1*c]] = int(u[-1*c:])

        # else:
        #     counts[u] = 0

    return counts


def balance(eq):
    parts = eq.split('->')
    left, right = parts[0], parts[1]
    left = [k.strip() for k in left.split('+')]
    right = [k.strip() for k in right.split('+')]

    # print(left)
    # print(right)

    counted_L = [countElements(l) for l in left]
    counted_R = [countElements(l) for l in right]

    print(counted_L)
    print(counted_R)


balance("H2O + CO2 -> C6H12O2")
    
