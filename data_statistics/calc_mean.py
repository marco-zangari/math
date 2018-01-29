"""Calculate the mean."""

def calc_mean(nums):
    """Calculate the mean of numbers."""
    s = sum(nums)
    N = len(nums)
    mean = s / N

    return mean

if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 503, 600, 1000, 1200]
    mean = calc_mean(donations)
    N = len(donations)
    print(f'Mean donation over the last {N} days is {mean}')
