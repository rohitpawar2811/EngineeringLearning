# Interview DSA Quesions

1. RainTrapping
 - left side is bigger than right then go for right and then 
 ```
 // class Solution { //Brute Force
//     public int trap(int[] a) {
//         int ans=0;
//         for(int i=0;i<a.length;i++){
//             int Lmax=a[i];
//             int Rmax=a[i];
//             for(int j=0;j<a.length;j++){
//                 if(i==j)continue;
//                 if(j<i){
//                    Lmax=Math.max(Lmax,a[j]); 
//                 }
//                 else{
//                   Rmax=Math.max(Rmax,a[j]);  
//                 }
//             }
//            ans+= Math.min(Lmax,Rmax)-a[i];
//         }
//         return ans;
//     }
// }
// class Solution { //O(n) O(n)time and space
//     public int trap(int[] a) {
//         if(a.length==0) return 0;
//         int ans=0;
//         int pre[]=new int[a.length];
//         int suf[]=new int[a.length];
//         pre[0]=a[0];
//         suf[a.length-1]=a[a.length-1];
//         for(int i=1;i<a.length;i++){
//             pre[i]=Math.max(pre[i-1],a[i]);
//         }
//         for(int i=a.length-2;i>=0;i--){
//             suf[i]=Math.max(suf[i+1],a[i]);
//         }
//         for(int i=0;i<a.length;i++){
//            ans+= Math.min(pre[i],suf[i])-a[i];
//         }
//         return ans;
//     }
// }
class Solution { //O(n) O(n)time and space  4 Pointer here we used left, right,leftMax, rightMax
    // when we got faith oneside is bigger check for another side and its another side max , comapare >greater current than another dir on max
    // if prev max(rightmax) is greater then water is holdble if not greater prevmax then set current as max for next iteration
    public int trap(int[] a) {
        int l=0,r=a.length-1;
        int Lmax=0,Rmax=0;
        int ans=0;
        while(l<r){
            if(a[l]<=a[r]){
                if(a[l]>=Lmax)
                    Lmax=a[l];
                else{
                   ans+=Lmax-a[l];   
                }
                l++;
            }
            else{
                if(a[r]>=Rmax)
                    Rmax=a[r];
                else{
                   ans+=Rmax-a[r];   
                }
                r--;
            }
        }
        return ans;
    }
}

 ```
2. Array with 0,1,2 with duplicate make it sorted Duch-Man Flag Algorithm: 
    - Freq sorted, 3pointer left, right, mid which track 1s
3. Remove Shorted Subarray to make array sorted. https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/description/
    - Just pointer left and right and here right will track right side sorted part and then on left side we would try to find suitable left if found then 
    ```
    class Solution {

        public int findLengthOfShortestSubarray(int[] arr) {
            int right = arr.length - 1;
            if (right == 0) return 0;
            while (right > 0 && arr[right] >= arr[right - 1]) {
                right--;
            }
            int ans = right;
            int left = 0;
            while (left < right) {
                if (left >0 && arr[left - 1] > arr[left]){
                    break;
                }
                while (right < arr.length && arr[left] > arr[right]) {
                    right++;
                }
                ans = Math.min(ans, right - left - 1);
                left++;
            }
            return ans;
        }
    }
    ```

4. Fuel and cost with circular road. Problem is you have have to find the index form where you can start and then you would reach again to same initial point.

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

1 2 3 4 5 



Total += Gas[i] -cost[i]

Example 1:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

0
1-3=-2
-2+2-4=-4


Example 2:
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.

 Solution: ToatlFuel-Totalcost if positive then there is solution exixted
 And Now just iterate over all starting points and find the point from where you positive answer. because now ofcourse there is a solution.

5. LinkedList nth Node
6. Hight of the LinkedList
7. 2 Pointer algorithm and 3 pointer algorithm 2Sum and 3Sum algorithm.
8. Plaindrome, Anagrame
9. There is array with n number and multiple zero, just place all 0 at left side corner without disturbing the order.
 Solution: Just take 2 pointer and back traverse that would save you from again iterating for suffling if we would do it from forward it is needed.
 Forward itration O(n2) - > BackwardIterations O(n)

10. Reverse a string  without using and any built-in functions. : Recursion

11. https://leetcode.com/problems/majority-element/description/

12. Major Elements 1 & 2 : Byorrs vore algorith which helps in finding n/2 occurence and it takes assumption that all other elements have then less than n/2 freqency.

