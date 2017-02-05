#Alex_Colegrove CS1111, Fall 2016
import urllib.request

def load_state_polls(state):
    url = 'http://elections.huffingtonpost.com/pollster/api/charts/2016-' + state + '-president-trump-vs-clinton.csv'
    stream = urllib.request.urlopen(url)
    biglist =[]
    for line in stream:
        decoded = (line.decode("UTF-8")).strip('\n')
        decoded = (decoded.split(','))
        biglist.append(decoded)

    del biglist[0]
    return(biglist)


def polls_average(state, completed_after, completed_before):
    url = 'http://elections.huffingtonpost.com/pollster/api/charts/2016-' + state + '-president-trump-vs-clinton.csv'
    stream = urllib.request.urlopen(url)
    biglist = []
    for line in stream:
        decoded = (line.decode("UTF-8")).strip('\n')
        decoded = (decoded.split(','))
        biglist.append(decoded)

    del biglist[0]
    trump_percents = 0.0
    clinton_percents = 0.0
    count =0
    for i in range(0,len(biglist)):
        while completed_before >= str(biglist[i][7]) and completed_after <= str(biglist[i][7]):
            trump_percents += float(biglist[i][0])
            clinton_percents += float(biglist[i][1])
            count += 1
            break
    if completed_after == completed_before:
        count =1
    trump_avg = format(trump_percents/count, '.2f')
    clinton_avg = format(clinton_percents/count, '.2f')
    polls_averages =[]
    polls_averages.append(str(trump_avg))
    polls_averages.append(str(clinton_avg))
    return(polls_averages)

def current_winner(poll):
    trump_avg = poll[0]
    clinton_avg = poll[1]
    if trump_avg > clinton_avg:
        return("Trump +" + str(int(float(trump_avg) - float(clinton_avg))))
    elif trump_avg < clinton_avg:
        return('Clinton +' + str(int(float(clinton_avg) - float(trump_avg))))
    else:
        return("Tie")



