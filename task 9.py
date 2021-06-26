# To merge two dictionary
d1 = {'a': 10, 'b': 20}
d2 = {'x': 30, 'y': 20}
d = d1.copy()
d.update(d2)
print(d)
#To sort the value from descending to ascending
c= ('23','2','1','76')
d = sorted(c, reverse=True)
print(d)
#To convert the list into set
x = set(d)
print("The set:",d)
#To count the items in list
c =  {'x': ['5', '2', '3'], 'A': ['1', '5']}
ctr = sum(map(len, c.values()))
print("Number of items in list:",ctr)
w = sorted(c)
print("The sorted list is:",w)
# To sort them without using builtin function
my_list = [4,8,17,3,1,-3,-27]
new_list = []

while my_list:
    min = my_list[0]  
    for x in my_list: 
        if x < min:
            min = x
    new_list.append(min)
    my_list.remove(min)    

print( "The sorted list:",new_list)
#To replace the string from the given string
x = str(input("Enter the string:"))
y = str(input("Enter the letter to be replaced:"))
z = x.replace(x[0],y)
print (" The replaced string:",z)
#To captalize the given string
string = str(input("Enter the string:"))

capitalized_string = string.title()

print('Old String: ', string)
print('Capitalized String:', capitalized_string)
#To find the repeated items
myList = [9, 1, 5, 9, 4, 2, 7, 2, 9, 5, 3]
occurrences = []
 
for item in myList :
    count = 0
    for x in myList :
        if x == item :
            count += 1
    occurrences.append(count)

duplicates = set()
index = 0
while index < len(myList) :
    if occurrences[index] != 1 :
        duplicates.add(myList[index])
    index += 1

print("The repeated items:",duplicates)
#To check the given condition
a= 10
b= 20
c = 30
d = a+b+c
print("The sum:",d)
f= int(input("Enter the number:"))
quotient = d/f
print ("The Quotient:",quotient)
#To find mean
n_num = [2,  5, 2] 
n = len(n_num) 
  
get_sum = sum(n_num) 
mean = get_sum / n 
  
print("The Mean is: " + str(mean))
#To find the Median
n_num = [2,5,2] 
n = len(n_num) 
n_num.sort() 
  
if n % 2 == 0: 
    median1 = n_num[n//2] 
    median2 = n_num[n//2 - 1] 
    median = (median1 + median2)/2
else: 
    median = n_num[n//2] 
print("Median is: " + str(median)) 

from collections import Counter 
  
# list of elements to calculate mode 
n_num = [2,5,2] 
n = len(n_num) 
  
data = Counter(n_num) 
get_mode = dict(data) 
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))] 
  
if len(mode) == n: 
    get_mode = "No mode found"
else: 
    get_mode = "Mode is / are: " + ', '.join(map(str, mode)) 
      
print(get_mode) 
#To swap case the string
txt= "DHoNI"
x = txt.swapcase()
print(x)
#To convert the integer into binary and octal decimal
r = int(input("Enter the integer:"))
y = bin(r)
print("The equivalent Binary number:",y)
z = oct(r)
print("The Equivalent octa decimal number