```
An analogy that might help.
Imagine some armies of people in a country with a population of 7.
4 people are from the army A and 3 are from the army B. The soldiers that fight each other die.
So, in this case we will be left with only 1 soldier of army A-the king/ majority element.

Now, Imagine a country with a population of 7 and we have 3 of army A, 3 of army B and 1 of army C.
If A and B fight with each other then the majority army might not win, so they are forced to form a truce and become partners.
To defeat the other members in the country both parties will send 1 of their soldiers since if only one of them sends, then the other becomes the stronger army.
Now we have 2 kings in the country/ 2 majorities.

If armies need a majority more than n/2 then we can have 1 dominant army.
If armies need a majority more than n/3 then we CAN have 2 dominant armies.
If armies need a majority more than n/4 then we CAN have 3 dominant armies.

So with more than n/3 and n/4 there is a possibility of having mutiple majority members.

This question-https://leetcode.com/problems/majority-element/ will help you find the 1 majority element with more than n/2 members.

```

class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int[] count = new int[2];
        int[] candidate = new int[2];

        for (int num : nums) {
            if (count[0] == 0 && candidate[1] != num) {
                candidate[0] = num;
                count[0] = 1;
            } else if (count[1] == 0 && candidate[0] != num) {
                candidate[1] = num;
                count[1] = 1;
            } else if (candidate[0] == num) {
                count[0]++;
            } else if (candidate[1] == num) {
                count[1]++;
            } else {
                count[0]--;
                count[1]--;
            }
        }

        count[0] = 0;
        count[1] = 0;
        for (int num : nums) {
            if (num == candidate[0]) count[0]++;
            else if (num == candidate[1]) count[1]++;
        }

        int threshold = nums.length / 3;

        List<Integer> result = new ArrayList<>();
        if (count[0] > threshold) result.add(candidate[0]);
        if (count[1] > threshold) result.add(candidate[1]);

        return result;
    }
}

```
class Solution {
    // 2,2,1,1,1,2,2
    public int majorityElement(int[] nums) {
        int count =0;
        int majEle = -1;
        for (int num : nums) {
            if (count ==0 ) {
                majEle = num; 
            }

            if (majEle != num) {
                count--;
            }
            else{
                count++;
            }
        }

        return majEle;
    }
}
```

13. Subarray Sum Equals K :
    - Commulative Sum array
    - Running Sum with frequency count and sum-k contains hack
    ```
    class Solution {
    public int subarraySum(int[] nums, int k) {
        // b=sum-currEle
        // if this b exists somewhere in the cumm some that means out sum also exists that much time assumption
        // 1. Generally there 1st approach would be prepare the commulative sum array and on each subarray check the sum exists or not but it will complexity would be  O(n) + O(n2) (for i->n, for j->n)
        //2. would be Running sum intiution is kaddane algorithm and parallely take the frequency of sum. If runsum-k one tt exist in the Map then we have the k sum subarray also so that was the significance. and for sum==k case put O-1freq element on it
        HashMap <Integer, Integer> hs = new HashMap<>();
        hs.put(0,1);
        int sum = 0;
        int noOfSubarray =0;
        for (int num : nums) {
            sum += num;
            if (hs.containsKey(sum-k)) {
                noOfSubarray += hs.get(sum-k);
            }

            hs.put(sum, hs.getOrDefault(sum,0)+1);
        } 
        
        return noOfSubarray;
    }
}
```

14. Longest Subarray with maxSum by using kadanne algorithm.
    - Break when ever we would go negative throw that we could track the longest the subarray of maxSum
    ```
        class Solution {

        // arr: input array
        // Function to find the sum of contiguous subarray with maximum sum.
        int maxSubarraySum(int[] arr) {
            int max = arr[0];
            int sum = 0;
            for (int num : arr) {
                sum += num;
                if (sum < 0){
                    max = Math.max(sum, max);
                    sum = 0;
                }
                else {
                max = Math.max(sum, max);
                }
            }
            
            return max;
        }
    }
    ```

15. Contigeous Subarray with equals zero and 1 in an binary subarray.

