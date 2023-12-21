result = 0

with open('input.txt', 'r') as file:
    for line in file:
        nums = [int(ch) for ch in line if ch.isnumeric()]
        print(nums)
        result += 10 * nums[0] + nums[-1]

print(result)
