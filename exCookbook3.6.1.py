#复数计算
a = complex(2,4)
b = 3 - 5j
print(a)
print(b)
print(a.real,b.real)
print(a.conjugate())
print(a +b)
print(a*b)
print(a /b)
print(abs(a))
#如果要执行有关复函数的操作，可以使用cmath
import cmath
print(cmath.sin(a))
print(cmath.cos(a))
print(cmath.exp(a))

import numpy as np 
a = np.array([2+3j,4+5j,6-7j,8+9j])
print(a)
print(a + 2)
print(np.sin(a))

#python的标准函数不会产生复数，如果希望产生复数的结果，要使用cmath函数
print(cmath.sqrt(-1))