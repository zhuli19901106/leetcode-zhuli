#301 Remove Invalid Parentheses

// #301 去除无效括号

描述：给定一个可能包含其他字符的括号序列，通过删除最少的字符，使括号成功匹配。要求返回所有可行的解法。

// [#301](https://leetcode.com/problems/remove-invalid-parentheses/) Description: Remove Invalid Parentheses | LeetCode OJ

解法1：难题。试想，如果多出了)，我们如何处理？没错，删掉。那么多出了(，怎么办呢？能删吗？不能，因为后面可能用得着。这就是一大难点。要求返回所有结果，这是另一大难点。为了处理这两点，我的代码写得非常繁琐，而且始终没通过。最终找了网上的解法，发现其中有一个绝妙的解法：对于多余的(，我们把问题反过来看。看看代码，你就知道怎么“反”了。

// Solution 1: A hard problem indeed. If there're redundant (s, what you gonna do? Remove it. If it's )s, what then? We can't remove them, because they might be needed later. This is the first challenge. The problem requests we find all possible solutions, that's the second challenge. It took me lots of time and efforts to put up a long and sloppy solution, which never got accepted. Here the solution is from the Internet. A major difference from mine is the way it deals with redundant (s: switch the role of () to )(. Read the code and you'll see how and why.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0301_remove-invalid-parentheses_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0301_remove-invalid-parentheses_1_AC.cpp)

<hr>

#302 Smallest Rectangle Enclosing Black Pixels

// #302 包围黑点的最小矩形

描述：给定一个01矩阵，1表示黑点。求能盖住所有黑点的最小矩形面积。

// [#302](https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/) Description: Smallest Rectangle Enclosing Black Pixels | LeetCode OJ

解法1：无聊。

// Solution 1: Boring.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0302_smallest-rectangle-enclosing-black-pixels_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0302_smallest-rectangle-enclosing-black-pixels_1_AC.cpp)

解法2：真无聊。

// Solution 2: Really boring.

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0302_smallest-rectangle-enclosing-black-pixels_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0302_smallest-rectangle-enclosing-black-pixels_2_AC.cpp)

<hr>

#303 Range Sum Query - Immutable

// #303 区间求和 - 不变

描述：给定一个元素不变的数组，处理多次区间求和。

// [#303](https://leetcode.com/problems/range-sum-query-immutable/) Description: Range Sum Query - Immutable | LeetCode OJ

解法1：前缀和。

// Solution 1: Prefix sum.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0303_range-sum-query-immutable_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0303_range-sum-query-immutable_1_AC.cpp)

<hr>

#304 Range Sum Query 2D - Immutable

// #304 二维区间求和 - 不变

描述：给定元素不变的矩阵，求各种子矩阵和。

// [#304](https://leetcode.com/problems/range-sum-query-2d-immutable/) Description: Range Sum Query 2D - Immutable | LeetCode OJ

解法1：还是前缀和。

// Solution 1: Still prefix sum.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0304_range-sum-query-2d-immutable_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0304_range-sum-query-2d-immutable_1_AC.cpp)

<hr>

#305 Number of Islands II

// #305 岛屿个数2

描述：给定一个01矩阵，开始全都是0。允许两种操作：1. 查询“1”连通分量的个数，2. 把某位置变成1。

// [#305](https://leetcode.com/problems/number-of-islands-ii/) Description: Number of Islands II | LeetCode OJ

解法1：并查集。

// Solution 1: Union-find set.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0305_number-of-islands-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0305_number-of-islands-ii_1_AC.cpp)

<hr>

#306 Additive Number

// #306 加性数

描述：斐波那契数列知道吧？现在给定这么一个数列，开头俩数可以不是1，把这个数列连成一个数，我们称其为“加性数”。现在给定一个数，判断是不是加性数。

// [#306](https://leetcode.com/problems/additive-number/) Description: Additive Number | LeetCode OJ

解法1：一看就得搜，不过要注意剪枝，否则妥妥的药丸。

// Solution 1: It looks like DFS, but make sure you got some pruning in stock. Otherwise, you're going down.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0306_additive-number_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0306_additive-number_1_AC.cpp)

<hr>

#307 Range Sum Query - Mutable

// #307 区间求和 - 可变

描述：给定允许改变元素的数组，处理各种区间求和。

// [#307](https://leetcode.com/problems/range-sum-query-mutable/) Description: Range Sum Query - Mutable | LeetCode OJ

解法1：树状数组。

// Solution 1: BIT.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0307_range-sum-query-mutable_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0307_range-sum-query-mutable_1_AC.cpp)

<hr>

#308 Range Sum Query 2D - Mutable

// #308 二维区间求和 - 可变

描述：给定元素可变的矩阵，处理子矩阵求和。

// [#308](https://leetcode.com/problems/range-sum-query-2d-mutable/) Description: Range Sum Query 2D - Mutable | LeetCode OJ

解法1：二维树状数组。

// Solution 1: 2D BIT.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0308_range-sum-query-2d-mutable_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0308_range-sum-query-2d-mutable_1_AC.cpp)

<hr>

#309 Best Time to Buy and Sell Stock with Cooldown

// #309 最佳炒股时机带CD

描述：给定股价，每次买卖股票有1天的冷却期，求最大收益。

// [#309](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) Description: Best Time to Buy and Sell Stock with Cooldown | LeetCode OJ

解法1：用一个有限状态机来考虑，昨天今天、有股没股。这两者的组合和状态转换搞清楚了，题目就做出来了。

// Solution 1: Use a finite state machine to deal with the problem. Today or yesterday, got stocks in hand or not, the state transitions among these are the key to the solution.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0309_best-time-to-buy-and-sell-stock-with-cooldown_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0309_best-time-to-buy-and-sell-stock-with-cooldown_1_AC.cpp)

<hr>

#310 Minimum Height Trees

// #310 最小高度树

描述：给定一个树形的无向图，允许你选一个节点作为根。请找出使得树最矮的根节点。

// [#310](https://leetcode.com/problems/minimum-height-trees/) Description: Minimum Height Trees | LeetCode OJ

解法1：关键在于找出图中最长的一条路径。做法就是两次遍历。这条最长的路径也叫作图的直径。

// Solution 1: The key is to find the longest path in the graph. Two traversals will suffice. This path is called the diameter of the graph.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0310_minimum-height-trees_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0310_minimum-height-trees_1_AC.cpp)

<hr>

#311 Sparse Matrix Multiplication

// #311 稀疏矩阵相乘

描述：给定两个很稀疏的矩阵，做乘法。

// [#311](https://leetcode.com/problems/sparse-matrix-multiplication/) Description: Sparse Matrix Multiplication | LeetCode OJ

解法1：很稀疏，有多稀疏？你输入是完整矩阵，输出也是，有谋搞错？

// Solution 1: Sparse matrix? I don't see no sparse matrix.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0311_sparse-matrix-multiplication_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0311_sparse-matrix-multiplication_1_AC.cpp)

<hr>

#312 Burst Balloons

// #312 爆气球

描述：给定n个气球排成一排，每个上面标了个数a[i]。如果爆掉某个气球，就获得左右俩球和该球的乘积作为奖分，之后左右俩球就相邻了。求爆掉所有气球获得的最高得分。

// [#312](https://leetcode.com/problems/burst-balloons/) Description: Burst Balloons | LeetCode OJ

解法1：记忆化搜索，动态规划的常见玩法。

// Solution 1: DFS with memorization, a common feat in DP.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0312_burst-balloons_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0312_burst-balloons_1_AC.cpp)

<hr>

#313 Super Ugly Number

// #313 超级丑数

描述：和之前一样，不过这次的质数是由输入钦点，不一定是2、3、5。求第n个。

// [#313](https://leetcode.com/problems/super-ugly-number/) Description: Super Ugly Number | LeetCode OJ

解法1：看代码。

// Solution 1: Read the code.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0313_super-ugly-number_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0313_super-ugly-number_1_AC.cpp)

<hr>

#314 Binary Tree Vertical Order Traversal

// #314 二叉树垂直遍历

描述：按照从左往右，从上往下的顺序，遍历二叉树。

// [#314](https://leetcode.com/problems/binary-tree-vertical-order-traversal/) Description: Binary Tree Vertical Order Traversal | LeetCode OJ

解法1：我倒看看你还有多少种遍历方式。

// Solution 1: Show me what you got on binary tree traversals.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0314_binary-tree-vertical-order-traversal_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0314_binary-tree-vertical-order-traversal_1_AC.cpp)

<hr>

#315 Count of Smaller Numbers After Self

// #315 后面小于自身的元素个数

描述：给定一个数组，对于每个元素，求在其后比其小的元素个数。

// [#315](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) Description: Count of Smaller Numbers After Self | LeetCode OJ

解法1：凡是这种限定数据范围、下标范围，统计个数的问题，都可以用树状数组来做。必要时可以用哈希表对离散化的数据进行连续化映射。

// Solution 1: Problems as such, that put restrictions on data range and index range and focus on counting, can be solved with BIT. Use a hash table to map a discretized sequence to a consecutive one.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0315_count-of-smaller-numbers-after-self_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0315_count-of-smaller-numbers-after-self_1_AC.cpp)

<hr>

#316 Remove Duplicate Letters

// #316 去除重复字母

描述：给定一个字符串，去除重复字母，使得所有字母只出现一次，并要求所得结果是字典序最小的。

// [#316](https://leetcode.com/problems/remove-duplicate-letters/) Description: Remove Duplicate Letters | LeetCode OJ

解法1：贪婪。

// Solution 1: Greed is good.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0316_remove-duplicate-letters_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0316_remove-duplicate-letters_1_AC.cpp)

<hr>

#317 Shortest Distance from All Buildings

// #317 最短距离之和

描述：和之前那一样，不过这次建筑物不能穿过了，而且还有一些障碍物也不能穿过。依然求最短距离之和。如果找不到，返回-1。

// [#317](https://leetcode.com/problems/shortest-distance-from-all-buildings/) Description: Shortest Distance from All Buildings | LeetCode OJ

解法1：因为涉及到连通性，简单的求和就不管用了。搜吧。

// Solution 1: Since connectivity problem is involved, simple summation no longer works. Let's search.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0317_shortest-distance-from-all-buildings_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0317_shortest-distance-from-all-buildings_1_AC.cpp)

<hr>

#318 Maximum Product of Word Lengths

// #318 单词长度最大乘积

描述：给定一堆单词，要求找出俩单词长度的最大乘积，要求俩单词不能有相同字母。

// [#318](https://leetcode.com/problems/maximum-product-of-word-lengths/) Description: Maximum Product of Word Lengths | LeetCode OJ

解法1：对于如何判断俩单词有没有相同字母，只要用位向量表示每个字母是否出现即可，俩位向量异或即可得出是否有相同字母。

// Solution 1: Use a bit vector to mark the occurrence of each letter. The XOR of two bit vectors will reveal if two words share a same letter.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0318_maximum-product-of-word-lengths_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0318_maximum-product-of-word-lengths_1_AC.cpp)

<hr>

#319 Bulb Switcher

// #319 开关灯

描述：有N盏灯，开始都关着。从1到N，数到K时，就把所有K的倍数的开关都按一次。如此N轮后，问有多少盏灯亮着。

// [#319](https://leetcode.com/problems/bulb-switcher/) Description: Bulb Switcher | LeetCode OJ

解法1：这是个数学题。

// Solution 1: It's about math.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0319_bulb-switcher_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0319_bulb-switcher_1_AC.cpp)

<hr>

#320 Generalized Abbreviation

// #320 缩写（广义的）

描述：定义一种广义的缩写：允许你把一个单词中的一个或多个部分替换成长度，但各部分不能相邻。给定一个单词，给出所有可能的替换方法。

// [#320](https://leetcode.com/problems/generalized-abbreviation/) Description: Bulb Switcher | LeetCode OJ

解法1：搜。

// Solution 1: DFS.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0320_generalized-abbreviation_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0320_generalized-abbreviation_1_AC.cpp)

<hr>

#321 Create Maximum Number

// #321 构成最大数

描述：给定俩长度为m和n的数组，元素全都是0~9数字。现要求从中选出k个数字，组成最大的数。要求选数的过程保持俩数组中元素的各自先后顺序。

// [#321](https://leetcode.com/problems/create-maximum-number/) Description: Create Maximum Number | LeetCode OJ

解法1：这很像归并排序，对吧？不过没那么简单，因为有些元素是要跳过的。仔细看dropOne()函数的作用，就会发现其作用是每次舍弃一个数字，使得结果尽可能大。我们之后的归并则是通过comp()保证结果尽可能大。两者配合，得到最终结果。

// Solution 1: It's like Merge Sort, right? Ain't that simple, because some digits are to be discarded. Read the function dropOne() carefully and you'll find it drops one digit to make the result as large as possible. The largest merge result is guaranteed by comp(). Use'em both, you'll get the correct result.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0321_create-maximum-number_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0321_create-maximum-number_1_AC.cpp)

<hr>

#322 Coin Change

// #322 找零钱

描述：给你足够多的几种面值的钱，问最少用几张能凑出某个金额。

// [#322](https://leetcode.com/problems/coin-change/) Description: Coin Change | LeetCode OJ

解法1：背包问题。

// Solution 1: Knapsack Problem.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0322_coin-change_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0322_coin-change_1_AC.cpp)

<hr>

#323 Number of Connected Components in an Undirected Graph

// #323 无向图连通分量个数

描述：如题。

// [#323](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) Description: Number of Connected Components in an Undirected Graph | LeetCode OJ

解法1：并查集。

// Solution 1: Union-find set.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0323_number-of-connected-components-in-an-undirected-graph_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0323_number-of-connected-components-in-an-undirected-graph_1_AC.cpp)

<hr>

#324 Wiggle Sort II

// #324 摇摆排序2

描述：和之前一样，但这次要求相邻元素不能相等。

// [#324](https://leetcode.com/problems/wiggle-sort-ii/) Description: Wiggle Sort II | LeetCode OJ

解法1：O(1)的空间复杂度还是算了，有功夫我还多睡会儿，操这闲心干嘛？

// Solution 1: O(1) space? Forget about it.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0324_wiggle-sort-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0324_wiggle-sort-ii_1_AC.cpp)

<hr>

#325 Maximum Size Subarray Sum Equals k

// #325 和为k的最长子数组

描述：给定数组，求和为k的最长子数组的长度。

// [#325](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/) Description: Maximum Size Subarray Sum Equals k | LeetCode OJ

解法1：用哈希表记录前缀和。

// Solution 1: Record prefix sums with a hash table.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0325_maximum-size-subarray-sum-equals-k_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0325_maximum-size-subarray-sum-equals-k_1_AC.cpp)

<hr>

#326 Power of Three

// #326 3的幂

描述：判断一个数是否是3的幂。

// [#326](https://leetcode.com/problems/power-of-three/) Description: Power of Three | LeetCode OJ

解法1：循环。

// Solution 1: Loop.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0326_power-of-three_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0326_power-of-three_1_AC.cpp)

解法2：对数。

// Solution 2: Logarithm.

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0326_power-of-three_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0326_power-of-three_2_AC.cpp)

