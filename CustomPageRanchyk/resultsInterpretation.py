def getTopNArticles(n, pageRankVector, dict):
    processing = list();
    for i in range(len(pageRankVector)):
        try:
            processing.append((i, pageRankVector[i], dict[str(i)]))
        except KeyError: continue
    processing.sort(key=lambda x: x[1], reverse=True)
    return processing[:n]