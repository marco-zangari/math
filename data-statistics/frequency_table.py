"""Create a frequency table."""

from collections import Counter

def frequency_table(nums):
    """Return a frequency table for given number list."""
    table = Counter(nums)
    print('Number\tFrequency')
    for num in table.most_common():
        print(f'{num[0]}\t{num[1]}')

if __name__ == '__main__':
    scores = [9,7,8,10,9,9,9,4,5,6,1,5,6,1,5,6,7,8,6,1,10]
    frequency = frequency_table(scores)
