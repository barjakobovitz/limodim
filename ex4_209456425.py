''' Exercise #4. Computational Thinking and Programming.'''

#########################################
# Question 1 - do not delete this comment
#########################################
n = 7
i=0
for elem in range(2,n):
    if (n%elem==0):
        print  (n,"is NOT a prime number")
        i=i+1
        break
if (i==0):
    print (n, "is a prime number")
        


#########################################
# Question 2 - do not delete this comment
#########################################
m = 0
n = 2
sum1=0
num=0
big= max(m,n)
mini= min(m,n)
for elem in range (mini+1,big):
    if (elem%2!=0):
        sum1+=elem
        num+=1
if num>=1:
   avg=(sum1/num)
   print (avg)
else:
    print (0.0)
#########################################
# Question 3 - do not delete this comment
#########################################
p = 3
i=0
listr=list(range(1,p+1))
listr.reverse()

for elem in listr:
    while i<elem:
        print (elem,sep="" ,end="")
        i+=1
    i=0
    print("\n")


#########################################
# Question 4 - do not delete this comment
#########################################
lst4 =  [0, 5.4, 0, 7, 6, 8.1, 3, 6, 0, 3]
new_list=[]
i=0
for elem in lst4:
    for elem2 in new_list:
        if (elem==elem2):
            i+=1
            break
    if (i==0):
         new_list.append(elem)
    i=0
print (new_list)





#########################################
# Question 5 - do not delete this comment
#########################################
lst5 = ["hi","ho", "do", "you", "copy"]
len5 = len(lst5)
i=0
for x in range(len5-1):
    if (lst5[x]==lst5[x+1]):
        i+=1
        print (lst5[x])
if i==0:
    print("No repetitions were found!")