<hr>

#327 Count of Range Sum

// #327 统计区间和

描述：给定一个数组，求有多少区间和在[low, high]之间。

// [#327](https://leetcode.com/problems/count-of-range-sum/) Description: Count of Range Sum | LeetCode OJ

解法1：参考Count of Smaller Number After Self，用树状数组搞定。想想1和-1是干嘛用的。

// Solution 1: Refer to the solution of Count of Smaller Number After Self. Use a BIT and think about the meaning of 1 and -1.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0327_count-of-range-sum_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0327_count-of-range-sum_1_AC.cpp)

<hr>

#328 Odd Even Linked List

// #328 奇偶链表

描述：给定一个链表，按照单双数位置把链表重排成单在前，双在后。注意，是位置，不是值。

// [#328](https://leetcode.com/problems/odd-even-linked-list/) Description: Odd Even Linked List | LeetCode OJ

解法1：水题。

// Solution 1: Easy.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0328_odd-even-linked-list_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0328_odd-even-linked-list_1_AC.cpp)

<hr>

#329 Longest Increasing Path in a Matrix

// #329 矩阵最长递增路径

描述：给定一个矩阵，允许从某点出发，上下左右走。请找出能走出的单调递增序列的最大长度。

// [#329](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) Description: Longest Increasing Path in a Matrix | LeetCode OJ

