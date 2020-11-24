#תרגיל 1
the_sum=0
count=0
while count<10:
    i=int(input("number: "))
    if i>0:
       the_sum = the_sum+i
    count=count+1
print (the_sum)   

#תרגיל 2
numbers_list=[1,2,7,19,-9]
the_sum=0
for x in numbers_list:
    the_sum+=x
print (the_sum)    
