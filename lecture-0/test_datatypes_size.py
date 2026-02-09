from sys import getsizeof

num1=1e300
print(getsizeof(num1))
print(type(num1))

num2=int(num1)
print(getsizeof(num2))

bool1=True
print(getsizeof(bool1))
