import matplotlib.pyplot as plt

def assignment(new_list, old_list, i, j):
    """
    assigns list element j of old list to list element i of new list
    """
    new_list[i] = old_list[j]
    return None 


def merge_sort(list_to_sort_by_merge):
    """
    sorts the input list: low -> high values 
    """
    if len(list_to_sort_by_merge) > 1:
        mid = len(list_to_sort_by_merge) // 2
        left = list_to_sort_by_merge[:mid]
        right = list_to_sort_by_merge[mid:]

        merge_sort(left)
        merge_sort(right)

        left_idx = 0
        right_idx = 0
        idx = 0

        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] <= right[right_idx]:
                assignment(list_to_sort_by_merge, left, idx, left_idx)
                left_idx += 1
            else:
                assignment(list_to_sort_by_merge, right, idx, right_idx)
                right_idx += 1
            idx += 1

        while left_idx < len(left):
            list_to_sort_by_merge[idx] = left[left_idx]
            left_idx += 1
            idx += 1

        while right_idx < len(right):
            list_to_sort_by_merge[idx] = right[right_idx]
            right_idx += 1
            idx += 1
    return None


def plotting(lst):
    """
    plots the input list: list index vs. list value 
    """
    x = range(len(my_list))
    plt.plot(x, my_list)
    plt.xlabel("list index")
    plt.ylabel("list value")
    plt.show()
    return None

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
plotting(my_list)
lst = merge_sort(my_list)
plotting(lst)
