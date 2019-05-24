# python supports int float and complex data types
# boolean is a sub class of int

# will print <class 'int'>
print(type(5))

# will print <class 'float'>
print(type(5.0))

val = 2 +3j
# will print <class 'complex'>
print(type(val))

# type conversion is handled by default
# python converts from small to large data type automatically to avoid loss of data
num = 2
flt_num = 3.5
sum = num + flt_num
print("sum =",sum,type(sum))

# python can do explicit conversion as well
# this is needed while dealing with num type and string
a = 22
b = "555"

# explicitly cast to integer
b_int = int(b)
# explicitly cast to string
a_str = str(a)

val_int = a + b_int
val_str = b + a_str

# will add the numbers and print 577
print("val_int =",val_int)
# will cncat the strings and print 55522
print("val_str =",val_str)
