from tree_node import TreeNode


def parse_list(data: list[any]) -> TreeNode | None:
    if len(data) == 0: return None

    root = TreeNode(data[0])
    queue = [root]
    for i in range(1, len(data)):
        node = queue.pop(0)
        if data[i]:
            if i % 2 == 1:
                node.left = TreeNode(data[i])
                queue.append(node.left)
            else:
                node.right = TreeNode(data[i])
                queue.append(node.right)

    return root
