# A high level description of most solutions i have uploaded so far.

## Motivation:
I decided to go back and rebuild my skills from the ground up. So i started with Data Structures and Algorithms.

## Accomplishments thus far:
- was able to pass an Amazon coding challenge to get into the selection process. and the follow up interview
- Participated in 6 Leetcode contests, rated 1587, top 23% , still climbing
- Got my 50 days of leetcode badge
- 200 problems solved.

## What i gained so far:
- I'm able to read and understand code much faster
- Gained an understanding of DSA stronger than what i had coming out of college years ago.
- Learned python
- Wrote faster code overal ever since

# Hard
### 23. Merge k Sorted Lists
    - Divide-and-conquer
    - make a helper function to merge 2 lists and decrement the running count of lists
    - treverse the input in pairs mergin the pairs while the count of lists > 1
    - easier than most mediums.

### 30. Substring with Concatenation of All Words
    - Sliding window, setup by figuring out the window size (len(word)) and initializing a hashmap with the words and count in the input
    - traverse the input string jumping by window size
    - check the substring from the current position to the end of the window size, and update a copy of the counting hashmap to keep track of the remaining words.
    - if the remaining goes below zero or the number or words remaining is different from the words used continue, else add the current index to the output.
### 42. Trapping Rain Water.py
    - get a helper array
    - traverse normaly registering the max height seen up to the current
    - traverse backwards updating the helper with min(maxFromRight, maxFromLeft - h) ( the amount of water in any given rectangle
    - sum the helper

### 51 N-Queens and 52. N-Queens II
    - this one is actually hard.
    - backtracking (dfs)
    - use the len of queens as rows, that takes care of that check
    - put in the array of queens the column in which the queen should go
    - if you placed 4 queens append the array to the output
    - check for the column by checking the array of queens
    - check for diagonals by checking X-Y = P-Q for the antidiagonal and X+Y = P+Q for the diagonal
    - if you pass, recursive call adding the column to the rows array and the diff and sum to the arrays of diff and sum
    - you can also use a set or a hashmap, but the array has less overhead since you are already checking for existance

### 76. Minimum Window Substring
    - sliding window, expand right until you get a valid window
    - remove from left until window is invalid
    - keep walking right and left to the end and testing agains the minimum window

### 239. Sliding Window Maximum
    - keep a queue of elements
    - at every new element:
      - remove from the queue the ones outside the window range
      - remove the ones smaller than the current
      - append the current
      - if you are in window range, append to the output the head of the queue

### 297. Serialize and Deserialize Binary Tree
    - either BFS or DFS, not that hard tbh, just traverse to serialize and keep an index running
    - to deserialize

### 295 Find the running medinan (hackerrank and leetcode):
    - 2 heaps, one min one max, top of each heap should be the middle of the stream
    - push into one, pop from that one and push into the other.
    - that reorders the middle
    - determine which one is always gonna be bigger, test and pushpop accordingly
    - to get the median check if the designated bigger is bigger, if so peek it
    - if not they are equal, so peak both and divide by 2

### swap nodes algo (hackerrank)
    - not that difficult, assemble the tree by using a queue (basicaly bfs)
    - implement the inorder traversal
    - do bfs but swapping if the level (1 indexed ) % k == 0.
    - push the result to the output
    - make sure that the recursion pile doesnt break.

# Medium
### 3  Longest Substring Without Repeating Characters
    - keep a sliding window, right pointer is just the variable of the foor loop
    - track a set of the seen characters
    - remove all characters maching the left pointer as it walks along , till you get to the repeated character
    - update maxsize after before walking the right pointer

### 5. Longest Palindromic Substring
    - two pointer scan on every position
    - keep track of the largest string
    - check for odd and even length strings by having the check start with r and l at the same position (odd) and on consecutive positions (even)

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

### 33. Search in Rotated Sorted Array
    - its still binary search
    - for every mid you have to figure out in what sorted half you are and then act acordingly

### 36. Valid Sudoku
    - this one hinges heavily on the data structure you choose
    - get some defaultdict(set)s going. for rows, collumns and squares
    - the trick is to address the squares one with a tuple made of x//3, y//3 to check for repetitions within the square
    - then just itterate, check for repetitions on all 3, return false if repeated, and add to the sets if not.

### 49. Group Anagrams
    - use a hashmap. key is the word sorted( ''.join(sorted(word))) value is an array of lists.
    - you can use a defaultdict(list) for that.
    - iterate over the values and append to output
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

### 62. Unique Paths
    - two dimentional dp.
    - figure out what a position needs to calculate
    - work backwards from the end
    - realize the last column and last row have all 1's in the how many paths from here to the end department
    - fill those ones,
    - iterate inside the remaining matrix calculating the current position by calculating the sum of the right and the down one from there
    - return the [0][0] position
    - IF YOU EVEN SUSPECT DP PUT IT IN PAPER. the problem gets much easier once you have visualized it

### 63. Unique Paths II
    - Basicaly the obstacle sets the value to 0
    - And you have to pay attention to propagate zeroes on the last column and last row.
    - Once you solved Unique Paths 1 it's just a small adjustment

### 73. Set Matrix Zeroes
    - use the first position of the rows and colums to mark for zeroes and sweep around
    - to actualy do it easier use 2 arrays to index where to blank out

### 128. Longest Consecutive Sequence
    - hashmap all values
    - traverse the array again, if the current is not the start of a sequence ( last one is not in the map)
    - start counting and updating the max
### 131. Palindrome Partitioning
    - traverse the input calling dfs, only go deeper if the substring up to the index checked is a palindrome
    - to go deeper, add the current partition to the path and reduce the input
### 136. Single Number
    - just xor everything, make use of the fact that x^x = 0
### 138. Copy list with random pointer
    - iterate once creating the copy without the rando
    - make a reference with a hashmap from the old to the new
    - traverse the old again linking the random with the adress
### 143. Reorder List
    - put the nodes on a hashmap so you can index them like an array
    - then just iterate pointing the next at the right nodes
    - take care of the indexing in the hashmap.  
### 150. Evaluate Reverse Polish Notation
    - nasty type conversions in the division case
    - otherwise its polish notation, just stack it up and
    - mind the order of the operators
### 153. Find Minimum in Rotated Sorted Array
    - binary search in rotated, same idea as the other one (ctrl+f for rotated)
### 167. Two Sum II - Input Array Is Sorted
    - binary search
    - walk the right and left pointers one by one
### 198. House Robber
    - A pretty fundamental problem in learning DP
    - Always the same approach, identify the recursive relationship, simplify into what is actualy needed to calculate the next position.
    - this one is way easier if you visualize the dp cache in terms of robIncludingLast and robExcludingLast

### 213. House Robber II
    - run house robber 1 on the array ignoring the first and last position and take the max
    - House robber 1 is dp with the two variables for robIncludingLast and robExcludingLast
### 211. Design Add and Search Words Data Structure
    - Use a trie
    - use a dfs helper function to get the wildcard characters
    - pretty easy
### 221. Maximal Square
    - DP, also it's anoying that the matrix is in chars instead of int
    - m[i][j] = 1 + min(m[i+1][+1], m[i+1][j], m[i][j+1]).
    - nothing much else aside from the fundamental relation of the problem and subproblem
### 236. Lowest Common Ancestor of a Binary Tree
    - you don`t have to keep going once you find one of the nodes
    - run dfs, return if you find the node or on null
    - check if left and right (found both on different branches) and return root
    - then left or right (found one and the other was downstream) and return the one not null (it is the ancestor itself)
### 238. Product of Array Except Self
    - calculate the list of prefix multis and postfix multis for every i.
    - return pre[i]*pos[i]
    - the operation can be done inside the output array for O(N) extra memory
### 253. Meeting rooms 2
    - get a sorted list of start and end times
    - iterate on the start list
    - compare start and end
    - each start before and end increments
    - each end decrements
    - get the max
#### 287. Find the Duplicate Number
    - floyds algo. use slow fast to find the cycle. reset one of them to the start
    - walk both at the same pace till they meet at the start of the loop

### 371. Sum of Two Integers
    - this is easy on every language but python
    - carry is an and shifted
    - sum is a xor. keep iterating

### 347. Top K Frequent Elements
    - iterate first to create a counter map
    - iterate the keys and push them into a max heap
    - pop the heap k times
### 416. Partition Equal Subset Sum
    - Knapsack 0/1 for half the value of the sum.

### 516. Longest Palindromic Subsequence
    - 2D dp. dp[l][r] is the longest palindromic subsequence from l to r
    - draw it out
    - if l = r then 1
    - if the positions match the length is 2 + the length of the inner subsequence
    - if they are not dp is equal the max of each subsequence reducing from the left or right
    - iterate backwards through the rows. 

### 547. Number of Provinces
    - Run union find.
    - after the union, if a union has been performed you can decrement a counter starting at the number of cities
### 567. Permutation in String
    - count into a dictionary the letters of s1
    - slide a window of size (len(s1)-1) on s2 putting into a dictionary and check for equality of values in the dict.

### 621. Task Scheduler
    - traverse to make a counter
    - get a maxheap for the counter
    - get a queue to model the cooldownzone,
    - the length of the queue is the cooldown

### 647. Palindromic Substrings
    - run a two pointers scan for every position (l and r at i)
    - accounting for odd lengths and even lengths (l = i, r = i+1)
### 739. Daily Temperatures
    - monotone decreasing stack
    - start output with all 0s
    - stack the temps lower than the top
    - pop the ones larger than the top and update the corresponding index
### 853. Car Fleet
    - sort the array by distance
    - iterate in reverse
    - use the eta to count the fleets
### 981. Time Based Key-Value Store
    - hashmap of lists for the store
    - binary search for the indexing
### 994. Rotting Oranges
    - Matrix BFS
    - Treverse first to determine where are the first rotten oranges and count the fresh ones
    - Run bfs from each rotten one and everytime you hit a fresh one update the count and put it in the rotten queue.

### 1091. Shortest Path in Binary Matrix
    - Run BFS on the matrix.
    - check for stop condition as you pop from the pile
    - return -1 on default
    - pay attention to the conditions,
    - min(rows,cols) < 0 is a nice way to cut down on too much code.
    - max(rows,cols) > ROWS or COLS also a nice way if it is always square

### 1147 Longest Common Subsequence
    - Both bottom up and top down approaches work
    - with DP the problem is always figuring out how to find the subproblems and visualizing
    - the relationship of the problem and the subproblem
    - in this case we use a matrix of len(text1)+1 x len(text2)+1 to serve as the cache
    - the relationship is that if your indexed characters mach you increment both strings so you move diagonaly
    - if they dont you get the max of the increment of either, so the right and down ( or up and left, depending on how you are traversing.)
    - 

### 1161. Maximum Level Sum of a Binary Tree (google prep)
    - Run bfs, make sure to use -inf as the maxSum

### 1448. Count Good Nodes in Binary Tree
    - DFS
    - keep a running maximum, compare each node to the maximum
    - add to the list of good nodes accordingly

### 2491. Divide Players Into Teams of Equal Skill
    - find the target skill by finding the max and min in the same treversal.
    - while populating a counting dictionary
    - walk the min and max closer to the midle in a loop checking if both hit the dict simetrically
    - decrement the counts on the dict and update the running sum accordingly
    - return -1 all the way if conditions are not satisfied

### 2527. Find Xor-Beauty of Array
    - this one is nice. once you put the computation to paper everything cancels out
    - and you just have to XOR the main diagonal of the matrix
    - only the cases where i=j=k actually contribute to the output

### 2530. Maximal Score After Applying K Operations
    - be greedy, put everything into a max heap
    - pop and push k times applying the opperation
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

## 191. Number of 1 Bits
    - hamming weight algo
    - just shift and count with & 1
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

## 338. Counting Bits
    - sum the &1 and shift

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

### 2529. Maximum Count of Positive Integer and Negative Integer
    - the title is the answer, this took 40 seconds