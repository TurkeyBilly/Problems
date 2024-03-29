#题目
'''
有N件物品和一个容量为V的背包。
第i件物品的重量是w[i]，价值是v[i]。
求解将哪些物品装入背包可使这些物品的重量总和不超过背包容量，且价值总和最大。

'''

'''
Example: given Weight and Value list which describe weight and value for each item
    Weight = [2, 3, 4, 5]
    Value = [3, 4, 5, 8]
find the way to maximize values while total weight does not exceed the maximum (given)
    Max_Weight = 8

Input:                                                 Output:
    backpack_max_comb(Max_Weight, Weight, Value)   ->         (12, [1,3])
'''
Weight = [2, 3, 4, 5]
Value = [3, 4, 5, 8]
Max_Weight = 8

try:
    from typing import List, Tuple
except ImportError:
    print("Does not have module named typing, please delete annotations")

def backpack_objs(
    # Input Parameters
    max_weight : int, 
    weight : List[int], 
    value : List[int], 
    # None-input inherit parameters
    index : int = -2, 
    objs : List[int] = [],
    know_value : int = 0
    ): #-> Tuple(int, List[int]):
    '''
    This function accepts three inputs parameters and returns a tuple containing the maximum value and the combination of objs
    However, it only returns one type of the best ways if there exist multiple to get a maximum
    max_weight: the maximum of the backpack
    weight: a list containing of the weights of all objs
    value: a list containing of values of all objs
    Return type: (MaxValue, [*objs_combination])
    '''
    # Define the recursion base case: 
    # when there's no more space for the backpack to hold or no more things to hold return 0
    if index == -1 or max_weight == 0:
        return [know_value, objs]
    
    # Define initialize: initialize the index if not given
    if index == -2:
        index = len(Weight) - 1
    # If there is stil space to hold the item at index
    if max_weight - weight[index] >= 0 :
        # Update object list 
        new_objs = objs.copy()
        new_objs.append(int(index))
        return max(
            # 不拿的情况
            backpack_objs(max_weight, weight, value, index-1, objs, know_value),
            # 拿的情况
            backpack_objs(max_weight - weight[index], weight, value, index-1, new_objs, know_value + value[index]), # 拿
            # 最大值参考依据是 return 的 value
            # TODO 大部分情况不知道为什么会返回((int,[*objs]),)，于是为了防止报错加了一个 x[0][0] 的情况
            key = lambda x: x[0][0] if type(x[0]) is not int else x[0]
            )
    # If there is no enough space to hold the item at index
    else:
        return backpack_objs(max_weight, weight, value, index-1, objs, know_value), # 不拿


def get_backpack_max_comb(max_weight, weight, value, display = True, GiveVal = True):
    example = backpack_objs(max_weight, weight, value)
    max_val = example[0][0] if type(example[0]) is not int else example[0]
    objs = example[0][1] if type(example[0]) is not int else example[1]
    if display: print('Maximum benifit: {}, Combination: {}'.format(max_val, sorted(objs))) 
    if GiveVal: return(max_val, sorted(objs))


get_backpack_max_comb(Max_Weight, Weight, Value)
