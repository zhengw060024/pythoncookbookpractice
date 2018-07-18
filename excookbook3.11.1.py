#随机选择，或者生成随机数
import random
value = [1,2,3,4,5,6]
print(random.choice(value))
print(random.choice(value))
print(random.sample(value,2))
print(random.sample(value,2))
print(random.sample(value,3))
print(random.sample(value,3))

#如果只是要打乱元素顺序可以使用random.shuffle()洗牌函数
random.shuffle(value)
print(value)
#要产生随机整数可以使用random.randint()
print(random.randint(0,10))
print(random.randint(0,10))
#要产生0-1之间分布均匀的随机值可以使用random.random()
print(random.random())
print(random.random())

#如果要得到有N个随机比特位所表示的整数可以使用random.getrandbits()
print(random.getrandbits(200))
#random函数不要出现在加密相关的处理程序中，如果有这样的需求，使用ssl模块的相关函数代替
#可以考虑使用ssl.RAND_bytes()等函数