```
class Solution {
    public int findMaxLength(int[] nums) {
        // n2
        // windowing fail we could not able to take decision when to leave and when to extend.
        // commulitive array

        // -1 0 -1
        // 0 1 0 1 0 0 1 0 1 n3 -> n2 optimized
        // -1 0 -1 0 -1 -2 -1 -2 -1 n2 -> whenever the values is reapeted that means somwhere in the mid 0 is created check its least index - currindex and compare it with maxsizeSubarray.

        //Q. subarray with 0 sum contains(runsum-0) check for no of subaaray thing. 
        // Running sum something is the last way to optimally solve this problem.

        // j-i = 2

// Solution => we could use a map to store the sum with lowest index , just by getting the running sum. and on each itr we could check if that sum alreay came or not if yes then currIndex-lowIndex and compare with maxsubarray that's it.


    HashMap<Integer, Integer> hs = new HashMap<>();
    hs.put(0, -1);
    int sum = 0;
    int max =0;
    for ( int i =0; i< nums.length; i++) {
        if ( nums[i] ==0) sum--;
        if ( nums[i] ==1) sum++;

        if (hs.containsKey(sum)) {
            int li = hs.get(sum);
            max = Math.max(Math.abs(i-li), max);
        }
        else {
            hs.put(sum, i);
        }
    }
    return max;
    }
}
```

16. K-Rotate Array : reversing logic that's it 
17. Merge-K Shorted Linked List
    - MergeLikedList K*nLogn
    - Heap -> 1. O(nlogn) , Space O(n.k) 2. O(nlogn) , Space O(k)
18. Robarry in alternative room 
    - inc, exec
    - Dp
19. Smallest Positive Integer in an array
    https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/
    - Sort and iterate
    - Use Visted array and iterate overthat and check the flag.
20. https://leetcode.com/problems/letter-combinations-of-a-phone-number/solutions/6051513/video-simple-solution/
    - Recurstion and HashSet
    ```
        class Solution {
        public List<String> letterCombinations(String digits) {
            String alpha="abcdefghijklmnopqrstuvwxyz";
            HashMap<Integer,String> hs=new HashMap<>();
            int s=0;
            int e=3;
            for(int i=2;i<=9;i++)
            {
                String t=alpha.substring(s,e);
                hs.put(i,t);
                s=e;
                e+=3;
                if(i+1 ==7 || i+1 ==9){
                
                e+=1;
                }
            }
            System.out.println(hs);
            //hashmap ready;
            ArrayList<String> arr=new ArrayList<String>();
            solve(0,digits,hs,arr,"");
            return arr;
                
                
        }
        
    public void solve(int i,String s,HashMap<Integer,String> hs,ArrayList<String> arr,String ans){
            if(i==s.length()){
                if(ans.equals(""))return;
            arr.add(ans);  
                return;
            }
            
            char ch=s.charAt(i);
            String itr=hs.get((int)(ch-'0'));
            for(char c:itr.toCharArray()){
                solve(i+1,s,hs,arr,ans+""+c);
            }
        }
    }
    ```
21. https://leetcode.com/problems/combination-sum/description/
    - Unbounded coins problem
    - here we have given unique distinct coins dinomination
    ```
    class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> ans = new ArrayList<>();
        solve(0, 0,candidates, target,ans ,new ArrayList<>());
        return ans;
    }

    public void solve(int prev, int runSum,int nums[], int target, List<List<Integer>> ans, List<Integer> toAdd ){
        if (runSum == target){
            ans.add(new ArrayList<>(toAdd)); // Create a copy of toAdd
            return;
        }

        for (int i= prev; i <nums.length; i++) {
            if ( nums[i]+runSum <= target){
                toAdd.add(nums[i]);
                solve(i,runSum+nums[i], nums, target, ans, toAdd);
                toAdd.remove(toAdd.size()-1);
            }
        }
    }
    }
    ```

22. https://leetcode.com/problems/combination-sum-ii/description/
    - Bounded coins problem no unlimites execution
    - No unique coins, so sort and check prev one is same yes then skip it.
    ```
    class Solution {
        public List<List<Integer>> combinationSum2(int[] candidates, int target) {
            List<List<Integer>> ans = new ArrayList<>();
            Arrays.sort(candidates);
            solve(0, 0,candidates, target,ans ,new ArrayList<>());
            return ans;
        }

        public void solve(int prev, int runSum,int nums[], int target, List<List<Integer>> ans, List<Integer> toAdd ){
            if (runSum == target){
                ans.add(new ArrayList<>(toAdd)); // Create a copy of toAdd
                return;
            }

            for (int i= prev; i <nums.length; i++) {
                if(i>prev && nums[i]==nums[i-1])continue;
                
                if ( nums[i]+runSum <= target){
                    toAdd.add(nums[i]);
                    solve(i+1,runSum+nums[i], nums, target, ans, toAdd);
                    toAdd.remove(toAdd.size()-1);
                }
            }
        }


    }
    ```
23. https://leetcode.com/problems/word-break/description/

