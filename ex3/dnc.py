def dnc(baseFunc, combineFunc):
    def func(arr: list) -> int:
        if len(arr) == 1:
            return baseFunc(arr[0])
        else:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]
            return combineFunc(func(left_half), func(right_half))
    return func


def maxAreaHist(hist):
    maxTerritory = dnc(lambda n: n, lambda n, m: min(n, m) * 2)
    return max(maxTerritory(hist), maxTerritory(hist[1:]), maxTerritory(hist[:-1])) 
