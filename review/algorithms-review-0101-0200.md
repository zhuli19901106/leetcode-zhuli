#101 Symmetric Tree

// #101 对称树

描述：给定二叉树，判断其是否左右对称。

// [#101](https://leetcode.com/problems/symmetric-tree/) Description: Symmetric Tree | LeetCode OJ

解法1：递归。

// Solution 1: Recursion.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0101_symmetric-tree_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0101_symmetric-tree_1_AC.cpp)

解法2：水平遍历。

// Solution 2: Level-order traversal.

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0101_symmetric-tree_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0101_symmetric-tree_2_AC.cpp)

<hr>

#102 Binary Tree Level Order Traversal

// #102 二叉树水平遍历

描述：如题。

// [#102](https://leetcode.com/problems/binary-tree-level-order-traversal/) Description: Binary Tree Level Order Traversal | LeetCode OJ

解法1：由于这题的返回数据形式特殊，所以随便用什么遍历都行。通常是要用队列的。

// Solution 1: Any traversal is fine due to the special format of the return value. Usually we use a queue.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0102_binary-tree-level-order-traversal_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0102_binary-tree-level-order-traversal_1_AC.cpp)

解法2：用队列。

// Solution 2: Use a queue.

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0102_binary-tree-level-order-traversal_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0102_binary-tree-level-order-traversal_2_AC.cpp)

<hr>

#103 Binary Tree Zigzag Level Order Traversal

// #103 二叉树来回遍历

描述：懒得说。吃饱了撑的，净瞎折腾。

// [#103](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) Description: Binary Tree Zigzag Level Order Traversal | LeetCode OJ

解法1：折腾呗。

// Solution 1: Do it.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0103_binary-tree-zigzag-level-order-traversal_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0103_binary-tree-zigzag-level-order-traversal_1_AC.cpp)

<hr>

#104 Maximum Depth of Binary Tree

// #104 二叉树最大深度

描述：如题。

// [#104](https://leetcode.com/problems/maximum-depth-of-binary-tree/) Description: Maximum Depth of Binary Tree | LeetCode OJ

解法1：递归。

// Solution 1: Recursion.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0104_maximum-depth-of-binary-tree_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0104_maximum-depth-of-binary-tree_1_AC.cpp)

<hr>

#105 Construct Binary Tree from Preorder and Inorder Traversal

// #105 由前序和中序遍历重建二叉树

描述：如题。

// [#105](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) Description: Construct Binary Tree from Preorder and Inorder Traversal | LeetCode OJ

解法1：理解前序、中序、后序的性质，然后用哈希表快速查找各元素的位置，以达到O(N)时间重建的目的。

// Solution 1: Understand the properties of pre-order, inorder and post-order traversal. Use a hash table to look up indices efficiently, so that the reconstruction can be done in O(N) time.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0105_construct-binary-tree-from-preorder-and-inorder-traversal_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0105_construct-binary-tree-from-preorder-and-inorder-traversal_1_AC.cpp)

<hr>

#106 Construct Binary Tree from Inorder and Postorder Traversal

// #106 由中序和后序遍历重建二叉树

描述：如题。

// [#106](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) Description: Construct Binary Tree from Inorder and Postorder Traversal | LeetCode OJ

解法1：和之前一样。要知道前序和后序是不足以重建二叉树的。

// Solution 1: Same as before. Know that pre-order and post-order are not sufficient for reconstruction.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0106_construct-binary-tree-from-inorder-and-postorder-traversal_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0106_construct-binary-tree-from-inorder-and-postorder-traversal_1_AC.cpp)

<hr>

#107 Binary Tree Level Order Traversal II

// #107 二叉树水平遍历

描述：和之前一样，不过这次结果要上下颠倒。

// [#107](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/) Description: Binary Tree Level Order Traversal II | LeetCode OJ

解法1：倒呗。

// Solution 1: Reverse the result.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0107_binary-tree-level-order-traversal-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0107_binary-tree-level-order-traversal-ii_1_AC.cpp)

<hr>

#108 Convert Sorted Array to Binary Search Tree

// #108 将有序数组转为二叉搜索树

描述：要平衡的。

// [#108](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) Description: Convert Sorted Array to Binary Search Tree | LeetCode OJ

解法1：递归。

// Solution 1: Recursively.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0108_convert-sorted-array-to-binary-search-tree_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0108_convert-sorted-array-to-binary-search-tree_1_AC.cpp)

<hr>

#109 Convert Sorted List to Binary Search Tree

// #109 将有序链表转为二叉搜索树

描述：如题。

// [#109](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/) Description: Convert Sorted List to Binary Search Tree | LeetCode OJ

解法1：和之前一样，只不过这次改链表了。你可以凑活，也可以先转成数组。

// Solution 1: Same as before, only in that it's a list this time. You can either make do with it or convert it to array first.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0109_convert-sorted-list-to-binary-search-tree_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0109_convert-sorted-list-to-binary-search-tree_1_AC.cpp)

<hr>

#110 Balanced Binary Tree

// #110 平衡二叉树

描述：如题。

// [#110](https://leetcode.com/problems/balanced-binary-tree/) Description: Balanced Binary Tree | LeetCode OJ

解法1：按定义来。

// Solution 1: By the definition.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0110_balanced-binary-tree_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0110_balanced-binary-tree_1_AC.cpp)

<hr>

#111 Minimum Depth of Binary Tree

