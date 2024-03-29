from __future__ import annotations
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int,
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


# for binary search tree
def search(node: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not node:
        return None

    if node.val > val:
        return search(node.left, val)

    if node.val < val:
        return search(node.right, val)

    return node


def insert(node: Optional[TreeNode], val: int) -> None:
    if not node:
        return

    if val < node.val:
        if not node.left:
            node.left = TreeNode(val)
        else:
            insert(node.left, val)

    elif val > node.val:
        if not node.right:
            node.right = TreeNode(val)
        else:
            insert(node.right, val)


def delete(node: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not node:
        return None

    if val < node.val:
        node.left = delete(node.left, val)
        return node

    if val > node.val:
        node.right = delete(node.right, val)
        return node

    # val == node.val

    if not node.left:
        return node.right

    if not node.right:
        return node.left

    node.right = lift(node.right, node)
    return node


def lift(node: Optional[TreeNode], node_to_delete: TreeNode):
    if not node:
        return None

    if node.left:
        node.left = lift(node.left, node_to_delete)
        return node

    # override deleted node value with successor value
    node_to_delete.val = node.val
    return node.right


def find_greatest(node: Optional[TreeNode]) -> Optional[TreeNode]:
    if not node:
        return None

    if node.right:
        return find_greatest(node.right)
    return node


def traverse_inorder(node: Optional[TreeNode]):
    if not node:
        return
    traverse_inorder(node.left)
    print(node.val, end=" ")
    traverse_inorder(node.right)


def traverse_preorder(node: Optional[TreeNode]):
    if not node:
        return
    print(node.val, end=" ")
    traverse_preorder(node.left)
    traverse_preorder(node.right)


def traverse_postorder(node: Optional[TreeNode]):
    if not node:
        return
    traverse_postorder(node.left)
    traverse_postorder(node.right)
    print(node.val, end=" ")


if __name__ == "__main__":
    tree = TreeNode(
        50,
        TreeNode(
            25,
            TreeNode(
                10,
                TreeNode(
                    4,
                ),
                TreeNode(
                    11,
                ),
            ),
            TreeNode(
                33,
                TreeNode(
                    30,
                ),
                TreeNode(
                    40,
                ),
            ),
        ),
        TreeNode(
            75,
            TreeNode(
                56,
                TreeNode(
                    52,
                ),
                TreeNode(
                    61,
                ),
            ),
            TreeNode(
                89,
                TreeNode(
                    82,
                ),
                TreeNode(
                    95,
                ),
            ),
        ),
    )

    insert(tree, 83)
    delete(tree, 50)
    found = search(tree, 83)
    if found:
        print(found.__dict__)

    greatest = find_greatest(tree)
    if greatest:
        print(greatest.__dict__)

    traverse_inorder(tree)
    print()
    traverse_preorder(tree)
    print()
    traverse_postorder(tree)
