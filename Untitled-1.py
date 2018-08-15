class BinaryTree(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insertLeft(self, item):
        if self.left is None:
            self.left = BinaryTree(item)
        else:
            t = BinaryTree(item)
            t.left = self.left
            self.left = t

    def insertRight(self, item):
        if self.right is None:
            self.right = BinaryTree(item)
        else:
            t = BinaryTree(item)
            t.right = self.right
            self.right = t


def build_tree_with_post():
    tree = BinaryTree(1)
    tree.insertLeft(-5)
    tree.insertRight(2)
    tree.left.insertLeft(0)
    tree.left.insertRight(3)
    tree.right.insertLeft(-4)
    tree.right.insertRight(-5)
    return tree


class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    def maxDepth(self, root):
        # write your code here
        if root is None:
            return 0
        else:
            leftd = self.maxDepth(root.left)
            print(root.val)
            rightd = self.maxDepth(root.right)
        return max(leftd, rightd) + 1


if __name__ == '__main__':
    so = Solution()
    print(so.maxDepth(build_tree_with_post()))