// #111 二叉树最小深度

描述：如题。

// [#111](https://leetcode.com/problems/minimum-depth-of-binary-tree/) Description: Minimum Depth of Binary Tree | LeetCode OJ

解法1：水题。

// Solution 1: Easy.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0111_minimum-depth-of-binary-tree_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0111_minimum-depth-of-binary-tree_1_AC.cpp)

<hr>

#112 Path Sum

// #112 路径和

描述：给定二叉树和一个值，判断从根到叶是否存在一条路径，其路径和等于该值。

// [#112](https://leetcode.com/problems/path-sum/) Description: Path Sum | LeetCode OJ

解法1：奉旨遍历。

// Solution 1: Traverse.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0112_path-sum_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0112_path-sum_1_AC.cpp)

<hr>

#113 Path Sum II

// #113 路径和2

描述：和之前一样，不过这次要找出所有符合条件的路径。

// [#113](https://leetcode.com/problems/path-sum-ii/) Description: Path Sum II | LeetCode OJ

解法1：搜。

// Solution 1: Make a search.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0113_path-sum-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0113_path-sum-ii_1_AC.cpp)

<hr>

#114 Flatten Binary Tree to Linked List

// #114 将二叉树展开式链表

描述：给定二叉树，将其展开成一个右倾的链表。

// [#114](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/) Description: Flatten Binary Tree to Linked List | LeetCode OJ

解法1：递归解决。

// Solution 1: Recursively.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0114_flatten-binary-tree-to-linked-list_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0114_flatten-binary-tree-to-linked-list_1_AC.cpp)

<hr>

#115 Distinct Subsequences

// #115 不同子序列

描述：给定字符串S和T，问S有多少个子序列等于T。

// [#115](https://leetcode.com/problems/distinct-subsequences/) Description: Distinct Subsequences | LeetCode OJ

解法1：典型的动态规划问题。

// Solution 1: Typical DP problem.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0115_distinct-subsequences_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0115_distinct-subsequences_1_AC.cpp)

<hr>

#116 Populating Next Right Pointers in Each Node

// #116 填充next指针

描述：给定一个二叉树，其中每个节点都有next指针。设法将next指针指向同一层紧邻靠右的节点。这棵二叉树一定是满的。

// [#116](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/) Description: Populating Next Right Pointers in Each Node | LeetCode OJ

解法1：这题有意思，初次见到还是很难的。我第一次想了俩钟头没想出来，于是上网找了题解。非常巧妙且高效。

// Solution 1: This problem can be quite challenging if it's your first attempt. I didn't work it out after almost two hour, so I referred to this solution from the internet. Very clever and efficient.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0116_populating-next-right-pointers-in-each-node_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0116_populating-next-right-pointers-in-each-node_1_AC.cpp)

<hr>

#117 Populating Next Right Pointers in Each Node II

// #117 填充next指针。

描述：和之前一样，但这次的二叉树可以是任何二叉树。

// [#117](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/) Description: Populating Next Right Pointers in Each Node II | LeetCode OJ

解法1：递归。

// Solution 1: Recursion.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0117_populating-next-right-pointers-in-each-node-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0117_populating-next-right-pointers-in-each-node-ii_1_AC.cpp)

解法2：循环

// Solution 2: Loop.

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0117_populating-next-right-pointers-in-each-node-ii_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0117_populating-next-right-pointers-in-each-node-ii_2_AC.cpp)

<hr>

#118 Pascal's Triangle

// #118 杨辉三角

描述：如题。二项式定理知道吧？

// [#118](https://leetcode.com/problems/pascals-triangle/) Description: Pascal's Triangle | LeetCode OJ

解法1：DP。

// Solution 1: DP.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0118_pascals-triangle_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0118_pascals-triangle_1_AC.cpp)

<hr>

#119 Pascal's Triangle II

// #119 杨辉三角2

描述：和之前一样，但这次只要最后一行。

// [#119](https://leetcode.com/problems/pascals-triangle-ii/) Description: Pascal's Triangle II | LeetCode OJ

解法1：一样。

// Solution 1: The same.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0119_pascals-triangle-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0119_pascals-triangle-ii_1_AC.cpp)

<hr>

#120 Triangle

// #120 三角

描述：给定一个金字塔形，从上往下求走，最小路径和。

// [#120](https://leetcode.com/problems/triangle/) Description: Triangle | LeetCode OJ

解法1：DP。

// Solution 1: DP.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0120_triangle_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0120_triangle_1_AC.cpp)

<hr>

#121 Best Time to Buy and Sell Stock

// #121 最佳炒股时机

描述：给定一系列股价，允许买卖各一次。求最大收益。

// [#121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) Description: Best Time to Buy and Sell Stock | LeetCode OJ

解法1：贪婪。

// Solution 1: Greed is good.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0121_best-time-to-buy-and-sell-stock_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0121_best-time-to-buy-and-sell-stock_1_AC.cpp)

<hr>

#122 Best Time to Buy and Sell Stock II

// #122 最佳炒股时机2

描述：和之前一样，不过你可以买卖任意多次。

// [#122](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) Description: Best Time to Buy and Sell Stock II | LeetCode OJ

解法1：贪婪。

// Solution 1: Greed is good.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0122_best-time-to-buy-and-sell-stock-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0122_best-time-to-buy-and-sell-stock-ii_1_AC.cpp)

<hr>

