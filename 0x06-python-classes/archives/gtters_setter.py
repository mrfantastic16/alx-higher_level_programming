# class P:
#     def __init__(self, x):
#         self.__x = x
#
#     def get_x(self):
#         return self.__x
#
#     def set_x(self, x):
#         self.__x = x
#
#
# p1 = P(42)
# p2 = P(4711)
# print(p1.get_x())
#
# p1.set_x(47)
# p1.set_x(p1.get_x() + p2.get_x())
# print(p1.get_x())


# class P:
#     def __init__(self, x):
#         self.x = x
#
#
# p1 = P(42)
# p2 = P(4711)
# print(p1.x)
#
# p1.x = 47
# p1.x = p1.x + p2.x
# print(p1.x)


# class P:
#     def __init__(self, x):
#         self.set_x(x)
#
#     def get_x(self):
#         return self.__x
#
#     def set_x(self, x):
#         if x < 0:
#             self.__x = 0
#         elif x > 1000:
#             self.__x = 1000
#         else:
#             self.__x = x
#
#
# p1 = P(1001)
# print(p1.get_x())
#
# p2 = P(15)
# print(p2.get_x())
#
# p3 = P(-1)
# print(p3.get_x())


# class P2:
#     def __init__(self, x):
#         self.x = x
#
#
# p1 = P2(42)
# p1.x = 1001
# print(p1.x)


# class P:
#     def __init__(self, x):
#         self.x = x
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         if x < 0:
#             self.__x = 0
#         elif x > 1000:
#             self.__x = 1000
#         else:
#             self.__x = x
#
#
# p1 = P(1001)
# print(p1.x)


# class P:
#     def __init__(self, x):
#         self.set_x(x)
#
#     def get_x(self):
#         return self.__x
#
#     def set_x(self, x):
#         if x < 0:
#             self.__x = 0
#         elif x > 1000:
#             self.__x = 100
#         else:
#             self.__x = x
#
#     x = property(get_x, set_x)
#


# class P:
#     def __init__(self, x):
#         self.__set_x(x)
#
#     def __get_x(self):
#         return self.__x
#
#     def __set_x(self, x):
#         if x < 0:
#             self.__x = 0
#         elif x > 1000:
#             self.__x = 1000
#         else:
#             self.__x = x
#
#     x = property(__get_x, __set_x)
#
#
# p = P(1)
# print(p.x)


# class Robot:
#     def __init__(self, name, build_year, lk = 0.5, lp = 0.5):
#         self.name = name
#         self.build_year = build_year
#         self.__potential_physical = lk
#         self.__potential_psychic = lp
#
#     @property
#     def condition(self):
#         s = self.__potential_physical + self.__potential_psychic
#
#         if s <= -1:
#             return "I feel miserable!"
#         elif s <= 0:
#             return "I feel bad!"
#         elif s <= 0.5:
#             return "Could be worse!"
#         elif s <= 1:
#             return "Seems to be okay!"
#         else:
#             return "Great!"
#
#
# if __name__ == '__main__':
#     x = Robot("Marvin", 1979, 0.2, 0.4)
#     y = Robot("Calibean", 1993, -0.4, 0.3)
#
#     print(x.condition)
#     print(y.condition)


class OurClass:
    def __init__(self, a):
        self.OurAtt = a

    @property
    def OurAtt(self):
        return self.__OurAtt

    @OurAtt.setter
    def OurAtt(self, val):
        if val < 0:
            self.__OurAtt = 0
        elif val > 1000:
            self.__OurAtt = 1000
        else:
            self.__OurAtt = val


x = OurClass(10)
print(x.OurAtt)
