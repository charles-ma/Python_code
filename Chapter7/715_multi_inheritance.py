class super_class_1(object):
    def __init__(self):
        self.name = '1'

    def set_name(self, string):
        self.name = string

class super_class_2(object):
    def __init__(self):
        self.name = '2'
    
    def set_name(self):
        self.name = '3'

class derived_class(super_class_1, super_class_2):
    def set_name(self):
        super_class_2.set_name(self)

#The following content solves question 7.16
class A(object):
    def __init__(self):
        self.value = 0
    def get_value(self):
        return self.value

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

d = derived_class()
d.set_name()
print d.name
e = D()
print len(e.__dict__)
