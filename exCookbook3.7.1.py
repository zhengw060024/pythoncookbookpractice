
#处理无穷大和NaN
import math
a = float('inf')
b = float('-inf')
c = float('nan')
print(a,b,c)
#要检测是否出现了这些值可以使用math.isinf和math.isnan函数
print(math.isinf(a))
print(math.isnan(c))
#无穷大值会在计算中传播
print(a + 45)
print(a * 10)
print( 10 / a)
#但是某些操作导致未定义的行为，并产生NaN
print (a /a)
print (a + b)
#NaN会通过所有的操作进行传播，并且不会引发异常
#NaN 在做比较的时候从不会被判定为相等。
d = float('nan')
print( c == c)
print( c is d)