num = 10


def demo1():

    # 希望修改全局变量的值，可以使用global声明一下变量即可
    # global关键字会告诉解析器后面的变量是一个全局变量
    # 再使用赋值语句时，就不会创建局部变量
    global num

    num = 99

    print("demo1 ==> %d" % num)


def demo2():

    print("demo2 ==> %d" % num)


demo1()
demo2()