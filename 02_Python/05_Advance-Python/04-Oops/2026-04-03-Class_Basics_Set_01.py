# class Student():
#     def __init__(self):
#         print('object value initialize')


#     def __new__(cls):
#         print('new object created')
#         return super().__new__(cls)


# obj=Student()



class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age


obj1=Student('maaz',50)
print('obj1 ki value',obj1)
print('obj1 ka name',obj1.name)
print('obj1 ka city',obj1.age)
