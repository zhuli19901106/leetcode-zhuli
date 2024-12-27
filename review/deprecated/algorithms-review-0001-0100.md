#1 Two Sum

// #1 两数之和

描述：给定一个整数数组和一个值target，求两个下标i、j，使得a[i] + a[j] = target，返回下标。

// [#1](https://leetcode.com/problems/two-sum/) Description: Two Sum | LeetCode OJ

解法1：可以用哈希表不断记录每个元素对应的下标，然后查找target - a[i]就行了，查到了就有，查不到就没有。时间空间复杂度都是O(N)。中规中矩。

// Solution 1: Use a hash table to record the index of every element and look for target - a[i] in the hash table. Positive, bingo; negative, keep looking. Time and space are both O(N). Will do.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0001_two-sum_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0001_two-sum_1_AC.cpp)

解法2：把数组排序，然后前后两指针向中间靠拢。如果数组本身有序，此方法更好。时间O(N * logN)，空间O(1)。

// Solution 2: Sort the array and let two pointers close in on each other from both ends. This works better when the array is already sorted. O(N * logN) time and O(1) space.

代码2：太懒不写

// Code 2: Too lazy to write.

<hr>

#2 Add Two Numbers

// #2 两数相加

描述：两个大数，用链表表示。您给做个加法。

// [#2](https://leetcode.com/problems/add-two-numbers/) Description: Add Two Numbers | LeetCode OJ

解法1：加呗。

// Solution 1: Just get it done.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0002_add-two-numbers_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0002_add-two-numbers_1_AC.cpp)

<hr>

#3 Longest Substring Without Repeating Characters

// #3 字母不带重样儿的最长子串

描述：给定一个字符串，看标题。

// [#3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) Description: Longest Substring Without Repeating Characters | LeetCode OJ

解法1：用一个数组实时统计每个字母的出现次数，边走边数就行了。

// Solution 1: Maintain a counter array to keep the statistics of letters. Keep two pointers on watch and count as you go.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/longest-substring-without-repeating-characters_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/longest-substring-without-repeating-characters_1_AC.cpp)

<hr>

#4 Median of Two Sorted Arrays

// #4 俩有序数组的中位数

描述：给定俩有序数组，找出把它俩合并后所得数组的中位数。要求对数时间搞定。

// [#4](https://leetcode.com/problems/median-of-two-sorted-arrays/) Description: Median of Two Sorted Arrays | LeetCode OJ

解法1：暴力归并，O(N)时间。

// Solution 1: Brute-force merge, O(N) time.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0004_median-of-two-sorted-arrays_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0004_median-of-two-sorted-arrays_1_AC.cpp)

解法2：二分思想，递归实现。你要迭代也可以，不过代码更复杂些就是了。然而这个解法不是O(logN)，而是O(log ^ 2 N)时间。更好的解法我还没想出来。

// Solution 2: Binary search solution by recursion. Iterative solution is OK, but requires more sophisticated measures. Yet this is not an O(logN), but an O(log ^ 2 N) solution. I'm still working on a better one.

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0004_median-of-two-sorted-arrays_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0004_median-of-two-sorted-arrays_2_AC.cpp)

<hr>

#5 Longest Palindromic Substring

// #5 最长回文子串

描述：如题。

// [#5](https://leetcode.com/problems/longest-palindromic-substring/) Description: Longest Palindromic Substring | LeetCode OJ

解法1：暴力过。

// Solution 1: Brute-force.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0005_longest-palindromic-substring_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0005_longest-palindromic-substring_1_AC.cpp)

解法2：Manacher算法，动态规划的经典实例。

// Solution 2: Manacher Algorithm, one of most classical application of dynamic programming.

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0005_longest-palindromic-substring_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0005_longest-palindromic-substring_2_AC.cpp)

<hr>

#6 ZigZag Conversion

// #6 字符串Z形排列

描述：给定字符串，按某种奇怪的方式排列一下。

// [#6](https://leetcode.com/problems/zigzag-conversion/) Description: ZigZag Conversion | LeetCode OJ

解法1：不涉及算法，小心行事即可。

// Solution 1: Got nothing to do with algorthms, just beware of any bugs.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0006_zigzag-conversion_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0006_zigzag-conversion_1_AC.cpp)

<hr>

#7 Reverse Integer

// #7 反转整数

描述：给定一个10进制整数，翻转它。

// [#7](https://leetcode.com/problems/reverse-integer/) Description: Reverse Integer | LeetCode OJ

解法1：能用整数就别用浮点，能用数值就别用字符串。

// Solution 1: Make do with integer or numberic whenever possible. Extra type conversion means extra overhead.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0007_reverse-integer_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0007_reverse-integer_1_AC.cpp)

<hr>

#8 String to Integer (atoi)

// #8 字符串转整数

描述：atoi，你懂的。

// [#8](https://leetcode.com/problems/string-to-integer-atoi/) Description: String to Integer (atoi) | LeetCode OJ

解法1：转呗。

// Solution 1: Just do it.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0008_string-to-integer-atoi_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0008_string-to-integer-atoi_1_AC.cpp)

<hr>

#9 Palindrome Number

// #9 回文数

描述：如题。

// [#9](https://leetcode.com/problems/palindrome-number/) Description: Palindrome Number | LeetCode OJ

解法1：跟回文串一个道理。

// Solution 1: Same as palindromic strings.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0009_palindrome-number_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0009_palindrome-number_1_AC.cpp)

<hr>

#10 Regular Expression Matching

// #10 正则匹配

描述：如题。

// [#10](https://leetcode.com/problems/regular-expression-matching/) Description: Regular Expression Matching | LeetCode OJ

解法1：理解“回溯”二字。

// Solution 1 Try to understand the word "backtracking".

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0010_regular-expression-matching_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0010_regular-expression-matching_1_AC.cpp)

<hr>

#11 Container With Most Water

// #11 存水最多的容器

描述：给定一堆高矮不一的平行的墙，选择其中两堵作为两壁，问最多能存多少水。

// [#11](https://leetcode.com/problems/container-with-most-water/) Description: Container With Most Water | LeetCode OJ

