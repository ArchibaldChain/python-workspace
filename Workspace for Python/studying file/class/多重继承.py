class PrntA:
    nameA = 'PrntA'

    def set_value(self, a):
        self.a = a
        self.b = 0

    def set_nameA(self, nameA):
        PrntA.nameA = nameA

    def info(self):
        print('PrintA : \n', PrntA.nameA, self.a, self.b)


class PrntB:
    nameB = 'PrntB'

    def set_nameB(self, nameB):
        PrntA.nameA = nameB
        PrntB.nameB = nameB

    def info(self):
        print('PrntB:\n', 'PrntA.nameA:', PrntA.nameA, 'PrntB.nameB:', PrntB.nameB)


class sub1(PrntB, PrntA):
    pass


class sub2(PrntA, PrntB):
    def info(self):                       # 修改info
        PrntA.info(self)                  # This is very strange, unlike in book, there is no 'self' in ()
                                      # This may because the PrntA.info is in sub2
        PrntB.info(self)


class sub3(PrntA, PrntB):
    pass


PrntA1 = PrntA()
PrntA1.set_nameA('nameA')
PrntA1.set_value('aaaa')
PrntA1.b = 1
PrntA1.info()

print("Use the sub1 class:")
sub1 = sub1()
sub1.set_nameA('AAAA')
sub1.set_nameB('BBBB')
sub1.info()

print("Use the sub2 class:")
sub2 = sub2()
sub2.set_value(5)
sub2.set_nameB('BBBB')
sub2.info()
print("use the sub3")
sub = sub3()
sub.set_value(5)
sub.info()