#123 Best Time to Buy and Sell Stock III

// #123 最佳炒股时机3

描述：和之前一样，这次你至多能买卖两次。

// [#123](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) Description: Best Time to Buy and Sell Stock III | LeetCode OJ

解法1：把数组分成左右两部分考虑，每部分做一次交易。

// Solution 1: Split the array in two, one trade each.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0123_best-time-to-buy-and-sell-stock-iii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0123_best-time-to-buy-and-sell-stock-iii_1_AC.cpp)

<hr>

#124 Binary Tree Maximum Path Sum

// #124 二叉树最大路径和

描述：从二叉树任意节点出发，到任意节点终止。计算最大路径和。

// [#124](https://leetcode.com/problems/binary-tree-maximum-path-sum/) Description: Binary Tree Maximum Path Sum | LeetCode OJ

解法1：搜，不过要想清楚怎么搜，搜什么。

// Solution 1: DFS. Make sure you know how and what exactly you're searching.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0124_binary-tree-maximum-path-sum_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0124_binary-tree-maximum-path-sum_1_AC.cpp)

<hr>

#125 Valid Palindrome

// #125 判断回文串

描述：判断回文串，只检查字母，不分大小写。

// [#125](https://leetcode.com/problems/valid-palindrome/) Description: Valid Palindrome | LeetCode OJ

解法1：水题。

// Solution 1: Easy.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0125_valid-palindrome_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0125_valid-palindrome_1_AC.cpp)

<hr>

#126 Word Ladder II

// #126 单词接龙

描述：给定一个词典，一个起始词，一个终止词。要求每次只能变换一个字母，从起始词变到终止词。变化过程必须一直在词典里。求所有变换方法。

// [#126](https://leetcode.com/problems/word-ladder-ii/) Description: Word Ladder II | LeetCode OJ

解法1：我选择双向BFS，因为数据量比较大，分分钟超时。

// Solution 1: Bidirectional BFS is barely fast enough for large test cases, while normal BFS is not.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0126_word-ladder-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0126_word-ladder-ii_1_AC.cpp)

<hr>

#127 Word Ladder

// #127 单词接龙

描述：和之前一样，不过这次求的是变换序列的最短长度。

// [#127](https://leetcode.com/problems/word-ladder/) Description: Word Ladder | LeetCode OJ

解法1：BFS。有一点很重要，每次搜到的单词都应从词典里删除，这样能明显提高效率。

// Solution 1: BFS. Remove every word you reach from the dictionary, it matters a lot in running time.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0127_word-ladder_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0127_word-ladder_1_AC.cpp)

<hr>

#128 Longest Consecutive Sequence

// #128 最长连续序列

描述：给定一个数组，计算将其排序以后能形成的最长连续序列。

// [#128](https://leetcode.com/problems/longest-consecutive-sequence/) Description: Longest Consecutive Sequence | LeetCode OJ

解法1：使用哈希表记录区间，即使进行更新合并即可。

// Solution 1: Use a hash table to record intervals. Update and merge as needed.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0128_longest-consecutive-sequence_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0128_longest-consecutive-sequence_1_AC.cpp)

<hr>

#129 Sum Root to Leaf Numbers

// #129 根至叶求和

描述：水题懒得翻译。

// [#129](https://leetcode.com/problems/sum-root-to-leaf-numbers/) Description: Sum Root to Leaf Numbers | LeetCode OJ

解法1：懒得说。

// Solution 1: Etc.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0129_sum-root-to-leaf-numbers_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0129_sum-root-to-leaf-numbers_1_AC.cpp)

<hr>

#130 Surrounded Regions

// #130 包围区域

描述：给定矩形棋盘，将所有被X完全包围的O改为X。

// [#130](https://leetcode.com/problems/surrounded-regions/) Description: Surrounded Regions | LeetCode OJ

解法1：Floodfill。不用DFS也行。

// Solution 1: Floodfill. No need to do DFS.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0130_surrounded-regions_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0130_surrounded-regions_1_AC.cpp)

<hr>

#131 Palindrome Partitioning

// #131 回文划分

描述：将字符串划分为多个子串连接，使每个子串均为回文串。求所有划分方法。

// [#131](https://leetcode.com/problems/palindrome-partitioning/) Description: Palindrome Partitioning | LeetCode OJ

解法1：搜。

// Solution 1: DFS.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0131_palindrome-partitioning_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0131_palindrome-partitioning_1_AC.cpp)

<hr>

#132 Palindrome Partitioning II

// #132 回文划分2

描述：和之前一样，不过这次求的是最少能划分多少段。

// [#132](https://leetcode.com/problems/palindrome-partitioning-ii/) Description: Palindrome Partitioning II | LeetCode OJ

解法1：DP。

// Solution 1: DP.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0132_palindrome-partitioning-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0132_palindrome-partitioning-ii_1_AC.cpp)

<hr>

#133 Clone Graph

// #133 克隆图

描述：给定一个无向图的节点，克隆能克隆的一切。

// [#133](https://leetcode.com/problems/clone-graph/) Description: Clone Graph | LeetCode OJ

解法1：DFS。

// Solution 1: DFS.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0133_clone-graph_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0133_clone-graph_1_AC.cpp)

<hr>

#134 Gas Station

// #134 加油站

描述：给定一条环形路，上面有N个加油站。每个加油都有到达所需油量和可加油量。求能走完全程的出发站。

