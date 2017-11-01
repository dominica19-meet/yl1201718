
'''
anything=input("Input number")

a=[1,1,2,3,5,8,13,21,34,55,89]
e=[]
for i in a: 
	if i < anything:
		e.append(i)
print (e)		
'''

a=[1,1,2,3,5,8,13,21,34,55,89]
b=[1,2,3,4,5,6,7,8,9,10,11,12,13]
c=[]
for i in a:
	for r in b:

		if i == r:
			if i in c:
				pass
			else:
				c.append(i)

				
			

		
print (c)		





