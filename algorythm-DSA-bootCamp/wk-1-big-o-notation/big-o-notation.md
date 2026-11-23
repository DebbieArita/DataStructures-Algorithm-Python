# Big O notation

**Big O notation** is a mathematical notation used in computer science to describe the upper bound, or worst-case scenario, of an algorithm's runtime complexity in terms of the input size. It provides a standardized and concise way to express how an algorithm's performance scales as the input size grows.
Why do we need Big O?

Not all code is created equal. Some solutions are fast and efficient; others are slow and break down when the data gets big. Big O helps us measure how well our code scales as input grows.

Whether you're writing a search algorithm for 10 users or 10 million, Big O lets you reason about performance before you even run the code — which is key if you care about speed, cost, or user experience.

## Why does it matter?

    Compare algorithms. 
    > Know which one handles large inputs better.

    Predict performance. 
    > Understand how code will scale as data grows.
    
    Optimize wisely. 
    > Focus on the slowest part of your code.
    
    Plan resources. 
    > Be smart about memory or CPU usage.
    
    Solve problems better. 
    > Pick the right tools and data structures.

**Big O notation — formal rules**

    > Ignore constants: O(2n) → O(n)

    > O(0.5n²) → O(n²)
    
    > Discard lower-order terms: O(n² + n) → O(n²)

