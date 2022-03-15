""""
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Example 1:

Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:

Input: n = 1
Output: [[1]]



Constraints:

    1 <= n <= 8
"""


from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder(root:TreeNode):
    if (root != None):
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)



class UniqueBinaryTreeStructures:
    """
    The design of the solution is to rely on the BST rule that all the nodes should carry values greater than
    the root in the right substree and less in the left substree. As such, we want to create a function to recursively
    seek, at all levels, all the possible left subtree and right subtree structures for each at-level, in-range number
    which we will use as the root to combine with the left subtree and right subtree for all the possible combinations/
    permutations.

    Therefore, for a given starting number and an ending number, we will create a loop from the starting
    number to the ending number as our depth-0 iteration with each iterative number being the root. In each iteration,
    we will recursively call the same function to generate all possible lower level left subtrees and lower level
    right subtrees. In each of the further subsequent recursive function calls if necessary, lower level subtrees are
    further determined.

    At code level, the logic constructs leaf nodes from the bottom up in the recursive calls (null at the ending case).
    And the upper level logic will use the leaf nodes as either the left or right node in all permutations for its
    current level till the recursive logic reaches back to the top level.
    """
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.generateTrees_0(1, n)

    def generateTrees_0(self, start: int, end: int) -> List[Optional[TreeNode]]:
        """
        :param start: starting number
        :param end: ending number
        :return: a tree containing all the possible BST structures
        """
        list = []

        """ if start > end then subtree will be
            empty so returning None in the list """
        if (start > end):
            list.append(None)
            return list

        """ iterating through all values from
            start to end for constructing
            left and right subtree recursively """
        for i in range(start, end + 1):

            """ constructing left subtree """
            leftSubtree = self.generateTrees_0(start, i - 1)

            """ constructing right subtree """
            rightSubtree = self.generateTrees_0(i + 1, end)

            """ now looping through all left and
                right subtrees and connecting
                them to ith root below """
            for l in leftSubtree:
                left = l
                for r in rightSubtree:
                    right = r
                    node = TreeNode(i)  # making value i as root
                    node.left = left  # connect left subtree
                    node.right = right  # connect right subtree
                    list.append(node)  # add this tree to list
        return list




trees = UniqueBinaryTreeStructures()

list = trees.generateTrees(3)

for tree in list:
    preorder(tree)
    print()