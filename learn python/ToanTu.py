# gan hai bien
a = 2
b = 60
# cong, tru, nhan, chia, chia lam tron, modulo, luy thua
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

from decimal import Decimal, getcontext

# dat so chu so sau dau thap phan
getcontext().prec=50002
# tinh 10^50000
result = Decimal(a) ** Decimal(b) - 1
print("mu: ",result, type(result))

# toan tu gan
a += 4
b -= 4

# toan tu so sanh
print(a>b)

print('a=b: ', a==b)
print('a!=b', a != b)

# toan tu logic
print((a == b) or (a != b))
print((a == b) and (a != b))
print(not (a != b))

# toan tu bitwise
x = 10      # 0000 1010
y = 4       # 0000 0100

print(x&y)  # 0000 0000
print(x|y)  # 0000 1110
print(~x)   # 1111 0101
print(x^y)  # 0000 1110
print(x>>2) # 0000 0010
print(x<<2) # 0010 1000
# x, y sau bitwise giu nguyen
print(x)
print(y)

# toan tu nhan dang identity 'is' 'is not'
x1 = 5
y1 = 5
x2 = 'hi'
y2 = 'hi'
x3 = [1,2,3]
y3 = [1,2,3]

print(x1 is not y1)
print(x2 is y2)
print(x3 is y3)

# toan tu thanh vien(membership) 'in' 'not in'
x = 'Hello world'
y = {1:'a', 2:'b'}

print('H' in x)  
print('hello' not in x)  
print(1 in y) 
print('a' in y) 
