''' Exercise #2. Computational Thinking and Programming.'''

#########################################
# Question 1 - do not delete this comment
#########################################
number = int(input("Please enter a number: "))
if number%3==0:
    print (f"I am {number} and I am a multiplication of 3")
else:
    print(f"I am {number} and I am not a multiplication of 3")


#########################################
# Question 2 - do not delete this comment
#########################################
number = int(input("Please enter a number: "))
if number%2==0:
    print ("Even number")
elif number%3==0:
    print ("Divisible by 3")
if len(str(number))%2!=0:
    print ("Odd number of digits")


#########################################
# Question 3 - do not delete this comment
#########################################
grade = 88
if grade<0 or grade>100:
    grade= "Illegal grade"
    print(grade)
elif grade<60:
    grade= "F"
    print(grade)
elif grade<70:
    grade= "D"
    print(grade)
elif grade<80:
    grade= "C"
    print(grade)
elif grade<90:
    grade= "B"
    print(grade)
elif grade<=100:
    grade= "A"
    print(grade)
    




#########################################
# Question 4 - do not delete this comment
#########################################
my_str = "bar"
my_str= my_str.lower()
my_str_len= len(my_str)
if my_str==(my_str[::-1]):
    print(True)
else:
    print (False)
    




