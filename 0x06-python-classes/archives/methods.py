# def hi(obj):
#     print("Hi, I am " + obj.name + "!")
#
#
# class Robot:
#     say_hi = hi
#
#
# x = Robot()
# x.name = "Marvin"
# Robot.say_hi(x)

#
# class A:
#     def __init__(self):
#         print("__init__ has been executed!")
#
#
# x = A()

#

# class Robot:
#     def __init__(self, name=None):
#         self.name = name
#
#     def say_hi(self):
#         if self.name:
#             print(f"Hi, I am {self.name}")
#         else:
#             print("Hi, I am a robot without a name")
#
#
# x = Robot()
# x.say_hi()
# y = Robot("Marvin")
# y.say_hi()


# class Robot:
#     def __init__(self, name=None):
#         self.name = name
#
#     def say_hi(self):
#         if self.name:
#             print(f"Hi, I am {self.name}")
#         else:
#             print("Hi, I am a robot without a name")
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# x = Robot()
# x.set_name("Henry")
# x.say_hi()
#
# y = Robot()
# y.set_name(x.get_name())
# print(y.get_name())


# class Robot:
#     def __init__(self,
#                  name=None,
#                  build_year=None):
#         self.name = name
#         self.build_year = build_year
#
#     def say_hi(self):
#         if self.name:
#             print(f"Hi, I am {self.name}")
#         else:
#             print("Hi, I am a robot without a name")
#
#         if self.build_year:
#             print(f"I was built in {str(self.build_year)}")
#         else:
#             print("It's not known, when I was created!")
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#     def set_build_year(self, by):
#         self.build_year = by
#
#     def get_build_year(self):
#         return self.build_year


# class A:
#     def __str__(self):
#         return "42"
#
#
# a = A()
# print(a)


class A:
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"


x = A()
# x.pub = x.pub + " and my value can be changed"
# print(x.pub)

# x._prot += " can I be changed"
# print(x._prot)

# print(x.__priv)


class Robot:
    def __init__(self, name=None, build_year=200):
        self.__name = name
        self.__build_year = build_year

    def say_hi(self):
        if self.__name:
            print(f"Hi, I am {self.__name}")
        else:
            print("Hi, I am a robot without a name")

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_build_year(self, by):
        self.__build_year = by

    def get_build_year(self):
        return self.__build_year

    def __repr__(self):
        return "Robot('" + self.__name + "', " + str(self.__build_year) + ")"

    def __str__(self):
        return "Name: " + self.__name + ", Build Year: " + str(self.__build_year)


if __name__ == '__main__':
    x = Robot("Marvin", 1978)
    y = Robot("Calibean", 1943)

    for rob in [x, y]:
        rob.say_hi()

        if rob.get_name() == "Calibean":
            rob.set_build_year(1993)

        print("I was built in the year " + str(rob.get_build_year()) + "!")
