# 定义字符串变量name,输出 我的名字叫小明，请多多关照！
name = '大明'
print('我的名字叫%s，请多多关照！' % name)

# 定义整数变量 student_no, 输出 我的学号是 00001
student_no = 1
print('我的学号是 %06d' % student_no)

# 定义小数price、weight、money
# 输出苹果的单价9.00元/斤，购买了5.00斤，需要支付45.0元
price = 9.00
weight = 5.00
money = price * weight
print('苹果的单价%.2f元/斤，购买了%.2f斤，需要支付%.2f元' % (price,weight,money))

# 定义一个小数scale，输出数据比例是10.00%
scale = 0.25
print("数据比例是%.2f%%" % (scale * 100))