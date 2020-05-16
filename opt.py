from random import randint
from random import seed

class OPT:
    # generate page ref string
    # run algo in page frames from size 1 - 30

    OPTPageRefString = []
    seed(1)
    for _ in range(100):
        value = randint(0, 49)
        OPTPageRefString.append(value)

    OPTDistance = []
    OPTDistanceSorted = []
    pageFrame = []
    missCount = 0
    start = 0

    def __init__(self):
        print()

    # check PageRefString list for the values in pageFrames[i-n], count how many times each number comes up
    # (store in pageFrame list clone), sort, delete the last value from the real pagefram, put new val in that spot
    def runOPTAlgo(self, pagesize):
        print("OPT Algorithm for Page Size: ", pagesize)
        self.pageFrame = [-1] * pagesize
        for i in range(len(self.OPTPageRefString)):
            self.start = i
            for j in range(len(self.pageFrame)):
                if self.OPTPageRefString[i] == self.pageFrame[j]:
                    # page hit
                    break
                elif self.pageFrame[j] == -1:
                    # page miss
                    self.pageFrame[j] = self.OPTPageRefString[i]
                    self.missCount += 1
                    break
            else:
                for k in range(len(self.pageFrame)):
                    for l in range(self.start, len(self.OPTPageRefString)):
                        if self.pageFrame[k] == self.OPTPageRefString[l]:
                            self.OPTDistance.append(l - self.start)
                            self.OPTDistanceSorted = list(self.OPTDistance)
                            self.OPTDistanceSorted.sort()
                            break
                    else:
                        self.pageFrame[k] = self.OPTPageRefString[i]
                        self.missCount += 1
                        break

                if len(self.OPTDistanceSorted) == len(self.pageFrame):
                    self.pageFrame[self.OPTDistance.index(self.OPTDistanceSorted[len(self.OPTDistanceSorted) - 1])] = self.OPTPageRefString[i]
                    self.missCount += 1
            #self.OPTDistance.clear()
            del self.OPTDistance[:]
            #self.OPTDistanceSorted.clear()
            del self.OPTDistanceSorted[:]


        print("Number of Page Faults in OPT Algorithm for Page Size ", pagesize, ": ", self.missCount)
        self.missCount = 0
        #self.pageFrame.clear()
        del self.pageFrame[:]
        #self.OPTDistance.clear()
        del self.OPTDistance[:]
        #self.OPTDistanceSorted.clear()
        del self.OPTDistanceSorted[:]
