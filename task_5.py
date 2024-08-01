import heapq
import matplotlib.colors as mcolors
import numpy as np
from collections import deque
from task_4 import draw_tree, build_heap_tree


def color_nodes_in_order(nodes, color_start, color_end):
    colors = list(
        mcolors.LinearSegmentedColormap.from_list("", [color_start, color_end])(np.linspace(0, 1, len(nodes))))
    for i, node in enumerate(nodes):
        rgb_color = mcolors.rgb2hex(colors[i])
        node.color = rgb_color


def dfs(tree_root):
    stack = [tree_root]
    visited = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    return visited


def bfs(tree_root):
    queue = deque([tree_root])
    visited = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return visited


def visualize_tree_traversal(tree_root):
    # DFS Visualization
    dfs_order = dfs(tree_root)
    color_nodes_in_order(dfs_order, "#00008B", "#87CEFA")  # From dark blue to light blue
    draw_tree(tree_root)

    # Reset colors for BFS visualization
    for node in dfs_order:
        node.color = "skyblue"

    # BFS Visualization
    bfs_order = bfs(tree_root)
    color_nodes_in_order(bfs_order, "#8B0000", "#FFA07A")  # From dark red to light salmon
    draw_tree(tree_root)


def main():
    # Example heap array
    heap = [0, 1, 4, 5, 10, 3]

    # Convert the array into a heap in-place
    heapq.heapify(heap)

    # Build and visualize the binary heap
    root = build_heap_tree(heap)
    visualize_tree_traversal(root)


if __name__ == "__main__":
    main()
