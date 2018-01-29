"""Create frequency table with values lowest to highest."""

from collections import Counter

def frequency_table(nums):
    """Create frequency table with sorted values."""
    table = Counter(nums)
    numbers_freq = table.most_common()
    numbers_freq.sort()

    print(f'Number\tFrequency')
    for num in numbers_freq:
        print(f'{num[0]}\t{num[1]}')

if __name__ == '__main__':
    scores = [9,7,8,10,9,9,9,4,5,6,1,5,6,1,5,6,7,8,6,1,10]
    frequency_table(scores)
