#401 Binary Watch

// #401 二进制手表

描述：有一个手表，假设小时范围是0~11，分钟范围是0~59。如果时和分的二级制表示总共有N个1，求所有可能的时间。

// [#401](https://leetcode.com/problems/binary-watch/) Description: Binary Watch | LeetCode OJ

解法1：水题。

// Solution 1: Easy.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0401_binary-watch_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0401_binary-watch_1_AC.cpp)

<hr>

#402 Remove K Digits

// #402 移除K个数字

描述：给定一个数字串，从中删除K个数字，使得剩下的数最小。

// [#402](https://leetcode.com/problems/remove-k-digits/) Description: Remove K Digits | LeetCode OJ

解法1：你可以一位一位地删，但这么干时间复杂度就是O(N^2)。你也可以一位位不停地删，区别在哪儿？就在于“局部性”三个字。虽然最坏时间复杂度还是O(N ^ 2)，但平均起来则是O(N)，性能明显提高了。

// Solution 1: You can remove the digits one by one, which results in a total of O(N ^ 2) time. You can also remove them in a row. The difference lies in "locality", here it means spatial locality. Although the worst case stays in O(N ^ 2), the average case is improved to O(N), good progress indeed.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0402_remove-k-digits_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0402_remove-k-digits_1_AC.cpp)

<hr>

#403 Frog Jump

// #403 青蛙跳

描述：一只青蛙站在0点，有一些石头分布在前面。第一步必须跳1格，之后每步距离可以比上一步多1或少1。只能跳石头上，不能掉水里。问能否成功跳到最后一颗石头上。

// [#403](https://leetcode.com/problems/frog-jump/) Description: Frog Jump | LeetCode OJ

解法1：从数据范围看，我猜是个O(N ^ 2)的问题。于是我选择BFS。为什么不用DP？因为DP的代码写起来也未必多简洁。

// Solution 1: Judging from the number of stones, I think O(N ^ 2) is tolerable. Thus I chose BFS. Why not DP instead. With the constraints in the jumping distance, I don't think using DP can make your code any cleaner.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0403_frog-jump_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0403_frog-jump_1_AC.cpp)

<hr>

#404 Sum of Left Leaves

// #404 左叶子之和

描述：给定二叉树，求左叶节点之和。

// [#404](https://leetcode.com/problems/sum-of-left-leaves/) Description: Sum of Left Leaves | LeetCode OJ

解法1：水题。

// Solution 1: Piece of date cake.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0404_sum-of-left-leaves_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0404_sum-of-left-leaves_1_AC.cpp)

<hr>

#405 Convert a Number to Hexadecimal

// #405 十进制转十六进制

描述：如题。

// [#405](https://leetcode.com/problems/convert-a-number-to-hexadecimal/) Description: Convert a Number to Hexadecimal | LeetCode OJ

解法1：碰见负数怎么办？看着办。

// Solution 1: What about negative numbers? What about it.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0405_convert-a-number-to-hexadecimal_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0405_convert-a-number-to-hexadecimal_1_AC.cpp)

<hr>

#406 Queue Reconstruction by Height

// #406 按高度重建队列

描述： 有N个人排成一条队。现在给你每个人的高度，以及站他前面不比他矮的人的个数。请把整个队列重建出来。

// [#406](https://leetcode.com/problems/queue-reconstruction-by-height/) Description: Queue Reconstruction by Height | LeetCode OJ

解法1：直接看代码吧。注意两点，第一是排序方式，第二是插入方式。

// Solution 1: Just read the code. Two points worth noting, one is the sorting comparator, one is the insertion process.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0406_queue-reconstruction-by-height_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0406_queue-reconstruction-by-height_1_AC.cpp)

解法2：这个解法很巧妙，我鼓捣了一个多钟头才想明白。首先，这题除了O(N ^ 2)的暴力解法，肯定有更高效的解法。为什么？因为这是个关于“排序”的问题，你们都知道O(N * logN)是比较排序的下界。而且这题涉及到了数数。所以，我决定用树状数组试试，结果还真搞出来了。虽然实际复杂度不是O(N * logN)，而是O(N * log ^2 N)。但总体的思想，还是二分搜索。用树状数组，只是为了区间求和。

// Solution 2: This is a clever solution. (I'm not saying it's a short solution.) Took me more than an hour to figure out. First of all, I believed there's a better solution to this problem than an O(N ^ 2) brute-force one. Because it's about "order", and you know there's a lower bound of O(N * logN) for any comparative sorting algorithm. This problem also involved counting, which led me to BIT. It worked, as expected. The overall time complexity is actually O(N * log ^ 2 N) instead of O(N * logN), due to the binary search in a BIT. Using a BIT here is because I need range summation.

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0406_queue-reconstruction-by-height_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0406_queue-reconstruction-by-height_2_AC.cpp)

<hr>

#407 Trapping Rain Water II

// #407 雨水积水问题

描述：跟之前一样，但这次的地形是二维的。

// [#407](https://leetcode.com/problems/trapping-rain-water-ii/) Description: Trapping Rain Water II | LeetCode OJ

解法1：首先，你不能像之前一样，还用几层for循环搞定。因为水只往低处流，不管东西南北，而for循环的方向，总是固定的。那怎么办呢？BFS。

// Solution 1: First, you can't get it done with just a few nested for-loops. Because water flows downhill, no matter which direction it might be, while the direction inside a for-loop is pre-defined. So how do we deal with it? BFS.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0407_trapping-rain-water-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0407_trapping-rain-water-ii_1_AC.cpp)

<hr>

#408 Valid Word Abbreviation

// #408 合法单词缩写

描述：给定一个单词，允许把其中一个或多个部分替换成对应长度，但替换的部分不能相邻。先给定一个单词和一个对应缩写，判断缩写是否合法。

// [#408](https://leetcode.com/problems/valid-word-abbreviation/) Description: Valid Word Abbreviation | LeetCode OJ

解法1：水题。

// Solution 1: Trivial.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0408_valid-word-abbreviation_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0408_valid-word-abbreviation_1_AC.cpp)

<hr>

#409 Longest Palindrome

// #409 最长回文串

描述：给定一个串，允许从其中选一些字母，问能拼成的最长回文串有多长？

