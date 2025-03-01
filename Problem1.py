# Problem 1 : Flatten Nested List Iterator
# Time Complexity : 
'''
next() - O(1)
hasNext() - O(m) where m is the total number of elements in nested list
'''
# Space Complexity : O(m+d) where m is the total number of integer and d is the depth of the nested structure
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :
'''
None
'''

# Your code here along with comments explaining your approach

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # initialize the stack which will store the iterator of Nested Integer
        self.stack = []
        # check if the nestedList is not None and if it is none then append to the stack
        if nestedList != None:
            self.stack.append(iter(nestedList))
        # initialize the variable currElement to store the currentElement of the Nested list
        self.currElement = None
    
    def next(self) -> int:
        # store the value of self.currElement
        value = self.currElement
        # reset the currElement to None
        self.currElement = None
        return value
    
    def hasNext(self) -> bool:
        # iterate till the stack is not empty
        while (len(self.stack) > 0):
            # peek the stack top iterator
            it = self.stack[-1]
            # get the next element of the iterator if it exists else set to None
            nextElement = next(it, None)
            # if the nextElement is None then pop the iterator from stack and continue 
            if nextElement == None:
                self.stack.pop()
                continue
            # check if the nextElement is an integer and if it is then set the self.currElement to value of the nextElement and return true
            if nextElement.isInteger():
                self.currElement = nextElement.getInteger()
                return True
            # else if it is list then append the iterator of the list to the stack
            else:
                self.stack.append(iter(nextElement.getList()))
        # else return false
        return False

         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())