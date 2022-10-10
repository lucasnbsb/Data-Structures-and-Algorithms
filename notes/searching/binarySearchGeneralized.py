def binary_search(array) -> int:
    def condition(value) -> bool:
        pass
    left, right = 0, len(array)
    while left < right:
        mid = left + ((right - left)>>1)
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left

# generalized algorithm is for finding minimum number k in a search space such that a condition holds
# apply when some form of monotonicity is found within the search space.

# left is the minimun number s.t condition = true.
# left-1 is the maximun number s.t condition = false.
