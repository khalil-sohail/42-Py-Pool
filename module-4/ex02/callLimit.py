def callLimit(limit: int):
    count = 0
    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
            nonlocal count
            if count >= limit:
                print('Error: <function g at 0x7fabdc243ee0> call too many times')
                return
            count += 1
            return function(*args, **kwds)
        return limit_function
    return callLimiter