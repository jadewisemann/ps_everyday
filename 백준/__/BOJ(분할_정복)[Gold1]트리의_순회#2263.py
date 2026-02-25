import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def print_preorder(inorder_pos, postorder, in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    root = postorder[post_end]
    print(root, end=' ')

    root_idx = inorder_pos[root]
    left_size = root_idx - in_start

    print_preorder(inorder_pos, postorder, in_start, root_idx - 1, post_start, post_start + left_size - 1)
    print_preorder(inorder_pos, postorder, root_idx + 1, in_end, post_start + left_size, post_end - 1)

n = int(input())
inorder, postorder = list(map(int, input().split())), list(map(int, input().split()))

print_preorder({val : i for i, val in enumerate(inorder)}, postorder, 0, n - 1, 0, n -1)