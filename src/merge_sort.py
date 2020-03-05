"""
merge_sort.py
"""

def homogenous_type(array):
    """ homogenous_type """
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
        mid = len(array)//2 
        left_side = array[:mid] ; right_side = array[mid:]
  
        merge(left_side)  ; merge(right_side)
       
        i = j = k = 0
          
        while i < len(left_side) and j < len(right_side): 
            if left_side[i] < right_side[j]: 
                array[k] = left_side[i] ; i+=1
            else: 
                array[k] = right_side[j] ; j+=1
            k+=1
          
        while i < len(left_side): 
            array[k] = left_side[i] ; i+=1 ; k+=1
          
        while j < len(right_side): 
            array[k] = right_side[j] ; j+=1 ; k+=1
