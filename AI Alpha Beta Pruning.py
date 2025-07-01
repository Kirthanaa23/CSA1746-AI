def minimax(node, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or is_terminal(node):
        return evaluate(node)

    if maximizingPlayer:
        maxEval = float('-inf')
        for child in get_children(node, 'MAX'):
            eval = minimax(child, depth - 1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cut-off
        return maxEval
    else:
        minEval = float('inf')
        for child in get_children(node, 'MIN'):
            eval = minimax(child, depth - 1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cut-off
        return minEval
