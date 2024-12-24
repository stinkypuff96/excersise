# Use binary search to find an element in a list


def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence)

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint

        elif item < midpoint_value:
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1

    return None


sequence_1 = [1, 5, 8, 14, 29, 41, 47, 50, 63, 100]
item_1 = int(input("Enter a number to look for: "))

print(binary_search(sequence_1, item_1))