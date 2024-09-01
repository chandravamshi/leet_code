## Binary Search

Binary search is an efficient algorithm for finding a specific element in a sorted array. It works by repeatedly dividing the search interval in half, narrowing down the possible locations of the target element.

### How it works

1. Start with the entire sorted array.
2. Find the middle element of the current search range.
3. Compare the middle element with the target value:
   - If they match, the search is successful.
   - If the target is less than the middle element, repeat the search on the left half.
   - If the target is greater than the middle element, repeat the search on the right half.
4. Repeat steps 2-3 until the element is found or the search range is empty.

### Key Points

- The array must be sorted for binary search to work correctly.
- Binary search is much faster than linear search for large datasets.
- It's particularly useful when you need to perform multiple searches on the same sorted data.

### Time Complexity

- Best case: O(1) - when the target is the middle element
- Average case: O(log n)
- Worst case: O(log n)

Where n is the number of elements in the array.

### Space Complexity

- Iterative implementation: O(1) - constant space
- Recursive implementation: O(log n) - due to the call stack

Binary search's logarithmic time complexity makes it highly efficient for large datasets, as the number of operations grows very slowly compared to the size of the input.

### Use Cases

- Searching in large sorted datasets
- Implementing efficient lookup tables
- Optimizing other algorithms that require searching
