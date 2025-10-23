import time
from functools import wraps

def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f" Starting: {func.__name__}()")
        result = func(*args, **kwargs)
        print(f" Finished: {func.__name__}()\n")
        return result
    return wrapper


def log_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f" Execution time for {func.__name__}(): {end_time - start_time:.4f} seconds\n")
        return result
    return wrapper


from Exercise1 import CSVReader
class CSVReaderWithLogging(CSVReader):
    @log_action
    @log_time
    def read(self):
        return super().read()
    @log_action
    @log_time
    def preview(self, n=5):
        return super().preview(n)
# Example usage:

