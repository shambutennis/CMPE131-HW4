def cacti_number(res):
    dirs = [[0,1],[0,-1],[1,0],[-1,0]]
    l = len(res)
    r = len(res[0])
    ans = 0
    for i in range(l):
        for j in range(r):
            if res[i][j]==0:
                canPlant = True
                for d in dirs:
                    x,y = i+d[0],j+d[1]
                    if x>=0 and x<l and y>=0 and y<r:
                        if res[x][y]==1:
                            canPlant = False
                if canPlant:
                    res[i][j]=1
                    ans+=1
    return ans

