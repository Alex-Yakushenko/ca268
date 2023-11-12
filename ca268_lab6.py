#!/usr/bin/env python3

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def preorder(node):
    if node:
        # Print the value of the root node first
        print(node.val)

        # Recursively call preorder on the left subtree until we reach a leaf node.
        preorder(node.left)

        # Recursively call preorder on the right subtree until we reach a leaf node.
        preorder(node.right)


def insert(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.val:
        root.left = insert(root.left, key)
    elif key > root.val:
        root.right = insert(root.right, key)
    return root

# Usage
#root = TreeNode(10)
#root = insert(root, 5)
#root = insert(root, 15)

def is_valid_bst(root):
    def inorder_list(node):
        if not node:
            return []
        return inorder_list(node.left) + [node.val] + inorder_list(node.right)
    values = inorder_list(root)
    return values == sorted(values)
'''
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(6)
root.right.right = TreeNode(3)
print(is_valid_bst(root))
'''
#preorder(root)

def find_kth_smallest(root, k):
    def inorder_list(node):
        if not node:
            return []
        return inorder_list(node.left) + [node.val] + inorder_list(node.right)
    values = inorder_list(root)
    return values[k -1]
'''
root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(4)
root.left.left = TreeNode(1)
root.right.right = TreeNode(5)
print(find_kth_smallest(root, 2))
'''
def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))
def is_balanced(root):
    if not root:
        return True

    left_height = height(root.left)
    right_height = height(root.right)

    if abs(left_height - right_height) <= 1:
        return is_balanced(root.left) and is_balanced(root.right)
    else:
        return False
'''
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(5)
#root.left.left = TreeNode(0)
#root.left.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(6)
root.right.right.right = TreeNode(7)

print(is_balanced(root))
'''
def iterative_inorder(root):
    result = []
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.val)
        current = current.right

    return result
'''
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(iterative_inorder(root))
'''

def binary_tree_paths(root):
    def dfs(node, path):
        if not node:
            return

        path += str(node.val)

        if not node.left and not node.right:
            paths.append(path)
        else:
            path += '->'
            dfs(node.left, path)
            dfs(node.right, path)

    paths = []
    dfs(root, "")
    return paths
'''
# Example usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
print(binary_tree_paths(root)) 
'''