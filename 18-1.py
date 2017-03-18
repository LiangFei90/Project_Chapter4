#  -*- encoding:utf-8  -*-

class Pystack:
    def __init__(self,size=20):
        self.stack=[]
        self.size=size
        self.top=-1

    def setSize(self,size):
        self.size=size
    def push(self,element):
        if self.isFull():
            raise StackException('PyStackOverflow')
        else:
            self.stack.append(element)
            self.top=self.top+1
    def pop(self):
        if self.isEmpty():
            raise StackException('PyStackOverflow')
        else:
            element=self.stack[-1]
            self.top=self.top-1
            del self.stack[-1]                      #del 删除列表中的元素
            return element
    def empty(self):
        self.stack=[]
        self.top=-1
    def Top(self):
        return self.top
    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False
    def isFull(self):
        if self.top==self.size-1:
            return True
        else :
            return False

class StackException(Exception):
    def __init__(self,data):
        self.data=data
    def __str__(self):
        return self.data

if __name__=='__main__':
    stack=Pystack()
    for i in range(10):
        stack.push(i)
    print (stack.Top())
    for i in range(10):
        print(stack.pop())
    stack.empty()
    #stack.setSize(30)
    for i in range(21):
        stack.push(i)
        
