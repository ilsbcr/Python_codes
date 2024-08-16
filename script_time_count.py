import time

def block_of_code():
  # Your code to be timed here
  for i in range(1000000):
    pass  # Simulate some work

start_time = time.time()
block_of_code()
end_time = time.time()

execution_time = end_time - start_time
print(f"Execution time: {execution_time:.4f} seconds")