```
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Map<String, Boolean> memo = new HashMap<>();
        Set<String> wordSet = new HashSet<>(wordDict);
        return dfs(s, wordSet, memo);
    }
    
    private boolean dfs(String s, Set<String> wordSet, Map<String, Boolean> memo) {
        if (memo.containsKey(s)) return memo.get(s);
        if (wordSet.contains(s)) return true;
        for (int i = 1; i < s.length(); i++) {
            String prefix = s.substring(0, i);
            if (wordSet.contains(prefix) && dfs(s.substring(i), wordSet, memo)) {
                memo.put(s, true);
                return true;
            }
        }
        memo.put(s, false);
        return false;
    }
}
```

24. https://leetcode.com/problems/integer-to-roman/submissions/1481145562/
    - Simple solution build values and roman number map and then iterate untill the value is greater than map of n[i]
    ```
    class Solution {
    public String intToRoman(int num) {
        int[] n = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] s = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        int i =0;
        String str = new String(); 
        while (num>0){
            if (num>=n[i]){
                str=str+s[i];
                num-=n[i];
            } else{
                i++;
            }
        }
        return str;
    }
}
    ```

25. https://leetcode.com/problems/roman-to-integer/submissions/1126427013/

```
class Solution {
    public int romanToInt(String s) {
        HashMap<Character,Integer> map = new HashMap<>();
        map.put('I',1);
        map.put('V',5);
        map.put('X',10);
        map.put('L',50);
        map.put('C',100);
        map.put('D',500);
        map.put('M',1000);

        int n = s.length();
        int ans = 0;

        for(int i = 0; i < n; i++){
            if(i < n-1 && map.get(s.charAt(i)) < map.get(s.charAt(i+1))){
                ans = ans - map.get(s.charAt(i));
            } else{
                ans = ans + map.get(s.charAt(i));
            }

        }
        System.out.println(map); //Checking the output
        return ans;
    }
}
```

26. https://leetcode.com/problems/word-break/submissions/1481982001/
    - Intiution behind this just iteratively try to break the string and then check it is contained in the hashSet of words or not.

    ```
    class Solution {
        public boolean wordBreak(String s, List<String> wordDict) {
            Map<String, Boolean> memo = new HashMap<>();
            Set<String> wordSet = new HashSet<>(wordDict);
            return dfs(s, wordSet, memo);
        }
        
        private boolean dfs(String s, Set<String> wordSet, Map<String, Boolean> memo) {
            if (memo.containsKey(s)) return memo.get(s);
            if (wordSet.contains(s)) return true;
            for (int i = 1; i < s.length(); i++) {
                String prefix = s.substring(0, i);
                if (wordSet.contains(prefix) && dfs(s.substring(i), wordSet, memo)) {
                    memo.put(s, true);
                    return true;
                }
            }
            memo.put(s, false);
            return false;
        }
    }
    ```
27. https://leetcode.com/problems/next-greater-element-ii/submissions/1482057568/
    - [8,2,9] -> [9, 9, -1]
    - Stack : Approach is simple in stack the hold the index init and iterate over the nums and if you got got greater simply pop that index from stack and update the nexGtElement in the array you would do that repeatedly untill you got a index who is bigger, if found then break and insert/push the curr index in the stack as it is small. and then repeat whole thing as is.
    - In this another one thing is circular array checking [10, 8, 2, 9] -> [-1, 9, 9, 10]
    ```
        class Solution {
        public int[] nextGreaterElements(int[] nums) {
            // 1. N2
            // 2. Stack 

            Stack<Integer> st = new Stack<Integer>();
            st.push(0);
            int i=1;
            int res[] = new int[nums.length];
            Arrays.fill(res, -1);

            while (i< 2*nums.length-1) {
                while(!st.isEmpty() && nums[i % nums.length] > nums[st.peek()]) {
                    res[st.pop()] = nums[i%nums.length];
                }
                st.push(i%nums.length);
                i++;
            }

            return res;
        }
        }
    ```
28. https://leetcode.com/problems/container-with-most-water/submissions/1482093749/?envType=problem-list-v2&envId=xf7wjegr
    - This question is different from ranwatertrapping because there is block and for each block we were try to find the max water contained
    - But here there is given vertical line we have to find the most water contained between them (rightindex -leftindex) -> space between two line  and just multiply with height.
    ```
    class Solution {
    public int maxArea(int[] height) {
        int leftmax = 0;
        int rightmax = height.length-1;
        int ans = 0;
        while(leftmax < rightmax) {
            if (height[leftmax] > height[rightmax]) {
                ans = Math.max(ans, (rightmax-leftmax)*height[rightmax]);
                rightmax--;
            } else {
                ans = Math.max(ans, (rightmax-leftmax)*height[leftmax]);
                leftmax++;
            }
        }
        return ans;   
    }
}
    ```

