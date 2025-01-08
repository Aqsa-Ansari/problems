nums = [2,2,1]


def singleNumber(nums):
    output = 0
    for n in nums:
        output = output ^ n
    return output

print(singleNumber(nums))