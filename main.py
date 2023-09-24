"""
Matrix build run with Python 3.8 and below should fail
"""

# main.py
from src.merge_operator import merge_dicts_new, merge_dicts_old

def merge_dicts_new_way(dict1, dict2):
    # Test the new way (Python 3.9 merge operator)
    result_new = merge_dicts_new(dict1, dict2)
    print("Merged dictionary (Python 3.9):", result_new)

def merge_dicts_old_way(dict1, dict2):
    # Test the old way (using a loop)
    result_old = merge_dicts_old(dict1, dict2)
    print("Merged dictionary (Old way):", result_old)

if __name__ == "__main__":
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    
    #merge_dicts_new_way(dict1, dict2)
    merge_dicts_old_way(dict1, dict2)