解法1：O(N)算法的思想很巧妙，需要一点推理。

// Solution 1: The O(N) solution is clever. You'll need a little reasoning to get ahold of it.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0011_container-with-most-water_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0011_container-with-most-water_1_AC.cpp)

<hr>

#12 Integer to Roman

// #12 整数转罗马数字

描述：如题。

// [#12](https://leetcode.com/problems/integer-to-roman/) Description: Integer to Roman | LeetCode OJ

解法1：模拟题。

// Solution 1: Simulation problem.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0012_integer-to-roman_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0012_integer-to-roman_1_AC.cpp)

<hr>

#13 Roman to Integer

// #13 罗马数字转整数

描述：如题。

// [#13](https://leetcode.com/problems/roman-to-integer/) Description: Roman to Integer | LeetCode OJ

解法1：模拟题。

// Solution 1: Simulation problem.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0013_roman-to-integer_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0013_roman-to-integer_1_AC.cpp)

<hr>

#14 Longest Common Prefix

// #14 最长公共前缀

描述：给定一组字符串，找出最长公共前缀。

// [#14](https://leetcode.com/problems/longest-common-prefix/) Description: Longest Common Prefix | LeetCode OJ

解法1：找呗。

// Solution 1: Don't bother with trie or something.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0014_longest-common-prefix_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0014_longest-common-prefix_1_AC.cpp)

<hr>

#15 3Sum

// #15 三数之和

描述：给定一个数组和一个值target，找出所有三数加起来等于target的组合。

// [#15](https://leetcode.com/problems/3sum/) Description: 3Sum | LeetCode OJ

解法1：将数组排序，一维度自由，剩下两维度按Two Sum来搞。时间O(N ^ 2)，空间O(1)。

// Solution 1: Sort the array. Set one dimension free and do Two Sum with the other two.O(N ^ 2) time and O(1) space.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0015_3sum_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0015_3sum_1_AC.cpp)

<hr>

#16 3Sum Closest

// #16 最接近的三数之和

描述：给定一个数组和一个值target，找出其中仨元素，使其加起来最接近target。

// [#16](https://leetcode.com/problems/3sum-closest/) Description: 3Sum Closest | LeetCode OJ

解法1：和3Sum思路类似，不过这次不断更新结果即可。

// Solution 1: Similar to 3Sum, but this time we keep updating the result as we go.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0016_3sum-closest_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0016_3sum-closest_1_AC.cpp)

<hr>

#17 Letter Combinations of a Phone Number

// #17 手机键盘的字母组合

描述：Nokia手机，给定一个数字串，看看有多少种对应的字母串。

// [#17](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) Description: Letter Combinations of a Phone Number | LeetCode OJ

解法1：搜呗。

// Solution 1: Just make a search for it.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0017_letter-combinations-of-a-phone-number_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0017_letter-combinations-of-a-phone-number_1_AC.cpp)

<hr>

#18 4Sum

// #18 四数之和

描述：不用多说了。

// [#18](https://leetcode.com/problems/4sum/) Description: 4Sum | LeetCode OJ

解法1：两维度自由，两维度Two Sum。当然，该排序排序。

// Solution 1: Set two dimensions free, do a Two Sum on the other two. Sort the array if you have to.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0018_4sum_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0018_4sum_1_AC.cpp)

<hr>

#19 Remove Nth Node From End of List

// #19 删除链表倒数第N个节点

描述：如题。

// [#19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) Description: Remove Nth Node From End of List | LeetCode OJ

解法1：链表题，小心驶得万年船。

// Solution 1: Can't be too careful with a linked list.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0019_remove-nth-node-from-end-of-list_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0019_remove-nth-node-from-end-of-list_1_AC.cpp)

<hr>

#20 Valid Parentheses

// #20 有效括号序列

描述：给定一个括号序列，判断其是否合法。

// [#20](https://leetcode.com/problems/valid-parentheses/) Description: Valid Parentheses | LeetCode OJ

解法1：用了个栈。

// Solution 1: Use a stack.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0020_valid-parentheses_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0020_valid-parentheses_1_AC.cpp)

<hr>

#21 Merge Two Sorted Lists 

// #21 归并两个有序链表

描述：如题。

// [#21](https://leetcode.com/problems/merge-two-sorted-lists/) Description: Merge Two Sorted Lists | LeetCode OJ

解法1：只要是链表题，就要极力避免new新节点。你可以从操作系统的角度去考虑一次new操作背后发生的事情，尤其是内核态的部分。知其然，弗若知其所以然。

// Solution 1: Avoid using “new” whenever dealing with a linked list problem. Think about the things behind a "new" operation, especially the kernel-space part. It takes more to get to the "how" and "why" than a mere "what".

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0021_merge-two-sorted-lists_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0021_merge-two-sorted-lists_1_AC.cpp)

<hr>

#22 Generate Parentheses 

// #22 生成括号。

描述：给定一个长度，生成所有此长度的合法括号序列。

// [#22](https://leetcode.com/problems/generate-parentheses/) Description: Generate Parentheses | LeetCode OJ

解法1：Catalan数知道吧？搜。

// Solution 1: Ever heard of the Catalan Numbers? Just DFS.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0022_generate-parentheses_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0022_generate-parentheses_1_AC.cpp)

<hr>

#23 Merge k Sorted Lists 

// #23 归并k个有序链表

描述：如题。

// [#23](https://leetcode.com/problems/merge-k-sorted-lists/) Description: Merge k Sorted Lists | LeetCode OJ

解法1：快使用最小堆，红红火火。

// Solution 1: Yo, Min heap. Check it out, dogg.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0023_merge-k-sorted-lists_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0023_merge-k-sorted-lists_1_AC.cpp)

<hr>

#24 Swap Nodes in Pairs 

// #24 交换节点对

描述：给定一个链表，每两个节点做一下交换。

// [#24](https://leetcode.com/problems/swap-nodes-in-pairs/) Description: Swap Nodes in Pairs | LeetCode OJ

解法1：换呗。

// Solution 1: Do it.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0024_swap-nodes-in-pairs_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0024_swap-nodes-in-pairs_1_AC.cpp)

<hr>

#25 Reverse Nodes in k-Group 

