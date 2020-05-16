from random import randint
from random import seed


class FIFO:
    # generate page ref string
    # run algo in page frames from size 1 - 30

    FIFOPageRefString = []
    seed(1)
    for _ in range(100):
        value = randint(0, 49)
        FIFOPageRefString.append(value)

    pageFrame = []
    missCount = 0
    listFull = False

    def __init__(self):
        print()

    def runFIFOAlgo(self, pagesize):

        print("FIFO Algorithm for Page Size: ", pagesize)
        self.pageFrame = [-1] * pagesize
        for i in range(len(self.FIFOPageRefString)):
            for j in range(len(self.pageFrame)):
                if self.FIFOPageRefString[i] == self.pageFrame[j]:
                    # page hit
                    break
                elif self.pageFrame[j] == -1:
                    # page miss
                    self.pageFrame[j] = self.FIFOPageRefString[i]
                    self.missCount += 1
                    break
            else:
                # frames are full, so we delete the first element then append the last element
                del self.pageFrame[0]
                self.pageFrame.append(self.FIFOPageRefString[i])
                self.missCount += 1

        print("Number of Page Faults in FIFO Algorithm for Page Size ", pagesize, ": ", self.missCount)
        self.missCount = 0
        #self.pageFrame.clear()
        del self.pageFrame[:]