// [#409](https://leetcode.com/problems/longest-palindrome/) Description: Longest Palindrome | LeetCode OJ

解法1：不是判断回文子串，水题。

// Solution 1: This is not palindromic substring. Piece of zaogao.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0409_longest-palindrome_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0409_longest-palindrome_1_AC.cpp)

<hr>

#410 Split Array Largest Sum

// #410 分割子数组最大和

描述：给定一个数组，要求分割为M段，求其中最大子数组和的最小值。

// [#410](https://leetcode.com/problems/split-array-largest-sum/) Description: Split Array Largest Sum | LeetCode OJ

解法1：要求最大值最小，这种问题是算法中经常研究的问题。决策理论里不也有Minimax问题么。因为这题是分割子数组，所以可以用DP搞定。那么，如果是分成M堆，不要求元素连续的话，又当如何求解？那就是集装箱问题喽，谁爱做谁做。

// Solution 1: To minimize the maximum, these sort of problems are widely studied in computer science. Isn't there something called "Minimax" in Decision Thoery, for instance? As this problem is about splitting subarrays, we can do it with DP. Say, if the problem is about partitioning the set into M subsets. What do we do? I guess it's then a combinatorial problem, anyway, not mine to worry about.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0410_split-array-largest-sum_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0410_split-array-largest-sum_1_AC.cpp)

解法2：省点空间。

// Solution 2:  Save some space, for the rainy days.

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0410_split-array-largest-sum_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0410_split-array-largest-sum_2_AC.cpp)

<hr>

#411 Minimum Unique Word Abbreviation

// #411 最短唯一单词缩写

描述：按照之前给定的缩写规则，现在给你一个词和一个词典。为该词找一个长度最短的缩写，要求该缩写不能和词典里的其他单词对上号儿。

// [#411](https://leetcode.com/problems/minimum-unique-word-abbreviation/) Description: Minimum Unique Word Abbreviation | LeetCode OJ

解法1：首先，基本思路就是搜。怎么搜呢？随便，反正代码都挺难看的。重要的是，怎么判断一个缩写是否和词典里的缩写发生重合呢？请看markBit函数。

// Solution 1: Firstly, this is about DFS. How? Doesn't matter. The code can't possibly look any better. What really matters is the way we check if an abbreviation collides with one in the dictionary. See markBit() for more details.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0411_minimum-unique-word-abbreviation_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0411_minimum-unique-word-abbreviation_1_AC.cpp)

<hr>

#412 Fizz Buzz

// #412 报数

描述：从1~N依次报数，3的倍数说Fizz，5的倍数说Buzz，15的倍数说FizzBuzz。

// [#412](https://leetcode.com/problems/fizz-buzz/) Description: Fizz Buzz | LeetCode OJ

解法1：水题。

// Solution 1: Most trivial.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0412_fizz-buzz_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0412_fizz-buzz_1_AC.cpp)

<hr>

#413 Arithmetic Slices

// #413 等差数列片段

描述：给定数组，找出最长的满足等差数列条件的子数组长度。

// [#413](https://leetcode.com/problems/arithmetic-slices/) Description: Arithmetic Slices | LeetCode OJ

解法1：水题。

// Solution 1: Easy.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0413_arithmetic-slices_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0413_arithmetic-slices_1_AC.cpp)

<hr>

#414 Third Maximum Number

// #414 第三大的数

描述：给定一个数组，找出第三大的数。

// [#414](https://leetcode.com/problems/third-maximum-number/) Description: Third Maximum Number | LeetCode OJ

解法1：水题。

// Solution 1: Easy.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0414_third-maximum-number_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0414_third-maximum-number_1_AC.cpp)

<hr>

#415 Add Strings

// #415 高精度加法

描述：如题。

// [#415](https://leetcode.com/problems/add-strings/) Description: Add Strings | LeetCode OJ

解法1：水题。

// Solution 1: Easy.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0415_add-strings_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0415_add-strings_1_AC.cpp)

<hr>

#416 Partition Equal Subset Sum

// #416 平分集合

描述：给定一堆数，判断能否分为两堆，使得两堆的和相等。

// [#416](https://leetcode.com/problems/partition-equal-subset-sum/) Description: Partition Equal Subset Sum | LeetCode OJ

解法1：背包问题。

// Solution 1: Knapsack Problem.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0416_partition-equal-subset-sum_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0416_partition-equal-subset-sum_1_AC.cpp)

<hr>

#417 Pacific Atlantic Water Flow

// #417 太平洋大西洋水流

描述：给定mxn矩阵，左上挨着太平洋，右下挨着大西洋。已知水能流向等高或者更低的地方。 请找出所有两大洋的位置。

// [#417](https://leetcode.com/problems/pacific-atlantic-water-flow/) Description: Pacific Atlantic Water Flow | LeetCode OJ

解法1：搜。

// Solution 1: Flood it.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0417_pacific-atlantic-water-flow_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0417_pacific-atlantic-water-flow_1_AC.cpp)

<hr>

#418 Sentence Screen Fitting

// #418 屏幕文字填充

描述：给定一句话，和一个尺寸固定的屏幕。单词之间至少要用一个空格分割，行尾的空格可以省略。求这句话能在屏幕里完整重复多少次。

// [#418](https://leetcode.com/problems/sentence-screen-fitting/) Description: Sentence Screen Fitting | LeetCode OJ

解法1：网上有的解法， 是找循环节。我觉得这办法虽然可行，但会存在bad case，使得复杂度接近O(N ^ 2)。于是我琢磨了个二分搜索的办法。对于屏幕上的每一行，每一次都通过二分查找，尽量填充到行尾，然后换行。

// Solution 1: Some of the solutions from the Internet focus on determining the length of the cycle. This is a feasible, but vulnerable one, as there might be bad cases that lead to an O(N ^ 2) running time. Mine here is devised from the idea of binary search. For each line, fill as many words as you can with one binary search and go to the next.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0418_sentence-screen-fitting_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0418_sentence-screen-fitting_1_AC.cpp)

<hr>

#419 Battleships in a Board

// #419 棋盘上的战舰

