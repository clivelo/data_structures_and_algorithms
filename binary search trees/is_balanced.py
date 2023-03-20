def is_balanced(node):
    if node is None:
        return True, 0
    balanced_l, height_l = node.left.is_balanced()
    balanced_r, height_r = node.right.is_balanced()
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <= 1
    height = 1 + max(height_l, height_r)
    return balanced, height
