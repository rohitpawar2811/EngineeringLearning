## Python Language: 

### 9 date each day 5 questions then I will be completing 75 Questions Follow that strictly
26 nov : 5
27 nov : 


## Questions : 
    - Find all the negative number count in 2d array : Binary Search
    - Ship the packete of weights[] in d days: find min cap of ship BS coco ,problem,min-max sum
    - Add Binary : simple question
    - DI String Match : easy but twicky can get soln in first time
    - 27. Remove Element : It was a Great Question
    - 26. Remove Duplicates from Sorted Array
    - 15. 3Sum
    - 1002. Find Common Characters *****
    - 6. Zigzag Conversion : if row ==1 row or len(word)<row column : 1hit
    - 5. Longest Palindromic Substring
    - 3. Longest Substring Without Repeating Characters
    - 1365. How Many Numbers Are Smaller Than the Current Number,count
    -Concatenation of Array : easy
    - 219. Contains Duplicate II *********
    Hashing =>
    - 456. 132 Pattern : n3 , interval, stack, binarySearch 
    - 855. Exam Room :Learn it : https://leetcode.com/problems/exam-room/submissions/1115043217/ Design 
    - Tweet Count Per Frequency : https://leetcode.com/problems/tweet-counts-per-frequency/description/ Design
    - 729. My Calendar I : Design P
    - 731. My Calendar II : Design

    LinkedList
    - 19. Remove Nth Node From End of List : L3
    - https://leetcode.com/problems/rotate-list/ : L4
    - 109. Convert Sorted List to Binary Search Tree : L5 : Finding the mid one and while doing so break left one by prev.next=null and then same thing
    and traversal would be like root left right.
    - Merge k Sorted Lists : L6

    DP
    - 509. Fibonacci Number
    - Buy and sell stock 1/2/3
    - Burst Bullon
    - House Robber
    - House Robber 2
    - LIS 

    DP2
    - Coin change
    - Combination sum 4
    - partition equal subset sum
    - 0/1 Matrix : **done** (https://leetcode.com/problems/01-matrix/solutions/3921258/simple-java-solution-bfs/)

    LiskedList,BT,BST,
    1569. Number of Ways to Reorder Array to Get Same BST
    1373. Maximum Sum BST in Binary Tree
    235. Lowest Common Ancestor of a Binary Search Tree

    Queue
    - 918. Maximum Sum Circular Subarray : Great Question
    -https://leetcode.com/problems/maximum-subarray/description/ :pending

    Stack 1,2 :
    - 155. Min Stack : submitted
    - 84. Largest Rectangle in Histogram : done
    - 1209. Remove All Adjacent Duplicates in String II : done
    - 853. Car Fleet
    - 880. Decoded String at Index
    - 71. Simplify Path
    - https://leetcode.com/problems/longest-valid-parentheses/(hard) : done
    -
    


    Backtrack
    - 51. N-Queens
    - 78. Subsets
    - 79. Word Search
    - 22. Generate Parentheses : P
    - 17. Letter Combinations of a Phone Number
    - 257. Binary Tree Paths

    Heap
    - 451. Sort Characters By Frequency
    - 215. Kth Largest Element in an Array
    - 692. Top K Frequent Words
    - 347. Top K Frequent Elements

    BFS-DFS 1/2
    - 
    -
    -
    -

    Greddy
    - Jump Game
    -

    Graph
    - Critical Connections in a Network
    
https://drive.google.com/drive/folders/1yZKJzRF1fWeDVZ-lD0E3KPjZdfwleuGp


300 * 20 = 60 problems solution
279 questions are left problem

## Sala dudo to entna dubo ki bhagwan utha da, otherwise bhagwan ko bhi lagta hai ye sattle ho gya hai:
## - Aag laga di 
## - pagalpan chahiya.

Additional Knowledge:
1. https://www.geeksforgeeks.org/what-are-max-parallel-http-connections-in-a-browser/

string is access through indexes also ,-1 last index
str="123"
print(str[0]) // 1

## Supported Types
len(),type(),str(),int(),list() => [] ,tuple(),dict()->key-val = {},set

## Data Types
 - int : no limit if goes extra long number internally convert into string and then stores it
 - float : !5 digit precision allowed
 - complex
 - bool

## Some Prefix : 0b, 00 , OXF

## Utility things
1. sorted() -> sort the str data
2. list(str(num)).sort()
3. return [li.index(i) for i in num]
4.    for i in range(start, stop, incr):

5.  if :
    else :

6. for in range()
7. for in list,dict,set
8 [ if i != 2 for i in range(0,10) ] //this thing create the list with intialization

9. String/str -> Slicing operator/substring str ="Python"
    - str[0:3] //Pyt
    - str[0:6] //Python
    - st[0] = 'M'  // this is not supported because string is immutable

10. List-> Hetrogenous, mutable, duplicates allowed
    append(x)
    extend(iterable)
    insert(i, x)
    remove(x)
    pop([i])
    index(x)
    count(x)
    sort()
    reverse()
    copy()

11. tuple -> immutable, static , fixed size and changes not performed ,memory-adv as it is faster
    - It can pe used as Pair datastructure

12. set {}= mutable,sorted,dub allow, insertion order not preserved so set[1] //error
    - append 
    - add

13. Dict Data Types
    - key, value 
    - preserved order

14. Identity Operator & Membership operators
    - is , is not  , in (we can use this in if conditions) , not in ,= .

15 for i, n in enumerate(nums):
        if n in d and abs(i- d[n])<=k:
            return true;
        else :
            d[n] = i
16 == and != used in case of value thing , and it is not good to use is and is not operator

17 reversing a list
    list.reverse()
    list[::-1]
    list[1:3][::-1] reverse the list from 1:3 index only

18 Bitwise Operator
    &
    |
    ^ :xor
    ~ :not
    >>
    <<

19. Dict will print the an object operation what is possible inside.

20. Typeof 

21. Genarator funtions using yield and it also known as for pupose of LazyLoad

In Python, yield is used in the context of a generator function to produce a sequence of values over time, without generating the entire sequence upfront. It allows the function to return a value and then later resume from where it left off when the generator is iterated.

Here are some reasons why yield is used:
## Lazy Evaluation:
Generators produced by yield are lazy. They generate values on-the-fly when requested.
This can be more memory-efficient than creating a list or sequence upfront, especially for large datasets.
## Iterative Computation:
yield allows you to perform computations iteratively. You can generate and process values one at a time, potentially avoiding the need to store the entire sequence in memory.
## Stateful Generators:
Generators maintain their state between successive calls, allowing them to "remember" where they left off.
This is useful for tasks like parsing, where you may need to process a stream of data step by step.
## Infinite Sequences:
yield enables the creation of infinite sequences. Since values are generated on demand, a generator can produce an infinite number of values without running out of memory.
## Enhanced Readability:
Using yield can often result in cleaner and more readable code, especially when dealing with sequences of data or iterative processes.

```
def countupto(start, end):
    for i in range(start,end):
        yield i

genratoritr = countupto(0,10);  //it is not runned yet

for items in genratoritr :  // now here generator iterator will generate the data
    print(items)


``
Some Random Thoughts: 

Because by seeing the topics your mind knows that what logic is needed for the particular problem your are solving.
Let's say you pick a problem from binary search and you know that you have to apply binary search so your mind already precomputed the stuff.

While in interviews you will see a direct problem there is no topic that will state you about what topic you can apply to solve the particular problem.
This is the main reason you are not getting confidence.

Now what's the solution bhaia ?
Solution is very easy peezy, you just have to pick your one friend and ask him to select the problems for you and give it to you.
Now the benefit is you don't know that from which topics that problem belongs and you will train your mind in this way to figure out what topics to apply.

Now when you got the confidence in easy problem then shift yourself to medium and do the same process with medium and hard also .


After 6 months trust me your will se aa great diffrence.
-----------------------------------------------------------------------------------------------------
.items()
.key()
.values()

.get(,default_value)
["check"]