描述：棋盘上有一些战舰，都是横平竖直的，而且相互不接触。求总共有多少条。

// [#419](https://leetcode.com/problems/battleships-in-a-board/) Description: Battleships in a Board | LeetCode OJ

解法1：O(1)空间，很好。

// Solution 1: O(1) space, good.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0419_battleships-in-a-board_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0419_battleships-in-a-board_1_AC.cpp)

<hr>

#420 Strong Password Checker

// #420 高安全性密码检查

描述：给定一个密码字符串，要求通过最少的“编辑”（还记得最短编辑距离吗？）使密码具有高安全性。怎么才算安全呢，第一长度要6~20，第二要有大写有小写有数字，第三连续重复字母不能达到3个。

// [#420](https://leetcode.com/problems/strong-password-checker/) Description: Strong Password Checker | LeetCode OJ

解法1：难题。这题搞了我将近两个钟头，所以我一句都不想说。面试碰见这种题，你就认倒霉吧。

// Solution 1: A hard problem. It took me almost two hours to get it done. Too tired to say a word. Just pray you don't meet it in a real battle, because chances are that you're gonna be f*ed up.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0420_strong-password-checker_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0420_strong-password-checker_1_AC.cpp)

<hr>

#421 Maximum XOR of Two Numbers in an Array

// #421 俩数组元素异或的最大值

描述：如题。

// [#421](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) Description: Maximum XOR of Two Numbers in an Array | LeetCode OJ

解法1：暴力解法就不说了。这个解法不是我想出来的，非常精妙。

// Solution 1: Brute-force solution is trivial. This one here is not by me, very clever and concise.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0421_maximum-xor-of-two-numbers-in-an-array_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0421_maximum-xor-of-two-numbers-in-an-array_1_AC.cpp)

<hr>

#422 Valid Word Square

// #422 有效字母方阵

描述：给定几排字符串，判断是不是按对角线对称的。

// [#422](https://leetcode.com/problems/valid-word-square/) Description: Valid Word Square | LeetCode OJ

解法1：注意边界。

// Solution 1: Mind the edge.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0422_valid-word-square_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0422_valid-word-square_1_AC.cpp)

<hr>

#423 Reconstruct Original Digits from English

// #423 根据英语重建数字串

描述：给定一个数字串，把它用英语说出来，然后字母全连一块儿，再打乱顺序。现在给你这个乱序的字母串，把数字串重建出来。

// [#423](https://leetcode.com/problems/reconstruct-original-digits-from-english/) Description: Reconstruct Original Digits from English | LeetCode OJ

解法1：介尼玛是个脑筋急转弯，嘛玩意儿。

// Solution 1: I got a name for problems like this: brain teasers.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0423_reconstruct-original-digits-from-english_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0423_reconstruct-original-digits-from-english_1_AC.cpp)

<hr>

#424 Longest Repeating Character Replacement

// #424 替换后的最长重复子串

描述：给定一个字符串，允许你任选最多K个字符进行任意替换。问替换以后，能得到的包含同一字母的子串最长能有多长？

// [#424](https://leetcode.com/problems/longest-repeating-character-replacement/) Description: Longest Repeating Character Replacement | LeetCode OJ

解法1：还是俩指针。这种最长XX子串问题都见了一堆了，还有多少个？

// Solution 1: Still two pointers. I've seen enough of these problems, just how many more to go?

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0424_longest-repeating-character-replacement_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0424_longest-repeating-character-replacement_1_AC.cpp)

<hr>

#425 Word Squares

// #425 单词方阵

描述：给定一堆长度相同的单词，从中选出一些构成方阵，要求方阵依对角线对称。求出所有可能的方阵。

// [#425](https://leetcode.com/problems/word-squares/) Description: Word Squares | LeetCode OJ

解法1：题目虽然不简单，但思路倒是很简单，搜呗。

// Solution 1: The problem is rated "hard", but the solution is simple. Run a DFS.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0425_word-squares_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0425_word-squares_1_AC.cpp)

<hr>

#432 All O`one Data Structure

// #432 全O(1)数据结构

描述：设计一个类似hash map的计数器，但要提供最大值对应键值、最小值对应键值的功能。

// [#432](https://leetcode.com/problems/all-oone-data-structure/) Description: All O&amp;#x60;one Data Structure | LeetCode OJ

解法1：哈希表 + 双向链表，想想都觉得麻烦。碰见这种破题，面试能给多长时间？药丸。

// Solution 1: Hash table + doubly linked list, the very thought is tiring enough. How long do you think you can spare for this one?

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0432_all-oone-data-structure_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0432_all-oone-data-structure_1_AC.cpp)

<hr>

#434 Number of Segments in a String

// #434 单词个数

描述：给个句子，数词儿。

// [#434](https://leetcode.com/problems/number-of-segments-in-a-string/) Description: Number of Segments in a String | LeetCode OJ

解法1：水题。

// Solution 1: Trivial.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0434_number-of-segments-in-a-string_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0434_number-of-segments-in-a-string_1_AC.cpp)

<hr>

#435 Non-overlapping Intervals

// #435 不重合区间

描述：给定一堆区间，进行适当合并，使结果互不重叠。紧邻不算重合。

// [#435](https://leetcode.com/problems/non-overlapping-intervals/) Description: Non-overlapping Intervals | LeetCode OJ

解法1：DP。

// Solution 1: DP.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0435_non-overlapping-intervals_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0435_non-overlapping-intervals_1_AC.cpp)

解法2：贪婪。

// Solution 2: Be greedy.

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0435_non-overlapping-intervals_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0435_non-overlapping-intervals_2_AC.cpp)

<hr>

#436 Find Right Interval

// #436 找右区间

描述：给定一系列区间，对每个区间，找出其右侧（不是下标，而是区间值）最近的区间。

// [#436](https://leetcode.com/problems/find-right-interval/) Description: Find Right Interval | LeetCode OJ

解法1：先排序，后二分。

// Solution 1: Sort and binary search.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0436_find-right-interval_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0436_find-right-interval_1_AC.cpp)

<hr>

#437 Path Sum III

// #437 路径和3

描述：给定一棵二叉树，允许从任意点出发，到任意点为止，但要求必须从上往下走。对于给定的值target，求路径和等于target的路径有多少条？

