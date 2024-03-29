# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def prettyPrintTree(node, prefix="", isLeft=True):
    if not node:
        print("Empty Tree")
        return

    if node.right:
        prettyPrintTree(node.right, prefix + ("│   " if isLeft else "    "), False)

    print(prefix + ("└── " if isLeft else "┌── ") + str(node.val))

    if node.left:
        prettyPrintTree(node.left, prefix + ("    " if isLeft else "│   "), True)

def main():
    import sys

    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            node = stringToTreeNode(line)
            prettyPrintTree(node)
            ret = Solution().isBalanced(node)
            out = (ret)
            print(out)
        except StopIteration:
            break

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(root):
            if not root:
                return True, 0

            lb, ld = helper(root.left)
            rb, rd = helper(root.right)

            return lb and rb and abs(ld - rd) <= 1, max(ld, rd) + 1

        balanced, depth = helper(root)
        return balanced

    def isBalanced2(self, root: TreeNode) -> bool:
        def helper(root):
            if not root:
                return 0

            ldepth = helper(root.left)
            if ldepth == -1:
                return -1

            rdepth = helper(root.right)
            if rdepth == -1:
                return -1

            if abs(ldepth - rdepth) > 1:
                return -1

            return max(ldepth, rdepth) + 1

        depth = helper(root)
        return depth != -1

if __name__ == '__main__':
    main()