// #25 每k个节点反转一下

描述：给定一个链表，每k个节点一组，做一次反转。尾巴凑不齐的，自己看着办。

// [#25](https://leetcode.com/problems/reverse-nodes-in-k-group/) Description: Reverse Nodes in k-Group | LeetCode OJ

解法1：很容易出bug的题，小心行事。把常用操作单独写成函数是个好习惯。强行压缩代码长度，迟早是要栽跟头的。

// Solution 1: A tricky problem, proceed with caution. It's good practice to wrap what you do frequently in a function. Excessive obsession with shortest code length is gonna bring you down, one of these days.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0025_reverse-nodes-in-k-group_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0025_reverse-nodes-in-k-group_1_AC.cpp)

<hr>

#26 Remove Duplicates from Sorted Array 

// #26 去除有序数组的重复元素

描述：如题。

// [#26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) Description: Remove Duplicates from Sorted Array | LeetCode OJ

解法1：水题。以后会经常写这个的，就跟打字一样。

// Solution 1: Piece of cake, you'll be seeing a lot of this in the future.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0026_remove-duplicates-from-sorted-array_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0026_remove-duplicates-from-sorted-array_1_AC.cpp)

<hr>

#27 Remove Element 

// #27 删除元素

描述：删除数组中所有等于某个值的元素。

// [#27](https://leetcode.com/problems/remove-element/) Description: Remove Element | LeetCode OJ

解法1：删呗。

// Solution 1: Do it.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0027_remove-element_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0027_remove-element_1_AC.cpp)

<hr>

#28 Implement strStr() 

// #28 实现strStr()

描述：字符串匹配，经典问题。

// [#28](https://leetcode.com/problems/implement-strstr/) Description: Implement strStr() | LeetCode OJ

解法1：暴力过，O(N ^ 2)时间。

// Solution 1: Brute-force solution with O(N ^ 2) time.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0028_implement-strstr_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0028_implement-strstr_1_AC.cpp)

解法2：Rabin-Karp算法。对字符串做哈希是一种非常巧妙的做法，这种思想在很多情景下可以大大提高匹配效率。有必要的话，可以复查以严格保证匹配的正确性。

// Solution 2: Rabin-Karp Algorithm. Hashing a string is clever way to immensely accelerate pattern matching. Double check if you can't tolerate false positives.

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0028_implement-strstr_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0028_implement-strstr_2_AC.cpp)

解法3：传说中的KMP算法，一个我写了不下十次还是很难独立一次性写对的算法。next数组堪称艺术品，很清真。

// Solution 3: The legendary KMP Algorithm, which I can't possibly write down perfectly even after using a dozen of it. The "next" array is simply a great work of art, as beautiful as it is powerful.

[代码3](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0028_implement-strstr_3_AC.cpp)

// [Code 3](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0028_implement-strstr_3_AC.cpp)

<hr>

#29 Divide Two Integers 

// #29 两整数相除

描述：不准乘除，不准膜。

// [#29](https://leetcode.com/problems/divide-two-integers/) Description: Divide Two Integers | LeetCode OJ

解法1：加减配合移位。照搞不误。

// Solution 1: +-&|<<, nomsayin?

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0029_divide-two-integers_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0029_divide-two-integers_1_AC.cpp)

<hr>

#30 Substring with Concatenation of All Words 

// #30 由所有单词连成的子串

描述：给定一个无重复单词的字典D，和一个长字符串S。找出S中的子串，该子串恰好是D中所有单词连接而成。

// [#30](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) Description: Substring with Concatenation of All Words | LeetCode OJ

解法1：碰见这种字典多而短的问题，本能地会想到字典树。其实用也可以，不用也可以。反正都要搜索一番。然而我闲字典树麻烦，所以想到用哈希值来代替字符串，这样能够O(1)时间进行匹配。结果确实很不错。哈希大法好，但有一点要记住：虽然哈希碰撞很难发生，但墨菲定律在那儿摆着，不检查的话迟早要完。

// Solution 1: It's intuitive to think of trie when dealing with a large dictionary of short words. Use it or not, you'll figure out a solution yourself. I chose string hashing to accelerate my string matching, which worked out just fine. Hashing it powerful, but keep Murphy's Law in mind, that hashing collisons do happen. You don't do a double check, your call.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0030_substring-with-concatenation-of-all-words_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0030_substring-with-concatenation-of-all-words_1_AC.cpp)

<hr>

#31 Next Permutation 

// #31 下一个排列

描述：给定一个排列，按照字典序把下一个弄出来。

// [#31](https://leetcode.com/problems/next-permutation/) Description: Next Permutation | LeetCode OJ

解法1：O(N)时间，注意要从后往前找。

// Solution 1: O(N) time. Search from back to front.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0031_next-permutation_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0031_next-permutation_1_AC.cpp)

<hr>

#32 Longest Valid Parentheses 

// #32 最长合法括号子串

描述：给定一个括号序列，找出最长的合法括号子串。

// [#32](https://leetcode.com/problems/longest-valid-parentheses/) Description: Longest Valid Parentheses | LeetCode OJ

解法1：碰见这种子串问题，基本都是一前一后两个指针，不过写法倒是各有不同。看代码。

// Solution 1: These "substring" problems can usually be solved with two running pointers. Although they come in various forms. Find more in the code.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0032_longest-valid-parentheses_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0032_longest-valid-parentheses_1_AC.cpp)

<hr>

#33 Search in Rotated Sorted Array 

// #33 旋转过有序数组的查找问题

描述：一个有序数组，可能进行了循环移位，在里面进行查找。

// [#33](https://leetcode.com/problems/search-in-rotated-sorted-array/) Description: Search in Rotated Sorted Array | LeetCode OJ

解法1：先把旋转的偏移量算出来，再二分查找。两部分都是O(logN)，所以还行。

// Solution 1: Find the rotation offset and do an offsetted binary search. Both parts are O(logN), works for me.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0033_search-in-rotated-sorted-array_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0033_search-in-rotated-sorted-array_1_AC.cpp)

<hr>

#34 Find First and Last Position of Element in Sorted Array

// #34 找出有序数组元素的起点终点。