// [#134](https://leetcode.com/problems/gas-station/) Description: Gas Station | LeetCode OJ

解法1：贪婪。

// Solution 1: Be greedy

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0134_gas-station_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0134_gas-station_1_AC.cpp)

<hr>

#135 Candy

// #135 糖

描述：N个小朋友站一排，每个小朋友有个分数。要求比隔壁分数高的小朋友，拿糖要比隔壁多。问老师最少带多少个糖才够分。

// [#135](https://leetcode.com/problems/candy/) Description: Candy | LeetCode OJ

解法1：真尼玛唯分数论。

// Solution 1: Left to right, right to left.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0135_candy_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0135_candy_1_AC.cpp)

<hr>

#136 Single Number

// #136 孤独数

描述：数组里所有元素都出现两次，唯独一个数只出现一次，找出次数。

// [#136](https://leetcode.com/problems/single-number/) Description: Single Number | LeetCode OJ

解法1：异或。

// Solution 1: XOR.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0136_single-number_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0136_single-number_1_AC.cpp)

<hr>

#137 Single Number II

// #137 孤独数2

描述：和之前一样，不过这次其他元素都出现了3次。

// [#137](https://leetcode.com/problems/single-number-ii/) Description: Single Number II | LeetCode OJ

解法1：既然都出现了3次，那么“1”的个数必然是3的倍数。所以，只要看余数是0还是1就知道某一位上是0还是1了。一位一位地求就行了。

// Solution 1: Since every element appears three times, the number of "1"s must be multiple of three. Just we see the remainder mod 3. Be it 0 or 1, we know the oddbird bit by bit in this way.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0137_single-number-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0137_single-number-ii_1_AC.cpp)

<hr>

#138 Copy List with Random Pointer

// #138 复制带随机指针的链表

描述：给定一个链表，链表里有个random指针，指向链表里不知道哪个节点，或者指空。做一份硬拷贝。

// [#138](https://leetcode.com/problems/copy-list-with-random-pointer/) Description: Copy List with Random Pointer | LeetCode OJ

解法1：传统哈希做法，节点一一对应。

// Solution 1: Hash and clone.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0138_copy-list-with-random-pointer_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0138_copy-list-with-random-pointer_1_AC.cpp)

解法2：匪夷所思的O(1)空间解法，我想了俩钟头愣是搞出来了。

// Solution 2: Whimsical O(1) space solution, took me 2 hours to figure it out.

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0138_copy-list-with-random-pointer_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0138_copy-list-with-random-pointer_2_AC.cpp)

<hr>

#139 Word Break

// #139 单词分割

描述：给定一个长串S，将其分割成若干单词，要求单词必须在给定词典中。问能否成功分割。

// [#139](https://leetcode.com/problems/word-break/) Description: Word Break | LeetCode OJ

解法1： DP。

// Solution 1: DP.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0139_word-break_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0139_word-break_1_AC.cpp)

<hr>

#140 Word Break II

// #140 单词分割2

描述：和之前一样，但这次要求出所有可能的分割方式。

// [#140](https://leetcode.com/problems/word-break-ii/) Description: Word Break II | LeetCode OJ

解法1：基本思路显然是DFS，但数据量大了就需要各种优化手段，比如哈希、DP等等。

// Solution 1: When DFS alone isn't fast enough, accelerate it with DP, hashing, etc..

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0140_word-break-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0140_word-break-ii_1_AC.cpp)

<hr>

#141 Linked List Cycle

// #141 链表循环

描述：给定一个链表，判断是否有环。

// [#141](https://leetcode.com/problems/linked-list-cycle/) Description: Linked List Cycle | LeetCode OJ

解法1：追赶法。

// Solution 1: Run and run.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0141_linked-list-cycle_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0141_linked-list-cycle_1_AC.cpp)

解法2：哈希法。

// Solution 2: Hash and check.

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0141_linked-list-cycle_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0141_linked-list-cycle_2_AC.cpp)

<hr>

#142 Linked List Cycle II

// #142 链表循环2

描述：和之前一样，不过这次要找出循环的入口节点。

// [#142](https://leetcode.com/problems/linked-list-cycle-ii/) Description: Linked List Cycle II | LeetCode OJ

解法1：哈希法。

// Solution 1: Hash and check.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0142_linked-list-cycle-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0142_linked-list-cycle-ii_1_AC.cpp)

解法2：追赶法。

// Solution 2: Run and run.

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0142_linked-list-cycle-ii_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0142_linked-list-cycle-ii_2_AC.cpp)

<hr>

#143 Reorder List

// #143 重排链表

描述：按照头尾交替的方式重排一个链表。

// [#143](https://leetcode.com/problems/reorder-list/) Description: Reorder List | LeetCode OJ

解法1：注意边界条件。

// Solution 1: Mind the edge cases.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0143_reorder-list_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0143_reorder-list_1_AC.cpp)

<hr>

#144 Binary Tree Preorder Traversal

// #144 二叉树前序遍历

描述：如题。

// [#144](https://leetcode.com/problems/binary-tree-preorder-traversal/) Description: Binary Tree Preorder Traversal | LeetCode OJ

解法1：递归。

// Solution 1: Recursively.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0144_binary-tree-preorder-traversal_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0144_binary-tree-preorder-traversal_1_AC.cpp)

解法2：迭代。

// Solution 2: Iteratively.

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0144_binary-tree-preorder-traversal_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0144_binary-tree-preorder-traversal_2_AC.cpp)

