jeff_words = set(input())
for _ in range(int(input())):
    word = set(input())
    print('Yes') if word == jeff_words else print('No')
