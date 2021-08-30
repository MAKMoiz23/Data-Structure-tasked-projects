class HashTable:
    count=0
    def __init__(self, size=4):
        self.size = size
        self.arr = [None for i in range(size)]


    def __hashed(self, k):
        a = 0
        k=str(k)
        for i in k:
            a += ord(i)
        return a % self.size


    # returns value for the key 'k'
    # returns none if it doesn't exist
    # runs in O(1)
    def Get(self, k):
        h = self.__hashed(k)
        n = h + 1

        if self.arr[h] != None and self.arr[h][0] == k:
            return self.arr[h][1]

        elif self.arr[h] == None or self.arr[h][0] != k:
            if n < self.size:
                for i in range(n, len(self.arr)):
                    if self.arr[i]:
                        if self.arr[i][0] == k:
                            re = self.arr[i][1]
                            return re
                    else:
                        continue

            for i in range(n):
                if self.arr[i]:
                    if self.arr[i][0] == k:
                        re = self.arr[i][1]
                        return re
                else:
                    continue


    # store value 'v' for the key 'k'
    # if 'k' already in the table then overwrite
    # returns: old value of 'k'
    # runs in O(1)
    def Put(self, k, v):
        if self.count >= (self.size*50//100):
            self.ReSize()

        h = self.__hashed(k)
        n=h+1

        if self.arr[h] != None and self.arr[h][0]==k:
            re = self.arr[h][0]

        elif self.arr[h] != None and self.arr[h][0]!=k:
            if n<self.size:
                for i in range(n, len(self.arr)):
                    if self.arr[i] != None and self.arr[i][0] == k:
                        re = self.arr[i][0]
                        self.arr[i] = (k, v)
                        return re

                    if self.arr[i] == None:
                        self.count += 1
                        self.arr[i] = (k, v)
                        return

            for i in range(n):
                if self.arr[i] != None and self.arr[i][0] == k:
                    re = self.arr[i][0]
                    self.arr[i] = (k, v)
                    return re

                if self.arr[i] == None:
                    self.count += 1
                    self.arr[i] = (k, v)
                    return

        if self.arr[h]==None:
            self.count+=1
        self.arr[h] = (k, v)

        try:
            return re
        except:
            return


    # remove 'k' from the table if exists
    # returns: current value for the key 'k'
    # runs in O(1)
    def Remove(self, k):
        if self.count < (self.size*50//100):
            self.ReSize()

        h = self.__hashed(k)
        n=h+1

        if self.arr[h] != None and self.arr[h][0] == k:
            re = self.arr[h][1]
            self.arr[h] = None
            self.count-=1

        elif self.arr[h] == None or self.arr[h][0] != k:
            if n<self.size:
                for i in range(n, len(self.arr)):
                    if self.arr[i]:
                        if self.arr[i][0] == k:
                            re = self.arr[i][1]
                            self.arr[i] = None
                            self.count -= 1
                            return re
                    else:
                        continue

            for i in range(n):
                if self.arr[i]:
                    if self.arr[i][0] == k:
                        re = self.arr[i][1]
                        self.arr[i] = None
                        self.count -= 1
                        return re
                else:
                    continue

        try:
            return re
        except:
            return

    # returns all keys as a list
    def Keys(self):
        k_l = []
        for i in self.arr:
            if i == None:
                continue
            k_l.append(i[0])
        return k_l


    # returns all values as a list
    def Values(self):
        v_l = []
        for i in self.arr:
            if i == None:
                continue
            v_l.append(i[1])
        return v_l


    # returns a list containing key value pairs as
    # tuples i.e. [(k,v)]
    def Entries(self):
        kv_l = []
        for i in self.arr:
            if i == None:
                continue
            kv_l.append(i)
        return kv_l


    # returns the number of elements
    def Size(self):
        return self.size


    # returns True if the table is empty
    # otherwise returns false
    def IsEmpty(self):
        for i in self.arr:
            if i != None:
                return False

        return True


    # resize the array when the array
    def ReSize(self):
        if self.count > (self.size*75//100):
            arr=[]
            for i in range(len(self.arr)):
                if self.arr[i]:
                    arr.append((self.arr[i][0], self.arr[i][1]))
            self.arr = [None for i in range(self.size * 2)]
            self.size *= 2
            self.count=0
            for i, j in arr:
                self.Put(i, j)

        elif self.count <= (self.size*25//100):
            arr=[]
            for i in range(len(self.arr)):
                if self.arr[i]:
                    arr.append((self.arr[i][0], self.arr[i][1]))
            self.arr = [None for i in range((self.size*50//100))]
            self.size//=2
            self.count=0
            for i,j in arr:
                self.Put(i,j)

        else:
            return
# A wrapper for HashTable class to implement
# logic for frequency 
class FrequencyTable:
    # constructor
    def __init__(self):
        self.hashtable = HashTable()

    # add e in the table and set counter to 1
    # if already exists then add the counter
    # returns the value of counter after adding
    # runs in O(1)
    def Add(self, e):
        g=self.hashtable.Get(e)
        if g:
            self.hashtable.Put(e,g+1)
            return

        self.hashtable.Put(e,1)

    # if the counter of e is greater
    # then 1 then reduce by 1
    # otherwise remove the element
    # returns the current value of counter
    # runs in O(1)
    def Remove(self, e):
        g=self.hashtable.Get(e)
        if g>1:
            self.hashtable.Put(e,g-1)
            return
        elif g==1:
            self.hashtable.Remove(e)

    # returns the total number of elements/locations
    def Count(self):
        return self.hashtable.count

    # returns a list of tuples where first value
    # shows the element and second value shows frequency
    # [(1,2),(3,4)] shows two elements 1 and 3 with
    # frequency 2 and 4, respectivelly 
    def Frequency(self):
        return self.hashtable.Entries()

# Driving code to load data from files and process
# ********************************************
class FrequencyUtility:
    # constructor
    def __init__(self, entrancefile, exitfile):
        self.entrance = entrancefile
        self.exit = exitfile
        # table to store data
        self.freqTable = FrequencyTable()

    # process the data and returns freuence table
    def Process(self):
        self.__ProcessEntrance()
        self.__ProcessExit()
        return self.freqTable.Frequency()

    # private method to process enterance data
    def __ProcessEntrance(self):
        f = open(self.entrance, "r")
        allLines = f.read().split('\n')
        f.close()

        for aLine in allLines:
            if len(aLine)>0:
                self.freqTable.Add(int(aLine))

    # private method to process exit data
    def __ProcessExit(self):
        f = open(self.exit, "r")
        allLines = f.read().split('\n')
        f.close()

        for aLine in allLines:
            if len(aLine)>0:
                self.freqTable.Remove(int(aLine))
            
        
        
def Test():
    d = FrequencyUtility("entrance.txt","exit.txt")
    print(d.Process())

Test()
