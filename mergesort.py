import matplotlib.pyplot as plt


def merge_sort(list_to_sort_by_merge):
    """
    sorts the input list: low -> high values 
    """
    if len(list_to_sort_by_merge) > 1:
        # splits the input list into two halfs 
        mid = len(list_to_sort_by_merge) // 2
        left = list_to_sort_by_merge[:mid]
        right = list_to_sort_by_merge[mid:]

        # recursive use of the function 
        # -> if the lists are longer than 1, it splits them again, until they have length 1
        merge_sort(left)
        merge_sort(right)

        left_idx = 0
        right_idx = 0
        idx = 0

        # this compares the entries in the lists of length 1,
        # and sorts them by value and puts them into the original
        # list
        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] <= right[right_idx]:
                list_to_sort_by_merge[idx] = left[left_idx]
                left_idx += 1
            else:
                list_to_sort_by_merge[idx] = right[right_idx]
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
    fig,(ax1,ax2) = plt.subplots(figsize=(10,5),ncols=2)
    fig.suptitle("Comparison", fontsize=20)
    x = range(len(lst))

    ax1.set_title("before mergesort",fontsize=20)
    ax1.bar(x, lst,color="navy")
    ax1.set_xlabel("index", fontsize=20)
    ax1.set_ylabel("value", fontsize=20)
    
    mergeSort(lst)
    ax2.bar(x,lst,color="crimson")
    ax2.set_title("after mergesort",fontsize=20)
    ax2.set_xlabel("index", fontsize=20)
    ax2.sharey(ax1)
    plt.show()


my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
plotting(my_list)
