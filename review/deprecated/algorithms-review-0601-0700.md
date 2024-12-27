#605 Can Place Flowers

// #605 能放花吗

描述：给定一个01数组，问能否将其中N个0变成1，使得数组中不存在相邻的1。

// [#605](https://leetcode.com/problems/can-place-flowers/) Description: Can Place Flowers

解法1：水题。

// Solution 1: Easy.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0605_can-place-flowers_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0605_can-place-flowers_1_AC.cpp)

<hr>

#606 Construct String from Binary Tree

// #606 二叉树序列化

描述：给定一棵二叉树，按照规则将其序列化，要求在无二义性的情况下，省去尾部多余的空括号。

// [#606](https://leetcode.com/problems/construct-string-from-binary-tree/) Description: Construct String from Binary Tree

解法1：水题。

// Solution 1: Trivial.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0606_construct-string-from-binary-tree_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0606_construct-string-from-binary-tree_1_AC.cpp)

<hr>

#609 Find Duplicate File in System

// #609 文件系统查重

描述：给定文件列表，和每个文件的内容，找出内容重复的文件。

// [#609](https://leetcode.com/problems/find-duplicate-file-in-system/) Description: Find Duplicate File in System

解法1：这题不是算法题，而是系统设计题。题目本身没什么挑战性，值得仔细思考的是follow-up部分的要求。系统设计的关键，通常是代码复用、接口扩展以及计算并行化。

// Solution 1: This is not an algorithmic, but a system design problem. The problem itself is no challenge, but the follow-up section down below. The key criteria of system design problems are usually code reusability, interface scalability and computation parallelizability.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0609_find-duplicate-file-in-system_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0609_find-duplicate-file-in-system_1_AC.cpp)

<hr>

#611 Valid Triangle Number

// #611 有效三角数

描述：给定一个非负数组，从中选取3个数（不同顺序算一样）作为三角形的三边。问有多少个这样的三元组？

// [#611](https://leetcode.com/problems/valid-triangle-number/) Description: Valid Triangle Number

解法1：a + b > c

// Solution 1: a + b > c

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0611_valid-triangle-number_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0611_valid-triangle-number_1_AC.cpp)

<hr>

#617 Merge Two Binary Trees

// #617 合并二叉树

描述：给定两个二叉树，按照对应位置值相加，空节点作0处理的方法，合并两个二叉树。

// [#617](https://leetcode.com/problems/merge-two-binary-trees/) Description: Merge Two Binary Trees

解法1：遍历即可，不过每个节点都应该额外分配，不能用旧节点。

// Solution 1: Just traverse them, only in that every merged node should be newly allocated, instead of tearing old ones from the two.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0617_merge-two-binary-trees_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0617_merge-two-binary-trees_1_AC.cpp)

<hr>

#621 Task Scheduler

// #621 任务调度

描述：有一些任务若干个，用A-Z表示，相同任务可能有多个。每个单位时间运行一个任务，要求两个相同任务之间间隔不小于N，问运行完全部任务的最小时间。

// [#621](https://leetcode.com/problems/task-scheduler/) Description: Task Scheduler

解法1：数据规模不大，直接模拟。

// Solution 1: Run a simulation, considering the data scala is reasonable.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0621_task-scheduler_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0621_task-scheduler_1_AC.cpp)

<hr>

#623 Add One Row to Tree

// #623 给二叉树加一行

描述：给定一个二叉树，要求在深度为d的地方加一层节点，值统一设为v。

// [#623](https://leetcode.com/problems/add-one-row-to-tree/) Description: Add One Row to Tree

解法1：随便怎么遍历，记录深度即可。

// Solution 1: Traverse it all you want, just keep track of the depth.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0623_add-one-row-to-tree_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0623_add-one-row-to-tree_1_AC.cpp)

<hr>

#624 Maximum Distance in Arrays

// #624 最大数组距离

描述：给定m个有序数组，允许你从两数组中各选一数，问最大差值是多少？

// [#624](https://leetcode.com/problems/maximum-distance-in-arrays/) Description: Maximum Distance in Arrays

解法1：其实问题不难，不过为了达到O(N)复杂度，并且使代码简洁些，在写法上有点技巧。首先我么只关心每个数组中的最大值和最小值。其次，要在O(N)时间内求出对于每个数组而言，除它以外其他数组中的最大值和最小值。（看懂了吗？）至于代码写法，我为了避免复制粘贴代码，选择将比较符作为一个函子，这点如果有函数式编程的思维，是很容易想到的。高阶函数的使用可以优化代码结构，宜善用之。

// Solution 1: The problem itself is easy, except no really if you wish to attain O(N) time. The writing is a bit tricky if you wish to make it clean. First, we care only the max and min for each array. Then, we calculate the max and min for each array except itself. (Capisch?) As for the matter of writing, I chose a functor to do the comparison, so as to reuse one piece of code to do two similar jobs. With some sense in functional programming, higher-order functions can be useful for better code organization, use it wisely.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0624_maximum-distance-in-arrays_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0624_maximum-distance-in-arrays_1_AC.cpp)

