#print(x[::3])
#print('123'.rjust(5,"*"))
l1='Python is easy to learn'.split()
#print(*l1)

x=[1,2,3]
y=[3,4,5]
#print(*set(x+y))

x=20
if x<10:
    if x<5:
        print("Number less than 5")
    else:
        print("Number greater than 5")
else:
    print("Number greater than 10")

colors=['violet','indigo','red','blue','green','yellow']
colors2=filter(lambda x:len(x)==5,colors)
#print(list(colors2))

colors=['Violet','Indigo','Blue','Green','Yellow','Orange','Red']
#for index,item in enumerate(colors):
    #print(item,"occurs at index",index)


(a,b,c,d)=range(4)
#print(a,b,c,d)

numbers=dict([('English','One'),('Spanish','Uno'),('German','Ein')])
#print(numbers)

import re
regex=re.compile(r'[crbmdhw]ash')
print(regex.findall('cash rash bash mash dash hash wash crash ash'))

