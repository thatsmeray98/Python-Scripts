tweets, clicks = map(int, input().split())
tweet_state = [0 for _ in range(tweets)]
for _ in range(clicks):
    operation = input().split()
    if operation[0] == 'CLICK':
        count = int(operation[1])
        if tweet_state[count-1] == 0:
            tweet_state[count-1] = 1
        else:
            tweet_state[count-1] = 0
    else:
        tweet_state = [0 for _ in range(tweets)]
    print(tweet_state.count(1))
