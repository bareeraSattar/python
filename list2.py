square =[]
for x in range(10):
    square.append(x**2)
    print(x)
square =[x**2 for x in range(10)]
print (square)
even = [x for x in range(20)if x%2==0]    
print(even)