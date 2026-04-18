def cod(x, y):
    x.replace(" ", "")
    y.replace(" ", "")
    
    if(len(y) != len(x)):
        print("not anagram")
        return
    
    z = {}
    
    for i in range(len(x)):
        if(x[i] in z):
            z[x[i]] += 1
        else:
            z[x[i]] = 1
    
    for i in range(len(y)):
        if(y[i] in z):
            z[y[i]] -= 1
        else:
            print("not anagram")
            return

    for i in z.values():
        if i != 0:
            print("not anagram")
            return
    print("anagram")
        
cod("sixseven", "nevseisx")
