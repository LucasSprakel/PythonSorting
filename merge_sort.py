from time import process_time
import sys


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged





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
sorted_list = merge_sort(numbers)
end_time = process_time()
execution_time = end_time - start_time

print(sorted_list)
print(f"Execution time: {execution_time} seconds")