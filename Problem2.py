# Problem 2 : LRU Cache
# Time Complexity : 
'''
get() - O(1)
put()- O(1)
'''
# Space Complexity : O(n) where n is the value of capacity
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :
'''
None
'''

# Your code here along with comments explaining your approach
# defining the node of double linked list
class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        # initialize the hash map for storing key:node pair for quick look up
        self.hashMap = {}
        # initializing the cap variable to store the capacity of LRU
        self.cap = capacity
        # creating dummy head and tail node
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    # function to remove a node from the double linked list
    def removeNode(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
    
    # function to add node at the head of the double linked list
    def addNode(self, node: Node) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node

    def get(self, key: int) -> int:
        # first check in the hashmap if key is present or not
        if key not in self.hashMap:
            # if key is not present in hash map return -1
            return -1
        # remove the node from its orginal position since it is used so need to add in front of the list by definition of LRU
        self.removeNode(self.hashMap[key])
        # add the node to head of the linked list
        self.addNode(self.hashMap[key])
        #return the value of the node
        return self.hashMap[key].val

    def put(self, key: int, value: int) -> None:
        # check if the key is present in the hash map
        if key in self.hashMap:
            # if the key is present then get the node of the key
            tempNode = self.hashMap[key]
            # update the value of the node with new value
            tempNode.val = value
            # remove the node from the original position and add to new position
            self.removeNode(tempNode)
            self.addNode(tempNode)
        else:
            # else check the capacity with the count. If they are equal means cache is full so will need to remove the element which is least used which will be at the end of the list
            if self.cap == len(self.hashMap):
                # get the last element of the linked list
                lastNode = self.tail.prev
                # remove the last node from the linked list
                self.removeNode(lastNode)
                # remove the entry from hash map 
                self.hashMap.pop(lastNode.key)
            # create a new node for the key and value
            newNode = Node(key, value)
            # add new node to the front of the linked list
            self.addNode(newNode)
            # add the entry for the new key to the hash map
            self.hashMap[key] = newNode


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)