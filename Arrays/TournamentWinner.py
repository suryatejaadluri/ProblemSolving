def tournamentWinner(competitions, results):
    # Write your code here.
    winCount = {}
    bestteam = ""
    winCount[bestteam] = 0
    for idx in range(0,len(competitions)):
        res = int(not results[idx])
        winner = competitions[idx][res]
        if winner in winCount:
            winCount[winner] += 3
        else:
            winCount[winner] = 3
        if winCount[winner] > winCount[bestteam]:
            bestteam = winner
    return bestteam