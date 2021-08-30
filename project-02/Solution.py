class Node:
    def __init__(self,val,next=None,prev=None):
        self.val=val
        self.next=next
        self.previous=prev

class SatelliteData:
    count=0
    # stores an element at the front of queue
    def __init__(self):
        self.head=None
        self.tail=None
    # must be implemented in O(1)
    def InsertAtFront(self, e):
        n=Node(e)
        self.count+=1
        if self.head is None:
            self.head=n
            self.tail=self.head
            return

        self.head.previous=n  # to set previous value of pre existing head equals to node object created
        n.next=self.head
        n.previous=None
        self.head=n

    # removes an element from the front of queue
    # must be implemented in O(1)
    def RemoveFront(self):
        if self.head is None:
            raise Exception('No Data available to delete')
        self.count-=1

        if self.head is self.tail:
            self.head=None
            self.tail=None
            return

        i_del=self.head
        self.head=self.head.next
        del i_del

    # stores an element at the end of the queue
    # must be implemented in O(1)
    def InsertAtEnd(self, e):
        n=Node(e)
        self.count+=1

        if self.tail is None:
            self.tail=n
            self.head=self.tail
            return

        n.next=None
        n.previous=self.tail
        self.tail.next=n
        self.tail=n

    # removes an element from the end of the queue
    # must be implemented in O(1)
    def RemoveAtEnd(self):
        if self.head is None:
            raise Exception('No Data available to delete')

        self.count -= 1
        if self.head is self.tail:
            self.head=None
            self.tail=None
            return

        i_del=self.tail
        self.tail=self.tail.previous
        self.tail.next=None
        del i_del

    # returns an element from the queue at i_th position
    # must be implemented in O(1)
    def Get(self, i):
        itr=self.head
        count=0

        while itr:
            if itr.val==i:
                return count
            itr=itr.next
            count+=1
        return "No Such value found!"

    # sort the data
    # # must be implemented in O(n log(n) )

    def sortedMerge(self, a, b):
        result=None

        if a==None:
            return b
        if b==None:
            return a

        if a.val<=b.val:
            result=a
            result.next=self.sortedMerge(a.next, b)
        else:
            result=b
            result.next=self.sortedMerge(a, b.next)
        return result

    def Sort(self, h):

        if h==None or h.next==None:
            return h

        middle=self.getMiddle(h)
        nxt_mid=middle.next

        middle.next=None

        left=self.Sort(h)

        right=self.Sort(nxt_mid)

        s_lst=self.sortedMerge(left, right)
        return s_lst

    def getMiddle(self, head):
        if (head==None):
            return head

        slow=head
        fast=head

        while (fast.next!=None and fast.next.next!=None):
            slow=slow.next
            fast=fast.next.next

        return slow

    # returns the number of elements in the queue
    # must be implemented in O(1)
    def Count(self):
        return self.count

    # returns the number of elements can be store by the queue
    # must be implemented in O(1)
    def Capacity(self):
        return 'Until your memory runs out!'

    # returns the entire data as a list
    def GetAll(self):
        lst=[]
        itr=self.head
        while itr:
            lst.append(itr.val)
            itr=itr.next

        return lst


class SatelliteUtility:

    # instance must be initilized with a filename
    # filename represents the file containing data
    # to be processed
    def __init__(self, filename):
        self.filename=filename
        # store instance for each satellite
        self.satellites = []
        # store all data from file to this list
        self.allLines = []

    # this function should read lines from
    # text file and store in self.allLines list
    # each entry in the list represent one line
    def ReadData(self):
        with open(self.filename, 'r') as f:
            for line in f:
                self.allLines.append(line)
        f.close()
        # read data from file and

    # this function should Process each line
    # for each line we have to parse data
    # and store in the respective queue for a satelite
    def ProcessData(self):
        self.ReadData()

        def search(word):
            for i in self.satellites:
                if i[0]==word:
                    return i[1]
            return None

        for aLine in self.allLines:
            # parse the line to get data for S A D
            word = aLine.split()

            if word[1] =='I':
                x=search(word[0])
                if x is None:
                    y=SatelliteData()
                    self.satellites.append([word[0],y])
                    y.InsertAtEnd(word[2])
                    continue

                x.InsertAtEnd(word[2])

            elif word[1] == 'D':
                x=search(word[0])
                if x is None:
                    return

                if word[2]== '1':
                    x.RemoveAtEnd()

                elif word[2]== '0':
                    x.RemoveFront()
            # store data for respective satellite

    def GetSummary(self):
        # returns a list of tuples where each tuple shows
        # a satellite with number of data for each entry
        # for example: [(1,100),(2,200)] shows 2 satellites
        # 1 and 2 with 100 and 200 data elements, respectively
        # lst=[(int(i),j.Count())for i,j in self.satellites]
        lst=[]
        for i, j in self.satellites:
            try:
                i=eval(i)
                lst.append((i, j.Count()))
            except:
                lst.append((i, j.Count()))

        return lst

def Test():
    utility = SatelliteUtility('testfile.txt')
    # utility.ReadData()
    utility.ProcessData()
    summary = utility.GetSummary()
    # for our test file, it should print the following
    # [(1,1) , (2,0)]
    print(summary)

Test()