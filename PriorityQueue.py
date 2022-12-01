import sys


class obj(object):
    value = ""
    priority = 0;

    def __init__(self, value, priority):
        self.value = value
        self.priority = int(priority)

    def printValue(self):
        print(self.value + " [" + str(self.priority) + "]")

class PriorityQueue(object):
    size = 0

    def __init__(self, size):
        self.queue = []
        self.size = int(size)

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) == 0

    def insert(self, data):
        if len(self.queue) >= self.size:
            print("Cannot enter any more data because queue is full")
        if len(self.queue) < self.size:
            if len(self.queue) > 0:
                for i in range(len(self.queue)):
                    if data.value == self.queue[i].value:
                        del self.queue[i]
                    if data.priority == self.queue[i].priority:
                        data.priority += 1
            self.queue.append(data)


    def delete(self):
        try:
            list_ind = 0;
            for i in range(len(self.queue)):
                for j in range(0, len(self.queue) - i - 1):
                    if self.queue[j].priority < self.queue[j + 1].priority:
                        list_ind = j
            item = self.queue[list_ind]
            del self.queue[list_ind]
            return item
        except IndexError:
            print()
            exit()

    def sort(self):
        try:
            for i in range(len(self.queue)):
                for j in range(0, len(self.queue) - i - 1):
                    if self.queue[j].priority > self.queue[j + 1].priority:
                        self.queue[j], self.queue[j+1] = self.queue[j+1], self.queue[j]
        except IndexError:
            print()
            exit()

    def printQueue(self):
        self.sort()
        for i in range(len(self.queue)):
            self.queue[i].printValue()
        print("All elements have been printed")

    def printHead(self):
        maxVal = self.queue[0]
        for i in range(len(self.queue)):
            if maxVal.priority > self.queue[i].priority:
                maxVal = self.queue[i]
        maxVal.printValue()

    def printElementWithPriority(self, priority):
        found = -1
        for i in range(len(self.queue)):
            if self.queue[i].priority == int(priority):
                self.queue[i].printValue()
                found = i
        if found == -1:
            print("Value not found with priority: " + priority)

    def printTail(self):
        maxVal = self.queue[0]
        for i in range(len(self.queue)):
            if maxVal.priority < self.queue[i].priority:
                maxVal = self.queue[i]
        maxVal.printValue()

    def findValue(self, element):
        found = 0
        for i in range(len(self.queue)):
            if self.queue[i].value == element:
                found = 1
        if found == 1:
            print(element + " found")
        else:
            print("Cannot find " + element)

    def concatenate(self, queueTwo):
        maxVal = self.queue[0]
        for i in range(len(self.queue)):
            if maxVal.priority < self.queue[i].priority:
                maxVal = self.queue[i]
        self.size += queueTwo.size
        for i in range(len(queueTwo.queue)):
            queueTwo.queue[i].priority += maxVal.priority
        for i in range(len(self.queue)):
            for j in range(len(queueTwo.queue)):
                if self.queue[i].value == queueTwo.queue[j].value:
                    del queueTwo.queue[j]
        temp = self.queue + queueTwo.queue
        self.queue = temp
        while not queueTwo.isEmpty():
            queueTwo.delete()

    def swap(self, queueTwo):
        temp = []
        tempSize = self.size
        self.size = queueTwo.size
        queueTwo.size = tempSize
        for i in range(len(self.queue)):
            temp.append(self.queue[i])
        placeholder = obj("/", 1)
        temp.append(placeholder)
        ind = temp.index(placeholder)
        for i in range(len(queueTwo.queue)):
            temp.append(queueTwo.queue[i])
        while not self.isEmpty():
            self.delete()
        while not queueTwo.isEmpty():
            queueTwo.delete()
        for i in range(ind):
            queueTwo.insert(temp[i])
        for i in range(ind + 1, len(temp)):
            self.insert(temp[i])

    def reverse(self):
        self.queue.reverse()
        try:
            for i in range(len(self.queue)):
                for j in range(0, len(self.queue) - i - 1):
                    if self.queue[j].priority > self.queue[j + 1].priority:
                        temp = self.queue[j].priority
                        self.queue[j].priority = self.queue[j + 1].priority
                        self.queue[j + 1].priority = temp
        except IndexError:
            print()
            exit()

    def exitQueue(self, element):
        found = 0
        for i in range(len(self.queue)):
            if self.queue[i].value == element:
                del self.queue[i]
                found = 1
                break
        if found == 0:
            print("Error: cannot find element in queue")
