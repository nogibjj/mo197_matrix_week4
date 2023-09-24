"""
Demonstration of matrix test the merge_dicts_new method should 
only work with python3.9 and above

"""

# merge_operation.py

def merge_dicts_new(dict1, dict2):
    """
    Merge two dictionaries with Python 3.9 'merge' operator (|).
    If there are overlapping keys, values from dict2 take precedence.

    Args:
        dict1 (dict): The first dictionary.
        dict2 (dict): The second dictionary.

    Returns:
        dict: A new dictionary containing the merged key-value pairs.
    """
    merged_dict = dict1 | dict2
    return merged_dict

def merge_dicts_old(dict1, dict2):
    """
    Merge two dictionaries into a new one using a loop.
    If there are overlapping keys, values from dict2 take precedence.

    Args:
        dict1 (dict): The first dictionary.
        dict2 (dict): The second dictionary.

    Returns:
        dict: A new dictionary containing the merged key-value pairs.
    """
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        merged_dict[key] = value
    return merged_dict