解法1：可以搜，也可以DP，道理其实是一样的。

// Solution 1: BFS or DP, different means, same goal.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0329_longest-increasing-path-in-a-matrix_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0329_longest-increasing-path-in-a-matrix_1_AC.cpp)

<hr>

#330 Patching Array

// #330 数组补丁

描述：给定一个数组和一个值target，允许你添加一些数，使得数组中的数能加成target。问最少添加多少个数？

// [#330](https://leetcode.com/problems/patching-array/) Description: Patching Array | LeetCode OJ

解法1：代码非常短，思路却很聪明。贪婪。

// Solution 1: Very short code and bright idea. It's greedy.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0330_patching-array_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0330_patching-array_1_AC.cpp)

<hr>

#331 Verify Preorder Serialization of a Binary Tree

// #331 验证二叉树前序序列化

描述：给定一个前序遍历的序列化字符串，判断其是否能够成一棵有效地二叉树。

// [#331](https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/) Description: Verify Preorder Serialization of a Binary Tree | LeetCode OJ

解法1：水题。

// Solution 1: Easy.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0331_verify-preorder-serialization-of-a-binary-tree_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0331_verify-preorder-serialization-of-a-binary-tree_1_AC.cpp)

<hr>

#332 Reconstruct Itinerary

// #332 重建行程

描述：给你一堆机票，请重建整个行程。如果有多种可能，选字典序最小的那个。

// [#332](https://leetcode.com/problems/reconstruct-itinerary/) Description: Reconstruct Itinerary | LeetCode OJ

解法1：拓扑排序。

// Solution 1: Topological sort.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0332_reconstruct-itinerary_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0332_reconstruct-itinerary_1_AC.cpp)

<hr>

#333 Largest BST Subtree

// #333 最大二叉搜索树子树

描述：给定二叉树，找出最大的二叉搜索树子树。

// [#333](https://leetcode.com/problems/largest-bst-subtree/) Description: Largest BST Subtree | LeetCode OJ

