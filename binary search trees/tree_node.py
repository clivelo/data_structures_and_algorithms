class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def height(self) -> int:
        if self is None:
            return 0
        return 1 + max(self.left.height(), self.right.height())

    def size(self) -> int:
        if self is None:
            return 0
        return 1 + self.left.size() + self.right.size()

    def is_bst(self) -> bool:
        if self.left is None and self.right is None:
            return True
        elif self.left is None:
            return self.val <= self.right.val and self.right.is_bst()
        elif self.right is None:
            return self.val >= self.left.val and self.left.is_bst()

        return self.left.val <= self.val <= self.right.val and self.left.is_bst() and self.right.is_bst()

    def insert(self, val):
        if val < self.val:
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = TreeNode(val)
            else:
                self.right.insert(val)

    def find(self, val):
        if val < self.val:
            if self.left is None:
                return None
            else:
                return self.left.find(val)
        elif val > self.val:
            if self.right is None:
                return None
            else:
                return self.right.find(val)
        else:
            return self

    def update(self, key, value):
        target = self.find(key)
        if target is not None:
            target.val = value