29.  https://leetcode.com/problems/substring-with-concatenation-of-all-words/submissions/440778866/
    - Given String s which contains the concataineted words and list of words
    - First we could maintain the each each characters hashmap freq but that will cost because firstly you would take freq and if matches then you would go for next words matching thing.
    - Instead simple store freq of words and then iterate concatinated string in windowing approach and window size would be words[0].length()*words.size() and internally prepare words and temp hashmap and check hashmap matches or not.

```
class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        
        int l = words[0].length(); // size of one word
        int k = words.length * l ; // size of concatenated words
        
        Map<String, Integer> map = new HashMap<String, Integer>();
        
        for (String word : words)
            map.put(word, map.getOrDefault(word,0) + 1);
        
        List<Integer> results = new ArrayList<Integer>();
        
        for (int i = 0 ; i <= s.length() - k ; i++)
        {
            if(helper(s.substring(i, i+k),map,words,l,k))
                results.add(i);
        }
        
        return results;
    }
    
    public boolean helper(String s, Map<String, Integer> map, String [] words, int l, int k)
    {
       
        Map<String, Integer> temp = new HashMap<String, Integer>();
        
        for (int i = 0 ; i < s.length() ; i = i + l)
        {
            String arr = s.substring(i, i+l);
            temp.put(arr, temp.getOrDefault(arr,0) + 1);
        }
        
        //compare if both the maps are same
          // System.out.println(map);
          //   System.out.println(temp);
        if(temp.equals(map))
            return true;
        else
            return false;
    }
}
```
30. First Missing Number 

```
class Solution {
    // Binary Search
    // Visited Marking Array O(n) space
    // Inplace tracking of 1-n number by negating the values at 0-n index places. make sure to remove negatives and greater number than n
    // Cyclic Sort : just swap the number untill the actuall number would not places on its actuall position.
    public int firstMissingPositive(int[] nums) {
        for (int i = 0; i < nums.length;) {
            int correctIdx = nums[i] - 1;
            if (nums[i] > 0 && nums[i] <= nums.length && nums[i] != nums[correctIdx]) 
                swap(nums, i, correctIdx);
            else 
                i++;
        }
        for (int i = 0; i < nums.length; i++) 
            if (nums[i] != i + 1) 
                return i + 1;
        return nums.length + 1;
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}

```

31. https://leetcode.com/problems/max-chunks-to-make-sorted/description/?envType=daily-question&envId=2024-12-19  Max Chunk Sorted

"Logic is simple just thougth for index and in question it is given that array would contain 0 to n-1 elements only."

```
class Solution {
    public int maxChunksToSorted(int[] arr) {
        HashMap<Integer, Boolean> hs = new HashMap<>();
        int chunk = 0;
        for (int i =0; i< arr.length; i++) {
            if (hs.isEmpty()) { //Break chunk and increase
                chunk++;
            }

            if (hs.containsKey(arr[i])) {
                hs.remove(arr[i]);
            } else {
                hs.put(arr[i],false);
            }

            if (hs.containsKey(i)) {
                hs.remove(i);
            } else {
                hs.put(i,false);
            }
        } 

        return chunk;
    }
}

class Solution {
        public int maxChunksToSorted(int[] arr) {
        int n = arr.length;
        int chunks = 0;
        int prefixSum = 0, sortedPrefixSum = 0;

        // Iterate over the array
        for (int i = 0; i < n; i++) {
            prefixSum += arr[i];
            sortedPrefixSum += i;

            if (prefixSum == sortedPrefixSum) {
                chunks++;
            }
        }
        return chunks;
    }
}

```

32. BuySell Stock : 1 transaction

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1115842722/

33. BuySell Stock-2: Multiple transaction allowed

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/1115856056/

"Logic Just track the min index whenever you would get the min value stock you have to buy and clear the previous transaction and
 add the previous transaction profit into the total-profit."
 Valley and mountain approach just find for pic then sell the previous one simply.
 Throw recursion  also are able to solve this problem.