解法1：跟判断BST一样。

// Solution 1: Same as validating a BST.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0333_largest-bst-subtree_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0333_largest-bst-subtree_1_AC.cpp)

<hr>

#334 Increasing Triplet Subsequence

// #334 递增三元组

描述：给定数组，问是否存在长度为3的递增子序列。

// [#334](https://leetcode.com/problems/increasing-triplet-subsequence/) Description: Increasing Triplet Subsequence | LeetCode OJ

解法1：看代码。

// Solution 1: Read the code.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0334_increasing-triplet-subsequence_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0334_increasing-triplet-subsequence_1_AC.cpp)

<hr>

#335 Self Crossing

// #335 自交叉

描述：给定一系列长度，从(0, 0)出发按照“上左下右...”顺序依长度逐个走下去。问走过的轨迹是否存在交叉？碰上就算。

// [#335](https://leetcode.com/problems/self-crossing/) Description: Self Crossing | LeetCode OJ

解法1：谜之解法，很聪明。

// Solution 1: A clever solution, not mine.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0335_self-crossing_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0335_self-crossing_1_AC.cpp)

<hr>

#336 Palindrome Pairs

// #336 回文对

描述：给定一堆字符串，问哪两个连起来是回文串。求所有可能的回文对。

// [#336](https://leetcode.com/problems/palindrome-pairs/) Description: Palindrome Pairs | LeetCode OJ

解法1：字符串哈希，正向反向一起用。

// Solution 1: String hashing, both forward and reverse.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0336_palindrome-pairs_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0336_palindrome-pairs_1_AC.cpp)

<hr>

#337 House Robber III

// #337 小偷3

描述：这回房子构成一棵二叉树，依然不能偷相邻俩房子，求怎么偷最来钱。

// [#337](https://leetcode.com/problems/house-robber-iii/) Description: House Robber III | LeetCode OJ

解法1：搜呗。

// Solution 1: Search it.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0337_house-robber-iii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0337_house-robber-iii_1_AC.cpp)

<hr>

#338 Counting Bits

// #338 数位数

描述：给定一个非负整数num，求0~num每个数中二进制1的个数。

// [#338](https://leetcode.com/problems/counting-bits/) Description: Counting Bits | LeetCode OJ

解法1：DP。

// Solution 1: DP.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0338_counting-bits_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0338_counting-bits_1_AC.cpp)

<hr>

#339 Nested List Weight Sum

// #339 嵌套列表加权和

描述：如题。

// [#339](https://leetcode.com/problems/nested-list-weight-sum/) Description: Nested List Weight Sum | LeetCode OJ

解法1：手动递归。

// Solution 1: Manual recursion.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0339_nested-list-weight-sum_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0339_nested-list-weight-sum_1_AC.cpp)

<hr>

#340 Longest Substring with At Most K Distinct Characters

// #340 包含至多K个不同字母的最长子串

描述：如题。

// [#340](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/) Description: Longest Substring with At Most K Distinct Characters | LeetCode OJ

解法1：俩指针。

// Solution 1: Two pointers.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0340_longest-substring-with-at-most-k-distinct-characters_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0340_longest-substring-with-at-most-k-distinct-characters_1_AC.cpp)

<hr>

#341 Flatten Nested List Iterator

// #341 展开嵌套列表的迭代器

描述：像访问一个一维列表一样访问嵌套列表。

// [#341](https://leetcode.com/problems/flatten-nested-list-iterator/) Description: Flatten Nested List Iterator | LeetCode OJ

解法1：手动递归。

// Solution 1: Manual recursion.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0341_flatten-nested-list-iterator_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0341_flatten-nested-list-iterator_1_AC.cpp)

<hr>

#342 Power of Four

// #342 4的幂

描述：判断一个数是否为4的幂。

// [#342](https://leetcode.com/problems/power-of-four/) Description: Power of Four | LeetCode OJ

解法1：循环。

// Solution 1: Loop.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0342_power-of-four_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0342_power-of-four_1_AC.cpp)

解法2：对数。

// Solution 2: Logarithm.

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0342_power-of-four_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0342_power-of-four_2_AC.cpp)

<hr>

#343 Integer Break

// #343 整数分解

描述：将一个正整数分解为至少两个正整数，使其乘积最大。

// [#343](https://leetcode.com/problems/integer-break/) Description: Integer Break | LeetCode OJ

解法1：DP。

// Solution 1: DP.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0343_integer-break_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0343_integer-break_1_AC.cpp)

<hr>

#344 Reverse String

// #344 反转字符串

描述：如题。

// [#344](https://leetcode.com/problems/reverse-string/) Description: Reverse String | LeetCode OJ

解法1：转。

// Solution 1: Do it.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0344_reverse-string_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0344_reverse-string_1_AC.cpp)

解法2：转。

// Solution 2: Do it.

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0344_reverse-string_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0344_reverse-string_2_AC.cpp)

<hr>

#345 Reverse Vowels of a String

// #345 反转元音

描述：给定一个串，只反转元音。

// [#345](https://leetcode.com/problems/reverse-vowels-of-a-string/) Description: Reverse Vowels of a String | LeetCode OJ

解法1：水题。

// Solution 1: Trivial.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0345_reverse-vowels-of-a-string_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0345_reverse-vowels-of-a-string_1_AC.cpp)

<hr>

#346 Moving Average from Data Stream

// #346 滑动窗口平均值

描述：如题。

// [#346](https://leetcode.com/problems/moving-average-from-data-stream/) Description: Moving Average from Data Stream | LeetCode OJ

解法1：滑呗。

// Solution 1: Slide it.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0346_moving-average-from-data-stream_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0346_moving-average-from-data-stream_1_AC.cpp)

<hr>

#347 Top K Frequent Elements

// #347 K个最常见元素

描述：给定数组，求其中出现频率最高的K个元素。

// [#347](https://leetcode.com/problems/top-k-frequent-elements/) Description: Top K Frequent Elements | LeetCode OJ

解法1：没意思。

// Solution 1: Dull.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0347_top-k-frequent-elements_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0347_top-k-frequent-elements_1_AC.cpp)

<hr>

#348 Design Tic-Tac-Toe

// #348 井字棋

