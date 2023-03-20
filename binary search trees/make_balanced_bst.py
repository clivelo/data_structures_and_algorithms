from .tree_node import TreeNode


def make_balanced_bst(data, low=0, high=None, parent=None):
    if high is None:
        high = len(data) - 1
    if low > high:
        return None

    mid = (low + high) // 2
    val = data[mid]

    root = TreeNode(val)
    root.left = make_balanced_bst(data, low, mid - 1, root)
    root.right = make_balanced_bst(data, mid + 1, high, root)

    return root
