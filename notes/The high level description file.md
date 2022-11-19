# A high level description of every solution i have submitted to leetcode

# Easy
## 1 Two sum:
    - make a hashmap [dif:number]
    - check difference between target and curr
    - if the diff is in the map thats the 2 numbers
## 2 Valid parenthesis:
    - hashmap [closed:open]
    - if in map (is closed) -> pop from the stack, has to match the top of the stack, otherwise false
    - if is oppen just append
## 21 Merge Two Sorted Lists:
    - start a dummy pointer
    - two pointer for each list
    - while both are good, check and point acordingly
    - one of the pointers are still good, just point the tail to it
## 66 Plus One
    - traverse from smallest position to largest
    - add and set the carry
    - at the end check if the carry is 1 to put the new position
## 69 sqrt(x)
    - binary search the space between 0 and X
## 70 Climbing Stairs
    - DP from 0 to Number of stairs, turns out its fibbonacci
    - on n-1 how many ways to reach goal, what abount n-2, and n-3.
## 88 Merge Sorted Arrays
    - traverse reversed so you dont have to shift
    - walk along with m and n -> nums[m+n-1] is the first 0 from the back
    - num1 may be left at the end.
## 94 Binart Tree Inorder Traversal
    -left, node, right.
## 104 Maximum Depth of Binary Tree:
    - its dfs, but in a preorder fashion you test
    - for the max height and if its a leaf node
## 112 Path Sum
    - dfs with a stack
    - push,test if sum is path and leaf, left, right, pop
## 145 Binart tree Postorder
    - left, right, node
## 206 Reverse Linked List
    - keep a pointer to the last
    - use a temporary next pointr
    - point to last and walk last, then walk head
## 217 Contains Duplciate
    - just use a hashmap
## 219 Contains Duplicate 2
    - hashmap, and if its there, check the abs
## 278 First Bad Version
    - Thats a generic binary search, Remember the algo
    - gotta have a function to test.
## 344 Reverse String
    - Two pointers start and end, start < end, swap and walk
## 350 Intersection of Two Arrays
    - count the occurences with a hashmap
    - traverse the second and decrement the occurences in the map
## 374 Guess Number Higher Lower
    - Generic Binary search with higher lower
## 509 Fibonacci Number
    - 0 and 1 hardcoded
    - m = fib(n-1) fib(n-2), go recursive
## 682 Baseball Game
    - Its just stack operations in an array
## 700 Search in a binary search Tree:
    - if > self.search(right)
    - if < self.search(left)
    - else return 
## 704 Binary Search
    - Thats all that it is
## 724 Pivot Index
    - Calculate an array of sums up to the position
    - traverse and check if 2*sum[i] == sum[-1] + nums[-1] (total sum)
## 905 Sort Array By Parity
    - using 2 extra arrays, separate and concatenate
## 976 Largest Perimeter Triangle
    - traverse back to front the miolo of the array running the test
## 1700 Number of Students unable to Eat
    - track the number of refusals.
    - if everybody or nobody refuses get out
    - use a stack to model the behavior
## 1929 Concatenation of Array
    - just concatenate lol
## 2164 Sort Even and Odd Indempentently
    - append odds and evens to their helper arrays
    - bucket sort them out
    - merge
## 2373 Largest Local in the Matrix
    - its just a matter of treversing the right way
    - you have to check all of them.


# Medium
### 3  Longest Substring Without Repeating Characters
    - keep a sliding window, right pointer is just the variable of the foor loop
    - track a set of the seen characters
    - remove all characters maching the left pointer as it walks along , till you get to the repeated character
    - update maxsize after before walking the right pointer

### 30. Substring with Concatenation of All Words
    - build a method to check whether the window is valid by traversing it
    and checking it against a copy of the words dictionary
    - traverse the input string until 1+size(s)-wordlengh checking the
    validity of the window and appending the index to the result

# Hard