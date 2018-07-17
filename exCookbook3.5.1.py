#从字节串中打包或者解包大整数
#可以使用int.from_bytes(),然后指定字节序
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print(len(data))
print(int.from_bytes(data,'little'))
print(int.from_bytes(data,'big'))
x = 69120565665751139577663547927094891008
print(x.to_bytes(16,'little'))
#如果将一个整数打包成字节串，但是字节大小不合适的话就会得到一个错误的信息
#如果需要可以用int.big_length()方法来确定用刀多少位来存储这个值。
x = 523 **23
print(x)
print(x.bit_length())
nbytes,rem = divmod(x.bit_length(),8)
if rem:
    nbytes+=1
print(nbytes)
print(x.to_bytes(nbytes,'little'))
#x.to_bytes()