<hr>

#625 Minimum Factorization

// #625 最小因数分解

描述：给定正整数a，找出最小的的int32_t整数b，使得b的十进制位数相乘正好等于a。如果不存在就返回0。

// [#625](https://leetcode.com/problems/minimum-factorization/) Description: Minimum Factorization

解法1：思路其实挺简单，按照2、3、5、7进行因式分解，然后按9~2的顺序从大到小地从a中除去，直到不能分解为止。如果不能除到1，则无解。求得的字符串排成升序就是最小结果了。代码实现比较难看，不优雅。

// Solution 1: The idea is simple. Factorize by 2, 3, 5, 7 and divide by 9~2 all the way down from a. If it doesn't end up as 1, no solution. Otherwise, sort the resulting string in ascending order to get the final result. The implementation is a bit ugly though, uncool.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0625_minimum-factorization_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0625_minimum-factorization_1_AC.cpp)

<hr>

#628 Maximum Product of Three Numbers

// #628 三数最大乘积

描述：给定一个整数数组，求任取三元素所得乘积的最大值。

// [#628](https://leetcode.com/problems/maximum-product-of-three-numbers/) Description: Maximum Product of Three Numbers

解法1：只要不是0，乘积的绝对值就会越变越大。但是负号使得乘积在最大和最小之间交替，所以要同时记录最大值和最小值。

// Solution 1: As long as no zero is encountered, the absolute value of the product will keep growing. The presence of minus sign, however, will make the product switching between max and min. Thus we need to keep track of both.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0628_maximum-product-of-three-numbers_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0628_maximum-product-of-three-numbers_1_AC.cpp)

<hr>

#629 K Inverse Pairs Array

// #629 K逆序对数组

描述：给定1~N的排列，问逆序数为K的排列共有多少种？

// [#629](https://leetcode.com/problems/k-inverse-pairs-array/) Description: K Inverse Pairs Array

解法1：dp[i][j]表示1~(i+1)排列中逆序数为j的种类数，动规搞起。

// Solution 1: Let dp[i][j] be the number of permutations with inverse number j, you know what to do.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0629_k-inverse-pairs-array_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0629_k-inverse-pairs-array_1_AC.cpp)

<hr>

#630 Course Schedule III

// #630 课表3

描述：有N门课，每门都有固定的时长和最晚完成时间。允许你自由选择开始上课的时间以及上课顺序，时间不能重叠。问最多能完成多少门课？

// [#630](https://leetcode.com/problems/course-schedule-iii/) Description: Course Schedule III

解法1：这是个贪婪的问题，请思考代码中的now的意义。

// Solution 1: This is a greedy one, please think about the meaning of "now" in the code.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0630_course-schedule-iii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0630_course-schedule-iii_1_AC.cpp)

<hr>

#632 Smallest Range Covering Elements from K Lists

// #632 覆盖K个列表元素的最小范围

描述：给定k个有序数组，求一个最小的区间，使得该区间包含了每个数组中至少一个元素。

// [#632](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/) Description: Smallest Range

解法1：Minimum Window Substring这题里的解法可以用到本题，只要稍动脑筋就知道如何转化了。

// Solution 1: Minimum Window Substring The solution of that problem can be applied here, with just a little trick to convert the problem, we're good.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0632_smallest-range-covering-elements-from-k-lists_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0632_smallest-range-covering-elements-from-k-lists_1_AC.cpp)

<hr>

#633 Sum of Square Numbers

// #633 平方数之和

描述：给定非负整数c，问是否存在整数a、b，使得a^2+b^2=c？

// [#633](https://leetcode.com/problems/sum-of-square-numbers/) Description: Sum of Square Numbers

解法1：水题。

// Solution 1: Trivial.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0633_sum-of-square-numbers_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0633_sum-of-square-numbers_1_AC.cpp)

<hr>

#635 Design Log Storage System

// #635 设计日志文件系统

描述：比较无聊，懒得说。

// [#635](https://leetcode.com/problems/design-log-storage-system/) Description: Design Log Storage System

解法1：总体思路还是哈希。

// Solution 1: Hashing works just fine.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0635_design-log-storage-system_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0635_design-log-storage-system_1_AC.cpp)

<hr>

#636 Exclusive Time of Functions

// #636 函数独占时间

描述：给定函数调用站以及对应时间，求各个函数所占用的CPU时间。

// [#636](https://leetcode.com/problems/exclusive-time-of-functions/) Description: Exclusive Time of Functions

解法1：栈。

// Solution 1: Stack.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0636_exclusive-time-of-functions_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0636_exclusive-time-of-functions_1_AC.cpp)

