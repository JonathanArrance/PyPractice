class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_into_bst(root, val):
    # If the tree is empty, create a new node
    if not root:
        return TreeNode(val)
    
    # Insert into the left subtree if the value is smaller than the root
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    # Insert into the right subtree if the value is larger than the root
    elif val > root.val:
        root.right = insert_into_bst(root.right, val)

    return root

# Example usage:
# Given a tree: 2
#              / \
#             1   3
# Insert value 4 into the tree
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

new_value = 4
updated_root = insert_into_bst(root, new_value)

print(updated_root.val)
print(updated_root.left.val)
print(updated_root.right.val)