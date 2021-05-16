for _ in range(int(input())):
    n = int(input())
    color_config = input()
    print(len(color_config)-max(color_config.count('R'), color_config.count('B'), color_config.count('G')))