#lifo
# push  -add
#pop - remove top
# peek or top
# is empty
#not inbuilt

#implemented using list and modules

#push ---> append add element to the top of the list
#pop ---> remove the element from the top of the list

stack = []
stack.append(10)
stack.append(15)
stack.append(20)
stack.append(25)
print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)

#alt
class Stack1:
    
    #constructor
    def __init__(self) -> None:
        self.stack1 = []
        
    def push(self, element):
        self.stack1.append(element)
    
    def pop(self):
        if not self.stack1: #returns true if stack is empty
            print("Empty stack")
        else: 
            self.stack1.pop()
    
    def peek(self):
        return self.stack1[-1]
        
    def isEmpty(self):
        return len(self.stack1) == 0
    
    #printing string representaion of objects
    def __str__(self) -> str:
        return str(self.stack1)
    
myStack = Stack1()
myStack.push(10)
myStack.push(15)
myStack.push(20)
myStack.push(25)

print("Using functions", myStack.stack1)

print(myStack)
print(myStack.peek())