```
class Solution {
    public int maxProfit(int[] prices) {
        int profit=0;
        int bs=0;//buy stock
        int ss=0;//sell stock
        for(int i=1;i<prices.length;i++){
            if(prices[i]>=prices[i-1]){
                ss++;
            }
            else{
                profit+=prices[ss]-prices[bs];
                bs=ss=i;
            }
        }
        profit+=prices[ss]-prices[bs];
        return profit;
    }
}
```

34. 2471. Minimum Number of Operations to Sort a Binary Tree by Level
 - https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/description/?envType=daily-question&envId=2024-12-23

35. https://leetcode.com/problems/maximal-square/description/ MaximalSquare
    - You just need to find the max-square size where that square would contains all 1.
    - If you have finded pre maxSquare finded from specific i,j then from next i,j point you have to check for next maxSquare+1.
    - For reducing re-computation the checking code matrix-area as we are starting from 1 area here we can just faith the pre-area has all one then for next one, I just need to check the borders only.
    ```
    class Solution {
    public int maximalSquare(char[][] matrix) {
        int maxSquare =0;
        for (int i = 0; i< matrix.length; i++) {
            for (int j =0; j< matrix[0].length; j++) {
                if (matrix[i][j] == '1') {
                    maxSquare = recSolve(matrix, i, j, maxSquare+1);
                }
            }
        }
        return maxSquare*maxSquare;       
    }

    public int recSolve(char[][] matrix, int i, int j, int n) {
        int maxPossibleSquare= Math.min(matrix[0].length, matrix.length);
        if (n == maxPossibleSquare+1) {
            return n-1;
        }

        if (possibleSquare(i, j, n, matrix)) {
            return Math.max( n, recSolve(matrix, i, j, n+1));
        }
        return n-1;
    }

    boolean possibleSquare(int row, int col, int n, char[][] matrix) {
        if (row+n > matrix.length || col+n > matrix[0].length ){
            return false;
        }

        for (int i =row ; i< row+n ; i++) {
            for (int j =col; j< col+n ; j++) {
                if (matrix[i][j] == '0') return false;
            }
        }

        return true;
    }
}
    ```

36. https://leetcode.com/problems/minimum-path-sum/submissions/1487122115/ Minimum-Path-Sum problem
    - There are 2 direction you can travel either left or down the row.

37. https://leetcode.com/problems/sort-colors/submissions/1487180151/ 
    - Sort color 1, 0, 2 DMP flag/ 3pointer algorithm
    - On left side mid we are always assured that either there 1 or zero because we have started    the mid pointer from 0-th index or left side. But on the right side there is possibility 3 possible elements 0, 1, 2 when there is swap between 0 or 1 there is 1 more decision we have to take {0-> left swap , 1-> mid++} and with swapping  zero-side it is gurantted we would be swapped with 1 so on left hand side that why we are incrementing mid++. 
    ```
    class Solution {
    public void sortColors(int[] nums) {
        int left = 0, right = nums.length-1, mid = left;
        while (mid <= right) {
            if (nums[mid] == 1) {
                mid++;
            } else if (nums[mid] < 1) {
                //0 then swap with the left and increase the left and mid
                swap(left, mid, nums);
                mid++;
                left++;
            } else if (nums[mid] > 1) {
                //2 then swap with right and decrement right-- and mid++
                swap(right, mid, nums);
                right--;
            }
        }
    }

    public void swap (int i, int j, int[] nums ) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

}
    ```

38. https://leetcode.com/problems/find-bottom-left-tree-value/submissions/1487195970/ FindBottumLeft node of the tree.
39. https://www.geeksforgeeks.org/problems/symmetric-tree/1  

```
class Solution {
    // Return true/false denoting whether the tree is Symmetric or not
    public static boolean isSymmetric(Node root) {
        if (root == null) {
            return true;
        }
        
        Queue<Node> q = new LinkedList<>();
        q.add(root.left);
        q.add(root.right);
        
        while (!q.isEmpty()) {
            Node LN = q.poll();
            Node RN = q.poll();
            
            if(LN ==null&& RN == null){
                continue;
            }
            if(LN == null || RN == null || LN.data != RN.data){
                return false;
            }
            
            q.add(LN.left);
            q.add(RN.right);
            q.add(LN.right);
            q.add(RN.left);
        }
        
        return true;
    }
}
```

40. Biotonic/ Peak Element in the mountain: simple solution max element would be the maximum.
    - https://leetcode.com/problems/peak-index-in-a-mountain-array/description/


41. https://leetcode.com/problems/target-sum/description/
```
You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.
```

