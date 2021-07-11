#To create merged list of tuples
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd']

new_list = list(zip(list1, list2))

print(new_list)
#To merge the list and range together
lst1=["A", "B", "C", "D", "E", "F", "G","H","I"]
x= range(1,9)
lst=list(zip(lst1,x))
print(lst)
#To sort the list in ascending order
numbers = [6, 9, 3, 1]
x= sorted(numbers)
print(x)
#To filter even numbers from the list
x= [ 1, 2, 4, 5, 7, 8, 9, 10, 12,34,76,57] 
y= filter(lambda x: x % 2 == 1, x)
print("The new list:",list(y))
