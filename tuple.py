player = ('coldzera', 'fallen', 'fermonster')  #定义一个tuple - 无法修改的有序列表
print(type(player))

t = (1)   #定义只有一个元素的tuple，产生歧义，该变量为int
print(type(t))

r = (1,)  #定义只有一个元素的tuple时，需要在末未添加'，'，消除歧义
print(type(r))



