
Skip to content
All gists
Back to GitHub
Sign in
Sign up

Instantly share code, notes, and snippets.
@yigitpirildak
yigitpirildak/minimax.py
Created 2 years ago

0

    0

Code
Revisions 1
minimax demonstration
minimax.py
def make_best_move():
    bestScore = -math.inf
    bestMove = None
    for move in ticTacBoard.get_possible_moves():
        ticTacBoard.make_move(move)
        score = minimax(False, aiPlayer, ticTacBoard)
        ticTacBoard.undo()
        if (score > bestScore):
            bestScore = score
            bestMove = move
    ticTacBoard.make_move(bestMove)

def minimax(isMaxTurn, maximizerMark, board):
    state = board.get_state()
    if (state is State.DRAW):
        return 0
    elif (state is State.OVER):
        return 1 if board.get_winner() is maximizerMark else -1

    scores = []
    for move in board.get_possible_moves():
        board.make_move(move)
        scores.append(minimax(not isMaxTurn, maximizerMark, board))
        board.undo()

    return max(scores) if isMaxTurn else min(scores)
to join this conversation on GitHub. Already have an account? Sign in to comment

    © 2022 GitHub, Inc.

    Terms
    Privacy
    Security
    Status
    Docs
    Contact GitHub
    Pricing
    API
    Training
    Blog
    About

