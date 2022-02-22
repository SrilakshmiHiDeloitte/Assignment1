class StringClass:
    def __init__(self, userinput):
        self.userinput = userinput

    def stringlength(self):
        print(len(self.userinput))

    def stringtolist(self):
        print(list(self.userinput))


class PairsPossible(StringClass):
    pairs = []

    def __init__(self, userinput):
        StringClass.__init__(self, userinput)

    def getpairs(self):
        k = self.userinput
        a = len(self.userinput)
        op = []
        for i in range(0, a):
            for j in range(1, a):
                b = ''
                if len(b) <= 2:
                    b = b + str(k[i]) + str(k[j])
                    op.append(b)
        print(op)

    """def getpairswidspace(self):
        for i in self.getpairs():
            print(i, end=' ')"""


class SearchCommonElements(StringClass):
    def __init__(self, userinput, userinput2):
        self.userinput2 = userinput2
        StringClass.__init__(self, userinput)

    def comelements(self):
        k = self.userinput
        j = self.userinput2
        c = 0
        d = {}
        for i in k:
            c = 0
            for j in j:
                if i == j:
                    c = c + 1
            d[i] = c
        print(d)


class EqualSumPairs(SearchCommonElements):
    def __init__(self, userinput, userinput2):
        PairsPossible.__init__(self, userinput)
        SearchCommonElements.__init__(self, userinput, userinput2)

    def otput(self):
        print((PairsPossible.getpairs(self)))
        print(SearchCommonElements.comelements(self))




usr = EqualSumPairs('Srilakshmi','lak')
usr.otput()