<hr>

#145 Binary Tree Postorder Traversal

// #145 二叉树后序遍历

描述：如题。

// [#145](https://leetcode.com/problems/binary-tree-postorder-traversal/) Description: Binary Tree Postorder Traversal | LeetCode OJ

解法1：递归。

// Solution 1: Recursively.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0145_binary-tree-postorder-traversal_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0145_binary-tree-postorder-traversal_1_AC.cpp)

解法2：迭代。

// Solution 2: Iteratively.

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0145_binary-tree-postorder-traversal_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0145_binary-tree-postorder-traversal_2_AC.cpp)

<hr>

#146 LRU Cache

// #146 LRU缓存

描述：实现一个LRU缓存。

// [#146](https://leetcode.com/problems/lru-cache/) Description: LRU Cache | LeetCode OJ

解法1：哈希 + 双向链表。

// Solution 1: Hash + doubly linked list.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0146_lru-cache_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0146_lru-cache_1_AC.cpp)

解法2：双向链表用<list>。

// Solution 2: Use <list> as the doubly linked list.

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0146_lru-cache_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0146_lru-cache_2_AC.cpp)

<hr>

#147 Insertion Sort List

// #147 链表插入排序

描述：如题。

// [#147](https://leetcode.com/problems/insertion-sort-list/) Description: Insertion Sort List | LeetCode OJ

解法1：插呗。

// Solution 1: Do it.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0147_insertion-sort-list_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0147_insertion-sort-list_1_AC.cpp)

<hr>

#148 Sort List

// #148 链表排序

描述：如题。

// [#148](https://leetcode.com/problems/sort-list/) Description: Sort List | LeetCode OJ

解法1：归并排序。

// Solution 1: Merge sort.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0148_sort-list_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0148_sort-list_1_AC.cpp)

<hr>

#149 Max Points on a Line

// #149 多点共线

描述：给定二维平面上一些点，问最多多少个点共线

// [#149](https://leetcode.com/problems/max-points-on-a-line/) Description: Max Points on a Line | LeetCode OJ

解法1：对斜率进行哈希，不过斜率要用整数对表示，而不是浮点数。

// Solution 1: Hash the slope factors as integer pairs, not floating point numbers.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0149_max-points-on-a-line_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0149_max-points-on-a-line_1_AC.cpp)

<hr>

#150 Evaluate Reverse Polish Notation

// #150 逆波兰表达式求值

描述：如题。

// [#150](https://leetcode.com/problems/evaluate-reverse-polish-notation/) Description: Evaluate Reverse Polish Notation | LeetCode OJ

解法1：用栈。

// Solution 1: Use a stack.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0150_evaluate-reverse-polish-notation_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0150_evaluate-reverse-polish-notation_1_AC.cpp)

<hr>

#151 Reverse Words in a String

// #151 反转句中单词

描述：给定一句话，以单词为单位进行反转。

// [#151](https://leetcode.com/problems/reverse-words-in-a-string/) Description: Reverse Words in a String | LeetCode OJ

解法1：反转全句，反转每个词。

// Solution 1: Reverse the sentence, reverse the words.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0151_reverse-words-in-a-string_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0151_reverse-words-in-a-string_1_AC.cpp)

<hr>

#152 Maximum Product Subarray

// #152 最大乘积子数组

描述：给定一个整数数组，求子数组的最大乘积。

// [#152](https://leetcode.com/problems/maximum-product-subarray/) Description: Maximum Product Subarray | LeetCode OJ

解法1：这题有意思，因为元素都是整数，所以只要不是0，乘积的绝对值只会越变越大。这就造成了一个规律：乘积要么是最大值，要么是最小值，总在两极。于是我们持续关注两极即可。倘若存在[0, 1)间的小数，这做法就不成立了。不过，你应该会想到，用log函数可以转化问题吧？

// Solution 1: An interesting problem. As the elements are all integers, if not encountering 0, the absolute value of the product will continue to increase. Thus the product is either min or max. By keeping watch over both ends, we have the maximum product of subarrays. This holds only for integers. Given elements between [0, 1), the product could shrink. Still, using log() to convert the problem is obviously a feasible method, just know that the 0s are to be skipped.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0152_maximum-product-subarray_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0152_maximum-product-subarray_1_AC.cpp)

<hr>

#153 Find Minimum in Rotated Sorted Array

// #153 旋转有序数组最小值

描述：给定循环移位过的有序数组，求最小值。

// [#153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) Description: Find Minimum in Rotated Sorted Array | LeetCode OJ

解法1：二分

// Solution 1: Binary search.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0153_find-minimum-in-rotated-sorted-array_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0153_find-minimum-in-rotated-sorted-array_1_AC.cpp)

<hr>

#154 Find Minimum in Rotated Sorted Array II

// #154 旋转数组最小元素2

描述：和之前一样，这次元素可能有重复。

// [#154](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/) Description: Find Minimum in Rotated Sorted Array II | LeetCode OJ

解法1：二分。

// Solution 1: Binary search.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0154_find-minimum-in-rotated-sorted-array-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0154_find-minimum-in-rotated-sorted-array-ii_1_AC.cpp)

<hr>

#155 Min Stack

// #155 最小栈

描述：设计一个栈，能随时返回当前栈中的最小元素。

// [#155](https://leetcode.com/problems/min-stack/) Description: Min Stack | LeetCode OJ

