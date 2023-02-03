INFINITY = float("inf")
NEG_INFINITY = float("-inf")

def alphabeta(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or node.is_leaf():
        return node.value

    if maximizing_player:
        value = NEG_INFINITY
        for child in node.children:
            value = max(value, alphabeta(child, depth-1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = INFINITY
        for child in node.children:
            value = min(value, alphabeta(child, depth-1, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value






