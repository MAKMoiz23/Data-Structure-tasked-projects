class SharpSearch:
    def __init__(self, data=[]):
        self.data=data

    def SearchFirst(self, n):
        for i in range(len(self.data)):
            if self.data[i]==n:
                return i

    def SearchLast(self, n):
        for i in range(len(self.data)-1,-1,-1):
            if self.data[i]==n:
                return i

    x=0
    value=None
    def Search(self, n):
        for i in range(self.x,len(self.data)):
            if self.data[i]==n and self.value==None:
                self.value=self.data[i]
                self.x=i+1
                return i
            elif self.data[i]==n and self.data[i]==self.value:
                self.x=i+1
                return i
            elif self.data[i]!=self.value and self.value!=None and self.data[i]==n:
                self.x=0
                self.value=None
                return self.Search(n)


    def SearchAll(self, n):
        lst=[]
        for i in range(len(self.data)):
            if self.data[i]==n:
                lst.append(i)
        return lst
    

s = SharpSearch([5,4,7,1,4,9,4,6,4,5,6])
print(s.SearchFirst(4))
print(s.SearchLast(4))
print(s.Search(4))
print(s.Search(4))
print(s.Search(4))
print(s.Search(1))
print(s.Search(5))
print(s.Search(5))
print(s.SearchAll(4))
