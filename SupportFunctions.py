def timeit(number=1):
    def decorator(func):
        def func_wrapper(*args, **kwargs):
            import time
            start = time.time()
            for _ in range(number):
                result = func(*args, **kwargs)
            end = time.time()
            print(f"Time elapsed: {end - start}")
            return result
        return func_wrapper
    return decorator