描述：给定一个有序数组，找出某个值的起始和终止区间。

// [#34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) Description: Find First and Last Position of Element in Sorted Array | LeetCode OJ

解法1：lower_bound和upper_bound一起用。

// Solution 1: lower_bound and upper_bound will suffice.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0034_find-first-and-last-position-of-element-in-sorted-array_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0034_find-first-and-last-position-of-element-in-sorted-array_1_AC.cpp)

<hr>

#35 Search Insert Position 

// #35 寻找插入位置

描述：给定有序数组和一个值，寻找合适的插入位置。

// [#35](https://leetcode.com/problems/search-insert-position/) Description: Search Insert Position | LeetCode OJ

解法1：二分。

// Solution 1: Binary search.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0035_search-insert-position_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0035_search-insert-position_1_AC.cpp)

<hr>

#36 Valid Sudoku 

// #36 检查数独

描述：如题。

// [#36](https://leetcode.com/problems/valid-sudoku/) Description: Valid Sudoku | LeetCode OJ

解法1：按规矩来呗。

// Solution 1: Routine.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0036_valid-sudoku_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0036_valid-sudoku_1_AC.cpp)

<hr>

#37 Sudoku Solver 

// #37 解数独

描述：如题。

// [#37](https://leetcode.com/problems/sudoku-solver/) Description: Sudoku Solver | LeetCode OJ

解法1：标准递归回溯问题，注意递归写法，不要增加不必要的复杂度。跳舞链神马的，还是算了吧，太复杂。

// Solution 1: A typical DFS + backtracking problem. Write it carefully though, don't incur unnecessary time complexity. As for Dancing Links, I'll forget about it.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0037_sudoku-solver_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0037_sudoku-solver_1_AC.cpp)

<hr>

#38 Count and Say 

// #38 数数

描述：给定一个数字串，读出来。并把读的方法也表示成一个数字串。如此计算出第N个串。

// [#38](https://leetcode.com/problems/count-and-say/) Description: Count and Say | LeetCode OJ

解法1：不知道有没有什么数学解法？

// Solution 1: Is there any analytical solution? I mean, mathematically?

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0038_count-and-say_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0038_count-and-say_1_AC.cpp)

<hr>

#39 Combination Sum 

// #39 组合之和

描述：给定一个集合以及一个值target，找出所有加起来等于target的组合，要不带重样儿的。每个元素可以用无数次。

// [#39](https://leetcode.com/problems/combination-sum/) Description: Combination Sum | LeetCode OJ

解法1：搜。

// Solution 1: DFS.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0039_combination-sum_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0039_combination-sum_1_AC.cpp)

<hr>

#40 Combination Sum II 

// #40 组合之和2

描述：和之前差不多，区别是每个元素只能用一次。

// [#40](https://leetcode.com/problems/combination-sum-ii/) Description: Combination Sum II | LeetCode OJ

解法1：搜。

// Solution 1: DFS.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0040_combination-sum-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0040_combination-sum-ii_1_AC.cpp)

<hr>

#41 First Missing Positive

// #41 第一个未出现的正数

描述：给定无序数组，找出第一个未出现的正整数。

// [#41](https://leetcode.com/problems/first-missing-positive/) Description: First Missing Positive | LeetCode OJ

解法1：数组本身就可以用于标记。

// Solution 1: The input array itself can be used as marker array.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0041_first-missing-positive_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0041_first-missing-positive_1_AC.cpp)

<hr>

#42 Trapping Rain Water

// #42 雨水积水问题

描述：给定一个地形，计算能存多少雨水。

// [#42](https://leetcode.com/problems/trapping-rain-water/) Description: Trapping Rain Water | LeetCode OJ

解法1：不要考虑一个水坑能存多少水，而要考虑每一条能存多少雨水，这种违背直观的思考方式反而更容易编程。

// Solution 1: Don't try to calculate how much water can be trapped in a water pit. Think about how much water can be stored in each "stripe". This counter-intuitive way of thinking is actually better suited for programming.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0042_trapping-rain-water_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0042_trapping-rain-water_1_AC.cpp)

<hr>

#43 Multiply Strings

// #43 高精度乘法

描述：如题。

// [#43](https://leetcode.com/problems/multiply-strings/) Description: Multiply Strings | LeetCode OJ

解法1：暴力。FFT解法我没写。

// Solution 1: Brute-force. I didn't write the FFT solution myself, too much trouble.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0043_multiply-strings_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0043_multiply-strings_1_AC.cpp)

<hr>

#44 Wildcard Matching

// #44 通配符

描述：模式匹配的另一个基础示例。

// [#44](https://leetcode.com/problems/wildcard-matching/) Description: Wildcard Matching | LeetCode OJ

解法1：还是回溯。值得注意的是如何想办法剪枝。

// Solution 1: Use backtracking. How to do the pruning is one of the things worth noting.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0044_wildcard-matching_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0044_wildcard-matching_1_AC.cpp)

<hr>

#45 Jump Game II

// #45 青蛙跳2

描述：和Jump Game一样，这次计算最小步数。

// [#45](https://leetcode.com/problems/jump-game-ii/) Description: Jump Game II | LeetCode OJ

解法1： 扫一遍就行了。

// Solution 1: Sweep it over.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0045_jump-game-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0045_jump-game-ii_1_AC.cpp)

<hr>

#46 Permutations

// #46 全排列

描述：打印全排列。

// [#46](https://leetcode.com/problems/permutations/) Description: Permutations | LeetCode OJ

解法1：用next_permutation迭代。

// Solution 1: Iterate with next_permutation.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0046_permutations_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0046_permutations_1_AC.cpp)

解法2：DFS。

// Solution 2: DFS.

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0046_permutations_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0046_permutations_2_AC.cpp)

<hr>

#47 Permutations II 

// #47 全排列2

描述：和Permutations一样，不过序列可能有重复元素。

// [#47](https://leetcode.com/problems/permutations-ii/) Description: Permutations II | LeetCode OJ

解法1：用next_permutation迭代，不过函数自己写。

// Solution 1: Iterate with next_permutation, but write your own this time.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0047_permutations-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0047_permutations-ii_1_AC.cpp)