解法1：额外维护一个最小栈，栈顶总是放着当前栈中的最小值。于是这个栈是单调的，你说对吗？

// Solution 1: Maintain an extra min stack, whose top is always the minimum of elements in stack. This "min stack" is obviously monotonous, right?

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0155_min-stack_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0155_min-stack_1_AC.cpp)

<hr>

#156 Binary Tree Upside Down

// #156 颠倒二叉树

描述：把一棵二叉树，上下颠倒。一两句话讲不清楚。

// [#156](https://leetcode.com/problems/binary-tree-upside-down/) Description: Binary Tree Upside Down | LeetCode OJ

解法1：循环可以搞定，题目也不算难。不过这代码很容易写错。很考验人的思维缜密程度。

// Solution 1: This problem can be solved without recursion, not so difficult. But it's easy to write sloppy code. A perfect kill is very challenging.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0156_binary-tree-upside-down_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0156_binary-tree-upside-down_1_AC.cpp)

<hr>

#157 Read N Characters Given Read4

// #157 用Read4读取N个字符

描述：从前有个API叫read4，能用来读4个字符。请用其读取N个字符。

// [#157](https://leetcode.com/problems/read-n-characters-given-read4/) Description: Read N Characters Given Read4 | LeetCode OJ

解法1：凡是不涉及算法的题，都应小心行事。

// Solution 1: If it's not about algorithms, it's about discreetness.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0157_read-n-characters-given-read4_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0157_read-n-characters-given-read4_1_AC.cpp)

<hr>

#158 Read N Characters Given Read4 II - Call multiple times

// #158 用Read4读取N个字符2 - 调用多次

描述：和之前一样，但这次你的API可能要调用多次。

// [#158](https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/) Description: Read N Characters Given Read4 II - Call multiple times | LeetCode OJ

解法1：既然要调用多次，那么关键就在于对结尾几个字符的处理了。聪明人会尽量少用if else。

// Solution 1: The key is the vey few left-over characters at the tail. A smart brain won't tolerate a whole bunch of "if-else"s.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0158_read-n-characters-given-read4-ii-call-multiple-times_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0158_read-n-characters-given-read4-ii-call-multiple-times_1_AC.cpp)

<hr>

#159 Longest Substring with At Most Two Distinct Characters

// #159 至多包含两种字符的最长子串

描述：给定字符串，找出至多包含两种字符的最长子串。

// [#159](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/) Description: Longest Substring with At Most Two Distinct Characters | LeetCode OJ

解法1：俩指针，一个计数器。

// Solution 1: Two pointers and one counter.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0159_longest-substring-with-at-most-two-distinct-characters_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0159_longest-substring-with-at-most-two-distinct-characters_1_AC.cpp)

<hr>

#160 Intersection of Two Linked Lists

// #160 两链表交点

描述：给定两个链表，可能相交于某节点。请找出此节点。

// [#160](https://leetcode.com/problems/intersection-of-two-linked-lists/) Description: Intersection of Two Linked Lists | LeetCode OJ

解法1：用哈希表来判断重复。

// Solution 1: Detect duplicates with a hash table.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0160_intersection-of-two-linked-lists_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0160_intersection-of-two-linked-lists_1_AC.cpp)

解法2：这么奇怪的解法，居然是我亲手写的。

// Solution 2: I don't quite understand how I wrote such a weird solution.

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0160_intersection-of-two-linked-lists_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0160_intersection-of-two-linked-lists_2_AC.cpp)

解法3：想想“最近公共祖先”问题。

// Solution 3: Think about the LCA problem.

[代码3](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0160_intersection-of-two-linked-lists_3_AC.cpp)

// [Code 3](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0160_intersection-of-two-linked-lists_3_AC.cpp)

<hr>

#161 One Edit Distance

// #161 编辑距离为一

描述：给定两个字符串，判断其编辑距离是否为1。

// [#161](https://leetcode.com/problems/one-edit-distance/) Description: One Edit Distance | LeetCode OJ

解法1：按定义来。

// Solution 1: By the book.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0161_one-edit-distance_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0161_one-edit-distance_1_AC.cpp)

<hr>

#162 Find Peak Element

// #162 找出峰值

描述：给定一个数组，找出大于其左右邻居的元素，一个就好。假定，数组的两边界都是负无穷。

// [#162](https://leetcode.com/problems/find-peak-element/) Description: Find Peak Element | LeetCode OJ

解法1：从头到尾扫一遍即可，O(N)时间。

// Solution 1: Run a scan in O(N) time.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0162_find-peak-element_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0162_find-peak-element_1_AC.cpp)

解法2：二分搜索。如果一个条件你要写很多次，就用bool变量记下来。

// Solution 2: Binary search. Replace repetitive conditions with a boolean variable.

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0162_find-peak-element_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0162_find-peak-element_2_AC.cpp)

<hr>

#163 Missing Ranges

// #163 缺失范围

描述：给定一个区间和一堆数。统计一下在此区间有哪些数没在数组中出现，结果用区间表示。

// [#163](https://leetcode.com/problems/missing-ranges/) Description: Missing Ranges | LeetCode OJ

解法1：注意各种边界条件。

// Solution 1: Mind all kinds of edge cases.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0163_missing-ranges_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0163_missing-ranges_1_AC.cpp)

<hr>

#164 Maximum Gap

// #164 最大间隙