// [#437](https://leetcode.com/problems/path-sum-iii/) Description: Path Sum III | LeetCode OJ

解法1：搜。

// Solution 1: Traverse it.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0437_path-sum-iii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0437_path-sum-iii_1_AC.cpp)

解法2：加个缓存。

// Solution 2: Cache it.

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0437_path-sum-iii_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0437_path-sum-iii_2_AC.cpp)

<hr>

#438 Find All Anagrams in a String

// #438 找出所有变位词

描述：给定字符串S和P，找出S中所有和P字母构成相同（变位词）的子串，返回下标。

// [#438](https://leetcode.com/problems/find-all-anagrams-in-a-string/) Description: Find All Anagrams in a String | LeetCode OJ

解法1：俩指针。

// Solution 1: Two pointers.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0438_find-all-anagrams-in-a-string_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0438_find-all-anagrams-in-a-string_1_AC.cpp)

<hr>

#439 Ternary Expression Parser

// #439 三元表达式解析器

描述：如题。

// [#439](https://leetcode.com/problems/ternary-expression-parser/) Description: Ternary Expression Parser | LeetCode OJ

解法1：想清楚运算规则，分好词，用栈鼓捣去吧。

// Solution 1: Figure out the rules, tokenize it and see what you can do with the stacks.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0438_find-all-anagrams-in-a-string_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0438_find-all-anagrams-in-a-string_1_AC.cpp)

<hr>

#440 K-th Smallest in Lexicographical Order

// #440 字典序第K小的数

描述：将1~N按照字典序排序，找出第K个。

// [#440](https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/) Description: K-th Smallest in Lexicographical Order | LeetCode OJ

解法1：这倒是个难题，刚开始毫无头绪。后来看了看讨论区里大家的说法，其中“tree”一词让我茅塞顿开。什么树？十叉树。所以，你明白了吗？我们为什么要学各种抽象数据结构？因为这些东西能让你的思维形象化、具体化。

// Solution 1: This one seemed like tough. I got no lead at all for the first few minutes. After looking around the Discuss section, the word "tree" hit me. What tree? A denary tree. So, you got it? Why do we need those ADS? Because they help visualize and substantiate our thoughts. 

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0440_k-th-smallest-in-lexicographical-order_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0440_k-th-smallest-in-lexicographical-order_1_AC.cpp)

<hr>

#441 Arranging Coins

// #441 摆硬币

描述：你有N枚硬币，你想把它们摆成1、2、3、...的楼梯形。问最多能摆多少级楼梯？

// [#441](https://leetcode.com/problems/arranging-coins/) Description: Arranging Coins | LeetCode OJ

解法1：水题。

// Solution 1: Easy.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0441_arranging-coins_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0441_arranging-coins_1_AC.cpp)

<hr>

#442 Find All Duplicates in an Array

// #442 找出所有重复元素

描述：给定一个长度为N的数组，所有元素都在[1, N]之间。所有数要么出现一次，要么出现两次。找出出现两次的元素。

// [#442](https://leetcode.com/problems/find-all-duplicates-in-an-array/) Description: Find All Duplicates in an Array | LeetCode OJ

解法1：数数。

// Solution 1: Count them.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0442_find-all-duplicates-in-an-array_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0442_find-all-duplicates-in-an-array_1_AC.cpp)

<hr>

#444 Sequence Reconstruction

// #444 序列重建

描述：给你一个序列org，再给你一堆序列seqs。按照seqs每个序列中元素的先后顺序，问是否能重建出唯一一个序列来，而且该序列就是org。

// [#444](https://leetcode.com/problems/sequence-reconstruction/) Description: Sequence Reconstruction | LeetCode OJ

解法1：拓扑排序。

// Solution 1: Topological sort.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0444_sequence-reconstruction_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0444_sequence-reconstruction_1_AC.cpp)

<hr>

#445 Add Two Numbers II

// #445 两数相加2

描述：俩数用链表表示，做个加法。

// [#445](https://leetcode.com/problems/add-two-numbers-ii/) Description: Add Two Numbers II | LeetCode OJ

解法1：无聊。

// Solution 1: Boring.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0445_add-two-numbers-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0445_add-two-numbers-ii_1_AC.cpp)

<hr>

#446 Arithmetic Slices II - Subsequence

// #446 等差数列片段2 - 子序列

描述：和之前一样，不过这次是子序列。

// [#446](https://leetcode.com/problems/arithmetic-slices-ii-subsequence/) Description: Arithmetic Slices II - Subsequence | LeetCode OJ

解法1：一看就是DP，不过不能用二维数组表示，因为公差你不知道是多少。所以呢，咱们搞个哈希表。哈希大法好。

// Solution 1: It should be DP at first sight, but not to be done with a 2-d array, because you don't know how big the common differences can be. So, let's hash. Hashing rocks.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0446_arithmetic-slices-ii-subsequence_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0446_arithmetic-slices-ii-subsequence_1_AC.cpp)

<hr>

#447 Number of Boomerangs

// #447 回旋镖的个数

描述：给定平面上N个不重合的点，如果有ABC三点使得AB=AC，则称ABC是个回旋镖（等腰三角形嘛），求回旋镖的个数。

// [#447](https://leetcode.com/problems/number-of-boomerangs/) Description: Number of Boomerangs | LeetCode OJ

解法1：一看就是哈希。

// Solution 1: Hash at first sight.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0447_number-of-boomerangs_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0447_number-of-boomerangs_1_AC.cpp)

<hr>

#448 Find All Numbers Disappeared in an Array

// #448 找出数组中所有失踪的数

描述：和442题一样，这次找的是没出现的数。

// [#448](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) Description: Find All Numbers Disappeared in an Array | LeetCode OJ

解法1：数数。

// Solution 1: Count them.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0448_find-all-numbers-disappeared-in-an-array_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0448_find-all-numbers-disappeared-in-an-array_1_AC.cpp)

解法2：还是数数。

// Solution 2: Count already.

[代码2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0448_find-all-numbers-disappeared-in-an-array_2_AC.cpp)

// [Code 2](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0448_find-all-numbers-disappeared-in-an-array_2_AC.cpp)

