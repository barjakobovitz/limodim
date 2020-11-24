# ex1
list1=[1,2,3,4,5]
print(sum(list1)/len(list1))
          
#ex2
for i in range(1,11):
    for x in range (1,11):
        if x!=10:
            print (i*x, end="\t")
        else:
            print (i*x)

#ex3
l=[[2,4],[5,1],[6,0]]
avg=0
len1=0
for i in l:
    avg+=sum(i)
    len1+=len(i)

print (avg/len1)