描述：给定无序数组，求出给数组排序后，相邻元素的最大差值。

// [#164](https://leetcode.com/problems/maximum-gap/) Description: Maximum Gap | LeetCode OJ

解法1：思路类似桶排序，考虑相邻两个桶的最大值和最小值。

// Solution 1: Similar to bucket sort. Think about the min and max of each bucket.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0164_maximum-gap_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0164_maximum-gap_1_AC.cpp)

<hr>

#165 Compare Version Numbers

// #165 比较版本号

描述：比较俩版本号，看谁更新。

// [#165](https://leetcode.com/problems/compare-version-numbers/) Description: Compare Version Numbers | LeetCode OJ

解法1：字典序。

// Solution 1: Lexicographically.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0165_compare-version-numbers_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0165_compare-version-numbers_1_AC.cpp)

<hr>

#166 Fraction to Recurring Decimal

// #166 分数转小数

描述：分数转小数，要求能处理循环小数。

// [#166](https://leetcode.com/problems/fraction-to-recurring-decimal/) Description: Fraction to Recurring Decimal | LeetCode OJ

解法1：需要一个数组或者哈希表，来记录每一个余数对应的位置。为什么要关心余数？因为你要判断循环节，还需要记录下一个完整的循环节。

// Solution 1: We need an array or a hash table to record the appearing index of every remainder. Why care about this? Because we need to detect if there is an repetend and record it if so.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0166_fraction-to-recurring-decimal_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0166_fraction-to-recurring-decimal_1_AC.cpp)

<hr>

#167 Two Sum II - Input array is sorted

// #167 二数之和2 - 数组有序

描述：给定有序数组和一个值，求是否有两数加起来等于该值，返回下标。

// [#167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) Description: Two Sum II - Input array is sorted | LeetCode OJ

解法1：既然数组有序，俩指针搞定。

// Solution 1: Since the array is sorted already, let the two pointers get to work.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0167_two-sum-ii-input-array-is-sorted_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0167_two-sum-ii-input-array-is-sorted_1_AC.cpp)

<hr>

#168 Excel Sheet Column Title

// #168 Excel工作表列标号

描述：Excel用过吧？给出其列标号的转换算法，数字转字符串。

// [#168](https://leetcode.com/problems/excel-sheet-column-title/) Description: Excel Sheet Column Title | LeetCode OJ

解法1：转呗。

// Solution 1: Do it.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0168_excel-sheet-column-title_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0168_excel-sheet-column-title_1_AC.cpp)

<hr>

#169 Majority Element

// #169 众数

描述：找出元素中出现次数超过一半的元素。这个可以有。

// [#169](https://leetcode.com/problems/majority-element/) Description: Majority Element | LeetCode OJ

解法1：Boyer-Moore投票算法。

// Solution 1: Boyer-Moore Voting Algorithm.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0169_majority-element_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0169_majority-element_1_AC.cpp)

<hr>

#170 Two Sum III - Data structure design

// #170 两数之和3 - 数据结构设计

描述：设计一个数据结构，能像其中添加数，能查找其中是否存在两数相加等于某值。

// [#170](https://leetcode.com/problems/two-sum-iii-data-structure-design/) Description: Two Sum III - Data structure design | LeetCode OJ

解法1：用一个数组，每次插入元素都保证有序。查找时就采用Two Sum的策略。两种操作都是O(N)时间。中规中矩的解法。

// Solution 1: Maintain a sorted array for all inserted elements. The queries can be done in the same way as Two Sum. Both operations are O(N) time. Fair enough, no surprise.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0170_two-sum-iii-data-structure-design_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0170_two-sum-iii-data-structure-design_1_AC.cpp)

<hr>

#171 Excel Sheet Column Number

// #171 Excel工作表列标号

描述：和之前一样，不过这次是字符串转数字。

// [#171](https://leetcode.com/problems/excel-sheet-column-number/) Description: Excel Sheet Column Number | LeetCode OJ

解法1：转呗。

// Solution 1: Do it.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0171_excel-sheet-column-number_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0171_excel-sheet-column-number_1_AC.cpp)

<hr>

#172 Factorial Trailing Zeroes

// #172 阶乘尾0个数

描述：N的阶乘尾巴上有多少个0？

// [#172](https://leetcode.com/problems/factorial-trailing-zeroes/) Description: Factorial Trailing Zeroes | LeetCode OJ

解法1：0的个数等于2x5的个数，等于5的个数。

// Solution 1: The number of trailing zeroes equals the number of 2 x 5s, equals the number of 5s.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0172_factorial-trailing-zeroes_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0172_factorial-trailing-zeroes_1_AC.cpp)

<hr>

#173 Binary Search Tree Iterator

// #173 二叉搜索树迭代器

描述：就是中序遍历，要求写成迭代器的形式。

// [#173](https://leetcode.com/problems/binary-search-tree-iterator/) Description: Binary Search Tree Iterator | LeetCode OJ

解法1：中序遍历，不准递归。

// Solution 1: Inorder traversal, no recursion.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0173_binary-search-tree-iterator_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0173_binary-search-tree-iterator_1_AC.cpp)

<hr>

#174 Dungeon Game

// #174 地牢游戏

描述：纪念早期的文字RPG游戏Dungeon。给定一个矩阵型的地牢，王子，有血瓶有怪有空地。问王子能否营救公主，并求出能成功营救的最小HP值。