<hr>

#637 Average of Levels in Binary Tree

// #637 二叉树各层均值

描述：如题。

// [#637](https://leetcode.com/problems/average-of-levels-in-binary-tree/) Description: Average of Levels in Binary Tree

解法1：水。

// Solution 1: Boring.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0637_average-of-levels-in-binary-tree_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0637_average-of-levels-in-binary-tree_1_AC.cpp)

<hr>

#638 Shopping Offers

// #638 购物促销

描述：商场有一些物品，各有价格。你有份购物清单，各有数目。现在给你一些能够省钱的组合搭配。问你利用这些组合，最少花多少钱能完成购物任务？

// [#638](https://leetcode.com/problems/shopping-offers/) Description: Shopping Offers

解法1：多维背包。问题不难，但是理论上计算复杂度非常高。正因为如此，数据量小的一笔。数据量这么小，就给了我们利用编码来压缩空间的可能。通过把多维坐标展开成一维，数据结构的设计就简单多了。请看代码。

// Solution 1: It's multi-dimensional knapsack problem. Not difficult, but extremely computationally intensive in theory. That's exactly why the data scala is limited so tight. With such small data scale, we might utilitize some encoding scheme to compress space usage. Through flattening the n-dim coordinates to 1-dim, the data structure is reduced to simple arrays, making things a lot easier. Please read the code for more details.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0638_shopping-offers_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0638_shopping-offers_1_AC.cpp)

<hr>

#639 Decode Ways II

// #639 解码方式2

描述：按照A~Z对应1~26的规则，把一串字母进行编码。现在给你一个编码后的字符串，但其中可能含有通配符“*”，表示0~9的任意一个。问总共有多少种不同解码方式？结果膜1e9+7。

// [#639](https://leetcode.com/problems/decode-ways-ii/) Description: Decode Ways II

解法1：思路依然是DP，分析线性递推关系。不过这题我的代码写得乱七八糟，思路也不甚清晰。很不清真。

// Solution 1: Still a DP problem, solved by linear recurrence relation. Yet my version of code is totally f**ked up. So lame.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0639_decode-ways-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0639_decode-ways-ii_1_AC.cpp)

<hr>

#640 Solve the Equation

// #640 解方程

描述：给定一元一次只含加减法的方程，求解。

// [#640](https://leetcode.com/problems/solve-the-equation/) Description: Solve the Equation

解法1：水题。

// Solution 1: Easy.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0640_solve-the-equation_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0640_solve-the-equation_1_AC.cpp)

<hr>

#643 Maximum Average Subarray I

// #643 最大子数组均值1

描述：给定长度为N的数组，求长度为K的子数组的最大均值。

// [#643](https://leetcode.com/problems/maximum-average-subarray-i/) Description: Maximum Average Subarray I

解法1：水题。

// Solution 1: Trivial.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0643_maximum-average-subarray-i_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0643_maximum-average-subarray-i_1_AC.cpp)

<hr>

#644 Maximum Average Subarray II

// #644 最大子数组均值2

描述：给定长度为N的数组，求长度不小于K的子数组的最大均值。

// [#644](https://leetcode.com/problems/maximum-average-subarray-ii/) Description: Maximum Average Subarray II

解法1：这题不简单，我愣想了半小时也没个好思路，最后参考了讨论区。两点提示，0*n=0，前缀和。

// Solution 1: Quite a problem, took me half an hour for nothing, ended up seeking for help from discussion board. Two hints, 0*n=0, prefix sum.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0644_maximum-average-subarray-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0644_maximum-average-subarray-ii_1_AC.cpp)

<hr>

#645 Set Mismatch

// #645 集合不匹配

描述：给定1~N，其中某个数x变成了另一个数y，且x和y都在1~N之间，求出x和y。

// [#645](https://leetcode.com/problems/set-mismatch/) Description: 

解法1：数据范围1~N，数组长度为N。不用哈希对得起观众？

// Solution 1: Exact data range, exact data scale. Whatcha waitin' fer? Hash it. 

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0645_set-mismatch_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0645_set-mismatch_1_AC.cpp)

<hr>

#646 Maximum Length of Pair Chain

// #646 最大数对链长度

描述：对于数对(a,b)和(c,d)，已知a<b，c<d，如果b<c，则称两数对成链。给定一些数对，问能够组成的链的最大长度。

// [#646](https://leetcode.com/problems/maximum-length-of-pair-chain/) Description: Maximum Length of Pair Chain

解法1：贪婪，不过得动点脑筋。

// Solution 1: Greedy, but takes a little reckoning.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0646_maximum-length-of-pair-chain_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0646_maximum-length-of-pair-chain_1_AC.cpp)

<hr>

#647 Palindromic Substrings

// #647 回文子串

描述：给定一个字符串，求所有回文子串的个数。

