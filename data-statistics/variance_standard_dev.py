"""Calculate the variance and standard deviation of a list of numbers."""


def calculate_mean(nums):
    """Calculate the meand of a given list of numbers."""
    mean = sum(nums) / len(nums)
    return mean


def find_differences(nums):
    """Find differences between each number in given list and mean."""
    mean = calculate_mean(nums)
    diff = []
    for num in nums:
        diff.append(num - mean)
    return diff


def calculate_variance(nums):
    """Calculate variance of given list of numbers."""
    diff = find_differences(nums)
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)

    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff / len(nums)
    return variance

if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    variance = calculate_variance(donations)
    print(f'The variance in the list of numbers is {variance}.')

    std = variance**0.5
    print(f'The standard deviation of the list of numbers is {std}.')
