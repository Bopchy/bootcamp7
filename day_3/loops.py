a = [10, 40, 6, 9, -5, 4, 3, 7, 8,'']

'''for i in a:
	print i  

# print in reverse 

i = len (a)


while i > 0: 
	print a [i-1]
	i -= 1

for num in range (len (a) - 1, -1): #the second -1 is because you want the length to go up to zero
	print a[i]
'''
b = [(2,4), (5,10), (6,20), (50,50)]

'''
Make b appear as below
x:2, y:4
x:5, y:10

'''
for a in b:
	print "x:{}, y:{}".format(*a)

c = [(2,4,1), (5,10,2), (6,20,3), (50,50,4)]
for j in c:
	print "x:{}, y:{}, z:{}".format(*j) 



def all_add (a, *args):

	'''
		Takes in a list with variably sized tuples 
		and outputs as follows:  
		x:10, y:20, z:30
		x:11, y:40
		x:60
		x:5, y:6, z: 7

	'''




f = [(10,20,30), (11, 40), (60), (5, 6, 7)]


