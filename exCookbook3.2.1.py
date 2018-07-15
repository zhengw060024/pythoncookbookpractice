#执行精确的小数计算
a = 4.2
b = 2.1
print(a + b)
print((a + b) == 6.3)
#如果期望得到更高的精度，并愿意牺牲一些性能，可以使用decimal模块
#注意数字是以字符串的方式表示
#该模块主要用在金融模块中。
from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
print(a + b)
print((a + b) == Decimal('6.3'))