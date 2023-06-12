from time import process_time
import sys


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr



def read_input_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        numbers = [list(map(int, line.strip().split())) for line in lines]
    return numbers


if len(sys.argv) < 2:
    print("python3 sort.py <file.in>")
        

input_file = sys.argv[1]
numbers = read_input_file(input_file)

# Selection Sort
start_time = process_time()
sorted_list = bubble_sort(numbers)
end_time = process_time()
execution_time = end_time - start_time

print(sorted_list)
print(f"Execution time: {execution_time} seconds")