// [#174](https://leetcode.com/problems/dungeon-game/) Description: Dungeon Game | LeetCode OJ

解法1：看代码。尝试逆向思维。

// Solution 1: Read the code. Try thinking backwards.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0174_dungeon-game_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0174_dungeon-game_1_AC.cpp)

<hr>

#179 Largest Number

// #179 最大数

描述：给定一堆数，以适当顺序将它们连一块儿形成最大的数。

// [#179](https://leetcode.com/problems/largest-number/) Description: Largest Number | LeetCode OJ

解法1：适当排序即可。

// Solution 1: Sort the array in the right way.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0179_largest-number_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0179_largest-number_1_AC.cpp)

<hr>

#186 Reverse Words in a String II

// #186 按词反转句子2

描述：如题。

// [#186](https://leetcode.com/problems/reverse-words-in-a-string-ii/) Description: Reverse Words in a String II | LeetCode OJ

解法1：木有鼠么不同。——曲婉婷

// Solution 1: Anything different?

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0186_reverse-words-in-a-string-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0186_reverse-words-in-a-string-ii_1_AC.cpp)

<hr>

#187 Repeated DNA Sequences

// #187 重复DNA序列

描述：DNA序列里有ATCG四种碱基，求所有长度为10，出现此处超过一次的序列。

// [#187](https://leetcode.com/problems/repeated-dna-sequences/) Description: Repeated DNA Sequences | LeetCode OJ

解法1：哈希大法好。

// Solution 1: String hashing rocks.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0187_repeated-dna-sequences_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0187_repeated-dna-sequences_1_AC.cpp)

<hr>

#188 Best Time to Buy and Sell Stock IV

// #188 最佳炒股时间4

描述：给定股价，你最多可以进行k次交易。

// [#188](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/) Description: Best Time to Buy and Sell Stock IV | LeetCode OJ

解法1：非常典型的动态规划问题。由k次交易，自然会想到k - 1次交易。由“至多”，自然会想到局部最优和全局最优之间的相互关联。能理清这两件事，代码就能写利索了。

// Solution 1: A typical DP problem. Calculating the profits after k transactions requires the results from k - 1 transactions. Since we can do "at most" k transactions, you'll have to figure out the link between global and local optimals before coding. Here is a version without space optimization.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0188_best-time-to-buy-and-sell-stock-iv_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0188_best-time-to-buy-and-sell-stock-iv_1_AC.cpp)

解法2：空间优化为O(N)。

// Solution 2: Space optimized to O(N).

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0188_best-time-to-buy-and-sell-stock-iv_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0188_best-time-to-buy-and-sell-stock-iv_2_AC.cpp)

<hr>

#189 Rotate Array

// #189 旋转数组

描述：把数组循环移位。

// [#189](https://leetcode.com/problems/rotate-array/) Description: Rotate Array | LeetCode OJ

解法1：反转再反转。

// Solution 1: Reverse and reverse.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0189_rotate-array_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0189_rotate-array_1_AC.cpp)

<hr>

#190 Reverse Bits

// #190 反转二进制位

描述：给定32位整数，按位反转。

// [#190](https://leetcode.com/problems/reverse-bits/) Description: Reverse Bits | LeetCode OJ

解法1：水题。

// Solution 1: Easy.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0190_reverse-bits_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0190_reverse-bits_1_AC.cpp)

解法2：4位一起搞。

// Solution 2: 4 bits at a time.

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0190_reverse-bits_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0190_reverse-bits_2_AC.cpp)

<hr>

#191 Number of 1 Bits

// #191 1的个数

描述：求一个数二进制表示中1的个数。

// [#191](https://leetcode.com/problems/number-of-1-bits/) Description: Number of 1 Bits | LeetCode OJ

解法1：lowbit。

// Solution 1: lowbit.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0191_number-of-1-bits_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0191_number-of-1-bits_1_AC.cpp)

<hr>

#198 House Robber

// #198 小偷

描述：给定一个小偷和一排房子。偷了相邻俩屋子就会被抓，问咋偷最来钱。

// [#198](https://leetcode.com/problems/house-robber/) Description: House Robber | LeetCode OJ

解法1：什么破房子，还有这鸟规矩。

// Solution 1: Funny problem.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0198_house-robber_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0198_house-robber_1_AC.cpp)

<hr>

#199 Binary Tree Right Side View

// #199 二叉树右视图

描述：从右边看一棵二叉树。

// [#199](https://leetcode.com/problems/binary-tree-right-side-view/) Description: Binary Tree Right Side View | LeetCode OJ

解法1：水平遍历，只要每层最后一个。

// Solution 1: Level-order traversal. Keep only the last one on each level.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0199_binary-tree-right-side-view_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0199_binary-tree-right-side-view_1_AC.cpp)

解法1：其实随便怎么遍历都行，只要从左向右就行。

// Solution 1: Traverse whatever way you like, just from left to right.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0199_binary-tree-right-side-view_2_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0199_binary-tree-right-side-view_2_AC.cpp)

<hr>

#200 Number of Islands

// #200 岛屿个数

描述：给定01矩阵，求1构成的4-邻接连通分量个数。

// [#200](https://leetcode.com/problems/number-of-islands/) Description: Number of Islands | LeetCode OJ

解法1：DFS。

// Solution 1: DFS.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0200_number-of-islands_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0200_number-of-islands_1_AC.cpp)
