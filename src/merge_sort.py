"""
merge_sort.py

Algorithm
Conceptually, a merge sort works as follows:

Divide the unsorted list into n sublists, each containing one element (a list of one element is considered sorted).
Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list. - from Wikipedia
"""

def homogenous_type(array):
    """ homogenous_type
    Checks that the elements in a list are all the same type.

    In: array - a list of values
    Return: boolean True/False
    """

    if not array:
        return False
    element_type = type(array[0])
    for element in array[1:]:
        if type(element) is not element_type:
            return False
    return True

def merge(array):
    """ merge """
    if len(array) >1: 
        mid = len(array) // 2 
        left_side = array[:mid] ; right_side = array[mid:]
  
        merge(left_side)  ; merge(right_side)
       
        i = j = k = 0
          
        while i < len(left_side) and j < len(right_side): 
            if left_side[i] < right_side[j]: 
                array[k] = left_side[i] ; i +=1
            else: 
                array[k] = right_side[j] ; j +=1
            k+=1
          
        while i < len(left_side):
            array[k] = left_side[i]; i+=1 ; k += 1
          
        while j < len(right_side):
            array[k] = right_side[j]; j+=1 ; k += 1
