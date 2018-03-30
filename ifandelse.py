age = 20                   #定义一个变量
if age>=18:                #if语句判断为True时，执行缩进语句，否则什么也不做
    print('your age is', age)
    print('adult')


age = 3                    #进行多次判断
if age >= 18:              #条件不满足，跳过缩进语句
    print('your age is', age)
    print('adult')
elif age>= 6:              #条件不满足，跳过缩进语句
    print('your age is', age)
    print('teenager')
else:                      #条件成立，执行缩进语句
    print('kid')

#多个条件判断的语句中，条件从上之下进行匹配，如果在其中一条判断成立后，后续的esif与else都会被忽略。

age =  20
if age >= 6:              #age大于6，条件成立，执行缩进语句，后续elif、else语句被忽略，输出为'teenager'
    print('teenager')
elif age >=18:
    print('adult')
else:
    print('kid')




