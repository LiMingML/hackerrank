#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#
class Node:
    __slots__ = ['index', 'left', 'right']  # Reduces memory usage

    def __init__(self, index):
        self.index = index
        self.left = None
        self.right = None


def build_tree(indexes):
    """Build tree using BFS and track node depths"""
    root = Node(1)
    q = deque([(root, 1)])  # (node, depth)
    depth_map = {1: [root]}  # Maps depth to list of nodes

    for left, right in indexes:
        current, depth = q.popleft()
        if left != -1:
            current.left = Node(left)
            q.append((current.left, depth + 1))
            if depth + 1 not in depth_map:
                depth_map[depth + 1] = []
            depth_map[depth + 1].append(current.left)
        if right != -1:
            current.right = Node(right)
            q.append((current.right, depth + 1))
            if depth + 1 not in depth_map:
                depth_map[depth + 1] = []
            depth_map[depth + 1].append(current.right)

    return root, depth_map


def swapNodes(indexes, queries):
    root, depth_map = build_tree(indexes)
    """Perform swaps using precomputed depth map"""
    results = []
    for k in queries:
        # Find all depths that are multiples of k
        max_depth = max(depth_map.keys()) if depth_map else 0
        for d in range(k, max_depth + 1, k):
            if d in depth_map:
                for node in depth_map[d]:
                    node.left, node.right = node.right, node.left
        results.append(iterative_inorder(root))
    return results


def iterative_inorder(root):
    """Iterative in-order traversal to avoid recursion limits"""
    result = []
    stack = []
    current = root

    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            result.append(current.index)
            current = current.right
        else:
            break

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