// [#647](https://leetcode.com/problems/palindromic-substrings/) Description: Palindromic Substrings

解法1：根据Manacher算法可以求出每个位置的回文半径，于是可以在O(N)时间内求出所有回文子串的个数。不过，实在太麻烦了，于是暴力水过。

// Solution 1: With Manacher's algorithm we can deduce the palindromic radius of each position, thus getting the result in O(N) time. Considering the complication, I'd rather not tangle.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0647_palindromic-substrings_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0647_palindromic-substrings_1_AC.cpp)

<hr>

#648 Replace Words

// #648 替换单词

描述：给定一个含有一堆词根的词典，和一句话。要求在存在词根的情况下，把句中单词都替换为对应词根，要求越短越好。

// [#648](https://leetcode.com/problems/replace-words/) Description: Replace Words

解法1：对前缀取哈希，沿路查找是否有匹配即可。原理上和字典树类似，但是实现简单多了。

// Solution 1: Hash every prefixes andn search for a match along the path. It's similar to a trie, but much more efficient and simpler.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0648_replace-words_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0648_replace-words_1_AC.cpp)

<hr>

#649 Dota2 Senate

// #649 Dota2议会

描述：给定正反两派顺序排成一条队。从第一个开始，每个人有机会消灭任何一个敌人，如果自己已被消灭，则跳过。问谁赢？

// [#649](https://leetcode.com/problems/dota2-senate/) Description: Dota2 Senate

解法1：本以为是博弈论问题，结果贪婪就够了。

// Solution 1: I thought it was game theory, turned out greedy was good enough.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0649_dota2-senate_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0649_dota2-senate_1_AC.cpp)

<hr>

#650 2 Keys Keyboard

// #650 两键键盘

描述：给定一个字母A，每次操作允许你复制全部文本，或者把复制好的文本粘贴一份。问得到N个A至少需要多少次操作。

// [#650](https://leetcode.com/problems/2-keys-keyboard/) Description: 2 Keys Keyboard

解法1：DP。

// Solution 1: DP.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0650_2-keys-keyboard_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0650_2-keys-keyboard_1_AC.cpp)

<hr>

#652 Find Duplicate Subtrees

// #652 二叉树查重

描述：给定一个二叉树，找出所有存在重复的子树。重复的定义是从根节点往下完全一样。

// [#652](https://leetcode.com/problems/find-duplicate-subtrees/) Description: Find Duplicate Subtrees

解法1：序列化，哈希。

// Solution 1: Serialization and hashing.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0652_find-duplicate-subtrees_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0652_find-duplicate-subtrees_1_AC.cpp)

<hr>

#653 Two Sum IV - Input is a BST

// #653 两数之和——输入是二叉搜索树

描述：如题，求是否存在两数加起来等于某和。

// [#653](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/) Description: Two Sum IV - Input is a BST

解法1：看到不少手动递归、用迭代器遍历的解法。我觉得这种题（在Leetcode上并不少见）无聊的地方就在于，明明不能提供更优的时空复杂度，却硬要人想出一些奇奇怪怪的解法（茴），写代码搞得跟杂耍似的，花式装逼很吊？骨骼这么清奇你得练如来神掌，还写啥代码。我能想到的最简单粗暴的办法，中序遍历+哈希。

// Solution 1: I don't know what's the point about those fancy solutions when they offer neither a better time or space complexity, nor a clean and easy solution. We're programmer, not jugglers. So what? Am I supposed to be impressed? For me, it's plain and simple, an inorder traversal with hashing.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0653_two-sum-iv-input-is-a-bst_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0653_two-sum-iv-input-is-a-bst_1_AC.cpp)

<hr>

#654 Maximum Binary Tree

// #654 最大二叉树

描述：给定一个不含重复元素的数组，每次取最大元素作为二叉树的根节点，然后按照左右子数组、左右子树递归划分，构造出整个二叉树。

// [#654](https://leetcode.com/problems/maximum-binary-tree/) Description: Maximum Binary Tree

解法1：直接线性查找最大，然后递归划分。

// Solution 1: Linear search and recursive partition.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0654_maximum-binary-tree_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0654_maximum-binary-tree_1_AC.cpp)

解法2：“查找最大”这部分是可以优化的，请搜索“RMQ问题”。

// Solution 2: "Searching for max" is eligible for optimization. Google "RMQ problem" for more info.

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0654_maximum-binary-tree_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0654_maximum-binary-tree_2_AC.cpp)

<hr>

#655 Print Binary Tree

// #655 打印二叉树

描述：比较无聊，懒得说。

// [#655](https://leetcode.com/problems/print-binary-tree/) Description: Print Binary Tree

解法1：水题。

// Solution 1: Chores.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0655_print-binary-tree_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0501-1000/0655_print-binary-tree_1_AC.cpp)
