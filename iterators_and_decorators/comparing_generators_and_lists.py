import time

# print(sum([number for number in range(10)]))
# print(sum(number for number in range(10)))

list_start_time = time.time()
print(sum([number for number in range(100000000)]))
list_processing_time = time.time() - list_start_time


start_time = time.time()
print(sum(number for number in range(100000000)))
processing_time = time.time() - start_time


print(f'Prossising with list is: {list_processing_time}')
print(f'Prossising with generator is: {processing_time}')

