#密集型数组计算任务使用NumPy库
x = [1,2,3,4]
y = [3,5,6,8]
print (x * 2)
print(x + y)
import numpy as np 
ax = np.array([1,2,3,4])
bx = np.array([3,4,6,8])
print(ax * 2)
print(ax + 10)
print(ax + bx)
print(ax * bx)

print(np.sqrt(ax))
print(np.cos(ax))

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) #3 * 4
print (a)
print(a[1])
#获取第2列
print(a[:,1])
c = a[1:3,1:3]
print(c)
#选取其中一部分并改变值
a[1:3,1:3] += 10
print(a)
print(a + [100,101,102,103])
print(a)
print(np.where(a< 10,a,10))
print(a)