<hr>

#449 Serialize and Deserialize BST

// #449 序列化反序列化一棵二叉搜索树

描述：如题。

// [#449](https://leetcode.com/problems/serialize-and-deserialize-bst/) Description: Serialize and Deserialize BST | LeetCode OJ

解法1：老实说，我没想出“BST”有没有值得深挖的地方。好像没什么可以特殊处理的地方啊？

// Solution 1: Honestly, I haven't come up with a way to exploit the keyword "BST". Nothing seemed conspicuous to me.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0449_serialize-and-deserialize-bst_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0449_serialize-and-deserialize-bst_1_AC.cpp)

<hr>

#450 Delete Node in a BST

// #450 二叉搜索树删除节点

描述：如题。

// [#450](https://leetcode.com/problems/delete-node-in-a-bst/) Description: Delete Node in a BST | LeetCode OJ

解法1：这题貌似是个经典面试题，而且挺难的。我就不解释了，你自个儿琢磨去吧。反正我在草稿纸上花了半天，才把这破题给整明白，代码也是倒腾了好一会儿。面试碰见这种题，你就自求多福吧。

// Solution 1: This one, AFAIK is a real classic one, very challenging too. Pray you don't run into it. Save your prayers if you do, just think it through really carefully and write your code slow and steady.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0450_delete-node-in-a-bst_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0450_delete-node-in-a-bst_1_AC.cpp)

<hr>

#451 Sort Characters By Frequency

// #451 按频率将字母排序

描述：如题。

// [#451](https://leetcode.com/problems/sort-characters-by-frequency/) Description: Sort Characters By Frequency | LeetCode OJ

解法1：水题。

// Solution 1: Piece of pancake.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0451_sort-characters-by-frequency_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0451_sort-characters-by-frequency_1_AC.cpp)

<hr>

#452 Minimum Number of Arrows to Burst Balloons

// #452  射穿气球的最少箭数

描述：给定一些圆心在X轴上的气球，告诉你每个气球的左右边界。现在允许你以平行Y轴的方向射箭穿过X轴，问至少几支箭可以射破所有气球？

// [#452](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) Description: Minimum Number of Arrows to Burst Balloons | LeetCode OJ

解法1：可以贪婪。

// Solution 1: Greed is good.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0452_minimum-number-of-arrows-to-burst-balloons_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0452_minimum-number-of-arrows-to-burst-balloons_1_AC.cpp)

<hr>

#453 Minimum Moves to Equal Array Elements

// #453 令所有元素相等的最小操作数

描述：给定N个元素的数组，每次操作允许你把N - 1各元素加1。问至少多少次能把所有元素变成一样？

// [#453](https://leetcode.com/problems/minimum-moves-to-equal-array-elements/) Description: Minimum Moves to Equal Array Elements | LeetCode OJ

解法1：不就是把一个元素减1么？

// Solution 1: Ain't no difference than decrementing one element by 1, right?

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0453_minimum-moves-to-equal-array-elements_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0453_minimum-moves-to-equal-array-elements_1_AC.cpp)

<hr>

#454 4Sum II

// #454 四数之和2

描述：给定四个数组，从中各选一个元素使得加起来等于0。求共有多少种选法？

// [#454](https://leetcode.com/problems/4sum-ii/) Description: 4Sum II | LeetCode OJ

解法1：暴力过。

// Solution 1: Brute-force.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0454_4sum-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0454_4sum-ii_1_AC.cpp)

<hr>

#455 Assign Cookies

// #455 分饼干

描述：有M块饼干，有大有小。有N个孩子，孩子对饼干大小有要求，小了就发脾气。每个孩子至多分一块，问你最多能哄几个孩子高兴？

// [#455](https://leetcode.com/problems/assign-cookies/) Description: Assign Cookies | LeetCode OJ

解法1：贪婪。

// Solution 1: Be greedy.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0455_assign-cookies_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0455_assign-cookies_1_AC.cpp)

<hr>

#456 132 Pattern

// #456 132形式

描述：给定数组，问是否存在三个元素依次为ABC，使得A < C < B？

// [#456](https://leetcode.com/problems/132-pattern/) Description: 132 Pattern | LeetCode OJ

解法1：谜之题目，谜之解法。

// Solution 1: I see it , but I don't get it.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0456_132-pattern_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0456_132-pattern_1_AC.cpp)

<hr>

#459 Repeated Substring Pattern

// #459 重复模式串

描述：给定字符串，问其是否存在循环节。

// [#459](https://leetcode.com/problems/repeated-substring-pattern/) Description: Repeated Substring Pattern | LeetCode OJ

解法1：KMP算法知道吧？用next数组搞定。长度就算500万也没问题。

// Solution 1: You know KMP right? Use the "next" array on this. It can handle a string of 5 million charaters.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0459_repeated-substring-pattern_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0459_repeated-substring-pattern_1_AC.cpp)

<hr>

#460 LFU Cache

// #460 最低频率缓存

描述：LRU知道吧？与LRU不同，LFU的替换依据是使用频率。

// [#460](https://leetcode.com/problems/lfu-cache/) Description: LFU Cache | LeetCode OJ

解法1：懒得说，灰常麻烦。双向链表、哈希表、LRU缓存都用上了，还有什么好说的？赶紧写吧。

// Solution 1: Too much trouble. Here you got doubly linked list, hash table, LRU cache, what else would I wanna say? Just start coding before you run out of time.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0460_lfu-cache_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0460_lfu-cache_1_AC.cpp)

<hr>

#461 Hamming Distance

// #461 汉明距离

描述：两数异或二进制表示中1的个数。

// [#461](https://leetcode.com/problems/hamming-distance/) Description: Hamming Distance | LeetCode OJ

解法1：水题。

// Solution 1: Trivial.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0461_hamming-distance_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0461_hamming-distance_1_AC.cpp)

<hr>

#462 Minimum Moves to Equal Array Elements II

// #462 使所有元素相等的最少步数2

描述：给定数组，每次允许选一个元素加1或减1，问至少多少步，可以是所有元素相等？

// [#462](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/) Description: Minimum Moves to Equal Array Elements II | LeetCode OJ

解法1：找中位数。

