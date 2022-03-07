

def calculerscore(t):
    # check if horizontal wins : 
    for row in range(3):
        if (t[row][0]==t[row][1] and t[row][1]==t[row][2]):
            if t[row][0]=="x":
                return 10
            elif t[row][0]=="o":
                return -10
    #check if vertical wins : 
    for col in range(3):
        if (t[0][col]==t[1][col] and t[1][col]==t[2][col]):
            if t[0][col]=="x":
                return 10
            elif t[0][col]=="o":
                return -10
    # checking diagonals :
    if t[0][0] == t[1][1] and t[1][1]==t[2][2] :
        if t[0][0]=="x":
            return 10
        elif t[0][0]=="o":
            return -10
    if t[0][2] == t[1][1] and t[1][1]==t[2][0] :
        if t[0][2]=="x":
            return 10
        elif t[0][2]=="o":
            return -10
    # no one wins : return 0
    return 0

def minmax(t,j):
    # calculer le score du jeu en cours : 
    score = calculerscore(t)
    if score == 10 or score ==-10 :
        return score
    
    # x = aximizing player
    if j=='x':
        bestScore = -1000
        for i in range(3):
            for j in range(3):
                # if the place is free : 
                if (t[i][j]=='_'):
                    t[i][j]='x'
                    bestScore = max (bestScore,minmax(t,'o'))
                    t[i][j] = '_'
        return bestScore
    else: 
        bestScore = 1000
        for i in range(3):
            for j in range(3):
                # if the place is free : 
                if (t[i][j]=='_'):
                    t[i][j]='o'
                    bestScore = min (bestScore,minmax(t,'o'))
                    t[i][j] = '_'
        return bestScore

def meilleurMouvement(t):
    bestScore=-10000
    bestMove=(-1,-1)
    for i in range(3):
        for j in range(3):
            # if the place is free : 
            if (t[i][j]=='_'):
                t[i][j]='x'
                nextScore = minmax(t,'o')
                if nextScore>bestScore :
                    bestMove = (i,j)
                    bestScore = nextScore
    print( "Meilleur choix possible : ",bestMove, bestScore)
    return bestMove

table  = [
    ['x','o','o'],
    ['_','_','_'],
    ['_','_','x']]

bestMove = meilleurMouvement(table)
print ("The besto move is ROW=%i COL%i" % (bestMove[0],bestMove[1]))
