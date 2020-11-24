#ex1
a=5
b=2
c=((a**2)+(b**2))**0.5
area= (a*b)/2
circum= a+b+c
print(c, area, circum)
#ex2
s="bar"
sum= len(s)
mid= sum//2
mid_letter= s[mid]
up_mid_letter=mid_letter.upper() #big letter
print (up_mid_letter) 
new_string= s[0:mid]+up_mid_letter+s[mid+1:]
print(new_string)
