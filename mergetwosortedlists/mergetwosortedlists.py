# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        newList = []
        
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        while(l1): #iterate through each val in list one, appending them to newList
            newList.append(l1.val)
            l1 = l1.next
        while(l2): #same to list two
            newList.append(l2.val)
            l2 = l2.next
            
        newList = sorted(newList) #all the values are now in newList, sort em
        
        current = head = ListNode(newList[0]) #new ListNode with 0th index of newList as starting point
        
        for i in newList[1:]: #iterate through newList, adding each value to the listnode
            head.next = ListNode(i)
            head = head.next
        return current