<hr>

#48 Rotate Image

// #48 旋转图像

描述：顺时针旋转90度，尽量不用额外空间。

// [#48](https://leetcode.com/problems/rotate-image/) Description: Rotate Image | LeetCode OJ

解法1：矩阵分四块儿就行。轮换着赋值，可保证O(1)空间。

// Solution 1: Segment the matrix into 2 by 2. By doing the value reassignments in a rotated manner, O(1) space is thus achieved.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0048_rotate-image_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0048_rotate-image_1_AC.cpp)

<hr>

#49 Group Anagrams

// #49 变位词归类

描述：给定一堆单词，把变位词放一块儿去。

// [#49](https://leetcode.com/problems/group-anagrams/) Description: Group Anagrams | LeetCode OJ

解法1：变位词排序之后就一样了。

// Solution 1: Anagrams become one after sorting.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0049_group-anagrams_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0049_group-anagrams_1_AC.cpp)

<hr>

#50 Pow(x, n)

// #50 幂

描述：求幂。

// [#50](https://leetcode.com/problems/powx-n/) Description: Pow(x, n) | LeetCode OJ

解法1：快速幂。

// Solution 1: Binary exponentiation.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0050_powx-n_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0050_powx-n_1_AC.cpp)

<hr>

#51 N-Queens

// #51 N皇后

描述：NxN棋盘摆N个棋子，要求不能同行、同列、同对角线、同反对角线，返回所有摆法。

// [#51](https://leetcode.com/problems/n-queens/) Description: N-Queens | LeetCode OJ

解法1：DFS + 回溯.

// Solution 1: DFS + backtracking.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0051_n-queens_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0051_n-queens_1_AC.cpp)

<hr>

#52 N-Queens II

// #52 N-Queens II

描述：N皇后问题，输出解的个数。

// [#52](https://leetcode.com/problems/n-queens-ii/) Description: N-Queens II | LeetCode OJ

解法1：目前并没有数学解，所以还是搜。

// Solution 1: There's currently no known formula for N-queen problem. So we'll do it the old way.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0052_n-queens-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0052_n-queens-ii_1_AC.cpp)

<hr>

#53 Maximum Subarray

// #53 最大子数组和

描述：如题。

// [#53](https://leetcode.com/problems/maximum-subarray/) Description: Maximum Subarray | LeetCode OJ

解法1：教材经典例子。

// Solution 1: Algo 101 on the textbook.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0053_maximum-subarray_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0053_maximum-subarray_1_AC.cpp)

<hr>

#54 Spiral Matrix

// #54 螺旋矩阵

描述：按螺旋方式遍历矩阵。

// [#54](https://leetcode.com/problems/spiral-matrix/) Description: Spiral Matrix | LeetCode OJ

解法1：模拟题。

// Solution 1: Simulation problem.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0054_spiral-matrix_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0054_spiral-matrix_1_AC.cpp)

<hr>

#55 Jump Game

// #55 青蛙跳

描述：给定一个数组A，每个A[i]表示你最远能跳的距离。从0出发问是否能跳到终点。

// [#55](https://leetcode.com/problems/jump-game/) Description: Jump Game | LeetCode OJ

解法1：扫一遍就行了。

// Solution 1: Jump ahead, don't look back.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0055_jump-game_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0055_jump-game_1_AC.cpp)

<hr>

#56 Merge Intervals

// #56 归并区间

描述：给定一些区间，该合并合并。

// [#56](https://leetcode.com/problems/merge-intervals/) Description: Merge Intervals | LeetCode OJ

解法1：排个序，归并。

// Solution 1: Sort and merge.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0056_merge-intervals_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0056_merge-intervals_1_AC.cpp)

<hr>

#57 Insert Interval

// #57 插入区间

描述：给定一堆区间，插入一个新区间。

// [#57](https://leetcode.com/problems/insert-interval/) Description: Insert Interval | LeetCode OJ

解法1：跟Merge Intervals一个思路。

// Solution 1: Similar to Merge Intervals.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0057_insert-interval_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0057_insert-interval_1_AC.cpp)

<hr>

#58 Length of Last Word

// #58 最后一个词的长度

描述：如题。

// [#58](https://leetcode.com/problems/length-of-last-word/) Description: Length of Last Word | LeetCode OJ

解法1：无聊。

// Solution 1: Boring.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0058_length-of-last-word_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0058_length-of-last-word_1_AC.cpp)

<hr>

#59 Spiral Matrix II

// #59 旋转矩阵2

描述：把1之n ^ 2按照螺旋顺序填入方阵。

// [#59](https://leetcode.com/problems/spiral-matrix-ii/) Description: Spiral Matrix II | LeetCode OJ

解法1：模拟题。

// Solution 1: Simulation problem.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0059_spiral-matrix-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0059_spiral-matrix-ii_1_AC.cpp)

<hr>

#60 Permutation Sequence

// #60 排列序列

描述：1~n有n!个排列，找出其中字典序排第k的排列。

// [#60](https://leetcode.com/problems/permutation-sequence/) Description: Permutation Sequence | LeetCode OJ

解法1：看代码吧。

// Solution 1: Just read the code.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0060_permutation-sequence_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0060_permutation-sequence_1_AC.cpp)

<hr>

#61 Rotate List

// #61 旋转链表

描述：给定一个链表， 循环移位k次。

// [#61](https://leetcode.com/problems/rotate-list/) Description: Rotate List | LeetCode OJ

解法1：要面面俱到。

// Solution 1: Mind the edge cases.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0061_rotate-list_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0061_rotate-list_1_AC.cpp)

<hr>

#62 Unique Paths

// #62 不同路径

描述： 给定MxN棋盘，只允许从左上往右下走，每次走一格。共有多少种走法？

// [#62](https://leetcode.com/problems/unique-paths/) Description: Unique Paths | LeetCode OJ

解法1：排列组合。

// Solution 1: Combination.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0062_unique-paths_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0062_unique-paths_1_AC.cpp)

<hr>

#63 Unique Paths II

// #63 不同路径2

描述：和之前一样，不过这次有些格子不让走。

