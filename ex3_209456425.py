''' Exercise #3. Computational Thinking and Programming.'''

#########################################
# Question 1 - do not delete this comment
#########################################
lst = [1,2,3,4,5,5,"fff"]
lst2=[]
i=0
if len(lst)!=0:
    for x in lst:
         lst2.append(i)
         i+=1
print (lst2)        



#########################################
# Question 2 - do not delete this comment
#########################################
lst = ["b","a","r"]
print (lst[::-2])



#########################################
# Question 3 - do not delete this comment
#########################################
lst = [2,5,8,1,5,6]
sum1=0
for x in lst:
    if x%2==0:
        sum1+=x
print ("List’s even numbers sum is:", sum1)    



#########################################
# Question 4 - do not delete this comment
#########################################
x = "ba"
lst = ["baz",1,2,"bar"]
if x in lst:
    print (True)
else:
    print (False)



#########################################
# Question 5 - do not delete this comment
#########################################
lst = [1, 5.4, 7]
new_lst= lst
if len(lst)>7:
    new_lst=lst[:7:]
elif len(lst)<7:
    while len(lst)<7:
        new_lst.append(0)
        
print ("New list is", new_lst, sep="\n")


