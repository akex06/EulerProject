with open("13.txt") as f:
    nums = map(int, f.read().split("\n"))
    
    print(str(sum(nums))[:10])