#for...in循环
players = ['coldera', 'device', 'kennys']

for player in players:      #依次将players列表中的元素迭代打印出
    print(player)

#for x in循环，将每个元素带入变量X，执行缩进内的语句，上述代码将players列表中的元素依次带入到player中并打印

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   #新建列表X，为整数1-10
sum = 0   #新建变量sum等于0
for i in x:     #依次将x中的元素带入到变量i中
    sum = sum + i     #sum依次与i进行求和运算，sum = 0 + 1，sum = 1 + 2。。。。直到i = 10，运算结束

print(sum)   #打印出进行求和运算后的sum的值，为整数1-10的求和运算结果→55

#for...in循环即是将一个可迭代对象中的每一个元素带入到其中的x变量中，不断执行缩进中的语句，直到元素迭代完成
#range函数，range(start, stop,|,step)
#接收三个参数，起始数值，结束数值，步长，生成一个由起始数值到结束数值-步长的整数数列，起始数值默认为0，步长默认为1
#range(1,5)→[1,2,3,4]     range(5)→[0,1,2,3,4]   range(1,5,2)→[1,3]
#求1-100整数的和

sum = 0

for i in range(101):
    sum = sum + i

print(sum)