```
class Solution {
    public int findTargetSumWays(int[] nums, int target) {
       return waysToTarget(0, nums, target, 0);
    }

    public int waysToTarget(int curr,int nums[], int target, int sum) {
        if (curr >= nums.length){
            if (sum == target) return 1;
            return 0;
        }

        int cnt = 0;
        cnt = cnt + waysToTarget(curr+1, nums, target, sum+nums[curr]);
        cnt = cnt + waysToTarget(curr+1, nums, target, sum-nums[curr]);
        return cnt;
    }
}
```

42. https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/description/
43. https://leetcode.com/problems/permutations-ii/description/
44. https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/description/

45. https://leetcode.com/problems/minimum-cost-for-tickets/description/?envType=daily-question&envId=2024-12-31
```
class Solution {
    int dp[];
    public int mincostTickets(int[] days, int[] costs) {
        dp = new int[days.length];
        Arrays.fill(dp, -1);
        return solve(days, costs, 0);
    }

    public int solve( int[] days, int costs[], int index ) {
        if (index > days.length-1) {
            return 0;
        }

        if (dp[index] != -1) return dp[index];

        int oneDayCost = costs[0] + solve(days, costs, index+1);

        int j = index;
        while (j<days.length && days[j] < days[index] + 7 ) j++;
        int sevenDayCost = costs[1] + solve(days, costs, j);

        int k = index;
        while (k<days.length && days[k] < days[index] + 30) k++;
        int thirtyDayCost = costs[2] + solve(days, costs, k);


        dp[index] = Math.min(oneDayCost, Math.min(sevenDayCost, thirtyDayCost));

        return dp[index];
    }
}
```

46. Inversion Count GFG: 
    - MergeShort +cnt
47. https://www.geeksforgeeks.org/survival/ 
48. https://leetcode.com/problems/count-vowel-strings-in-ranges/description/ : 
    - simple prefix but inclusive one for n take n+1 size.

49. https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1
    - We could solve using finding all possible k-subarray. TLE
    - We can Binary-Search approach because here book pages are monotonouus.
    If it possible to pages-distribute under the limit with k or less than k element. 
    if greater then k that means we picked a limit too much low which distributes greater student 
    then mark it false and find slightly greater limit.

    ```
    class Solution {
    public static int findPages(int[] arr, int k) {
        if (arr.length < k) return -1;
        int max = 0;
        int sum = 0;
        for (int i =0; i< arr.length; i++) {
            sum += arr[i];
            max = Math.max(max, arr[i]);
        }
        
        int l = max;
        int h = sum;
        // we have to find the smallest limit where we would be able to distribute the all the pages among in k-students.
        int result =-1;
        if (k == 1) return sum;
        while (l<h) {
            int mid= (l+h)/2;
            if (isPossible(mid, arr, k)) {
                result = mid;
                h = mid;
            }
            else {
                l = mid+1;
            }
        }
        
        return h;
    }
    
    public static boolean isPossible (int limit, int[] arr, int k) {
        int cnt =1;
        int sum =0;
        for (int i = 0; i< arr.length; i++) {
            sum += arr[i];
            if (sum > limit) {
                cnt++;
                if (cnt > k) {
                    return false;
                }
                sum = arr[i];

            }
        }
        return true;
    }
}
    ```

50. https://www.geeksforgeeks.org/problems/check-if-it-is-possible-to-survive-on-island4922/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card

```
class Solution{

    static int minimumDays(int S, int N, int M){

        if (M>N){
            return -1;
        }

        if(S>=7 && (N-M)*6<M){
            return -1;
        }

        int day=1;
        int newBuy =1;
        int remFood = N;

        while (day <= S) {
            if (remFood < M) {
                remFood += N;
                newBuy++;
            }

            remFood -= M;
            if( (day+1)<=S && (day+1)%7==0 && remFood<M){
                remFood+=N;
                newBuy++;
            }
        //   System.out.println("remFood "+ remFood +" day = "+ day + " newbuy = " + newBuy);
            day++;
        }
        return newBuy;
    }
}
 
```
Question: 1

You are given the root of a binary tree with unique values, and an integer start. At Second 0, a virus infection starts from the node with value start.

Each Second, a node becomes infected if:

The node is currently uninfected.
The node is adjacent to an infected node.
Return the number of Seconds needed for the entire tree to be infected.

input:
         10  
      /     \
 12      13
        /       \
    14        15
   /  \        /   \
21 22  23  24

Start = 14
Output: 3 Seconds

Input: 
       3
    /    \
  4      1
            \
             2
Start = 1
Output: 2 Seconds

Constraints:

The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 105
Each node has a unique value.
A node with a value of start exists in the tree.



