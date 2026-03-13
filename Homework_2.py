def get_statistics():
    nums = [4, 8, 2, 10, 6]
    statistics = {
        'sum': sum(nums),
        'min': min(nums),
        'max': max(nums),
        'avg': sum(nums) / len(nums),
        'length': len(nums)
                }

    return statistics


result = get_statistics()
print(result)