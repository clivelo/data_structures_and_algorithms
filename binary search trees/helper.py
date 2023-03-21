from .tree_node import TreeNode


def equals(t1: TreeNode | None, t2: TreeNode | None) -> bool:
    if t1 is None and t2 is None:
        return True
    elif t1 is None or t2 is None:
        return False
    return t1.val == t2.val and equals(t1.left, t2.left) and equals(t1.right, t2.right)


def parse_list(data: list[any]) -> TreeNode | None:
    if len(data) == 0: return None
    if data[0] is None: return None

    root = TreeNode(data[0])
    queue = [root]
    pointer = 0
    while pointer < len(data) - 1:
        node = queue.pop(0)

        pointer += 1
        if data[pointer] is not None:
            node.left = TreeNode(data[pointer])
            queue.append(node.left)

        pointer += 1
        if pointer >= len(data): break
        if data[pointer] is not None:
            node.right = TreeNode(data[pointer])
            queue.append(node.right)

    return root


def parse_tree(root: TreeNode | None) -> list[any]:
    if root is None: return []

    queue = [root]
    output = [root.val]
    while queue:
        node = queue.pop(0)

        output.append(node.left.val if node.left is not None else None)
        if node.left is not None: queue.append(node.left)

        output.append(node.right.val if node.right is not None else None)
        if node.right is not None: queue.append(node.right)

    while output[-1] is None:
        del output[-1]

    return output

