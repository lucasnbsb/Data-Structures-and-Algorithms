
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
   e - start a dummy pointer
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

### 7. Reverse Integer
    - store a boolean for isnegative on the number
    - use the absolute value of the number
    - while x > 0: add the modulo to the output, multiply the output by 10
    - outside the while divide the output by 10, it will always run one more time
    - with modulo = 0, not affecting the number
    - put the negative back in if isneg
    - all math, no string manipulation for that 96 percentile

### 11. Container With Most Water
    - make a helper method to calculate the area
    - keep two pointers one at the start and one at the end of the array
    - check the area of the current pair (start, end)
    - check which one is bigger and walk the other towards the middle
    - stop when they cross

### 17. Letter Combinations of a Phone Number
    - Basic backtracking problem, iterate through the digits
    - make a recursive call with each of the letters on a stack
    - when the digits run out ''.join(the stack) into the output

### 19. Remove Nth Node From End of List
    - Hint says: keep a second pointer n steps behind
    - my solution whas to traverse and make an array
    - then treat the 3 cases. remove at start, end and middle

### 28. Find the Index of the First Occurrence in a String
    - https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm
    - basically use a hash to check the substring.
    - but also only do the hash if you have the first letter matching since it`s expensive
    - take good care of the limits in the range

### 30. Substring with Concatenation of All Words
    - build a method to check whether the window is valid by traversing it
    and checking it against a copy of the words dictionary
    - traverse the input string until 1+size(s)-wordlengh checking the
    validity of the window and appending the index to the result

### 36. Valid Sudoku
    - this one hinges heavily on the data structure you choose
    - get some defaultdict(set)s going. for rows, collumns and squares
    - the trick is to address the squares one with a tuple made of x//3, y//3 to check for repetitions within the square
    - then just itterate, check for repetitions on all 3, return false if repeated, and add to the sets if not.

### 54. Spiral Matrix.py
    - two pointers approach, four pointers edition
    - big loop, check if pointers cross
    - four small loops for every direction, check again in the middle for pointers crossing
    - take a lot of care with the indices on right and bottom for they are out of bounds

### 55. Jump Game
    - start backwards, keep a goalpost on the last element
    - shift the goalpost (greedy) as you find possible jumps to the goal
    - return true if goalpost hits the 0 element

### 56. Merge Intervals.py
    - sort the intervals by starting position
    - traverse the sorted intervals
    - check if the last interval ends after the current start, if so merge them in the output
    - if they dont just append to output

### 73. Set Matrix Zeroes
    - use the first position of the rows and colums to mark for zeroes and sweep around
    - to actualy do it easier use 2 arrays to index where to blank out

### 238. Product of Array Except Self
    - calculate the list of prefix multis and postfix multis for every i.
    - return pre[i]*pos[i]
    - the operation can be done inside the output array for O(N) extra memory

### 547. Number of Provinces
    - Run union find.
    - after the union, if a union has been performed you can decrement a counter starting at the number of cities

### 2491. Divide Players Into Teams of Equal Skill
    - find the target skill by finding the max and min in the same treversal.
    - while populating a counting dictionary
    - walk the min and max closer to the midle in a loop checking if both hit the dict simetrically
    - decrement the counts on the dict and update the running sum accordingly
    - return -1 all the way if conditions are not satisfied

# Hard

### Find the running medinan:
    - 2 heaps, one min one max, top of each heap should be the middle of the stream
    - push into one, pop from that one and push into the other.
    - that reorders the middle
    - determine which one is always gonna be bigger, test and pushpop accordingly
    - to get the median check if the designated bigger is bigger, if so peek it
    - if not they are equal, so peak both and divide by 2

### swap nodes algo
    - not that difficult, assemble the tree by using a queue (basicaly bfs)
    - implement the inorder traversal
    - do bfs but swapping if the level (1 indexed ) % k == 0.
    - push the result to the output
    - make sure that the recursion pile doesnt break.