描述：设计井字棋游戏。

// [#348](https://leetcode.com/problems/design-tic-tac-toe/) Description: Design Tic-Tac-Toe | LeetCode OJ

解法1：模拟题。

// Solution 1: Simulation problem.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0348_design-tic-tac-toe_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0348_design-tic-tac-toe_1_AC.cpp)

<hr>

#349 Intersection of Two Arrays

// #349 数组交集

描述：如题。

// [#349](https://leetcode.com/problems/intersection-of-two-arrays/) Description: Intersection of Two Arrays | LeetCode OJ

解法1：水题。

// Solution 1: Easy.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0349_intersection-of-two-arrays_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0349_intersection-of-two-arrays_1_AC.cpp)

<hr>

#350 Intersection of Two Arrays II

// #350 数组交集2

描述：如题，不去重。

// [#350](https://leetcode.com/problems/intersection-of-two-arrays-ii/) Description: Intersection of Two Arrays II | LeetCode OJ

解法1：水题。

// Solution 1: Easy.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0350_intersection-of-two-arrays-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0350_intersection-of-two-arrays-ii_1_AC.cpp)

<hr>

#351 Android Unlock Patterns

// #351 安卓解锁图案

描述：手机的解锁手势知道吧？找出经过格点数在m~n之间的所有解锁手势个数。手势中如果经过一个未访问的点，是不允许直接跳过的。

// [#351](https://leetcode.com/problems/android-unlock-patterns/) Description: Android Unlock Patterns | LeetCode OJ

解法1：搜。

// Solution 1: DFS.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0351_android-unlock-patterns_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0351_android-unlock-patterns_1_AC.cpp)

<hr>

#352 Data Stream as Disjoint Intervals

// #352 数据流表示为离散区间

描述：设计一个数据结构，允许添加数据，允许统计元素的分布区间。

// [#352](https://leetcode.com/problems/data-stream-as-disjoint-intervals/) Description: Data Stream as Disjoint Intervals | LeetCode OJ

解法1：哈希。

// Solution 1: Hash.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0352_data-stream-as-disjoint-intervals_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0352_data-stream-as-disjoint-intervals_1_AC.cpp)

<hr>

#353 Design Snake Game

// #353 贪食蛇

描述：设计贪食蛇游戏。

// [#353](https://leetcode.com/problems/design-snake-game/) Description: Design Snake Game | LeetCode OJ

解法1：很明显，用链表表示蛇比较合适，因为移动一格只需要改变头尾节点。

// Solution 1: Apparently, it's appropriate to represent the snake with a linked list, as moving one step requires only changing the head and the tail node.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0353_design-snake-game_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0353_design-snake-game_1_AC.cpp)

<hr>

#354 Russian Doll Envelopes

// #354 俄罗斯套娃

描述：给定一堆矩形，问最多能嵌套几层。

// [#354](https://leetcode.com/problems/russian-doll-envelopes/) Description: Russian Doll Envelopes | LeetCode OJ

解法1：O(N ^ 2) DP。

// Solution 1: O(N ^ 2) DP.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0354_russian-doll-envelopes_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0354_russian-doll-envelopes_1_AC.cpp)

解法2：LIS。

// Solution 2: LIS.

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0354_russian-doll-envelopes_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0354_russian-doll-envelopes_2_AC.cpp)

<hr>

#355 Design Twitter

// #355 设计推特

描述：太长不写。

// [#355](https://leetcode.com/problems/design-twitter/) Description: Design Twitter | LeetCode OJ

解法1：麻烦的一塌糊涂，这叫算法题？这叫系统设计题还差不多。

// Solution 1: You call this algorithmic problem? I think system design suits better.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0355_design-twitter_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0355_design-twitter_1_AC.cpp)

<hr>

#356 Line Reflection

// #356 对称轴

描述：给定N个点，看是否存在一条竖直线，使得全图关于这条线对称。

// [#356](https://leetcode.com/problems/line-reflection/) Description: Line Reflection | LeetCode OJ

解法1：挺无聊的一题。

// Solution 1: Relatively boring.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0356_line-reflection_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0356_line-reflection_1_AC.cpp)

<hr>

#357 Count Numbers with Unique Digits

// #357 数字不重复的数的个数

描述：给定整数N，求不超过N位的数字不重复的数的个数。

// [#357](https://leetcode.com/problems/count-numbers-with-unique-digits/) Description: Count Numbers with Unique Digits | LeetCode OJ

解法1：这是个数学题。

// Solution 1: Math problem.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0357_count-numbers-with-unique-digits_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0357_count-numbers-with-unique-digits_1_AC.cpp)

<hr>

#358 Rearrange String k Distance Apart

// #358 重排字符串使相同字符至少相距k位

描述：如题。

// [#358](https://leetcode.com/problems/rearrange-string-k-distance-apart/) Description: Rearrange String k Distance Apart | LeetCode OJ

解法1：总是从剩余最多的字母开始考虑。

// Solution 1: Always start looking from the letter with the highest remaining count.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0358_rearrange-string-k-distance-apart_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0358_rearrange-string-k-distance-apart_1_AC.cpp)

<hr>

#359 Logger Rate Limiter

// #359 日志限速器

描述：设计一个数据结构，能打印日志。但如果相同的日志在过去10s内已经打印过了，就不打。

// [#359](https://leetcode.com/problems/logger-rate-limiter/) Description: Logger Rate Limiter | LeetCode

解法1：模拟题。

// Solution 1: Simulation problem.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0359_logger-rate-limiter_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0359_logger-rate-limiter_1_AC.cpp)

<hr>

#360 Sort Transformed Array

// #360 排序变换后的数组

描述：给定一个数组，对每个元素执行f(x) = ax2 + bx + c的映射，求映射后结果，要求将结果排序，但不能使用排序算法。

// [#360](https://leetcode.com/problems/sort-transformed-array/) Description: Sort Transformed Array | LeetCode OJ

解法1：这就叫没事找事，吃饱了撑的。

// Solution 1: Don't you have better things to do?

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0360_sort-transformed-array_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0360_sort-transformed-array_1_AC.cpp)

<hr>

#361 Bomb Enemy

// #361 轰炸敌人

