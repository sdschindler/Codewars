#7kyu
def get_middle(s):
    for i in s:
        n = len(s)
        if len(s) % 2 != 0:
            
            return s[int(n/2)]
        else:
            return s[int(n/2)-1:int(n/2)+1]
