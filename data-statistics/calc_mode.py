"""Find the mode using Counter."""

from collections import Counter


def calc_mode(nums):
    """Calculate the number of number list."""
    c = Counter(nums)
    nums_freq = c.most_common()
    max_count = nums_freq[0][1]

    modes = []
    for num in nums_freq:
        if num[1] == max_count:
            modes.append(num[0])

    return modes

if __name__ == '__main__':
    scores = [9,7,8,10,9,9,9,4,5,6,1,5,6,1,5,6,7,8,6,1,10]
    modes = calc_mode(scores)
    print(f'The mode(s) of the list of numbers is/are:')
    for mode in modes:
        print(mode)
