from random import randint
from random import seed
class LRU:
    # generate page ref string
    # run algo in page frames from size 1 - 30

    LRUPageRefString = []
    seed(1)
    for _ in range(100):
        value = randint(0, 49)
        LRUPageRefString.append(value)
    missCount = 0
    LRUCache = []

    def __init__(self):
        print()

    def runLRUAlgo(self, pagesize):

        print("LRU Algorithm for Page Size: ", pagesize)
        self.pageFrame = [-1] * pagesize

        for i in range(len(self.LRUPageRefString)):
            for j in range(len(self.pageFrame)):
                if self.LRUPageRefString[i] == self.pageFrame[j]:
                    for k in range(len(self.LRUCache)):
                        if self.LRUPageRefString[i] == self.LRUCache[k]:
                            del self.LRUCache[k]
                            self.LRUCache.insert(0, self.LRUPageRefString[i])
                    break
                elif self.pageFrame[j] == -1:
                    # page miss
                    self.pageFrame[j] = self.LRUPageRefString[i]
                    self.LRUCache.insert(0, self.LRUPageRefString[i])
                    self.missCount += 1
                    break
            else:
                self.pageFrame.pop()
                self.pageFrame.insert(0, self.LRUPageRefString[i])
                self.LRUCache.insert(0, self.LRUPageRefString[i])
                self.missCount += 1

        print("Number of Page Faults in LRU Algorithm for Page Size ", pagesize, ": ", self.missCount)
        self.missCount = 0
        #self.LRUCache.clear()
        del self.LRUCache[:]
        #self.pageFrame.clear()
        del self.pageFrame[:]

