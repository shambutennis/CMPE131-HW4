
def merge(a,b):
    i,j = 0,0
    ans = []
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            ans.append(a[i])
            i+=1
        else:
            ans.append(b[j])
            j+=1
    if i<len(a):
        ans.extend(a[i:])
    else:
        ans.extend(b[j:])
    return ans

        