描述：炸弹人玩过吧？假设炸弹只能放在空地，不能炸穿墙，可以贯穿多个敌人，求一个炸弹最多能炸死多少敌人。

// [#361](https://leetcode.com/problems/bomb-enemy/) Description: Bomb Enemy | LeetCode OJ

解法1：也算是DP吧。

// Solution 1: I guess this is DP after all.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0361_bomb-enemy_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0361_bomb-enemy_1_AC.cpp)

<hr>

#362 Design Hit Counter

// #362 设计命中计数器

描述：设计一个计数器，可以在某个时间点命中，也可以统计以某个时间点截止的5分钟内的命中总次数。

// [#362](https://leetcode.com/problems/design-hit-counter/) Description: Design Hit Counter | LeetCode OJ

解法1：用map。

// Solution 1: Use a map.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0362_design-hit-counter_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0362_design-hit-counter_1_AC.cpp)

<hr>

#363 Max Sum of Rectangle No Larger Than K

// #363 和不超过K的最大子矩阵

描述：给定一个矩阵，求和不超过K的最大子矩阵。

// [#363](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/) Description: Max Sum of Rectangle No Larger Than K | LeetCode OJ

解法1：首先你要知道最大子矩阵和的求法，然后你要知道不超过K的最大子数组和的求法，然后就没有然后了。

// Solution 1: Know how to get maximal submatrix sum, know how to get maximal subarray sum no larger than K, know no more.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0363_max-sum-of-rectangle-no-larger-than-k_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0363_max-sum-of-rectangle-no-larger-than-k_1_AC.cpp)

<hr>

#364 Nested List Weight Sum II

// #364 嵌套列表加权和2

描述：和之前一样，不过这次权值反着来，越深的权值越小。

// [#364](https://leetcode.com/problems/nested-list-weight-sum-ii/) Description: Nested List Weight Sum II | LeetCode OJ

解法1：稍微变化一下。

// Solution 1: Minor change.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0364_nested-list-weight-sum-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0364_nested-list-weight-sum-ii_1_AC.cpp)

<hr>

#365 Water and Jug Problem

// #365 水和罐子问题

描述：给定两个罐子和足够多的水。每次允许你倒水，但要求要么倒空，要么倒满，要么来回倒。给定俩罐子容积v1、v2，和一个体积v3，问能够得到v3体积的水。

// [#365](https://leetcode.com/problems/water-and-jug-problem/) Description: Water and Jug Problem | LeetCode OJ

解法1：注意边界情况。

// Solution 1: Edge cases.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0365_water-and-jug-problem_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0365_water-and-jug-problem_1_AC.cpp)

<hr>

#366 Find Leaves of Binary Tree

// #366 捡树叶

描述：逐层移除二叉树的叶节点。

// [#366](https://leetcode.com/problems/find-leaves-of-binary-tree/) Description: Find Leaves of Binary Tree | LeetCode OJ

解法1：注意每个节点的高度，发现规律了吗？

// Solution 1: Note the height of each node, see?

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0366_find-leaves-of-binary-tree_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0366_find-leaves-of-binary-tree_1_AC.cpp)

<hr>

#367 Valid Perfect Square

// #367 验证完全平方数

描述：如题。

// [#367](https://leetcode.com/problems/valid-perfect-square/) Description: Valid Perfect Square | LeetCode OJ

解法1：匪开方，如之何？

// Solution 1: Any way around the square root?

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0367_valid-perfect-square_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0367_valid-perfect-square_1_AC.cpp)

<hr>

#368 Largest Divisible Subset

// #368 最大整除子集

描述：给定一个集合，找出最大的子集，使得子集中任意两数都有整除关系。

// [#368](https://leetcode.com/problems/largest-divisible-subset/) Description: Largest Divisible Subset | LeetCode OJ

解法1：DP.

// Solution 1: DP.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0368_largest-divisible-subset_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0368_largest-divisible-subset_1_AC.cpp)

<hr>

#369 Plus One Linked List

// #369 链表加一

描述：给定一个链表表示高精度数，给加个1。

// [#369](https://leetcode.com/problems/plus-one-linked-list/) Description: Plus One Linked List | LeetCode OJ

解法1：水题。

// Solution 1: Trivial.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0369_plus-one-linked-list_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0369_plus-one-linked-list_1_AC.cpp)

<hr>

#370 Range Addition

// #370 区间增加

描述：给定一个数组，开始全0.每次允许对一个区间统一加上某值。执行完一系列加法后，返回数组。

// [#370](https://leetcode.com/problems/range-addition/) Description: Range Addition | LeetCode OJ

解法1：树状数组的另一应用。

// Solution 1: Another application of BIT.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0370_range-addition_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0370_range-addition_1_AC.cpp)

<hr>

#371 Sum of Two Integers

// #371 整数加法

描述：不准用+-。

// [#371](https://leetcode.com/problems/sum-of-two-integers/) Description: Sum of Two Integers | LeetCode OJ

解法1：想想加法器的原理。

// Solution 1: Think about how an adder works.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0371_sum-of-two-integers_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0371_sum-of-two-integers_1_AC.cpp)

<hr>

#372 Super Pow

// #372 超级幂

描述：底数小，指数非常大，结果膜。

// [#372](https://leetcode.com/problems/super-pow/) Description: Super Pow | LeetCode OJ

解法1：快速幂，不过这次是十进制的。

// Solution 1: Denary exponentiation, not binary.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0372_super-pow_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0372_super-pow_1_AC.cpp)

<hr>

#373 Find K Pairs with Smallest Sums

// #373 找出和最小的前K对

描述：给定两个有序数组，允许从俩数组各选一个数组成数对。求和最小的前K对。

// [#373](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) Description: Find K Pairs with Smallest Sums | LeetCode OJ

解法1：最小堆。

// Solution 1: Min heap.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0373_find-k-pairs-with-smallest-sums_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0373_find-k-pairs-with-smallest-sums_1_AC.cpp)

<hr>

#374 Guess Number Higher or Lower

// #374 高了低了

描述：猜吧。

// [#374](https://leetcode.com/problems/guess-number-higher-or-lower/) Description: Guess Number Higher or Lower | LeetCode OJ

解法1：二分。

// Solution 1: Binary search.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0374_guess-number-higher-or-lower_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0374_guess-number-higher-or-lower_1_AC.cpp)

