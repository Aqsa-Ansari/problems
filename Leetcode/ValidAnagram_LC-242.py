s = "ratc"
t = "cat"

def ValidAnagram():
    #### SOLUTION-1 ####
    # return sorted(s) == sorted(t)


    #### SOLUTION-2 ####
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] = d[c]+1
    # print(d)

    for c in t:
        if c not in d:
            return False
        else:
            if d[c] == 1:
                d.pop(c)
            else:
                d[c] = d[c]-1

    # print(d)
    if bool(d):
        return False
    return True