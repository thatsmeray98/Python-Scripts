for _ in range(int(input())):
    races = int(input())
    alice = list(map(int, input().split()))
    bob = list(map(int, input().split()))
    alice.remove(max(alice))
    bob.remove(max(bob))
    if sum(bob) > sum(alice): print('Alice')
    elif sum(alice) > sum(bob): print('Bob')
    else: print('Draw')