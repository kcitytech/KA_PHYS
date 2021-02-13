#!/usr/bin/env python3
# Exercise 2.7

def catalan(n):	
    
    # Base case.
    if n == 0:
        return 1
    
    # Cast to return as integer instead of floating point number.
    return int((((4*(n-1))+2)/(n+1))*catalan(n-1))

def promptCatalanInput():
    
    # Prompt for input.
    return int(input("Catalan(n):"))

def unitTest():

    # Unit Testing first 30 values using OEIS A000108 (https://oeis.org/A000108/list) 
    expected = [1,1,2,5,14,42,132,429,1430,4862,16796,58786,
                208012,742900,2674440,9694845,35357670,129644790,
                477638700,1767263190,6564120420,24466267020,
                91482563640,343059613650,1289904147324,
                4861946401452,18367353072152,69533550916004,
                263747951750360,1002242216651368,3814986502092304]
        
    results = [catalan(index) for index in range(0,30+1)]
    assert(expected == results)

# Prompt user for input.
print(catalan(promptCatalanInput()))

# Perform unit test to validate.
unitTest()