// Solution 1: Find the median.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0462_minimum-moves-to-equal-array-elements-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0462_minimum-moves-to-equal-array-elements-ii_1_AC.cpp)

<hr>

#463 Island Perimeter

// #463 岛屿周长

描述：给定01矩阵，1表示陆地，求岛屿周长。

// [#463](https://leetcode.com/problems/island-perimeter/) Description: Island Perimeter | LeetCode OJ

解法1：只要考虑每个1四周有几个1就行了。

// Solution 1: Just find out how many 1s there are around each 1.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0463_island-perimeter_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0463_island-perimeter_1_AC.cpp)

<hr>

#464 Can I Win

// #464 我能赢吗

描述：给定1~N，以及一个整数S。开始和为0，两人轮流从1~N选一个数，加到和里去。谁让和达到或超过S就算赢。选出的数不能重复使用。

// [#464](https://leetcode.com/problems/can-i-win/) Description: Can I Win | LeetCode OJ

解法1：记忆化搜索。

// Solution 1: DFS with memorization.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0464_can-i-win_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0464_can-i-win_1_AC.cpp)

<hr>

#465 Optimal Account Balancing

// #465 最佳账户平衡策略

描述：朋友之间可以相互借钱还钱。现在给定一些朋友间借钱的操作，请你设计用最少的还钱策略，使得大家互不相欠。

// [#465](https://leetcode.com/problems/optimal-account-balancing/) Description: Optimal Account Balancing | LeetCode OJ

解法1：这是个难题，而且是NPC的难题。首先，难点在于你很容易把这题看成一个简单的贪婪问题。其次，难点在于你要明白这其实是个关于集合划分的问题。划分什么？对于一个和为0的集合S，划分一个个的子集，使得每个子集的和都为0，而且都不进一步划分。接着想吧。

// Solution 1: This is a tough one, an NPC one actually. The first challenge is to consider it a challenge, not a simple greedy one. Next, you have to see the partition problem out of it. What partition? Partition what? Given a multiset S which sums to 0, partition it into some sub-multisets, who sum to 0 as well and are not furtherly partitionable. Get on with it.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0465_optimal-account-balancing_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0465_optimal-account-balancing_1_AC.cpp)

<hr>

#466 Count The Repetitions

// #466 统计重复次数

描述：我们用[S, n]表示S字符串重复n遍。现在给定S1 = [s1, n1]和S2 = [s2, n2]，问使得[S2, M]是S1子序列的最大M是多少？

// [#466](https://leetcode.com/problems/count-the-repetitions/) Description: Count The Repetitions | LeetCode OJ

解法1：题目比较难懂，其实就是问S2能以子序列的形式在S1里重复多少遍。我的算法基本是暴力的。有什么更好的解法吗？

// Solution 1: The problem description is a bit confusing. It's about counting how many S2 you can find in S1 as subsequences. My solution here is basically brute-force. Got anything better to suggest?

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0466_count-the-repetitions_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0466_count-the-repetitions_1_AC.cpp)

<hr>

#467 Unique Substrings in Wraparound String

// #467 循环字符串中的唯一子串

描述：将a~z依次写下去，构成一个无限长串S。现在给定一个字符串P，问P中有多少不同的子串出现在了S中。

// [#467](https://leetcode.com/problems/unique-substrings-in-wraparound-string/) Description: Unique Substrings in Wraparound String | LeetCode OJ

解法1：想想，怎么比较高效地表示abc、zabcd之类的字符串？

// Solution 1: Think about how to represent strings like "abc", "zabcd" efficiently?

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0467_unique-substrings-in-wraparound-string_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0467_unique-substrings-in-wraparound-string_1_AC.cpp)

<hr>

#468 Validate IP Address

// #468 验证IP地址

描述：验证IPv4或者IPv6地址。

// [#468](https://leetcode.com/problems/validate-ip-address/) Description: Validate IP Address | LeetCode OJ

解法1：麻烦得很。

// Solution 1: I smell trouble.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0468_validate-ip-address_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0468_validate-ip-address_1_AC.cpp)

<hr>

#469 Convex Polygon

// #469 凸多边形

描述：给定一对顶点，判断是否为凸多边形。

// [#469](https://leetcode.com/problems/convex-polygon/) Description: Convex Polygon | LeetCode OJ

解法1：叉乘可以求面积，面积是有方向的，方向相反就不好了。

// Solution 1: Cross product can be used to calculate area, area is directed, opposite direction is not politically correct.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0469_convex-polygon_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0469_convex-polygon_1_AC.cpp)

<hr>

#471 Encode String with Shortest Length

// #471 以最小长度编码字符串

描述：对于字符串abcabcabc，你可以编码成3[abc]，也可以不编码。现在给你一个字符串S，允许你对其中的部分进行递归编码，求出一种长度最短的编码结果。

// [#471](https://leetcode.com/problems/encode-string-with-shortest-length/) Description: Encode String with Shortest Length | LeetCode OJ

解法1：难题。总体思路是记忆化搜索。另外，需要判断字符串里的循环节，所以又要用到next数组了。

// Solution 1: A tough one. The idea is DFS with memorization. Besides, we need to calculate the length of every repetend in the string, so bring you "next" array.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0471_encode-string-with-shortest-length_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0471_encode-string-with-shortest-length_1_AC.cpp)

<hr>

#472 Concatenated Words

// #472 连接而成的词

描述：给定一个词典，从中找出能够由其他至少两个词连接而成的词。

// [#472](https://leetcode.com/problems/concatenated-words/) Description: Concatenated Words | LeetCode OJ

解法1：暴力DP，也不完全算是暴力，好歹还有个排序。

// Solution 1: Brute-force DP, if not totally brute-force. At least there is a sorting before that.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0472_concatenated-words_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0472_concatenated-words_1_AC.cpp)

<hr>

#473 Matchsticks to Square

// #473 火柴棍拼正方形

描述：给定一些长度不一的火柴棍，允许首尾相接。问能否拼成一个正方形？

// [#473](https://leetcode.com/problems/matchsticks-to-square/) Description: Matchsticks to Square | LeetCode OJ

解法1：搜，但要注意姿势。

