def alpha_beta(tree, alpha, beta, is_max):
    global count

    if isinstance(tree, int):
        count += 1
        return tree

    if is_max:
        value = float('-inf')

        for child in tree:
            value = max(value, alpha_beta(child, alpha, beta, False))
            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:
        value = float('inf')

        for child in tree:
            value = min(value, alpha_beta(child, alpha, beta, True))
            beta = min(beta, value)

            if alpha >= beta:
                break

        return value


tree = [
    [[4, 3], [6, 2]],
    [[2, 1], [9, 5], [3, 1]],
    [[5, 4], [7, 5]]
]

count = 0
result = alpha_beta(tree, float('-inf'), float('inf'), True)

print("Alpha-Beta Value:", result)
print("Leaf Evaluations:", count)