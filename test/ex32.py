the_count =[1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dinners',3,'quartes']

for number in the_count:
    print ("THis is count %d"%number)

for fruit in fruits:
    print ("A fruit of type:%s"%fruit)

for i in change:
    print ("I got %r"%i)

element=[]
for i in range(0,6):
    print("Adding %d to the list."%i)
    element.append(i)

for i in element:
    print ("Element was :%d"%i)