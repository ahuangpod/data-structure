import sys


def find_two_smallest(nums):
    nums = list(map(float, nums.strip('[]').split(',')))
    first = nums[0]
    second = nums[0]
    for num in nums:
        if num < first:
            first = num
        elif num < second:
            second = num

    print(first, second)


if __name__ == "__main__":
    find_two_smallest(sys.argv[1])
