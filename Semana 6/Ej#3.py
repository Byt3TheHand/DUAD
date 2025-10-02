# Manera 1 ( utilisando sum()) 

def list_sum():
    num = [34,43,58]
    return sum(num)

def main():
    print(list_sum())

main()


Manera 2 ( utilizando iteradores)\

def list_sum():
    nums = [34,43,58,58]
    total = 0
    for i in nums:
        total += i
    return total

def main():
    print(list_sum())

main()

Manera 3

def list_sum():
    nums = [34,43,58]
    total = 0 
    for i in range(len(nums)):
        total += nums[i]
    return total

print(list_sum())