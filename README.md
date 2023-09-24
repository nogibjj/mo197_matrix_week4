[![Matrix Build](https://github.com/nogibjj/mo197_matrix_week4/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/mo197_matrix_week4/actions/workflows/cicd.yml)

# GitHub Actions Matrix Build Demo

This repository demonstrates the power of GitHub Actions Matrix Build to test multiple versions of Python and operating systems. We test two different methods for merging dictionaries: one using Python 3.9's 'merge' operator and another using a loop.

## Code Structure

### src.merge_operation.py

Contains two methods for merging dictionaries:

1. `merge_dicts_new(dict1, dict2)`: Merges two dictionaries using Python 3.9's 'merge' operator (|). If there are overlapping keys, values from `dict2` take precedence.

2. `merge_dicts_old(dict1, dict2)`: Merges two dictionaries into a new one using a loop. If there are overlapping keys, values from `dict2` take precedence.

### main.py
By uncommenting the line mentioned in the code comments, you can intentionally trigger a build failure when running your matrix build. This can be useful for testing your code and ensuring that the build process catches issues when using the merge_dicts_new_way function.
## Matrix Build Failure on Uncommenting merge_dicts_new_way

In the `main.py` script, uncommenting the `merge_dicts_new_way(dict1, dict2)` function call will intentionally trigger a build failure. This is a helpful indicator for testing purposes or ensuring code quality.

### Example in main.py

```python
if __name__ == "__main__":
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    
    # Uncomment the following line to see a build failure
    # merge_dicts_new_way(dict1, dict2)
    
    # Use the old way for a successful build
    merge_dicts_old_way(dict1, dict2)




