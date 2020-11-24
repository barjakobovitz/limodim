#ex 1
#Donuts=float(input("How much donuts: "))
#x= "x",5
#if(Donuts<5):
#    print ("Number of donuts: Want more")
#elif (Donuts<10):
#    print ("Number of donuts:", Donuts, "...")
#else:
#    print ("Number of donuts: a lot!")
#print (x)

name1= input("what is your name? ")
name2= input("what is your name? ")
name3= input("what is your name? ")

if name1==name2==name3:
    print(name1+"!")
elif name3[0] in name2:
    print (name2[-1], name3[-1])
elif (name1<name2):
      if (len(name2)<=len(name1)):
          print (name2)
      else:
        print (name1)
    

    
