# Moving Zeros to the End
# Instructions: Write an algorithm that takes an array and moves all of the
# zeros to the end, preserving the order of the other elements.
# Example:
# move_zeros([False, 1, 0, 1, 2, 0, 1, 3, "a"]) returns:
# [false, 1, 1, 2, 1, 3, "a", 0, 0]
# NOTE: When using `if item == 0`, if the item is False, then Python will
# return True and you will enter the conditional statement! To differentiate
# between 0 and False, use the `is` operator!
# NOTE: Using `some_list.remove(item)` will STILL remove the first instance
# of False!

# This solution failed because it is best to create a NEW list rather than
# modify the given list!
# def move_zeros(some_list):
#     for i in range(0, len(some_list)):
#         x = some_list[i]
#         if x is not False and x == 0:
            # With back-to-back zeros, once the index of the first zero is
            # reached and that zero is removed, the next zero takes it's
            # place keeping that same index! But the `for` loop keeps moving
            # the index forward, so we skip over the second zero!
    #         some_list.pop(i)
    #         some_list.append(0)
    # return some_list


def move_zeros(some_list):
    updated_list = []
    zero_list = []
    for i in range(0, len(some_list)):
        x = some_list[i]
        if x is False:
            updated_list.append(x)
        elif x is not False:
            if x == 0:
                zero_list.append(0)
            elif x != 0:
                updated_list.append(x)
    updated_list = updated_list + zero_list
    print(updated_list)

# There are many more solutions that are much nore concise!
# def move_zeros(array):
#     return sorted(array, key=lambda x: not isinstance(x, bool) and x==0)

# def move_zeros(lista):
    # Create a list for the zeros
  # zeros = []
  # new = []
  # for element in lista:
    # If element == 0 and not a boolean (as isinstance(True/False, int) -> True)
  #   if element == 0 and not isinstance(element, bool):
  #     zeros.append(element)
  #   else:
  #     new.append(element)
  # return new + zeros

# This solution had the highest number of "best pracitices" and "cleve" votes:
# def move_zeros(arr):
#     l = [i for i in arr if isinstance(i, bool) or i!=0]
#     return l+[0]*(len(arr)-len(l))


move_zeros([False, 1, 0, 1, 2, 0, 1, 3, "a"])

move_zeros([1,2,0,1,0,1,0,3,0,1])
# Should equal: [ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ]

# FAILED
move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9])
# Should equal: [9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0]

# FAILED
# move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9])
# Should equal: ["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0]

# FAILED
# move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9])
# Should: ["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0])

# move_zeros([0,1,None,2,False,1,0])
# Should equal: [1,None,2,False,1,0,0]

# move_zeros(["a","b"])
# Should equal: ["a","b"]

# move_zeros(["a"])
# Should equal: ["a"]

# move_zeros([0,0])
# Should equal: [0,0]

# move_zeros([0])
# Should equal: [0]

# move_zeros([False])
# Should equal: [False]

# move_zeros([])
# Should equal: []
