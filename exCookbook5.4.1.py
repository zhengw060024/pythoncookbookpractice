#读写二进制数据
#使用open函数的rb和wb模式就可以实现对二进制文件读写
#如果需要在二进制文件中读取或写入文本内容，要确保进行编码操作。
with open('somefile.bin','wb') as f:
    text = 'Hello world!';
    f.write(text.encode('utf-8'));
with open('somefile.bin', 'rb') as f:
    data = f.read();
    #注意在以字节流遍历时字节串返回代表该字节整数值而不是字符串
    for item in data:
        print(item)
    print(data)
    text = data.decode('utf-8');
strTemp = 'Hello world!'
for item in strTemp:
    print(item)


#像数组和c结构体这样的对象可以直接用来进行写操作，而不必先转成byte对象
import array
nums = array.array('i',[1,2,3,4])
with open('data.bin','wb') as f:
    f.write(nums)

#有许多对象还支持直接将二进制文件读入到它们底层的内存中，只要使用文件对象的readinto方法即可
a = array.array('i',[0,0,0,0,0,0,0])
with open('data.bin','rb') as f:
    #这里需要小心一些，这项特性是和平台相关的。
    f.readinto(a)
print(a);