Problem 2

Given n meetings in the form of start[] and end[], where start[i] is the start time of ith meeting and end[i] is the end time of ith meeting. The task is to print the meeting number of all the meetings which can be held in a single room such that total number of meetings held is maximized. The meeting room can have only one meeting at a particular time.

Note: The start time of one chosen meeting can’t be equal to the end time of any other chosen meeting.


Examples: 

Input: start[] = {1, 3, 0, 5, 8, 5}, end[] = {2, 4, 6, 7, 9, 9} 
Output: 1 2 4 5
Explanation: We can attend the 1st meeting from (1 to 2), then the 2nd meeting from (3 to 4), then the 4th meeting from (5 to 7), and the 5th meeting from (8 to 9).


Input: start[] = {10, 12, 20}, end[] = {20, 25, 30}
Output: 1
Explanation: We can attend at most one meeting in a single meeting room.

Pair<Integer, List<Integer>>

O(Nlogn + n)



class Main {
    public static void main(String[] args) {
        int start[] = {1, 3, 0, 5, 8, 5};
        int end[] = {2, 4, 6, 7, 9, 9}; 
        
        List<Pair<Integer, List<Integer>>> pq= new ArraysList<>();
        //Pair<Integer, List<Integer>>
        
 
        
        Collections.sort(pq, 
                    (a,b)->{b.second().get(2)- a.second().get(2) }
                    );
        List<Integer> ans = new ArrayList<Integer>(); 
        List<Integer> current = null;
        for (Pair<Integer, List<Integer>> pair : pq) {
            if (current ==null) {
                current = pair.second();
                ans.add(pair.first());
                continue;
            }
            List<Integer> temp = pair. 
            if (current.get(1) >= )
            
        }
        
        
    }
}





https://www.linkedin.com/company/singlestore/jobs/
---------------------------------------------------------------------


# DSA Patterns:
Until I found these 20 DSA patterns 

1. Fast and Slow Pointer
2. Merge intervals
3. Sliding window
4. Islands (Matrix Traversal)
5. Two pointers
6. Cyclic Sort
7. In-place Reversal of Linkedin List
8. Breadth First Search
9. Depth First Search
10. Two Heaps
11. Subsets
12. Modified Binary Search
13. Bitwise XOR
14. Top 'K' elements
15. K way merge
16. 0/1 Knapsack (Dynamic Programming)
17. Unbounded Knapsack (Dynamic Programming)
18. Topological Sort (Graphs)
19. Monotonic Stack
20. Backtracking

# System-Design

https://www.linkedin.com/posts/karan-saxena-466b07190_80-of-the-system-design-interviews-ive-activity-7274766004163940352-b3IZ?utm_source=share&utm_medium=member_desktop

https://www.linkedin.com/in/neha-sharma-2b4537269/

https://www.linkedin.com/company/scoremesolutions/posts/?feedView=all

```
2 hours ago
18 Banglore India based startups list continuously hiring for multiple positions:

1. Digit Insurance: https://lnkd.in/eTsqcNzf
2. Fisdom: https://lnkd.in/engZ8KdB
3. Chingari: https://lnkd.in/ecGZhB46
4. Medlife: https://lnkd.in/e8M8UrSc
5. Vymo: https://lnkd.in/eHgaXvup
6. LeadSquared: https://lnkd.in/eFVi2QKz
7. FamPay: https://lnkd.in/ecCmgmUW
8. Quikr: https://lnkd.in/eAEExEtM
9. Quizizz: https://lnkd.in/eTCxS4td
10. Cell Propulsion: https://lnkd.in/etgmztXB
11. Dukaan: https://lnkd.in/eegUuj6p
12. Play Shifu: https://lnkd.in/eV-QvMyu
13. MediBuddy: https://lnkd.in/edJ_4XV3
14. Furlenco: https://lnkd.in/e7pBHUEf
15. Swiggy: https://lnkd.in/e6uiBnUh
16. Treebo Hotels: https://lnkd.in/eqGV_QSy
17. Betterhalf: https://lnkd.in/e8wT62Gp
18. Portea Medical: https://lnkd.in/eNCc4QME

Check their career pages using the links attached.

Share this with everyone who needs to know.

Follow Tanmay Goel for more such updates.
```


https://www.linkedin.com/posts/karan-saxena-466b07190_ive-been-asked-this-one-question-in-80-activity-7276966289829494784-K5TE?utm_source=share&utm_medium=member_desktop
=============================================================================================================

# React

1. 