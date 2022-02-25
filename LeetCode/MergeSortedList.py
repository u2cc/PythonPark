"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

"""


from typing import Optional



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MergeSortedList:
    mergedList = []

    def putToList(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        print(f"list node one is :{list1}")
        print(f"list node two is :{list2}")
        if list1 is None:
            if list2 is not None:
                self.mergedList.append(list2)
                MergeSortedList.putToList(self, None, list2.next)
        elif list2 is None:
            if list1 is not None:
                self.mergedList.append(list1)
                MergeSortedList.putToList(self, list1.next, None)
        elif list1.val <= list2.val:
            self.mergedList.append(list1)
            MergeSortedList.putToList(self, list1.next, list2)
        else:
            self.mergedList.append(list2)
            MergeSortedList.putToList(self, list1, list2.next)

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        self.mergedList.clear()
        MergeSortedList.putToList(self, list1, list2)
        for i in range(len(self.mergedList)):
            if (i < len(self.mergedList) - 1):
                self.mergedList[i].next = self.mergedList[i + 1]
            else:
                self.mergedList[i].next = None

        print(len(self.mergedList))
        if len(self.mergedList) > 0:
            return self.mergedList[0]
        else:
            return None

    def mergeTwoListsV2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        else:
            """            
            We know the smaller one of the first nodes from the lists must be the first node
            of the combined list
            
            Before we return that smallest node to the caller, we need to recursively call the function to arrange/sort 
            through all the subsequent nodes in the two lists based on the same understanding of which node preceeds.
            
            The smaller node's next node will be the smaller one of the first nodes that are still left in the two lists                                   
            """
            if list1.val<=list2.val:

                list1.next = self.mergeTwoListsV2(list1.next, list2)

                return list1
            else:
                list2.next = self.mergeTwoListsV2(list1, list2.next)
                return list2



listNodea1 = ListNode(1)
listNodea2 = ListNode(2)
listNodea3 = ListNode(4)
listNodea1.next = listNodea2
listNodea2.next = listNodea3


listNodeb1 = ListNode(1)
listNodeb2 = ListNode(2)
listNodeb3 = ListNode(4)
listNodeb1.next = listNodeb2
listNodeb2.next = listNodeb3

sorter = MergeSortedList()
node = sorter.mergeTwoListsV2(listNodea1, listNodeb1)

while node:
    print(node.val)
    node = node.next