# leet_code
I will try every day to solve one leet code problem.

### Concepts I learned by solving
* array
* two pointers
* sliding window
* stack


# Concepts 

Absolutely! Let's dive deeper into the concept of stacks with explanations ranging from beginner to advanced levels.

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
- **Function Call Stack**: Stacks are used by the runtime to keep track of function calls and local variables.
- **Backtracking Algorithms**: Stacks are used in algorithms like depth-first search (DFS) to backtrack and explore all possible solutions.

2. Time and Space Complexity:
- The time complexity for most stack operations (push, pop, peek) is O(1).
- The space complexity for a stack depends on the number of elements stored, so it's O(n), where n is the number of elements in the stack.

**Advanced Level:**

1. Stack Implementations:
- **Using Linked List**: Stacks can also be implemented using a linked list instead of an array. This allows for dynamic resizing and efficient memory usage.
- **Thread-safe Stacks**: In multithreaded environments, special thread-safe stacks are implemented using synchronization techniques like locks or atomic operations.

2. Advanced Applications:
- **Expression Parsing**: Stacks are used in compilers and interpreters for parsing and evaluating complex expressions.
- **Undo Functionality**: Stacks are used to implement undo functionality in text editors and design software.
- **Call Stack in Debugging**: Understanding the call stack is essential for debugging programs, as it helps track function calls and execution flow.

3. Further Reading:
- **Recursive Stacks**: Understanding how recursion works helps in grasping the call stack and its importance in recursive function calls.
- **Stack-Based Virtual Machines**: Many programming languages use stack-based virtual machines for executing bytecode instructions efficiently.

**Summary:**
Stacks are fundamental data structures with a wide range of applications in computer science. Mastering the concepts and operations of stacks is crucial for understanding more complex data structures and algorithms. As you delve deeper into programming and computer science, you'll encounter stacks in various contexts, making them an essential tool in your toolkit.
