x = eval(input("Enter x : "))
y = eval(input("Enter y : "))
result = """
x   = { :.2f}
y   = {:.2f}
x+y = {:.2f}
x-y = {:.2f}
x*y = {:.2f}
x/y = {:.2f}
""".format(x,y,x+y,x-y,x*y,x/y)
print(result)
