class demomethod:

    x = 0
    y = 0
    z = []

    @staticmethod                 #静态方法的装饰器
    def static_mthd():            #define the static method
        print("static method")

    @classmethod              #类方法的装饰器
    def class_mthd(cls):         #define the class method
        print("class method")

    def demothod(a, b):
        x  = a
        y = b
demomethod.static_mthd()
demomethod.class_mthd()
ab = demomethod()
ab.static_mthd()
ab.class_mthd()


"""
We can use the staticmethod and the class method to use an unspecified class
"""
