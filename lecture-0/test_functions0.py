def add_numbers(a,b):
    global x1
    x1=a+b # Variable local
    return x1

x1=45.0
x2=-37.8
result=add_numbers(x1,x2)
print(result)
print(x1)

