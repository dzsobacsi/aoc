result = 0

digits = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

with open('input.txt', 'r') as file:
    for line in file:
        print(line)
        nums = []
        for i, start in enumerate(line):
            if line[i].isnumeric():
                nums.append(int(line[i]))
                continue
            for n in digits.keys():
                if line[i:].startswith(n):
                    nums.append(digits[n])

        print(nums)
        result += 10 * nums[0] + nums[-1]

print(result)
