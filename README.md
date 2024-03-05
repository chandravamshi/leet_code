# leet_code
I will try every day to solve one leet code problem.

### Concepts I learned by solving
* array
* two pointers
* sliding window
* [Stacks](#stacks)
    * [Daily Ttemperatures](#daily-temperatures)

---

# Concepts 

### Stacks 
**Beginner Level:**

1. What is a Stack?
    - A stack is a data structure that follows the Last In, First Out (LIFO) principle.
    - It operates like a stack of plates: you can only add or remove the top plate.

2. Basic Operations on a Stack:
    - **Push**: Adding an element onto the top of the stack.
    - **Pop**: Removing the top element from the stack.
    - **Peek (or Top)**: Viewing the top element of the stack without removing it.
    - **isEmpty**: Checking if the stack is empty.
    - **Size**: Finding the number of elements in the stack.

3. Implementation in Python (Basic):

    ```python
    class Stack:
        def __init__(self):
            self.stack = []
    
        def push(self, item):
            self.stack.append(item)
    
        def pop(self):
            if not self.isEmpty():
                return self.stack.pop()
            else:
                return "Stack is empty"
    
        def peek(self):
            if not self.isEmpty():
                return self.stack[-1]
            else:
                return "Stack is empty"
    
        def isEmpty(self):
            return len(self.stack) == 0
    
        def size(self):
            return len(self.stack)
    ```

**Intermediate Level:**

1. Applications of Stacks:
    - **Expression Evaluation**: Stacks are used to evaluate arithmetic expressions like infix, postfix, and prefix.

         ```python
            def evaluate_postfix(expression):
                stack = []
                for char in expression:
                    if char.isdigit():
                        stack.append(int(char))
                    else:
                        operand2 = stack.pop()
                        operand1 = stack.pop()
                        if char == '+':
                            stack.append(operand1 + operand2)
                        elif char == '-':
                            stack.append(operand1 - operand2)
                        elif char == '*':
                            stack.append(operand1 * operand2)
                        elif char == '/':
                            stack.append(operand1 // operand2)
                return stack.pop()
        
            result = evaluate_postfix("34+2*")  # Output: 14
         ```

    - **Function Call Stack**: Stacks are used by the runtime to keep track of function calls and local variables.
    - **Backtracking Algorithms**: Stacks are used in algorithms like depth-first search (DFS) to backtrack and explore all possible solutions.

2. Time and Space Complexity:
    - The time complexity for most stack operations (push, pop, peek) is O(1).
    - The space complexity for a stack depends on the number of elements stored, so it's O(n), where n is the number of elements in the stack.
  
   
   - **Time Complexity of Stack Operations:**
    
        1. **Push Operation**:
           - Time Complexity: O(1)
           - Explanation: Adding an element to the top of the stack takes constant time, regardless of the size of the stack. This is because stacks are typically implemented using arrays or linked lists, where appending an element to the end (or top) has a constant time complexity.
           - Example:
             ```python
             stack = []
             stack.append(1)  # Push operation
             ```
        
        2. **Pop Operation**:
           - Time Complexity: O(1)
           - Explanation: Removing the top element from the stack also takes constant time. Whether using arrays or linked lists, removing the last element (or top element) can be done in constant time.
           - Example:
             ```python
             stack = [1, 2, 3]
             popped_element = stack.pop()  # Pop operation
             ```
    
        3. **Peek (or Top) Operation**:
           - Time Complexity: O(1)
           - Explanation: Viewing the top element of the stack without removing it is also a constant-time operation. It involves accessing the last element of the array or linked list, which can be done in constant time.
           - Example:
             ```python
             stack = [1, 2, 3]
             top_element = stack[-1]  # Peek operation
             ```
    
   - **Space Complexity of Stacks:**
    
        - Space Complexity: O(n)
        - Explanation: The space complexity of a stack depends on the number of elements stored in the stack. Whether using arrays or linked lists, the space required to store 'n' elements grows linearly with the number of elements in the stack.
        - Example:
          ```python
          stack = []
          for i in range(1, n+1):
              stack.append(i)  # Pushing 'n' elements onto the stack
          ```
    
    **Summary:**
    
    - Stack operations such as push, pop, and peek have a time complexity of O(1) because they operate on the topmost element of the stack, which can be accessed in constant time.
    - The space complexity of a stack is O(n) because it grows linearly with the number of elements stored in the stack. Each element in the stack consumes a constant amount of space, resulting in a linear space complexity.
    - These time and space complexities make stacks efficient for implementing various algorithms and data structures, such as expression evaluation, backtracking, and function call stacks.

**Advanced Level:**

1. Stack Implementations:
    - **Using Linked List**: Stacks can also be implemented using a linked list instead of an array. This allows for dynamic resizing and efficient memory usage.

        ```python
        class Node:
            def __init__(self, data):
                self.data = data
                self.next = None
    
        class Stack:
            def __init__(self):
                self.top = None
    
            def push(self, data):
                new_node = Node(data)
                new_node.next = self.top
                self.top = new_node
    
            def pop(self):
                if self.top is None:
                    return "Stack is empty"
                popped = self.top.data
                self.top = self.top.next
                return popped
    
            def peek(self):
                return self.top.data if self.top else "Stack is empty"
    
        stack = Stack()
        stack.push(1)
        stack.push(2)
        print(stack.pop())  # Output: 2
        ```
    - **Thread-safe Stacks**: In multithreaded environments, special thread-safe stacks are implemented using synchronization techniques like locks or atomic operations.

2. Advanced Applications:
    - **Expression Parsing**: Stacks are used in compilers and interpreters for parsing and evaluating complex expressions.
    - **Undo Functionality**: Stacks are used to implement undo functionality in text editors and design software.

        ```python
        class TextEditor:
            def __init__(self):
                self.text = ""
                self.undo_stack = []
                self.redo_stack = []
        
            def insert(self, new_text):
                self.undo_stack.append(self.text)
                self.text += new_text
                self.redo_stack.clear()  # Clear redo stack after insert
        
            def delete(self, num_chars):
                if num_chars > len(self.text):
                    num_chars = len(self.text)
                deleted_text = self.text[-num_chars:]
                self.undo_stack.append(self.text)
                self.text = self.text[:-num_chars]
                self.redo_stack.clear()  # Clear redo stack after delete
                return deleted_text
        
            def undo(self):
                if len(self.undo_stack) > 0:
                    self.redo_stack.append(self.text)
                    self.text = self.undo_stack.pop()
        
            def redo(self):
                if len(self.redo_stack) > 0:
                    self.undo_stack.append(self.text)
                    self.text = self.redo_stack.pop()
        
            # Example usage:
            editor = TextEditor()
            
            editor.insert("Hello ")
            editor.insert("World!")
            print("Text after insertion:", editor.text)  # Output: Hello World!
            
            deleted_text = editor.delete(6)  # Delete "World!"
            print("Deleted text:", deleted_text)  # Output: World!
            
            editor.undo()  # Undo delete
            print("Text after undo:", editor.text)  # Output: Hello World!
            
            editor.redo()  # Redo delete
            print("Text after redo:", editor.text)  # Output: Hello
        
        ```
  
    - **Call Stack in Debugging**: Understanding the call stack is essential for debugging programs, as it helps track function calls and execution flow.

3. Further Reading:
    - **Recursive Stacks**: Understanding how recursion works helps in grasping the call stack and its importance in recursive function calls.
    - **Stack-Based Virtual Machines**: Many programming languages use stack-based virtual machines for executing bytecode instructions efficiently.

**Summary:**
Stacks are fundamental data structures with a wide range of applications in computer science. Mastering the concepts and operations of stacks is crucial for understanding more complex data structures and algorithms. As you delve deeper into programming and computer science, you'll encounter stacks in various contexts, making them an essential tool in your toolkit.


---

Here's how you can structure the README file for the "Daily Temperatures" problem:

---

#### Daily Temperatures 
https://leetcode.com/problems/daily-temperatures/description/

Given an array of integers `temperatures` representing the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i`th day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

Examples:

Example 1:
```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

Example 2:
```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```

Example 3:
```
Input: temperatures = [30,60,90]
Output: [1,1,0]
```

Solution

We can solve this problem using a stack. The stack will store the indices of the temperatures. As we iterate through the temperatures, we'll keep track of the indices of temperatures where we haven't found a warmer day yet. Whenever we find a temperature higher than the one corresponding to the top index in the stack, we'll pop from the stack and update the answer for that index.

Step-by-Step Explanation:

1. Initialize an array `res` of length equal to the length of `temperatures` with all elements set to 0.
2. Initialize an empty stack `stack`.
3. Iterate through the `temperatures` list using `enumerate()` to track both the index and the temperature.
4. For each temperature:
   - While the stack is not empty and the temperature at the top index of the stack (i.e., `temperatures[stack[-1]]`) is less than the current temperature:
     - Pop the index from the stack.
     - Update the corresponding element in `res` by subtracting the current index from the popped index.
   - Push the current index onto the stack.
5. Return the `res` array.

Time Complexity:

- The time complexity of this algorithm is O(n), where n is the number of temperatures in the input list. This is because we iterate through the temperatures list only once.

Space Complexity:

- The space complexity of this algorithm is also O(n). This is because, in the worst case, the stack can hold all the indices of temperatures in the input list.

Code Implementation

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                stackIndex = stack.pop()
                res[stackIndex] = (i - stackIndex)
            stack.append(i)
        return res
```

---

This README file provides a clear explanation of the problem, its solution approach, step-by-step explanation of the solution, time and space complexity analysis, and the code implementation. It should help users understand the problem and the provided solution effectively.

----


