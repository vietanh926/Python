import time
# define function to implement for loop
def for_loop(n):
    result = []
    for i in range(n):
        result.append(i**2)
    return result
# define function to implement list comprehension
def list_comprehension(n):
    return [i**2 for i in range(n)]
# Calculate time taken by for_loop()
begin = time.time()
for_loop(10**6)
end = time.time()
# Display time taken by for_loop()
print('Time taken for_loop:', round(end-begin, 2))
# Calculate time takens by list_comprehension()
begin = time.time()
list_comprehension(10**6)
end = time.time()
# Display time taken by for_loop()
print('Time taken for list_comprehension:', round(end-begin, 2))
def even_numbers(n):
    return [i for i in range(n) if i % 2 == 0]
# Ví dụ: tạo danh sách các số chẵn từ 0 đến 10