<hr>

#375 Guess Number Higher or Lower II

// #375 高了低了

描述：还是猜数字，不过这次如果你猜x，而且猜错了，就要罚款x元。问至少要带多少钱才能保证赢？

// [#375](https://leetcode.com/problems/guess-number-higher-or-lower-ii/) Description: Guess Number Higher or Lower II | LeetCode OJ

解法1：改个玩法，难度就完全不一样了。将[1, n]间猜数字作为总问题，则各种[i, j]可视为子问题，我们的目的是尽量少带钱，所以就要使罚款尽量少。由此，DP的根据就形成了。

// Solution 1: A small change in the rule create a whole new problem. If we view the guess among [1, n] as the whole problem, any [i, j] can be considered a subproblem. The goal is to bring as little money as possible, thus we need to minimize the cost of each subproblem. With these points clarified, the ground for DP is solid, now start coding.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0375_guess-number-higher-or-lower-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0375_guess-number-higher-or-lower-ii_1_AC.cpp)

<hr>

#376 Wiggle Subsequence

// #376 摆动子序列

描述：按照“大小大小...”或者“小大小大...”的定义。找出数组中最长摆动序列的长度。

// [#376](https://leetcode.com/problems/wiggle-subsequence/) Description: Wiggle Subsequence | LeetCode OJ

解法1：看代码。

// Solution 1: Read the code.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0376_wiggle-subsequence_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0376_wiggle-subsequence_1_AC.cpp)

<hr>

#377 Combination Sum IV

// #377 组合之和4

描述：给定集合，每个元素可使用任意多次。求加起来等于一个值target的所有组合种数，不同顺序也算数。

// [#377](https://leetcode.com/problems/combination-sum-iv/) Description: Combination Sum IV | LeetCode OJ

解法1：根本不用搜，DP就好。

// Solution 1: Don't resort to brute-force when there're more elegant ways.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0377_combination-sum-iv_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0377_combination-sum-iv_1_AC.cpp)

<hr>

#378 Kth Smallest Element in a Sorted Matrix

// #378 杨氏矩阵第K小元素

描述：如题。

// [#378](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) Description: Kth Smallest Element in a Sorted Matrix | LeetCode OJ

解法1：最小堆。

// Solution 1: Min heap.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0378_kth-smallest-element-in-a-sorted-matrix_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0378_kth-smallest-element-in-a-sorted-matrix_1_AC.cpp)

<hr>

#379 Design Phone Directory

// #379 设计手机路径

描述：设计一个电话簿，能够分配、释放号码，或检查号码是否存在。

// [#379](https://leetcode.com/problems/design-phone-directory/) Description: Design Phone Directory | LeetCode OJ

解法1：模拟题，懒得多说。

// Solution 1: Simulation problem.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0379_design-phone-directory_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0379_design-phone-directory_1_AC.cpp)

解法2：用哈希表代替位向量。

// Solution 2: Replace the bit vector with a hash table.

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0379_design-phone-directory_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0379_design-phone-directory_2_AC.cpp)

<hr>

#380 Insert Delete GetRandom O(1)

// #380 插入、删除、随机读取O(1)

描述：设计一个数据结构，能够插入、删除数据，并能够以均等的机会随机读取一个元素。

// [#380](https://leetcode.com/problems/insert-delete-getrandom-o1/) Description: Insert Delete GetRandom O(1) | LeetCode OJ

解法1：数组 + 哈希表。

// Solution 1: Array + hash table.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0380_insert-delete-getrandom-o1_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0380_insert-delete-getrandom-o1_1_AC.cpp)

<hr>

#381 Insert Delete GetRandom O(1) - Duplicates allowed

// #381 插入、删除、随机读取O(1)

描述：和之前一样，不过这次允许重复元素。

// [#381](https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/) Description: Insert Delete GetRandom O(1) - Duplicates allowed | LeetCode OJ

解法1：还是数组+哈希表，不过哈希表的内容稍加变化。

// Solution 1: Still array + hash table, just the value in the hash table needs a little change.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0381_insert-delete-getrandom-o1-duplicates-allowed_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0381_insert-delete-getrandom-o1-duplicates-allowed_1_AC.cpp)

<hr>

#382 Linked List Random Node

// #382 链表随机节点

描述：随机读取链表的一个节点。

// [#382](https://leetcode.com/problems/linked-list-random-node/) Description: Linked List Random Node | LeetCode OJ

解法1：水库采样。

// Solution 1: Reservoir Sampling.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0382_linked-list-random-node_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0382_linked-list-random-node_1_AC.cpp)

<hr>

#383 Ransom Note

// #383 赎金纸条

描述：判断一个字符串的字母是否是另一个字符串的子集。

// [#383](https://leetcode.com/problems/ransom-note/) Description: Ransom Note | LeetCode OJ

解法1：水题。

// Solution 1: Trivial.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0383_ransom-note_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0383_ransom-note_1_AC.cpp)

<hr>

#384 Shuffle an Array

// #384 洗牌

描述：如题。

// [#384](https://leetcode.com/problems/shuffle-an-array/) Description: Shuffle an Array | LeetCode OJ

解法1：O(N)时间搞定。

// Solution 1: O(N) time.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0384_shuffle-an-array_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0384_shuffle-an-array_1_AC.cpp)

<hr>

#385 Mini Parser

// #385 迷你解析器

描述：给定一个嵌套字符串，将其解析成嵌套列表。

// [#385](https://leetcode.com/problems/mini-parser/) Description: Mini Parser | LeetCode OJ

解法1：解呗。

// Solution 1: Solve it.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0385_mini-parser_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0385_mini-parser_1_AC.cpp)

<hr>

#386 Lexicographical Numbers

// #386 字典序数

描述：给定整数n，将1~n按字典序排序。

// [#386](https://leetcode.com/problems/lexicographical-numbers/) Description: Lexicographical Numbers | LeetCode OJ

解法1：想想相邻俩数之间有什么规律？

// Solution 1: What regularities do lexicographically adjacent numbers hold?

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0386_lexicographical-numbers_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0386_lexicographical-numbers_1_AC.cpp)

<hr>

#387 First Unique Character in a String

