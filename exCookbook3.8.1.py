#处理分数计算
from fractions import Fraction
a = Fraction(5,4)
b = Fraction(7,16)
print(a + b)
print(a * b)
c = a * b
print(c.numerator,c.denominator)
print(float(c))
print(c.limit_denominator(8))
#小数转分数
x = 3.75
y = Fraction(*x.as_integer_ratio())
print(y)