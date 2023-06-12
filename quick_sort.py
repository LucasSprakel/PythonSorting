from time import process_time
import sys

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + equal + quick_sort(right)


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
sorted_list = quick_sort(numbers)
end_time = process_time()
execution_time = end_time - start_time

print(sorted_list)
print(f"Execution time: {execution_time} seconds")
