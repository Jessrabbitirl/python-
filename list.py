player = ['coldzera', 'fallen', 'fermonster']  #定义列表 - 一个有序的元素的合集

print(player, len(player))   #打印出列表，以及列表的长度

print(player[1])    #打印出列表索引为1的元素

player.append('stewie2k')   #append方法向列表末尾添加新的元素
print(player)

player.insert(1, 'shox')   #insert方法可以向列表的指定位置添加新元素append(位置, 添加的元素)
print(player)


player.pop()  #pop方法删除列表的最后一个元素
print(player)

player.pop(1) #传入列表内元素的索引，删除指定位置的元素
print(player)


player[1] = 'olofmeister'   #列表中的元素可以被指定为新的元素
print(player)
