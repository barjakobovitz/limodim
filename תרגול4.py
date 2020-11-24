#ex1
lst=["what","is","The","matrix","neo"]
a=1
z=3
low= min(a,z)
high= max(a,z)
new_list= sorted(lst[low:high+1], key=str.lower)
print (lst)
print (new_list)

#ex2
phone_book=[["bar","0545900961"],["zvi","0545680300"]]
name="zvi"
found= False
phone= ""
for contact in phone_book:
    if contact[0]==name:
        found=True
        phone=contact[1]
    if found==True:
        print ("name: ", contact[0], "phone: ", contact[1])
        break
if found==False:
    print ("didnt found")
    