// #387 第一个不重复字母

描述：如题。

// [#387](https://leetcode.com/problems/first-unique-character-in-a-string/) Description: First Unique Character in a String | LeetCode OJ

解法1：水题。

// Solution 1: Trivial.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0387_first-unique-character-in-a-string_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0387_first-unique-character-in-a-string_1_AC.cpp)

<hr>

#388 Longest Absolute File Path

// #388 最长绝对路径

描述：给定文件树，求最长绝对文件路径。

// [#388](https://leetcode.com/problems/longest-absolute-file-path/) Description: Longest Absolute File Path | LeetCode OJ

解法1：这题测试数据有问题。

// Solution 1: The test cases of this problem are bugged.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0388_longest-absolute-file-path_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0388_longest-absolute-file-path_1_AC.cpp)

<hr>

#389 Find the Difference

// #389 找不同

描述：给定两个字符串，其中一个多了个字母，找出该字母。

// [#389](https://leetcode.com/problems/find-the-difference/) Description: Find the Difference | LeetCode OJ

解法1：数数。

// Solution 1: Count them.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0389_find-the-difference_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0389_find-the-difference_1_AC.cpp)

解法2：排序。

// Solution 2: Sort them.

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0389_find-the-difference_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0389_find-the-difference_2_AC.cpp)

<hr>

#390 Elimination Game

// #390 消除游戏

描述：从左到右1~n共n个数字，轮流按照“所有奇位置”“所有偶位置”的规则，去掉当前序列中对应的数，直到只剩一个数为止。问这个数是几？

// [#390](https://leetcode.com/problems/elimination-game/) Description: Elimination Game | LeetCode OJ

解法1：不管进行几轮，剩下的数列始终是个等差数列。算好首项和公差，一切就真相大白了。

// Solution 1: No matter how the elimination is done, the left sequence is always arithmetic. Thus we calculate the initial term and the common difference, everything else is brought to light.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0390_elimination-game_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0390_elimination-game_1_AC.cpp)

<hr>

#391 Perfect Rectangle

// #391 完美矩形

描述：给定一堆矩形，问能不能恰好覆盖成一个矩形，要求严丝合缝、不多不少。

// [#391](https://leetcode.com/problems/perfect-rectangle/) Description: Perfect Rectangle | LeetCode OJ

解法1：如果恰好能覆盖成完整矩形，那么面积、顶点会不会有什么规律呢？

// Solution 1: If there happens to be an exact cover, would anything special be in the vertices and areas?

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0391_perfect-rectangle_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0391_perfect-rectangle_1_AC.cpp)

<hr>

#392 Is Subsequence

// #392 是否为子序列

描述：给定一长一短俩串儿，判断短的是不是长的的子序列。

// [#392](https://leetcode.com/problems/is-subsequence/) Description: Is Subsequence | LeetCode OJ

解法1：扫一遍就行了。

// Solution 1: Scan it.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0392_is-subsequence_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0392_is-subsequence_1_AC.cpp)

<hr>

#393 UTF-8 Validation

// #393 UTF-8验证

描述：告诉你UTF-8的编码规则，请验证一段数据的合法性。

// [#393](https://leetcode.com/problems/utf-8-validation/) Description: UTF-8 Validation | LeetCode OJ

解法1：按规矩来。

// Solution 1: By the book.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0393_utf-8-validation_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0393_utf-8-validation_1_AC.cpp)

<hr>

#394 Decode String

// #394 字符串解码

描述：给定游程码字符串，进行解码。

// [#394](https://leetcode.com/problems/decode-string/) Description: Decode String | LeetCode OJ

解法1：递归解码。

// Solution 1: Decode recursively.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0394_decode-string_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0394_decode-string_1_AC.cpp)

<hr>

#395 Longest Substring with At Least K Repeating Characters

// #395 字母至少重复K次的最长子串

描述：如题，子串中的每个字母都要有至少K个，求最长子串。

// [#395](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/) Description: Longest Substring with At Least K Repeating Characters | LeetCode OJ

解法1：还是俩指针，不过代码稍微复杂些。

// Solution 1: Still needs two pointers. The code looks more complicated, though.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0395_longest-substring-with-at-least-k-repeating-characters_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0395_longest-substring-with-at-least-k-repeating-characters_1_AC.cpp)

<hr>

#396 Rotate Function

// #396 旋转函数

描述：懒得说。

// [#396](https://leetcode.com/problems/rotate-function/) Description: Rotate Function | LeetCode OJ

解法1：小把戏。

// Solution 1: Small trick.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0396_rotate-function_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0396_rotate-function_1_AC.cpp)

<hr>

#397 Integer Replacement

// #397 整数替换

描述：如果n是偶数，则变成n / 2；否则，变成n - 1或者n + 1。问至少多少次操作，能把n变成1。

// [#397](https://leetcode.com/problems/integer-replacement/) Description: Integer Replacement | LeetCode OJ

解法1：DP。

// Solution 1: DP.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0397_integer-replacement_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0397_integer-replacement_1_AC.cpp)

<hr>

#398 Random Pick Index

// #398 随机选下标

描述：给定一个可能有重复的数组，给定一个值，随机输出一个该值的下标。

// [#398](https://leetcode.com/problems/random-pick-index/) Description: Random Pick Index | LeetCode OJ

解法1：水库采样，时间换空间。

// Solution 1: Reservoir Sampling, trading time for space.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0398_random-pick-index_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0398_random-pick-index_1_AC.cpp)

<hr>

#399 Evaluate Division

// #399 变量相除

描述：给你一些变量相除的结果，要你求出另一些变量相除的结果。

// [#399](https://leetcode.com/problems/evaluate-division/) Description: Evaluate Division | LeetCode OJ

解法1：带权并查集？

// Solution 1: Weighted union-find set?

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0399_evaluate-division_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0399_evaluate-division_1_AC.cpp)

<hr>

#400 Nth Digit

// #400 第N位数

描述：把1、2、3、...写成一串。求第N位数是什么？

// [#400](https://leetcode.com/problems/nth-digit/) Description: Nth Digit | LeetCode OJ

解法1：我讨厌数数。

// Solution 1: I hate counting.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0400_nth-digit_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0400_nth-digit_1_AC.cpp)
