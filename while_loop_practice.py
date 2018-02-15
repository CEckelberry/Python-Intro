headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]


news_ticker = ""
# set news_ticker to a string that contains no more than 140 characters long.
# HINT: modify the headlines list to verify your loop works with different inputs
"""runline = ""
while len(news_ticker) < 140:
    if len(runline) > 140:
        length = len(runline) - 141
        break
    else:
        for x in headlines:
            runline += str(headlines[0]) + " "

    news_ticker = runline

print(news_ticker)"""
news_ticker = " ".join(str(x) for x in headlines)

news_ticker = news_ticker[0:140]

print(news_ticker)