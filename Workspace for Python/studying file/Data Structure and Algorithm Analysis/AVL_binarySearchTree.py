#  Python code to insert a node in AVL tree
class TreeNode(object):
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        #self.parent = none
        self.height = 1


class AVL_Tree(object):

    def insert(self, root, key):
        #Step 1 - perform normal BST
        if not root:
            return TreeNode(key)
        elif key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        #Step 2 - Update the height of the ancestor node
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        #Step 3 - get the balance factor
        balance = self.getBlance(root)

        # Step 4 - If the Node is unbalanced,then try out the 4 cases
        # Case 1 - left left
        if balance > 1 and key < root.left.value:
                return self.rightRotate(root)

        # Case 2 - right right
        if balance < -1 and key > root.right.value:
            return self.leftRotate(root)

        # Case 3 - left right
        if balance > 1 and key > root.right.value:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Case 4 - right left
        if balance < -1 and key < root.right.value:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def delete(self, root, key):
        # Step 1 - delete as the standard BST
        if not root:
            return root

        elif key < root.value:
            root.left = self.delete(root.left, key)
        elif key > root.value:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

        # It indicate that the number was not in the tree
        if root is None:
            return root

        # Step 2 - Update the height
        root.height = 1 + max( root.left.height,
                                               root.right.height)

        # Step 3 - Get the balance factor
        balance = self.getBlance(root)

        # Step 4 - If the Node is unbalanced, then try out the four cases
        # Case 1 - left left
        if balance > 1 and self.getBlance(root.left) >= 0:
                return self.rightRotate(root)

        # Case 2 - right right
        if balance < -1 and key > self.getBlance(root.right) >= 0:
            return self.leftRotate(root)

        # Case 3 - left right
        if balance > 1 and self.getBlance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Case 4 - right left
        if balance < -1 and self.getBlance(root.right) < 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root


    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        # rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))

        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        # Return the new root
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        # rotation
        y.right = z
        z.left = T3

        # Update the heights
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))

        y.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        # Return the new root
        return y

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root

        return self.getMinValueNode(root.left)

    def getHeight(self, root):
        if not root:
            return 0

        return root.height

    def getBlance(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - \
               self.getHeight(root.right)

    def preOrder(self, root):

        if not root:
            return 0

        print("{0} ".format(root.value), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)


# Driver program to test above function
myTree = AVL_Tree()
root = None
nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]

for num in nums:
    root = myTree.insert(root, num)

# Preorder Traversal
print("Preorder Traversal after insertion -")
myTree.preOrder(root)
print()

# Delete
key = 10
root = myTree.delete(root, key)

# Preorder Traversal
print("Preorder Traversal after deletion -")
myTree.preOrder(root)
print()

# This code is contributed by Ajitesh Pathak