// [#63](https://leetcode.com/problems/unique-paths-ii/) Description: Same as before, only in that some grids are blocked.

解法1：动态规划。

// Solution 1: Dynamic programming.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0063_unique-paths-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0063_unique-paths-ii_1_AC.cpp)

<hr>

#64 Minimum Path Sum

// #64 最小路径和

描述：和Unique Paths一样，不过这次每个点有权值，求最小路径和。

// [#64](https://leetcode.com/problems/minimum-path-sum/) Description: Same as Unique Paths, but this time we assign a weight to each grid and calculate minimum weight sum for the path.

解法1：DP。

// Solution 1: DP.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0064_minimum-path-sum_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0064_minimum-path-sum_1_AC.cpp)

<hr>

#65 Valid Number

// #65 数值判断

描述：给定一个字符串，判断是否符合数值类型的格式。

// [#65](https://leetcode.com/problems/valid-number/) Description: Valid Number | LeetCode OJ

解法1：典型的面试题，考察思维是否足够缜密。照理说一个正则表达式可以搞定，不过编译直接超时了，说明服务器对这个做了限制。所以只得手写各种判断。此题无须奇技淫巧，惟“认真”二字足矣。

// Solution 1: A typical filter for discreet thinkers. I thought a regular expression would suffice, but the compilation simply timed out. It appears the OJ servers discourage such attempt. Som no fancy tricks needed, just think it through and do it carefully.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0065_valid-number_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0065_valid-number_1_AC.cpp)

<hr>

#66 Plus One

// #66 加一

描述：高精度加一。

// [#66](https://leetcode.com/problems/plus-one/) Description: Plus One | LeetCode OJ

解法1：加呗。

// Solution 1: Do it.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0066_plus-one_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0066_plus-one_1_AC.cpp)

<hr>

#67 Add Binary

// #67 二进制加法

描述：二进制高精度加法。

// [#67](https://leetcode.com/problems/add-binary/) Description: Add Binary | LeetCode OJ

解法1：加呗。

// Solution 1: Do it.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0067_add-binary_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0067_add-binary_1_AC.cpp)

<hr>

#68 Text Justification

// #68 文字对齐

描述：给定一列单词，按照指定宽度将其排成格式工整的洋文。

// [#68](https://leetcode.com/problems/text-justification/) Description: Text Justification | LeetCode OJ

解法1：注意边界条件。

// Solution 1: Edge cases.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0068_text-justification_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0068_text-justification_1_AC.cpp)

<hr>

#69 Sqrt(x)

// #69 开方

描述：整数开方

// [#69](https://leetcode.com/problems/sqrtx/) Description: Sqrt(x) | LeetCode OJ

解法1：二分吧，你要牛顿法也行。

// Solution 1: Binary search will do. Newton-Raphson method is OK but a bit overpowered.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0069_sqrtx_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0069_sqrtx_1_AC.cpp)

<hr>

#70 Climbing Stairs

// #70 爬楼梯

描述：爬楼梯，每次能往上爬一或两级，问总共有多少种爬法。

// [#70](https://leetcode.com/problems/climbing-stairs/) Description: Climbing Stairs | LeetCode OJ

解法1：斐波那契。

// Solution 1: Fibonacci.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0070_climbing-stairs_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0070_climbing-stairs_1_AC.cpp)

<hr>

#71 Simplify Path

// #71 简化路径

描述：如题。

// [#71](https://leetcode.com/problems/simplify-path/) Description: Simplify Path | LeetCode OJ

解法1：栈。

// Solution 1: Stack.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0071_simplify-path_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0071_simplify-path_1_AC.cpp)

<hr>

#72 Edit Distance

// #72 编辑距离

描述：最短编辑距离，也叫Levenshtein距离。

// [#72](https://leetcode.com/problems/edit-distance/) Description: Edit Distance | LeetCode OJ

解法1：动态规划经典问题。

// Solution 1: A classic DP problem.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0072_edit-distance_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0072_edit-distance_1_AC.cpp)

<hr>

#73 Set Matrix Zeroes

// #73 矩阵置0

描述：给定一个矩阵，只要某个元素为0，就把对应的整行整列都置0。

// [#73](https://leetcode.com/problems/set-matrix-zeroes/) Description: Set Matrix Zeroes | LeetCode OJ

解法1：巧妙的地方在于如何避免外开辟空间，看代码吧。

// Solution 1: The tricky part is to do it in-place. Read the code for more detail.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0073_set-matrix-zeroes_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0073_set-matrix-zeroes_1_AC.cpp)

<hr>

#74 Search a 2D Matrix

// #74 二维矩阵查找

描述：给定一个二维数组，balabala。

// [#74](https://leetcode.com/problems/search-a-2d-matrix/) Description: Search a 2D Matrix | LeetCode OJ

解法1：说白了，就是个一维有序数组。

// Solution 1: Expand it into an 1-d array, you'll see.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0074_search-a-2d-matrix_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0074_search-a-2d-matrix_1_AC.cpp)

<hr>

#75 Sort Colors

// #75 颜色排序

描述：给定三中间色，分别标号为012， 按这个标号排序。

// [#75](https://leetcode.com/problems/sort-colors/) Description:

解法1：这种题除了用来面试，简直狗屁不通。正所谓千年科举，牢笼人才。天下读书人，一门心思都给了八股制艺，倒没几个人去富国强兵、振兴科教。这种为出题而出题的脑残面试题，岂不如出一辙？实乃可笑！你喜欢出这种卖弄奇技淫巧的面试题，我就如你所愿，写这么个“聪明”的解法。你说把0、1、2的个数都数出来不就得了？我偏要玩儿出个花儿来。否则，怎么显示我琢磨面试题下的苦功？倘若天下人都一门心思琢磨怎么考试，这国家也就药丸了。

// Solution 1: F* this problem.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0075_sort-colors_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0075_sort-colors_1_AC.cpp)

<hr>

#76 Minimum Window Substring

// #76 最小窗口子串

描述：给定一个长串S和一个短串T。求S中包含T所有字母的最短字串。

// [#76](https://leetcode.com/problems/minimum-window-substring/) Description: Minimum Window Substring | LeetCode OJ