// Solution 1: DFS, in the right stance.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0473_matchsticks-to-square_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0473_matchsticks-to-square_1_AC.cpp)

<hr>

#474 Ones and Zeroes

// #474 1和0

描述：给定一些01字符串，给你m个0和n个1，允许你做一些分配。问你最多能配出这些字符串中的几个？

// [#474](https://leetcode.com/problems/ones-and-zeroes/) Description: Ones and Zeroes | LeetCode OJ

解法1：半天没看懂题目，懂了以后发现是个二维背包问题。

// Solution 1: Took me quite a while to tune in. Seemed like a 2-d Knapsack problem to me.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0474_ones-and-zeroes_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0474_ones-and-zeroes_1_AC.cpp)

<hr>

#475 Heaters

// #475 暖气

描述：假设有一些房子，有一些暖气，全都排在一条直线上。为了保证所有房子都被暖气覆盖到， 求最小的供暖半径。

// [#475](https://leetcode.com/problems/heaters/) Description: Heaters | LeetCode OJ

解法1：想想归并排序。

// Solution 1: Think about Merge Sort.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0475_heaters_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0475_heaters_1_AC.cpp)

<hr>

#476 Number Complement

// #476 互补数

描述：给定一个数，按照二进制取反。

// [#476](https://leetcode.com/problems/number-complement/) Description: Number Complement | LeetCode OJ

解法1：位操作。

// Solution 1: Bit manipulations.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0476_number-complement_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0476_number-complement_1_AC.cpp)

<hr>

#477 Total Hamming Distance

// #477 总汉明距离

描述：给定一堆数，求两辆汉明距离之和。

// [#477](https://leetcode.com/problems/total-hamming-distance/) Description: Total Hamming Distance | LeetCode OJ

解法1：按位考虑。

// Solution 1: Bit by bit.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0477_total-hamming-distance_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0477_total-hamming-distance_1_AC.cpp)

<hr>

#479 Largest Palindrome Product

// #479 最大回文乘积

描述：给定一个数N，求两个N位数相乘所能构成的最大回文数，结果膜1337。据说N非常大，有8那么大，怕不怕？

// [#479](https://leetcode.com/problems/largest-palindrome-product/) Description: Largest Palindrome Product

解法1：你就说int64_t不就得了。另外，我跟大多数人一样，实在不知道这题到底哪儿简单了？暴力打表吗？

// Solution 1: Why don't you say int64_t already. Besides, like the rest majority, I don't know where the hell did that "Easy" come from. Precalculation or what?

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0479_largest-palindrome-product_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0479_largest-palindrome-product_1_AC.cpp)

<hr>

#480 Sliding Window Median

// #480 滑动窗口中位数

描述：给定一个数组，和一个固定大小的窗口。当窗口不断向前滑动时，求出一系列中位数。

// [#480](https://leetcode.com/problems/sliding-window-median/) Description: Sliding Window Median | LeetCode OJ

解法1：和Find Median from Data Stream一样的解法。

// Solution 1: Same as Find Median from Data Stream.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0480_sliding-window-median_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0480_sliding-window-median_1_AC.cpp)

<hr>

#481 Magical String

// #481 神奇字符串

描述：我说我看不懂题目，你信吗？

// [#481](https://leetcode.com/problems/magical-string/) Description: Magical String | LeetCode OJ

解法1：反正我信。

// Solution 1: The f* is that?

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0481_magical-string_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0481_magical-string_1_AC.cpp)

<hr>

#482 License Key Formatting

// #482 序列号格式化

描述：太长不写。

// [#482](https://leetcode.com/problems/license-key-formatting/) Description: License Key Formatting | LeetCode OJ

解法1：水题。

// Solution 1: Dull.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0482_license-key-formatting_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0482_license-key-formatting_1_AC.cpp)

<hr>

#483 Smallest Good Base

// #483 最小的好基数

描述：给定一个整数N，如果对于整数K，使得N在K进制表示下每一位都是1，则认为K很好。求最小的好基数K。

// [#483](https://leetcode.com/problems/smallest-good-base/) Description: Smallest Good Base | LeetCode OJ

解法1：显然N - 1很好，所以这题首先是有解的。而N - 1就是上界。接下来怎么办呢？二分搜呗。

// Solution 1: Apparently N - 1 is a good base, so the problem is always solvable. As N - 1 is the upper bound for solutions, what we do next is to enumerate some parameters and solve some equations with binary search. It's numerical, so make sure you know things like error, truncation, overflow, etc.. 

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0483_smallest-good-base_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0483_smallest-good-base_1_AC.cpp)

<hr>

#484 Find Permutation

// #484 找出排列

描述：有一个1~N组成的排列，现在给你一个长度为N - 1的由DI组成的字符串，表示相邻元素的关系是增还是减。根据这个串，请重建出字典序最小，而且满足要求的排列。

// [#484](https://leetcode.com/problems/find-permutation/) Description: Find Permutation | LeetCode OJ

解法1：想了半天，毫无头绪。于是参考了网上的神解法。

// Solution 1: Not a single lead on this one. Here is a most brilliant solution from the Internet.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0484_find-permutation_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0484_find-permutation_1_AC.cpp)

<hr>

#485 Max Consecutive Ones

// #485 最长连续1子串

描述：如题。

// [#485](https://leetcode.com/problems/max-consecutive-ones/) Description: Max Consecutive Ones | LeetCode OJ

解法1：水题。

// Solution 1: Trivial.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0485_max-consecutive-ones_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0485_max-consecutive-ones_1_AC.cpp)

<hr>

#486 Predict the Winner

// #486 预测赢家

描述：给定一个数组，每个元素表示一个分数。俩人轮流，每次从左端或右端拿走一个分数，如此直到拿完。分高的人赢。问先手是否必胜？

// [#486](https://leetcode.com/problems/predict-the-winner/) Description: Predict the Winner | LeetCode OJ

解法1：不要一看数据量很小，就暴力搜。暴力能解决问题吗？不能啊。年轻人嘛，还是要DP，不要暴力。

// Solution 1: If it looks like DP, it's DP.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0486_predict-the-winner_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0486_predict-the-winner_1_AC.cpp)

<hr>

#487 Max Consecutive Ones II

