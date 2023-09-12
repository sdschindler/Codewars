#You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

def find_outlier(integers):
    odd = 0
    even = 0
    even_out = 0
    odd_out = 0
    for i in integers:
        if i % 2 == 0:
            even += 1
            even_out = i
        else:
            odd += 1
            odd_out = i
    if odd > even:
        return even_out
    else:
        return odd_out
        
