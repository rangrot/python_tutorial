# list data structure in python
# a list can be made up of a single data type or multiple data types- woah !

# this is an empty list
emptyList = []
print(emptyList)

# this is a list of integers
listOfIntegers = [1,2,3]
print(listOfIntegers)

# this is a list of multiple data types
listOfAll = [1,1.5,"String"]
print(listOfAll)

# individual elements can be accessed normally
print(listOfIntegers[1],listOfAll[2])

# to delete an element
del listOfIntegers[1]
print(listOfIntegers)
# or remove pop also work

# to delete the entire list
del emptyList
#print(emptyList)

# tuple data structure in python
# works similar to a list but its immutable- cannot change the elements once they are defined
# the syntax is a little different instead of square brackets in list use circular brackets ()

daysOfWeek = ("Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
print(daysOfWeek)

# can print single element like a normal list
print(daysOfWeek[1])

# this is a neat trick, this will print Saturday
print(daysOfWeek[-1])
# this will also print Saturday
print(daysOfWeek[6])

# a single element of a tuple cannot be deleted.
# but the entire tuple can be deleted
del daysOfWeek

# string data structure
# string ca be created in a bunch of ways

myString = "String in double quotes"
print(myString)

myString = 'String in single quotes'
print(myString)

myString = '''String in comments style'''
print(myString)

myString = """String 
                spanning
                    multiple
                        lines"""
print(myString)