解法1：凡是这种滑动窗口的问题，都是两个指针一前一后，你追我赶。

// Solution 1: All such "sliding window" problems can be tackled with two running pointers, one after the other.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0076_minimum-window-substring_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0076_minimum-window-substring_1_AC.cpp)

<hr>

#77 Combinations

// #77 组合

描述：从1~N里选K个数，输出所有选法。

// [#77](https://leetcode.com/problems/combinations/) Description: Combinations | LeetCode OJ

解法1：DFS。

// Solution 1: DFS.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0077_combinations_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0077_combinations_1_AC.cpp)

解法2：类似next_permutation。

// Solution 2: Similar to next_permutation.

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0077_combinations_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0077_combinations_2_AC.cpp)

<hr>

#78 Subsets 

// #78 子集

描述：幂集。

// [#78](https://leetcode.com/problems/subsets/) Description: Subsets | LeetCode OJ

解法1：DFS。

// Solution 1: DFS.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0078_subsets_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0078_subsets_1_AC.cpp)

解法2：幂集中的元素和0~2 ^ n - 1可构成双射。

// Solution 2: There exists a bijection between the power set and {0, 1, ..., 2 ^ n - 1}, where n is the cardinality of the set S.

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0078_subsets_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0078_subsets_2_AC.cpp)

<hr>

#79 Word Search 

// #79 找单词

描述：给定一个字母矩阵，允许从任一点出发四处走。看轨迹能否构成一个单词。

// [#79](https://leetcode.com/problems/word-search/) Description: Word Search | LeetCode OJ

解法1：DFS。

// Solution 1: DFS.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0079_word-search_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0079_word-search_1_AC.cpp)

<hr>

#80 Remove Duplicates from Sorted Array II

// #80 有序数组去重2

描述：和之前一样，不过这次允许元素重复一次。

// [#80](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) Description: Remove Duplicates from Sorted Array II | LeetCode OJ

解法1：小把戏。

// Solution 1: Small trick.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0080_remove-duplicates-from-sorted-array-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0080_remove-duplicates-from-sorted-array-ii_1_AC.cpp)

<hr>

#81 Search in Rotated Sorted Array II

// #81 有序旋转数组查找2

描述：和之前一样，不过这次数组里可能有重复元素。

// [#81](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/) Description: Search in Rotated Sorted Array II | LeetCode OJ

解法1：对于相等元素，必须跳过，否则无从得知，这有序的部分究竟在重复元素的左侧还是右侧。所以时间复杂度最坏可以达到O(N)。

// Solution 1: The duplicates must be skipped one by one, or else there's no way to know which way to go during the binary search. Thus the worst-case time complexity can be O(N).

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0081_search-in-rotated-sorted-array-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0081_search-in-rotated-sorted-array-ii_1_AC.cpp)

<hr>

#82 Remove Duplicates from Sorted List II

// #82 有序链表去重2

描述：给定有序链表，凡有重复元素者，尽数去除。

// [#82](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) Description: Remove Duplicates from Sorted List II | LeetCode OJ

解法1：去呗。

// Solution 1: Do it.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0082_remove-duplicates-from-sorted-list-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0082_remove-duplicates-from-sorted-list-ii_1_AC.cpp)

<hr>

#83 Remove Duplicates from Sorted List

// #83 有序链表去重

描述：和之前一样，这次只去掉重复部分。

// [#83](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) Description: Remove Duplicates from Sorted List | LeetCode OJ

解法1：去呗。

// Solution 1: Do it.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0083_remove-duplicates-from-sorted-list_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0083_remove-duplicates-from-sorted-list_1_AC.cpp)

<hr>

#84 Largest Rectangle in Histogram

// #84 直方图中的最大矩形

描述：给定一个直方图，求其能覆盖的最大矩形。

// [#84](https://leetcode.com/problems/largest-rectangle-in-histogram/) Description: Largest Rectangle in Histogram | LeetCode OJ

解法1：和Trapping Rain Water那题一样，从每一条的角度来考虑问题。看向左向右各能延伸多长，用DP可以O(N)时间解决。

// Solution 1: Same as Trapping Rain Water, consider the problem from each single stripe. Calculate the left and right boundary for the stripes using DP in O(N) time, then we have the answer.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0084_largest-rectangle-in-histogram_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0084_largest-rectangle-in-histogram_1_AC.cpp)

<hr>

#85 Maximal Rectangle

// #85 最大矩形

描述：给定一个01矩阵，找出其中全由1构成的最大矩形。

// [#85](https://leetcode.com/problems/maximal-rectangle/) Description: Maximal Rectangle | LeetCode OJ

解法1：这题有意思，可以利用Largest Rectangle in Histogram那题的思路来做，请看代码。把一个问题化归为另一个问题，是复用代码的常见手段。

// Solution 1: An interesting problem. We can use Largest Rectangle in Histogram to solve this one. Please read the code. It's common practice to convert one problem to another, so that we can reuse existing code.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0085_maximal-rectangle_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0085_maximal-rectangle_1_AC.cpp)

<hr>

#86 Partition List

// #86 划分链表

描述：给定一个链表和一个值，把小于等于和大于该值的部分分别放到链表的一前一后去。

// [#86](https://leetcode.com/problems/partition-list/) Description:

解法1：分为两个链表，然后合并即可。

// Solution 1: Split in two and concatenate as one.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0086_partition-list_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0086_partition-list_1_AC.cpp)

<hr>

#87 Scramble String

// #87 乱序字符串

描述：给定一个字符串S，允许递归地将其分为左右两部分并调换位置，称其为“乱序”。现给定两字符串，判断其是否互为“乱序”。

// [#87](https://leetcode.com/problems/scramble-string/) Description: Scramble String | LeetCode OJ

解法1：DP。不知道有没有O(N^3)时间的解法？

// Solution 1: DP. I wonder if there's an O(N ^ 3) solution?

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0087_scramble-string_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0087_scramble-string_1_AC.cpp)

<hr>

#88 Merge Sorted Array

// #88 归并有序数组

描述：给定有序数组a1和a2，把a2归并到a1中。

