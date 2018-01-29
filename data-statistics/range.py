"""Calculate range of a set of numbers."""

def find_range(nums):
    """Calculate the range of a given set of numbers."""
    lowest = min(nums)
    highest = max(nums)
    r = highest - lowest
    return lowest, highest, r

if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    lowest, highest, r = find_range(donations)
    print(f'Lowest: {lowest} Highest: {highest} Range: {r}')
