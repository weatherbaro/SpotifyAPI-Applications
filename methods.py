def guess_MBTI(stats):
    print(stats)
    mbti = ""
    if (sum([(stats["danceability"] > 0.5), 
             (stats["energy"] > 0.5), 
             (stats["liveness"] > 0.5)]) >= 2):
        mbti += "E"
    else:
        mbti += "I"
    if (sum([(stats["instrumentalness"] > 0.5), 
             (stats["speechiness"] < 0.33), 
             (stats["tempo"] > 120)]) >= 2):
        mbti += "N"
    else:
        mbti += "S"
    if (sum([(stats["valence"] > 0.5), 
             (stats["speechiness"] < 0.33)]) >= 1):
        mbti += "F"
    else:
        mbti += "T"
    if (sum([(stats["acousticness"] > 0.5), 
             (stats["speechiness"] > 0.33), 
             (stats["tempo"] < 120)]) >= 2):
        mbti += "J"
    else:
        mbti += "P"
    return mbti