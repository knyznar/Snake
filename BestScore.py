def getBestScore():
    f = open("bestScore.txt", "r")
    score = f.read()
    f.close()
    return score

def updateBestScore(bestscore):
    f = open("bestScore.txt", "w")
    f.write(str(bestscore))
    f.close()
    return