#strings the band



#int and float
'''
num1 = 1
num2 = 3.5
'''

numchar = '101'
#print (type(num1))

'''
print ('5 mod 3 is',5%3)
print ('quotient of 5/3 is',5//3) 
print ('num 1 is',num1)

print('anything mod 2 if ' ,2 % 2,' is even') 
print('anything mod 2 if ' ,3 % 2,' is odd')

print(round(3.142,2))

print(num1 + int(numchar))
'''

#List Tupe Sets 

#courses = ['A' , 'B' , 'C' , 'D']
#course2 = ['B', 'C', 'D']
#course3 = course2

#print(courses[-1]) # -ve index is great for getting end of a list where the size is unknown 

# print (course3)

#for w in courses:
#	if w in course2:
#		print ("to be removed  Letter", w)
#		print ("before removal", courses)
#		courses.remove(w)
#		print ("After removal", courses)
#		print ('\t {} is in course2'.format (w))

	#	courses.remove(w) 

#courses.remove(w for w in course2)

#print ('after removal',courses)

#tup = [(1, 3), (3, 2), (2, 1)]
#print(tup)
#srt = tup

#def last_elem(list):
#	return list[-1]

#for i in range(len(tup)):
#	print(tup[i],'last elem',tup[i][-1])
	#srt.append(tup[i])
#	tup.sort(key = last_elem)

#print (srt.sort( key = last_elem))


#srt2 = map (lambda n )
#print (tup)
#print (srt.sort())

#print (srt)


#for t in tup:
#	print (t[-1])

#courses.append('E')
#courses.insert(2,'c')

#print(courses)

#c2 = ['f','F']

#courses.extend(c2)
#print(courses)
#courses.pop()
#print(courses)



#def fix_start(s):
#    first_char = s[0]
#    splited_string = s.split(first_char)
#    splited_string.replace(first_char, '*')
#    output = first_char + splited_string 
#    return output

#s = 'bubble'
#first_char = s[0]
#print ('1st usama char',first_char)
#splited_string = s.strip(first_char)
#print ('splited ',splited_string)
#splited_string = splited_string.replace('b', '*')
#output = first_char + splited_string 

#print (output)

#   'mix', pod' -> 'pox mid'
#n = [1,2,3,4,5,6,7,8,9,10]
# = 'abcdweghij'
#b = 'pod'
#c = b[0:2] + a[2:] + ' ' + a[0:2] + b[2:]
#print (c)
#print (a[-3:])
#a+='AAA' 

#print (a)

# ('This dinner is not that bad!') ===> 'This dinner is good!')
#txt = ('This movie is not so bad !')

#n = txt.find('not')
#b = txt.find('bad')
#print ('not is at index {}, bad is at index {}'.format(n,b))

#if b > n:
#	new_txt = txt[0:n] + 'good' + txt[(b+3):]

#print(new_txt)

# (front_back   ('abcd', 'xy') ====>  'abxcdy')


# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
  #test(front_back('abcd', 'xy'), 'abxcdy')
  #test(front_back('abcde', 'xyz'), 'abcxydez')
  #test(front_back('Kitten', 'Donut'), 'KitDontenut')

a = 'abcd'
b = 'xy'
len_a = len(a)
len_b = len(b)
half_a = int (len_a/2)
half_b = int (len_b/2)
print(half_b)
if ((len_a % 2) == 0):
	a_front = a[0:half_a]
	a_back = a[half_a:]
else:
	a_front = a[0:half_a+1]
	a_back = a[half_a+1:]

if ((len_b % 2) == 0):
	b_front = b[0:half_b]
	b_back = b[half_b:]
else:
	b_front = b[0:half_b+1]
	b_back = b[half_b+1:]
		



print (a_front)
print (a_back)
print (b_front)
print (b_back)


print((a_front + b_front + a_back + b_back))
#print (int(7/2))

	




	




''' comprihensions ''' 

#nums = [1,2,3,4,5,6,7,8,9,10]
#my_list = []

#for n in nums:
    #my_list.append(n)
    #my_list.append(n*n)
    #if n%2 == 0:
     #   my_list.append(n)

#my_list = [n for n in nums]
#my_list = [n*n for n in nums]

