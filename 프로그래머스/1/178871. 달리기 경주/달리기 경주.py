def solution(players, callings):
    ndict = {string: i for i,string in enumerate(players)}
    for call in callings:
        i = ndict[call]
        players[i] , players[i-1] = players[i-1], players[i]
        ndict[players[i]] = i
        ndict[players[i-1]] = i-1
        
    return players