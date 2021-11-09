l1=['a','b','c']
l2=[1,2,3]
dict={}
for i in l1:
    for j in l2:
        if i in dict:
            dict[i]=dict[i]+1
        else:
            dict[i]=1
            print(dict)

