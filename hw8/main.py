import time

def measure_execution_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time
def example_function():
    time.sleep(2)
    return "Done"

result, execution_time = measure_execution_time(example_function)
print(f"Result: {result}")
print(f"Time: {execution_time} seconds")

assert result == "Done"
assert 1.9 < execution_time < 2.1