#my_list = map(lambda n : n*n, nums)


# n for each n in nums if n is even
#my_list = [n for n in nums if n%2 == 0]

#my_list = filter(lambda n : n*n, nums)

# letter number (letter,num) pair for each letter in abcd and each nuber in 0123

#for l in 'abcd':
 #   for i in range (0,4):
  #      my_list.append((l,i))
   #     print (l,i)

#my_list = [(letter, num) for letter in 'abcd' for num in range (4)]

#print(my_list)


#names = ['Bruce', 'Clark' , 'Peter' , 'Logan' , 'Wade']
#heros = ['Batman', 'Superman', 'Spiderman' , 'Wolverine' , 'Deadpool']

#print (zip(names,heros))

#my_dict = {}

#for name , hero in zip (names,heros):
 #   my_dict[name] = hero

#my_dict = { name : hero for name,hero in zip (names,heros)}
#print (my_dict)


#num = [1,1,2,3,1,3,4,3,4,5,5,6,7,8,7,9,9,5]

#my_set = set()
#for n in num:
#    my_set.add(n)

#my_set = {n for n in nums}

#print (my_set) 

#def gen_fun(num):
 #   for n in num:
  #      yield n*n

#my_gen = gen_fun(num)

#my_gen = (n*n for n in num)

#for i in my_gen:
 #   print(i)

#srtd = sorted(num)
#print ('sorted var',srtd)
#print('orignal var',num)
#num.sort()

#print('orignal var after sort()',num)

#rev_srtd = sorted(num, reverse=True)
#print(rev_srtd)

#tup = (9,1,8,2,7,3,6,4,5)
#print (tup)
#s_tup = sorted(tup)
#print (s_tup)

#di = {'name':'Harry', 'job':'wizard', 'age': None , 'os':'Linux'}
#s_di = sorted(di)
#print (s_di)

#li = [-5,-3,-1,0,1,3,5]
#s_li = sorted(li)
#print (s_li)
#s_li = sorted(li,key=abs )
#print (s_li)

#class Employee():
 #   def __init__(self, name, age, salary):
  #      self.name = name
   #     self.age = age 
    #    self.salary = salary

    #def __repr__(self):
     #   return '({},{},${})'.format(self.name,self.age,self.salary)


#e1 = Employee('Jimmy',25,100000)
#e2 = Employee('Sheen',24,75000)
#e3 = Employee('Carl',24,60000)

#employees = [e1,e2,e3]
#print (employees)        


#def e_sort(emp):
 #   return emp.salary

#srtd_emp = sorted(employees, key=e_sort)

#srtd_emp = sorted(employees, key=lambda e: e.name)

#from operator import attrgetter

#srtd_emp = sorted(employees, key=attrgetter('age'))

#print = (srtd_emp)











'''FORMATTING'''



#person = {'name':'Li','age':21}

#sentence = 'My name is {}, and Im {}'.format(person['name'],person['age'])

#sentence = 'My name is {0}, and Im {1}'.format(person['name'],person['age'])

#sentence = 'My name is {0[name]}, and Im {1[age]}'.format(person,person)

#sentence = 'My name is {0[name]}, and Im {0[age]}'.format(person)

#lis = ['li',22]

#sentence = 'My name is {0[1]}, and Im {0[1]}'.format(lis)

#print (sentence)

#class Person():

#    def __init__(self, name , age):
#        self.name = name 
#        self.age = age

#p1 = Person('Jaxk','33')

#sentence = 'My name is {0.name}, and Im {0.age}'.format(p1)

#print (sentence)


#sentence = 'My name is {name}, and Im {age}'.format(name = 'Jen' ,  age = 22)

#print (sentence)


#person = {'name':'Li','age':21}

#sentence = 'My name is {name}, and Im {age}'.format(**person)

#print (sentence)


#for i in range(10):
 #   sen = 'Value of i is {:02}'.format(i)
  #  print (sen)

#pi = 3.14159265

#pis = 'Pi is = {:.2f}'.format(pi)

#print (pis)

#sen = '1MB is = {:,.2f}'.format(1000**2)
#print (sen)

#import datetime 
#date = datetime.datetime (2016, 9, 24, 12, 30, 45)
#ds = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(date)

#print(ds)







''' ############## OS ############## '''

#from operator import mod
#import os

#print (os.getcwd())

#os.chdir('')

#print (os.listdir())

#os.mkdir('folder')
#os.makedirs('folder/sub-folder') #preffered

#print (os.listdir())

#os.rmdir('folder') #preffered
#os.removedirs('folder/sub-folder')

#os.rename('folder','folder2')

#print (os.stat('folder2'))
#print (os.listdir())
#from datetime import datetime

#mod_time = os.stat('folder2').st_mtime
#print(datetime.fromtimestamp(mod_time))

#for dirpath, dirname, filename in os.walk('d:\Py_playlist\P1'):
 #   print ('Current Path:', dirpath)
  #  print ('Directories:',dirname)
   # print ('Files',filename )
    
#print(os.environ.get('waqars2'))
#os.chdir('C:\Users\waqars2\Desktop')
#os.chdir('C:\Users\waqars2\Desktop')

#print (os.getcwd())

#fpath = os.getcwd() + 'test.txt'
#print (fpath) 

#fpath2 = os.path.join(os.getcwd()), 'test.txt'
#print (fpath2) 
#print (os.path.basename('C:\Users\waqars2\Desktop'))


'''############## FILE HANDLING #################'''

#f = open("test.txt", "r") #reading
#f = open("test.txt", "w") #writing
#f = open("test.txt", "a") #appending
#f = open("test.txt", "r+") #read & write
#print(f.name)
#print(f.mode)
#f.close()

'''############### Reading Files ##############'''
#with open("test.txt", "r") as f:
	#pass
	#Small Files:
	#f_contents = f.read()
	#print(f_contents)
	#Big Files:
	#f_contents = f.readlines()
	#print(f_contents)
      ###With the extra lines:
	#f_contents = f.readline()
	#print(f_contents)
	#f_contents = f.readline()
	#print(f_contents)

#with open("test.txt", "r") as f:
    ###Iterating through the file:
	#for line in f:
	#	print(line, end = '')

#with open("test.txt", "r") as f: 
#######Without the extra lines:
	#f_contents = f.readline()
	#print(f_contents, end = '')
	#f_contents = f.readline()
	#print(f_contents, end = '')

#with open("test.txt", "r") as f:
######Printing by characters:
	#f_contents = f.read(100)
	#print(f_contents, end = '')
	#f_contents = f.read(100)
	#print(f_contents, end = '')
	#f_contents = f.read(100)
	#print(f_contents, end = '')


#with open("test.txt", "r") as f:
	###Iterating through small chunks, with 10 characters:
#	size_to_read = 10
#	f_contents = f.read(size_to_read)
#	print(f_contents, end = '')
#	f.seek(0)
#	f_contents = f.read(size_to_read)
#	print(f_contents, end = '')
#	print(f.tell())
#	while len(f_contents) > 0:
#		print(f_contents, end = '*')
#		f_contents = f.read(size_to_read)
#print(f.mode)
#print(f.closed)
#print(f.read())
	

'''##Writing Files:'''



###The Error:
#with open("test.txt", "r") as f:
	#f.write("Test")

###Writing Starts:

#with open("test2.txt", "w") as f:
	#pass
#	f.write("Test")
#	f.seek(0)
#	f.write("Test")
#	f.seek("R")

##Copying Files:
#with open("test.txt", "r") as rf:
#	with open("test_copy.txt", "w") as wf:
#		for line in rf:
#			wf.write(line)

#Copying the/your image:
###The Error
#with open("bronx.jpg", "r") as rf:
	#with open("bronx_copy.jpg", "w") as wf:
		#for line in rf:
			#wf.write(line)

###Copying the image starts, without chunks:.

#with open("Reanimation.jfif", "rb") as rf:
#	with open("Reanimation2.jfif", "wb") as wf:
#		for line in rf:
#			wf.write(line)

###Copying the image with chunks:
#with open("bronx.jpg", "rb") as rf:
	#with open("bronx_copy.jpg", "wb") as wf:
		#chunk_size = 4096
        #rf_chunk = rf.read(chunk_size)
        #while len(rf_chunk) > 0:
            #wf.write(rf_chunk)
            #rf_chunk = rf.read(chunk_size)
