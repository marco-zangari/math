"""Calculate the median."""


def calc_median(nums):
    """Calculate the median of a number list."""
    N = len(nums)
    nums.sort()

    if N % 2 == 0:
        m1 = N / 2
        m2 = (N / 2) + 1
        m1 = int(m1) - 1
        m2 = int(m2) - 1
        median = (nums[m1] + nums[m2]) / 2
    else:
        m = N / 2
        m = int(m) - 1
        median = nums[m]
    return median

if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    median = calc_median(donations)
    N = len(donations)
    print(f'Median donation over the last {N} days is {median}.')
