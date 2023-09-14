#The Challenge:

#Your code must return true or false (not 'true' and 'false') depending upon whether the given number is a Narcissistic number in base 10. 

def narcissistic( value ):
    list_of_digits = []
    for i in str(value):
        list_of_digits.append(i)
    size = len(list_of_digits)
    num=0
    for i in list_of_digits:
        num += int(i)**size
    if num == value:
        return True
    else:
        return False
    #return False # Code away
