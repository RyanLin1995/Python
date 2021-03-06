from collections.abc import Iterable, Iterator
import time


class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    # 如果想让创建的对象可以被迭代，需要在类中有__iter__方法，
    # 同时__iter__方法返回一个含有__iter__和__next__方法的对象的引用
    # 返回的对象就是迭代器
    def __iter__(self):
        return ClassIterator(self)


class ClassIterator(object):
    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        pass

    def __next__(self):
        return self.obj.names[0]


classmate = Classmate()
classmate.add('老王')
classmate.add('王二')
classmate.add('张三')

# print("判断classmate是否是可以迭代的对象:", isinstance(classmate, Iterable))
#
# # 使用iter方法，会调用对象的__iter__方法，返回的是一个迭代器
# classmate_iterator = iter(classmate)
# print("判断classmate_iterator是否为迭代器:", isinstance(classmate_iterator, Iterator))
#
# # 通过next调用迭代器，会自动调用迭代器的__next__方法
# print(next(classmate_iterator))

for name in classmate:
    print(name)
    time.sleep(1)