def sort_dictionary(input):
    listData = []
    for k,v in input.items():
        listData.append((v[1],k,v[0]))
    listData = sorted(listData)
    ans = [(item[1],item[2]) for item in listData]
    return ans
