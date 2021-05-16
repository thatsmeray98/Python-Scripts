def count_substring(string, sub_string):
    count = 0
    start = 0
    while start < len(string): 
        pos = string.find(sub_string, start) 
        if pos != -1: 
            start = pos + 1
            count += 1
        else: 
            break
    return count

string = input().strip()
sub_string = input().strip()
    
count = count_substring(string, sub_string)
print(count)