// #487 最长连续1子串2

描述：和之前一样，不过这次允许你把一个0变成1。

// [#487](https://leetcode.com/problems/max-consecutive-ones-ii/) Description: Max Consecutive Ones II | LeetCode OJ

解法1：搞个状态机试试？

// Solution 1: Try using a state machine?

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0487_max-consecutive-ones-ii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0487_max-consecutive-ones-ii_1_AC.cpp)

<hr>

#488 Zuma Game

// #488 祖玛游戏

描述：给定一串彩色球，再给你几个球用来发射。每次发射你都可以随便挑剩下的任一个，3个一消。问最少用多少个球可以消光。如果搞不定，返回-1。

// [#488](https://leetcode.com/problems/zuma-game/) Description: Zuma Game | LeetCode OJ

解法1：基本算是暴力搜吧。

// Solution 1: It's basically a brute-force DFS.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0488_zuma-game_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0488_zuma-game_1_AC.cpp)

<hr>

#490 The Maze

// #490 迷宫

描述：给定一个01矩阵，1表示墙，0表示空地。现在球从起点出发，目标是到达终点。每次球可以朝一个方向滚，但滚动时必须撞墙才能换方向。问是否能到达终点。

// [#490](https://leetcode.com/problems/the-maze/) Description: The Maze | LeetCode OJ

解法1：搜。

// Solution 1: DFS.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0490_the-maze_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0490_the-maze_1_AC.cpp)

<hr>

#491 Increasing Subsequences

// #491 递增子序列

描述：给定一个数组，找出总共有多少不同的递增子序列。

// [#491](https://leetcode.com/problems/increasing-subsequences/) Description: Increasing Subsequences | LeetCode OJ

解法1：暴力搜。我知道，这题的数据量非常小，而且数据范围也很小，明摆着是要你DP。懒得写了。

// Solution 1: Brute-force DFS. I know the size and range are both quite small. Clearly it's indicating a DP solution. Just too lazy to try it out.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0491_increasing-subsequences_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0491_increasing-subsequences_1_AC.cpp)

<hr>

#492 Construct the Rectangle

// #492 构造矩形

描述：给定一个面积A，求出矩形长宽，使得矩形面积等于A，并且长宽尽可能接近。

// [#492](https://leetcode.com/problems/construct-the-rectangle/) Description: Construct the Rectangle | LeetCode OJ

解法1：水题。

// Solution 1: Trivial.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0492_construct-the-rectangle_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0492_construct-the-rectangle_1_AC.cpp)

<hr>

#493 Reverse Pairs

// #493 逆序对

描述：给定一个数组，如果对于下标i < j，并且a[i] > 2 * a[j]，则称为一个逆序对。求逆序对的个数。

// [#493](https://leetcode.com/problems/reverse-pairs/) Description: Reverse Pairs | LeetCode OJ

解法1：又是比较 + 数数问题，树状数组搞定。

// Solution 1: Comparison and counting again, let BIT do the job.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0493_reverse-pairs_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0493_reverse-pairs_1_AC.cpp)

<hr>

#494 Target Sum

// #494 目标和

描述：给定一个数组，允许你对每个元素选择加或减。问有多少种选法，能让结果等于S。

// [#494](https://leetcode.com/problems/target-sum/) Description: Target Sum | LeetCode OJ

解法1：可以算是背包问题。

// Solution 1: Sort of like a Knapsack problem.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0494_target-sum_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0494_target-sum_1_AC.cpp)

<hr>

#495 Teemo Attacking

// #495 提莫进攻

描述：给定一些进攻的时间点，和进攻的中毒持续时间，求敌人总共的中毒时间。

// [#495](https://leetcode.com/problems/teemo-attacking/) Description: Teemo Attacking | LeetCode OJ

解法1：这么水的题，居然是medium？

// Solution 1: Too trivial to be rated "medium", I think.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0495_teemo-attacking_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0495_teemo-attacking_1_AC.cpp)

<hr>

#496 Next Greater Element I

// #496 下一个更大元素1

描述：给定无重复元素的数组a1和a2，其中a1是a2的子集。对于a1每个元素，找出其在a2中对应位置右边的第一个大于它的元素。

// [#496](https://leetcode.com/problems/next-greater-element-i/) Description: Next Greater Element I | LeetCode OJ

解法1：破题目，真难读懂。看样子要用个栈，试了试，我看行。

// Solution 1: Hell of a problem to read. Looks like I need a stack, looks like my instinct is right.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0496_next-greater-element-i_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0496_next-greater-element-i_1_AC.cpp)

<hr>

#498 Diagonal Traverse

// #498 对角遍历

描述：给定矩阵，按照“右上、左下”的方式轮换遍历整个矩阵。

// [#498](https://leetcode.com/problems/diagonal-traverse/) Description: Diagonal Traverse | LeetCode OJ

解法1：让干嘛就干嘛。

// Solution 1: Do as told.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0498_diagonal-traverse_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0498_diagonal-traverse_1_AC.cpp)

<hr>

#499 The Maze III

// #499 迷宫3

描述：和之前一样，不过这次终点是个洞。除了掉进洞以外，球依然是撞墙才能转向。现在请找出一条距离最短的路径，使得球能滚进洞。要求输出完整的路径，并保证输出的路径是可行解里字典序最小的。

// [#499](https://leetcode.com/problems/the-maze-iii/) Description: The Maze III | LeetCode OJ

解法1：输出路径也就算了，还尼玛字典序最小，这题简直把“麻烦”二字演绎到了极致。思路很简单，实现很复杂。

// Solution 1: You don't worry when it's not your problem. You don't suffer when it's not your headache. Simple idea, lengthy implementation.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0499_the-maze-iii_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0499_the-maze-iii_1_AC.cpp)

<hr>

#500 Keyboard Row

// #500 键盘行

描述：给定一些单词，问其中有多少可以在键盘的一行里打出来。

// [#500](https://leetcode.com/problems/keyboard-row/) Description: Keyboard Row | LeetCode OJ

解法1：水题。

// Solution 1: Easy.

[代码1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0500_keyboard-row_1_AC.cpp)

// [Code 1](https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0500_keyboard-row_1_AC.cpp)
