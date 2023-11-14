#How do you implement a bucket sort algorithm
"""
implement a bucket sort algorythem

What is bucket sort?
sorting technique that involves dividing elements into various groups, or buckets. 
These buckets are formed by uniformly distributing the elements. Once the elements are 
divided into buckets, they can be sorted using any other sorting algorithm. 
Finally, the sorted elements are gathered together in an ordered fashion.

"""

in_array = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]

def insertion_sort(bucket):
    for i in range (1, len (bucket)):
        var = bucket[i]
        j = i - 1
        while (j >= 0 and var < bucket[j]):
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = var

def bucket_sort(input_list):
    # Find maximum value in the list and use length of the list to determine which value in the list goes into which bucket 
    max_value = max(input_list)
    print(f'max val {max_value}')
    size = max_value/len(input_list)
    print(f'Size {size}')

    # Create n empty buckets where n is equal to the length of the input list
    buckets_list= []
    for x in range(len(input_list)):
        buckets_list.append([]) 

    # Put list elements into different buckets based on the size
    for i in range(len(input_list)):
        j = int (input_list[i] / size)
        print(f'this is j {j}')
        if j != len (input_list):
            print(f'in1 {input_list[i]}')
            buckets_list[j].append(input_list[i])
        else:
            print(f'in2 {input_list[i]}')
            buckets_list[len(input_list) - 1].append(input_list[i])

    # Sort elements within the buckets using Insertion Sort
    for z in range(len(input_list)):
        print(f'z {z}')
        insertion_sort(buckets_list[z])
            
    # Concatenate buckets with sorted elements into a single list
    final_output = []
    for x in range(len(input_list)):
        print(f'x is {x}')
        final_output = final_output + buckets_list[x]
    return final_output

print(bucket_sort(in_array))