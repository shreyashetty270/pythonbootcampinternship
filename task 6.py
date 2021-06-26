#python script to merge two dictionaries
def Merge(dict1 , dict2):
    s = {**dict1 ,** dict2}
    return s

dict1 = {"shreya":"shetty","shradha":"gowda","nidhi":"naik"}
dict2 = {"kim":"sharma","khloe":"kardash","katrina":"kaif"}
dict3 = Merge(dict1 , dict2)
print(dict3)


#removing a key from dictionaries
dict7={"vicky":"kaushal","amir":"khan","selena":"gomez"}
dict7.pop("selena")
print(dict7)


# program to map two list into dictionary
lst1 = []
sin = []
n = int (input("enter the number of elements for dictionaries:"))
print("For keys:")
for x in range(0,n):
    element = input("enter element" + str(x+1) + ":")
    lst1.append(element)
print("For values:")
for x in range(0,n):
    element = input("enter element" + str(x + 1) + ":")
    sin.append(element)
d = dict(zip(lst1,sin))
print("the dictionary is:")
print(d)


#program to find length of set
dict4 = {"shreya":5,"wuya":6,"aish":8,"pooja":9}
print("length of set:",len(dict4))


#removing intersection of 2nd set from 1st set:
print("removing intersection of 2nd set from 1st set:")
d1= {1,2,3,4,5}
d2= {2,3,8,6,4}
print("original set:")
print(d1,"\n",d2)

d1.difference_update(d2)
print("set 1 : " , d1)
print("set 2 :", d2)