// [#88](https://leetcode.com/problems/merge-sorted-array/) Description: Merge Sorted Array | LeetCode OJ

解法1：并呗。

// Solution 1: Do it.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0088_merge-sorted-array_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0088_merge-sorted-array_1_AC.cpp)

<hr>

#89 Gray Code

// #89 格雷码

描述：生成N位格雷码。

// [#89](https://leetcode.com/problems/gray-code/) Description: Gray Code | LeetCode OJ

解法1：想想N - 1位格雷码和N位格雷码的关系。

// Solution 1: Think about the relationship between (N - 1)-bit gray code and N-bit gray code.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0089_gray-code_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0089_gray-code_1_AC.cpp)

<hr>

#90 Subsets II

// #90 子集2

描述：还是幂集，不过这次是多重集的幂集。

// [#90](https://leetcode.com/problems/subsets-ii/) Description: Subsets II | LeetCode OJ

解法1：因为是多重集，所以这次咱还是搜吧。其实双射还是存在的，不过代码没那么好写了，所以我懒得写。

// Solution 1: I'd prefer DFS this time. Although the bijection still exists, the code isn't as easy to write. Never mind.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0090_subsets-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0090_subsets-ii_1_AC.cpp)

<hr>

#91 Decode Ways

// #91 解码方式

描述：将A~Z和1~26一一映射，现在给定一个数字串，请计算有多少种不同的解码方式。

// [#91](https://leetcode.com/problems/decode-ways/) Description: Decode Ways | LeetCode OJ

解法1：这个可以DP。

// Solution 1: DP will do.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0091_decode-ways_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0091_decode-ways_1_AC.cpp)

<hr>

#92 Reverse Linked List II

// #92 反转链表2

描述：给定一个链表，反转第m~n个节点。

// [#92](https://leetcode.com/problems/reverse-linked-list-ii/) Description: Reverse Linked List II | LeetCode OJ

解法1：分前中后三部分完成。

// Solution 1: Split in three.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0092_reverse-linked-list-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0092_reverse-linked-list-ii_1_AC.cpp)

<hr>

#93 Restore IP Addresses

// #93 还原IP地址

描述：给定一个没加点的IP地址，返回所有可能的合法IP地址。

// [#93](https://leetcode.com/problems/restore-ip-addresses/) Description: Restore IP Addresses | LeetCode OJ

解法1：加呗。

// Solution 1: Do it.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0093_restore-ip-addresses_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0093_restore-ip-addresses_1_AC.cpp)

<hr>

#94 Binary Tree Inorder Traversal

// #94 二叉树中序遍历

描述：如题。

// [#94](https://leetcode.com/problems/binary-tree-inorder-traversal/) Description: Binary Tree Inorder Traversal | LeetCode OJ

解法1：递归。

// Solution 1: Recursive.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0094_binary-tree-inorder-traversal_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0094_binary-tree-inorder-traversal_1_AC.cpp)

解法2：迭代。

// Solution 2: Iterative.

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0094_binary-tree-inorder-traversal_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0094_binary-tree-inorder-traversal_2_AC.cpp)

<hr>

#95 Unique Binary Search Trees II 

// #95 不同二叉搜索树2

描述：输出中序遍历是{1, 2, ..., n}的所有二叉搜索树。

// [#95](https://leetcode.com/problems/unique-binary-search-trees-ii/) Description: Unique Binary Search Trees II | LeetCode OJ

解法1：DFS。

// Solution 1: DFS.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0095_unique-binary-search-trees-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0095_unique-binary-search-trees-ii_1_AC.cpp)

<hr>

#96 Unique Binary Search Trees

// #96 不同二叉搜索树

描述：输出中序遍历是{1, 2, ..., n}的所有二叉搜索树个数。

// [#96](https://leetcode.com/problems/unique-binary-search-trees/) Description: Unique Binary Search Trees | LeetCode OJ

解法1：Catalan数。为什么呢？自己想。

// Solution 1: Catalan Number.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0096_unique-binary-search-trees_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0096_unique-binary-search-trees_1_AC.cpp)

<hr>

#97 Interleaving String

// #97 交叉字符串 

描述：给定仨字符串S1、S2、S3，判断S3是否可以由S1和S2交叉而成。

// [#97](https://leetcode.com/problems/interleaving-string/) Description: Interleaving String | LeetCode OJ

解法1：DP。

// Solution 1: DP.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0097_interleaving-string_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0097_interleaving-string_1_AC.cpp)

<hr>

#98 Validate Binary Search Tree

// #98 验证二叉搜索树

描述：给定二叉树，判断是否为二叉搜索树。

// [#98](https://leetcode.com/problems/validate-binary-search-tree/) Description: Validate Binary Search Tree | LeetCode OJ

解法1：针对“有序”二字做文章即可。

// Solution 1: Dig around the word “order”.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0098_validate-binary-search-tree_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0098_validate-binary-search-tree_1_AC.cpp)

<hr>

#99 Recover Binary Search Tree

// #99 恢复二叉搜索树

描述：二叉搜索树中的两个节点被调换了，麻烦给调回来。

// [#99](https://leetcode.com/problems/recover-binary-search-tree/) Description: Recover Binary Search Tree | LeetCode OJ

解法1：执行中序遍历，找出两个节点。注意边界情况。

// Solution 1: Perform an inorder traversal to locate target nodes. Watch for edge cases.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0099_recover-binary-search-tree_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0099_recover-binary-search-tree_1_AC.cpp)

解法2：应出题者装逼要求，强行写了个Morris中序遍历。难道现在面试都要求会写Morris遍历了？真乃世道艰危，国将不国啊。你敢再让写一遍这破玩意儿，我猪某宁死也要投降。

// Solution 2: Is this showing off or zhuangbi?

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0099_recover-binary-search-tree_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0099_recover-binary-search-tree_2_AC.cpp)

<hr>

#100 Same Tree

// #100 同一棵树

描述：同一个梦想。

// [#100](https://leetcode.com/problems/same-tree/) Description: Same Tree | LeetCode OJ

解法1：递归或者迭代，甚至序列化都行，烯烃尊便。

// Solution 1:

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0100_same-tree_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0100_same-tree_1_AC.cpp)

