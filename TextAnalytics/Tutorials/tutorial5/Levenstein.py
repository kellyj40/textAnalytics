# Used to calculate the distance between one another
import editdistance


normals = ["liverpool to win the champions league after that result, great win for the reds, #LFC #Coutinho #Salah #7-0 #Liverpool #Maribor",
            "ireland to face denmark in world cup qualifier, best possible draw for ireland, #COYBIG #November9th #EriksonvMcClean  #wc2018 #russia",
            "hurricane ophelia to hit ireland early next week, schools are set to close as the country prepares for distruption. Colleges to follow suit if nothing changes.",
            "anyone got any tickets to tomorrows match? Thinking of making the trip to slovenia #LFC #Maribor #CL #CHenderson #slovenia #CLQ",
            "world cup draw results #IREvDEN #wc2018"]

spams = ["@worldCup @IRE world cup draw results here @WC2018 #wc2018 #russia http://www.fifa.com/worldcup/preliminaries/matches/index.html",
        "@worldCup @IRE all world cup results here #IREvDEN @WC2018 #wc2018 #russia http://www.fifa.com/worldcup/preliminaries/matches/index.html",
        "@worldCup @IRE see world cup draw results here @WC2018 #wc2018 #russia http://www.fifa.com/worldcup/preliminaries/matches/index.html",
        "@worldCup @IRE visit link to see world cup draw results here @WC2018 #wc2018 #russia http://www.fifa.com/worldcup/preliminaries/matches/index.html",
        "@worldCup @IRE world cup results and fixtures here @WC2018 #wc2018 #russia http://www.fifa.com/worldcup/preliminaries/matches/index.html",
        "@worldCup @IRE world cup draw results here @WC2018 #wc2018 #russia http://www.fifa.com/worldcup/preliminaries/matches/index.html",
        "@worldCup @IRE #IREvDEN world cup draw results here @WC2018 #wc2018 #russia http://www.fifa.com/worldcup/preliminaries/matches/index.html",
        "@worldCup @IRE come see the results of fixtures for qualifiers @WC2018 #wc2018 #russia http://www.fifa.com/worldcup/preliminaries/matches/index.html",
        "@worldCup @IRE world cup draw results are now here @WC2018 #wc2018 #russia http://www.fifa.com/worldcup/preliminaries/matches/index.html",
        "@worldCup @IRE live action of the world cup draw results here @WC2018 #wc2018 #russia http://www.fifa.com/worldcup/preliminaries/matches/index.html",
        "@worldCup @IRE dont forget to visit here @WC2018 #wc2018 #russia http://www.fifa.com/worldcup/preliminaries/matches/index.html",
        "@worldCup @IRE half price tickets @WC2018 #wc2018 #russia http://www.fifa.com/worldcup/preliminaries/matches/index.html",
        "@worldCup @IRE free tickets retweet with a chance @WC2018 #wc2018 #russia http://www.fifa.com/worldcup/preliminaries/matches/index.html",
        "@worldCup @IRE Russia results here @WC2018 #wc2018 #russia http://www.fifa.com/worldcup/preliminaries/matches/index.html",
        "@worldCup @IRE World cup results now visible @WC2018 #wc2018 #russia http://www.fifa.com/worldcup/preliminaries/matches/index.html",
        "@worldCup @IRE Retweet for chance to see your country world @WC2018 #wc2018 #russia http://www.fifa.com/worldcup/preliminaries/matches/index.html",
        "@worldCup @IRE world cup draw results here @WC2018 #wc2018 #russia http://www.fifa.com/worldcup/preliminaries/matches/index.html",
        "@worldCup @IRE retweet and follow for chance to get ticket @WC2018 #wc2018 #russia http://www.fifa.com/worldcup/preliminaries/matches/index.html",
        "@worldCup @IRE world cup draw results here @WC2018 #wc2018 #russia http://www.fifa.com/worldcup/preliminaries/matches/index.html",
        "@worldCup @IRE follow and retweet to be with a chance of free tickets @WC2018 #wc2018 #russia http://www.fifa.com/worldcup/preliminaries/matches/index.html"]

normal_vals = []
for normal1 in normals:
    for normal2 in normals:
        if normal1 != normal2:
            ans = editdistance.eval(normal1, normal2)
            normal_vals.append(ans)
spam_vals = []
for spam1 in spams:
    for spam2 in spams:
        if spam1 != spam2:
            ans = editdistance.eval(spam1, spam2)
            spam_vals.append(ans)
mixed_vals = []
for normal in normals:
    for spam in spams:
        ans = editdistance.eval(normal, spam)
        mixed_vals.append(ans)

import matplotlib.pyplot as plt
count = 1
for spam in spam_vals:
    plt.plot([count], [spam], 'ro')
    count+=1


for normal in normal_vals:
    plt.plot([count], [normal], 'bx')
    count+=1

for normal in mixed_vals:
    plt.plot([count], [normal], 'go')
    count+=1

plt.show()

ans = editdistance.eval("This is spam", "This spam is")

print(ans)


