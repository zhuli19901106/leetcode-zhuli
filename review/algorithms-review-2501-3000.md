# LeetCode 一句话题解 - 2501-3000

[返回目录](./README.md)

- [LeetCode 一句话题解 - 2501-3000](#leetcode-一句话题解---2501-3000)
  - [2501 - 2600](#2501---2600)
  - [2601 - 2700](#2601---2700)
  - [2701 - 2800](#2701---2800)
  - [2801 - 2900](#2801---2900)

代码库地址：  
[https://github.com/zhuli19901106/leetcode-zhuli/tree/master/algorithms/2501-3000](https://github.com/zhuli19901106/leetcode-zhuli/tree/master/algorithms/2501-3000)

## 2501 - 2600

2501 Longest Square Streak in an Array

题意：给定数组nums，请从中找出一个子序列ss，使得<b>ss排序后</b>，每个元素都是前一元素的<b>平方</b>。求出ss的<b>最大长度</b>。

难度：medium

解法：先对nums<b>排序</b>，如果x是<b>完全平方数</b>，则`res[x]=res[sqrt(x)]+1`。对于1<b>特殊处理</b>，1的话，就是统计1的个数。总代价`O(n)`。

<hr>

2502 Design Memory Allocator

题意：设计一个简易的<b>内存分配器</b>。内存池大小为n，支持分配大小`size`的连续内存给`mID`进程；支持释放`mID`进程的所有内存。对于分配连续内存的规则，我们以<b>第一个足够大小</b>的内存块为准。

难度：medium

解法：别客气，内存分配器<b>怎么可能简易</b>。超难的。对于这题，<b>我简直疯了</b>...题目本身不难，思路也在题意中明确给出了。但是，实现真的超级复杂，有<b>好多细节要处理</b>。我居然写了1个钟头，然后1次提交过了。这算什么medium？简直比hard还hard。首先你是打算用什么来存储内存块？这个很重要。用<b>数组、链表、哈希映射</b>都会带来不同的优缺点，包括<b>组合使用</b>。我估计是考虑了不少情况，最后决定用<b>区间数组</b>的形式，来表示<b>连续的空闲内存</b>。这个其实等价于链表，或许我应该用<b>链表</b>的。操作区间数组，搞拆分、合并确实很复杂，但我想不出<b>更简洁</b>，而且能保证<b>合理复杂度</b>的方案。`allocate()`和`free()`都是`O(n)`复杂度，显然这两者不可能做到严格`O(1)`，毕竟你没有无限内存，总会有<b>碎片块块</b>，需要`O(n)`时间查找。

<hr>

2506 Count Pairs Of Similar Strings

题意：给定一个词表words，如果两个单词的唯一值相同，则称为<b>相似</b>。请求出相似的`(i,j)`对数。

难度：easy

解法：为了<b>比较唯一值</b>，我们可以把唯一值转为一个字符串。把w转换为`''.join(list(set(w)))`，用这个作为<b>哈希key</b>进行归类。对<b>每个类别</b>，如果数量是cc，则有`C(cc,2)=cc*(cc-1)/2`对。对所有类别的对数<b>求和</b>，就是最终结果。总代价`O(n)`。

<hr>

2511 Maximum Enemy Forts That Can Be Captured

题意：给定数组forts，1表示我方堡垒，0表示地方堡垒，-1表示空地。如果你要从1位置出发，到达某个0位置。要求中间的所有位置都是0。经过的所有0，都变成1，也就是<b>被我方占领</b>。请判断能占领的<b>最多敌城数量</b>。

难度：easy

解法：按<b>向左、向右</b>分别扫描一次，判断<b>1之后，连续0的个数</b>。总代价`O(n)`。

<hr>

2515 Shortest Distance to Target String in a Circular Array

题意：给定一个词表words和目标值target。如果你从i出发，可以<b>左右循环走</b>。请判断<b>至少多少步</b>，可以到达target值所在的位置。

难度：easy

解法：比如target在j位置，那么答案就是`min((n+i-j)%n,(n+j-i)%n)`。注意，j位置<b>可能不止一个</b>。总代价`O(n)`。

<hr>

2516 Take K of Each Character From Left and Right

题意：给定一个由abc组成的字符串s，每次你可以<b>从两端</b>拿走一个字符。请问至少多少次，你可以得到至少k个abc。

难度：medium

解法：<b>左右两端</b>分别用`i=0、j=n-1`双指针。先让<b>`i`右移</b>，直到<b>凑够k个abc</b>为止。然后`i`每<b>左移一步</b>，j就左移，直到>b?补足k个abc</b>。那么答案就是`min(i+1+n-j)`。这个<b>移动和更新</b>的过程是`O(1)`的，因此总代价是`O(n)`。

<hr>

2517 Maximum Tastiness of Candy Basket

题意：给定n种糖果，价格为`price[i]`。请从中选出k种糖果，使得任意两种糖果，价格差值的<b>最小值最大</b>。

难度：medium

解法：<b>minimax问题</b>。我们先把价格<b>排序</b>，然后针对这个<b>差值的最小值</b>做二分搜索。比如对于值x，我以`相邻差值>=x`为要求，尝试找出符合要求的糖果。如果能找到`>=k`个，则`ll=x`；如果`<k`个；则`rr=x`。为什么？因为如果我找不出k个，说明x<b>跨度太大了</b>，那么x就得<b>变小</b>。总代价`O(nlogn+nlog(int))`。

<hr>

2520 Count the Digits That Divide a Number

题意：给定整数`num`，请求出它的数位中，<b>整除</b>`num`的个数。

难度：easy

解法：水题。

<hr>

2521 Distinct Prime Factors of Product of Array

题意：给定数组nums，请求出nums元素乘积的<b>质因数</b>的个数。

难度：medium

解法：对每个元素做<b>质因数分解</b>，只保留<b>唯一值的集合</b>。然后所有集合<b>求并集</b>就是答案。如果你用<b>筛法</b>预先求出范围内所有的<b>质数</b>，则<b>因数分解</b>会很快。总代价可以接近`O(n)~O(nlogn)`。

<hr>

2525 Categorize Box According to Criteria

题意：给定一些箱子的<b>长宽高、质量</b>，按照一些奇奇怪怪的规则进行<b>分类打标签</b>。

难度：easy

解法：很枯燥的`if else elif`题，写一堆条件判断吧。

<hr>

2527 Find Xor-Beauty of Array

题意：对于数组nums，选一个三元组`(i,j,k)`，我们定义有效值为`(nums[i]|nums[j])&nums[k]`。如果允许ijk取值[0,n-1]，请求出<b>所有有效值</b>的<b>异或</b>。

难度：medium

解法：这是什么<b>诡异的位运算</b>？共有`n^3`种组合，求异或。这题我卡了很久，想了半天想不出什么巧妙的思路。但我肯定这题是个<b>智力题</b>。最后<b>瞎猜</b>`xor(nums)`，猜对了。我没法解释，就是猜的。总代价`O(n)`。

<hr>

2529 Maximum Count of Positive Integer and Negative Integer

题意：给定有序数组nums，请返回`max(正数个数,负数个数)`。请用`O(logn)`代价完成。

难度：easy

解法：题目已经明示了，<b>二分搜索</b>。

<hr>

2530 Maximal Score After Applying K Operations

题意：给定数组nums，每次你可以任选i位置，得到`nums[i]`分，并把它变为`ceil(nums[i]/3)`。请问<b>k次</b>能得到的<b>最大得分</b>是多少？

难度：medium

解法：我们每次都应该取<b>最大的值</b>，那么把所有值放入一个<b>最大堆</b>就行了。总代价`O(nlogn)`。

<hr>

2535 Difference Between Element Sum and Digit Sum of an Array

题意：给定数组nums，请求出`|sum(nums)-sum(digitSum(nums[i]))|`。

难度：easy

解法：水题。

<hr>

2536 Increment Submatrices by One

题意：给定一个n x n方阵mat。执行一些操作，每次你需要把左上`(r1,c1)`到右下`(r2,c2)`的子矩阵<b>所有值都+1</b>。执行完所有操作后，返回矩阵结果。

难度：medium

解法：因为是批处理，我们不需要<b>二维树状数组</b>。可以对`[r1][c1]`和`[r2][c2]`执行`+1`，对`[r1][c2]`和`[r2][c1]`执行`-1`。执行完所有操作后，<b>从右往左、从下往上</b>，执行<b>后缀累加</b>。得到的结果就是最终答案。这个做法非常巧妙，第一次遇到甚至会觉得很神奇。但仔细想明白后，就知道怎么用了。这种做法只能解决<b>批处理问题</b>，对于<b>随改随查</b>的情况是不管用的。总代价`O(n^2)`。

<hr>

2537 Count the Number of Good Subarrays

题意：给定数组nums，请找出至少<b>存在k对`(i,j)`</b>，使得`nums[i]==nums[j]`的子数组的个数。

难度：medium

解法：统计<b>相等的对数</b>，可以对值进行<b>哈希计数</b>，然后`sum(cc*(cc-1)/2)`。然后用<b>ij双指针+滑动窗口</b>的思路。i前进，扩大窗口；j前进，缩小窗口。i在前，j在后。至于怎么更新计数，就不细说了。总代价`O(n)`。为什么这么多滑动窗口的题？

<hr>

2540 Minimum Common Value

题意：给定有序数组nums1、nums2，找出最小的公共值。如果不存在，则返回-1。

难度：easy

解法：`i=0,j=0`，用类似<b>有序归并</b>的方式，双指针前进。

<hr>

2542 Maximum Subsequence Score

题意：给定n长度的数组nums1、nums2。你可以选择长度k的子序列，得到对应位置的ss1、ss2。我们定义分数为`sum(ss1)*min(ss2)`。也就是<b>第一个求和</b>，乘以<b>第二个的最小值</b>。请求出<b>最大分数</b>。

难度：medium

解法：这题很难，我起码<b>卡了一个钟头</b>没有思路。因为是子序列，相当于可以乱序。那么我们可以考虑<b>对nums1排序</b>，尽量取大的元素。但因为nums1、nums2对应位置是<b>绑定在一起的</b>，相当于`(nums1[i],nums2[i])`，最后想了一个<b>神奇的排序方式</b>，按`(-nums1,-nums2)`的方式排序，还要用一个最小堆，堆中放入的值是`(+nums2,+nums1)`。也就是排序按<b>1降2降</b>，最小堆中则按<b>2升1升</b>。按这个顺序，得到的`sum*min`一定是最优的。<b>我没法严格证明</b>，因为我没完全想清楚。总之，这题对我很难，非常难，就是那种<b>始终想不明白</b>的感觉。总代价`O(nlogn)`。

<hr>

2544 Alternating Digit Sum

题意：给定整数num，把<b>从高到低</b>的数位，按照`+-+-...`这样求和。

难度：easy

解法：水题。

<hr>

2545 Sort the Students by Their Kth Score

题意：给定m x n矩阵score，代表m个学生的n个考试成绩。给定整数k，请按照第k个考试的成绩<b>降序排列</b>。返回排序后的矩阵。

难度：medium

解法：按照`(-score[i][k],i)`排序，可以得到i的排序。按照<b>i的排序</b>把<b>行顺序</b>调整一下就是最终结果。作为medium难度，这题几乎就是easy。总代价`O(mlogm+mn)`。

<hr>

2549 Count Distinct Numbers on Board

题意：开始黑板上有一个整数n。每一步，对于黑板上所有数x，你都把`[1,n]`范围内，`x%i==1`的所有i加上去。请问经过`1e9`天后，黑板上有多少个<b>不同的值</b>？

难度：easy

解法：其实你想想，`n%(n-1)==1`，这就够了。经过n-2天，2~n都写上去了，只有1不会写上去。因此答案就是`n-1 if n>1 else 1`。无聊的<b>智力题</b>。

<hr>

2551 Put Marbles in Bags

题意：有n个球，k个包包。你需要把n个球<b>划分为连续的k段</b>，放入k个包包中。如果`i~j`是连续的一段，则代价为`weights[i]+weights[j]`。总代价是k个代价之和。请求出`最大总代价-最小总代价`。

难度：hard

解法：划分k段，每段的代价是<b>头尾元素之和</b>。然后让你求`max-min`，相当于解<b>两个问题</b>。有一种思路，可以把这题变得<b>非常简单</b>。但如果你想不到，这题就很难。我反正<b>想了很久</b>，才想出来。比如我要切k-1刀，但不论怎么切，w[0]和w[n-1]我总是要加的，对吧？剩下比如我选了`(w[i],w[i+1])`位置切一刀，那就加上`w[i]+w[i+1]`。因此，是不是我找出最大的`k-1`刀，就是<b>最大值</b>；找出最小的`k-1`刀，就是<b>最小值</b>。因此，思路有了。以`w[i]+w[i+1]`为比较依据，建立最大堆、最小堆。剩下就用不说了。总代价`O(nlogn)`。这题就是<b>“华山一条路”</b>。你想出这种思路，就超级简单；想不出来，你找其他各种办法都不好使。问题是，没人能保证<b>你一定想得出</b>，这也不是通过训练，能100%学会的。

<hr>

2553 Separate the Digits in an Array

题意：给定整数数组nums，请<b>把所有数位拆开</b>，返回数位数组。

难度：easy

解法：水题。

<hr>

2554 Maximum Number of Integers to Choose From a Range I

题意：给定数组banned，整数n、maxSum。你需要选出`[1,n]`范围内的<b>不同整数</b>，且不能取banned中的值，要求总和不超过maxSum。请求出你能选的<b>最多个数</b>。

难度：medium

解法：显然，按照<b>贪心原则</b>，枚举求和就行了。总是选<b>尽量小的值</b>，这样能多选几个。总代价`O(n)`。

<hr>

2558 Take Gifts From the Richest Pile

题意：有n堆礼物，每堆数量是`gifts[i]`。每次，你都选<b>最大</b>的一堆，把`gifts[i]`变为`floor(sqrt(gifts[i]))`。请问经过k次操作后，<b>剩余礼物总和</b>是多少？

难度：easy

解法：用<b>最大堆</b>。总代价`O(nlogn)`。

<hr>

2559 Count Vowel Strings in Ranges

题意：给定一个长度n的词表words，和m个查询`[i,j]`。对于每个查询，你需要求出`words[i:j+1]`中，以元音`aeiou`<b>开头结尾</b>的单词的个数。

难度：medium

解法：先`O(n)`代价判断每个词的开头结尾，得到一个<b>前缀和数组</b>pref。对于每个查询，求`pref[j+1]-pref[i]`即可。总代价`O(n+m)`。

<hr>

2562 Find the Array Concatenation Value

题意：给定数组nums，每次<b>取出</b>头尾元素，把<b>“头尾”</b>拼成一个数，加到结果中，比如`'12'+'345'='12345'`。如果最后只剩一个元素，则只取这一个。返回最终的<b>求和结果</b>。

难度：easy

解法：题意很明确，照做即可。

<hr>

2566 Maximum Difference by Remapping a Digit

题意：给定整数num，如果你可以把其中某数字x，换为另一数字y。请求出能得到的`最大值-最小值`的<b>差值</b>。

难度：easy

解法：这显然应该<b>换最高位</b>，因为最高位的影响最大。把最高位分别换9或者0。但要注意，如果<b>最高位已经是9或者0</b>，就要往后继续找。

<hr>

2568 Minimum Impossible OR

题意：给定数组nums，请找出一个最小正整数x，使得x不能由nums的<b>子序列的按位或</b>得到。

难度：medium

解法：子序列的按位或，这肯定有什么窍门，<b>智力题</b>之类的。首先，这是子序列，因此<b>顺序无所谓</b>。我们可以把nums先<b>排序</b>。元素都是正整数，那么比如我用k表示<b>当前`[1,k]`都可以表示</b>的最大值。那么，如果`nums[i]>k+1`，则`k+1`就<b>无法表示</b>。那么，我们知道`nums[i]<=k+1`，这说明什么？说明我<b>最多可以表示到</b>`[1,k|nums[i]]`。这点不容易想到。想明白了，这题就做完了。确实是<b>智力题</b>。总代价`O(nlogn)`。

<hr>

2570 Merge Two 2D Arrays by Summing Values

题意：给定个数是`[id,val]`的两个数组nums1、nums2，请做合并。结果按id升序排列。对于相同id值，则val进行相加。

难度：easy

解法：水题，<b>有序数组归并</b>。

<hr>

2571 Minimum Operations to Reduce an Integer to 0

题意：给定整数n，每次你可以<b>+-一个2的幂</b>。请求出最小次数，把n变成0。

难度：medium

解法：<b>位操作</b>，你可以写一个二进制数。比如`100110111100`，注意看<b>一段连续的1</b>。1111，如果减1需要减4次；如果加1，则变为10000，再减1次就变0，总共2次。因此，可以先转换成<b>连续1、连续0</b>的个数，然后做一个`O(n)`代价的<b>DP</b>。注意处理一些边界case。总体上，这题<b>思路简单</b>，但实现<b>略麻烦</b>。

<hr>

2574 Left and Right Sum Differences

题意：给定数组nums，对于每个位置i，请求出`|sum(nums[0:i])-sum(nums[i+1:n])|`。

难度：easy

解法：`|前缀和-后缀和|`，用两个数组做好<b>预计算</b>即可。总代价`O(n)`。

<hr>

2578 Split With Minimum Sum

题意：给定整数num，你可以把数位<b>任意排序</b>，然后分成两段，得到两个整数num1和num2。请求出`num1+num2`。

难度：easy

解法：<b>贪心策略</b>，把num按数位<b>升序排列</b>，然后按`1,2,1,2,...`交叉分配给num1和nums2。这样得到的结果，求和最小。

<hr>

2579 Count Total Number of Colored Cells

题意：t=1时刻，你有一个格子。对于每个i时刻，你都把边缘<b>上下左右相邻</b>的格子加入结果。请求出t=n时刻，结果中有多少个格子？

难度：medium

解法：很明显，这是个数列，而且是<b>二次多项式</b>。`a[n]=a[n-1]+4(n-1)`，解一下，得到结果`a[n]=2n^2-2n+1`。<b>数学题</b>，总代价`O(1)`。

<hr>

2582 Pass the Pillow

题意：传枕头，从`1~n`然后从`n~1`，如此循环。给定n和t，请求出t时刻谁拿到枕头。

难度：easy

解法：每`2n-2`是一个<b>周期</b>。按这个推算一下即可。

<hr>

2583 Kth Largest Sum in a Binary Tree

题意：给定二叉树，请求出<b>每层节点和</b>，找出<b>第k大</b>的值。

难度：medium

解法：用任意方式遍历，遍历时记录深度，按<b>深度</b>求和。结果<b>排序</b>，找出第k大。完全按照题目要求实现即可。总代`O(n+hlogh)`。

<hr>

2586 Count the Number of Vowel Strings in Range

题意：给定词表words，请找出`[left,right]`范围内，以元音`aeiou`开头和结尾的词的个数。

难度：easy

解法：水题，这题和2559不是基本一样吗？

<hr>

2588 Count the Number of Beautiful Subarrays

题意：对于一个数组，每次选两个位置(i,j)，使得存在k，`nums[i]&nums[i]&(1<<k)==1<<k`，也就是两元素<b>在k位都是1</b>。我们把两元素的第k位都变为0。如果经过任意次操作，可以把<b>整个数组都变为0</b>，则称为<b>漂亮数组</b>。给定数组nums，请求出<b>漂亮子数组</b>的个数。

难度：medium

解法：我感觉见过无数次<b>“good subarray”、“beautiful subarray”</b>的说法了。我们首先搞明白，怎么理解这个“漂亮”。每次我们选择2个1，都变成0。那么，对于每个二进制位，<b>1的个数都必须是偶数</b>。这样才能全变成0。那你想想，奇偶性，我<b>不用累加，直接做异或</b>就可以判断了。这样，我直接用一个哈希表，记录`nums[0:i+1]`的<b>前缀异或</b>。如果当前`i`位置，对应的<b>异或值是x</b>，则`mm[x]`就是以i为终点的漂亮子数组个数。所以，思路可以用三步概括：`x^=nums[i]; res+=mm[x]; mm[x]+=1;`。总代价`O(n)`。有点难度的一道<b>位操作题</b>，如果想不到<b>异或</b>的话，就很难。这题我很快就想出来了，但也只是<b>恰好想到</b>。

<hr>

2591 Distribute Money to Maximum Children

题意：你有m元金额，分给c个小朋友。已知钱要分完，每人至少1元，不能有人拿到4元。请问至多几个人能拿到8元？

难度：easy

解法：规则很具体，尽量多的人拿8元。那我们就按照每人1元，<b>剩余`/7`</b>。如果最后的余数恰好是3，表示<b>有一个人要拿4元</b>，则结果需要减1。挺枯燥无聊的一题。

<hr>

2592 Maximize Greatness of an Array

题意：给定数组nums，你可以任意排序，得到perm。请求出`max(count(perm[i]>nums[i]))`。

难度：medium

解法：你可能会想到田忌赛马思路。比如`abcde`，变成`bcdea`就有4个变大。按这个思路，我把`nums`先<b>排序</b>，得到`sorted_nums`。再把`sorted_nums`<b>循环右移1位</b>，结果就是最优的？<b>错了</b>，这个思路的错误，在于“循环右移1位”。其实，你应该用双指针i、j，<b>i前j后</b>。都往前走，总是保持`sorted_nums[i]>sorted_nums[j]`。如果i走到n，就停止。看<b>能找出多少对</b>。这样的总代价是`O(nlogn+n)=O(nlogn)`。这个解法比我以前写的，要简单得多。

<hr>

2593 Find Score of an Array After Marking All Elements

题意：给定数组nums，每次都选出`(值,下标)`最小的元素nums[i]。将nums[i]加入总分，并删除`(i-1,i,i+1)`三个元素。如果在<b>边界</b>，则不考虑界外情况。求出最终总分。

难度：medium

解法：首先，要明白这题的重点不在于<b>动脑</b>，而是<b>动手</b>。题目明确定义了<b>你要做什么</b>。问题在于你如何<b>高效实现它</b>。可以用一个`SortedDict`，以`nums[i]`为key。这样能快速找到<b>最小值</b>。或者直以`(nums[i],i)`元组作为key也可以。这样，每次更新的代价是`O(logn)`，总代价为`O(nlogn)`。还有一种思路，不用SortedDict，而是直接用<b>`(nums[i],i)`数组</b>，对数组进行<b>排序</b>，然后用一个`visited`<b>标记数组</b>，用来处理删除问题。<b>思路相同，实现方法不同。</b>总代价也是一样的。

<hr>

2595 Number of Even and Odd Bits

题意：给定整数n，请求出<b>二进制表示</b>里，偶数位、奇数位是1的个数。我们以<b>最低位为第0位</b>，依此类推。

难度：easy

解法：水题。

<hr>

2596 Check Knight Tour Configuration

题意：给定一个n x n的国际象棋棋盘，每个位置被访问的次序是`grid[i][j]`。如果用一个马，从0位置出发，按照给定的顺序走。请判断每一步跳马是否都按照<b>马走日</b>的规则。

难度：medium

解法：这题没有难度，就是要<b>仔细</b>，不要漏掉任何一个细节。`grid[0][0]`必须是0。把这些值按照`0~n*n-1`依次找到，判断相邻两个位置差，是不是<b>“马走日”</b>。总代价`O(n^2)`。

<hr>

2597 The Number of Beautiful Subsets

题意：给定数组nums，如果把它视为一个集合（multiset），如果其中不存在两个元素x、y，且`|x-y|==k`，则称为<b>好集合</b>。请求出nums的<b>非空好子集</b>的个数。

难度：medium

解法：相差不能为k，第一念头是<b>暴力搜索</b>。为什么？因为是子集，而不是子数组，它是<b>不连续的</b>。那么我们直接考虑当前nums[i]，判断搜索集合里，是否存在`nums[i]-k`或者`nums[i]+k`。如果存在，则冲突，不能选`nums[i]`。总代价`O(2^n)`。

<hr>

2600 K Items With the Maximum Sum

题意：有一个数组，其中包含`+1、0、-1`的个数分别是`a、b、c`个。我们要从中选k个，请返回k个值求和的最大值。

难度：easy

解法：水题。

## 2601 - 2700

2601 Prime Subtraction Operation

题意：给定数组nums，对于每个元素，你可以选择一个小于它的质数p，执行`nums[i]-=p`。请问能否经过任意次操作，使得nums变为<b>严格递增</b>？

难度：medium

解法：首先看数据范围，如果范围比较小，就简单了。（因为我很难快速找到一个<b>大质数</b>。）数据确实很小，那么先用<b>筛法</b>得到`[1,1000]`内的质数`primes`。我们用<b>贪心原则</b>，对于每个`nums[i]`，都要保证减p之后的下界是`nums[i-1]+1`，且尽量接近这个下界。对于`nums[0]`，这个下界则是1。因此，可以通过<b>二分搜索</b>，在质数列表`primes`中，找出符合条件的<b>最大质数</b>。如果在某个i位置，发现`nums[i]<nums[i-1]+1`，已经<b>越过了下界</b>，则无法完成目标。总代价`O(nlog(log(maxp)))`。其中这个`log(log())`也不精确，因为<b>质数的个数</b>有个专门的函数研究它，叫`pi(n)`，这个就不展开了，我也懂得不多。

<hr>

2605 Form Smallest Number From Two Digit Arrays

题意：给定数组nums1、nums2。从两数组中<b>各选一位</b>，组成一个最小的数。返回这个数。

难度：easy

解法：水题。

<hr>

2606 Find the Substring With Maximum Cost

题意：给定字符串s。我们给字符加上<b>分值</b>，`chars[i]`的分值为`vals[i]`。对于`a~z`中没有出现在`chars`的字符，则默认按`1~26`处理。请求出s中子串的最大分值。

难度：medium

解法：题目描述得挺费劲，其实就是做一次`char->int`的<b>转换</b>，变为一个整数数组。然后，就是<b>最大子数组和</b>，这个<b>经典问题</b>就不用说了。总代价`O(n)`。

<hr>

2609 Find the Longest Balanced Substring of a Binary String

题意：给定01字符串s，请用`0->(`、`1->)`的方式，按括号匹配的规则，找出最长的<b>括号匹配子串长度</b>。

难度：easy

解法：<b>数据量很小</b>，随便怎么做都行。不过一种比较直白的解法，可以`O(n^2)`代价解决。我们枚举每个i位置作为<b>起点</b>，进行括号匹配。如果出现-1，则失败终止；如果等于0，则该位置`(i,j)`是一个<b>匹配子串</b>。求出<b>匹配位置</b>的`max(j-i+1)`就是最终结果。这题应该还有<b>`O(n)`解法</b>，但那就属于脑力劳动了，没必要。

<hr>

2610 Convert an Array Into a 2D Array With Conditions

题意：给定数组nums，你需要用完nums中的所有元素，将其分为<b>若干个数组</b>。要求每个数组没有重复值，且<b>数组个数尽量少</b>。返回划分结果。

难度：medium

解法：题目有点难懂，最关键的信息没说清楚，就是<b>“必须用完nums所有元素”</b>。思路很简单，对nums进行<b>哈希计数</b>，对所有唯一值，按照<b>每轮各取一个</b>的方式处理，直到取完为止。比如`[1,3,4,1,2,3,1]->{1:3, 2:1, 3:2, 4:1}`。那么第一轮就是`[1,2,3,4]`，变为`{1:2, 3:1}`。继续拿，直到拿完为止。总代价`O(n)`。

<hr>

2614 Prime In Diagonal

题意：给定n x n方阵nums，请找出在两条对角线上的<b>最大质数</b>。

难度：easy

解法：<b>对角线，质数，最大</b>。按题意判断即可。

<hr>

2639 Find the Width of Columns of a Grid

题意：给定m x n矩阵，请求出每一列的宽度。宽度定义为这列<b>所有元素的最大宽度</b>。一个整数的宽度等于位数，如果是负数，则等于位数+1。

难度：easy

解法：按照题目给定的宽度定义，求解即可。位数计算，`floor(log10(n))+1`。

<hr>

2640 Find the Score of All Prefixes of an Array

题意：给定数组nums，我们定义`conv[i]=nums[i]+max(nums[0:i+1])`，定义`score(nums)=sum(conv)`。对于每个位置i，请求出`score(nums[0:i+1])`。

难度：medium

解法：这就是典型的<b>题目费解，问题简单</b>。按题目要求，求出<b>前缀max</b>，计算`conv[i]=nums[i]+max(nums[0:i+1])`，然后求`conv[i]`的<b>前缀和</b>。总代价`O(n)`。

<hr>

2641 Cousins in Binary Tree II

题意：993的变体。给定二叉树，把所有节点值都替换为它的所有<b>表亲节点</b>的值之和。表亲节点是<b>同层，且父节点不同</b>的节点。

难度：medium

解法：很容易想出<b>表亲节点</b>的位置，但怎么用代码<b>比较简洁地</b>写出来，这个还是要注意方法的。比如遍历时记录<b>父节点</b>，可以。但这样代码会<b>稍微难看点</b>。比如遍历时，我在遍历<b>r节点</b>时，直接修改`r.left`和`r.right`的值，这个比父节点的方式稍微容易些。不论哪种方法，首先都要按照<b>深度</b>，求<b>节点和</b>。总代价`O(n)`。

<hr>

2642 Design Graph With Shortest Path Calculator

题意：<b>有向图</b>，n个点，边的格式为`[x,y,w]`，表示`x->y`的权重为w。现在请设计一个数据结构，支持动态添加边`x->y`，支持查询x到y的最短路径，返回<b>总权重</b>。

难度：hard

解法：有向图最短路，Dijkstra。这个当然是教科书必知必会了。但这次要求能够<b>动态修改，动态查询</b>。离线算法和在线算法，难度差别是很大的。既然<b>Dijkstra单点最短路代价</b>是`O(ElogV)`，Floyd全最短路的代价是`O(V^3)`。那么对于<b>单查</b>，我们还是先考虑Dijkstra。看了下数据量，至多100。那么<b>每次都跑一下Dijkstra</b>是可以接受的。注意用<b>堆优化</b>的版本。事实证明，对于这题而言，这个解法效率确实OK。而且<b>简单易懂，不容易出bug。</b>

<hr>

2643 Row With Maximum Ones

题意：给定01矩阵，请求出1的数量最多的i行。返回<b>行号i和1的数量</b>。如果存在多个，则返回最小的i值。

难度：easy

解法：水题。

<hr>

2644 Find the Maximum Divisibility Score

题意：给定数组nums和divisors。对于每个`divisors[i]`，统计nums中它的<b>倍数的个数</b>，作为<b>分值</b>。求出分值最大的`divisors[i]`，如果存在多个，则返回最小的一个。

难度：easy

解法：水题，枚举即可。

<hr>

2651 Calculate Delayed Arrival Time

题意：给定x，y，求出`(x+y)%24`。

难度：easy

解法：水题，就，令人无语。

<hr>

2652 Sum Multiples

题意：给定整数n，请求出`[1,n]`中，3、5、7的倍数的总和。

难度：easy

解法：集合论里的<b>容斥原理</b>，用`3+5+7-35-57-37+357`。当然，也可以直接for循环计算，这样就是`O(n)`代价，但<b>节约脑细胞</b>。

<hr>

2656 Maximum Sum With Exactly K Elements 

题意：给定数组nums，每次你可以找出一个值`x`，并将其替换为`x+1`，并把x加到<b>总分</b>里。经过k次操作，请求出最大总分。

难度：easy

解法：显然，你要取的值就是`max(nums)`。那么总分就是`k*max(nums)+sum(1~k-1)`。总代价`O(n)`。

<hr>

2657 Find the Prefix Common Array of Two Arrays

题意：给定两个`1~n`的排列A、B。我们定义`A[0:i+1]`和`B[0:i+1]`中公共值的个数为`C[i]`。请求出数组C。

难度：medium

解法：如果两数组都很大，也不是什么`1~n`排列的话，这个问题<b>依然成立</b>，而且依然可以<b>高效解决</b>。这题的高效解法，应该做到`O(n)`代价。我们保持两个集合sa、sb。那么当添加`A[i]、B[i]`时，如果`A[i]`在sb中，则+1；如果`B[i]`在sa中，则+1。这些是建立在，A和B都没有<b>重复元素</b>的前提下。如果A、B是任意数组，则<b>集合</b>可以改为<b>哈希计数</b>。这样每次更新的代价是严格`O(1)`，总代价则是`O(n)`。

<hr>

2658 Maximum Number of Fish in a Grid

题意：给定m x n矩阵表示地形。0值表示陆地，正值<b>表示水，且有鱼</b>。你可以从任何水格子出发，并在相邻的水格子移动。请求出能钓到鱼的<b>最大数量</b>。

难度：medium

解法：任选正值格子作为起点，按照<b>洪泛思路</b>，执行BFS。你可以用一个额外的标记数组，也可以<b>把正值改为-1</b>，以便和0区别开来。<b>一边搜索，一边求和。</b>返回最大的求和值，就是答案。总代价`O(mn)`。

<hr>

2660 Determine the Winner of a Bowling Game

题意：保龄球。如果你`i-1`或者`i-2`轮打了<b>10个</b>，那么在第i轮可以获得<b>双倍分</b>。给定两人的得分记录player1、player2，请判断<b>1赢、2赢还是平手</b>。

难度：easy

解法：水题。

<hr>

2670 Find the Distinct Difference Array

题意：我们定义`distinct(nums)`为数组nums的唯一值个数。给定数组nums，请求出每个位置i的`distinct(nums[0:i+1])-distinct(nums[i+1:n])`。

难度：easy

解法：统计<b>唯一值个数</b>，而且随着i前进，要不断更新。这个可以用<b>前后两个哈希表</b>实现。按照哈希计数的思路，对于mm1、mm2，每次都向mm1中<b>添加</b>`nums[i]`，从mm2中<b>去掉</b>`nums[i]`。`len(mm1)、len(mm2)`就是唯一值个数。总代价`O(n)`。

<hr>

2672 Number of Adjacent Elements With the Same Color

题意：给定一个长度n的数组colors，一开始都是0，表示无色。执行m次查询，格式为`[i,c]`，表示`colors[i]=c`。然后返回<b>相邻且颜色相同</b>的对数，无色不算在内。

难度：medium

解法：执行`colors[i]=c`这个简单，赋值即可。对于统计相邻同色的对数，我们可以在执行`colors[i]=c`的时候，也检查一下`colors[i-1]`和`colors[i+1]`。毕竟这个<b>局部修改</b>只会影响左右的元素。单次更新代价`O(1)`，总代价`O(m)`。

<hr>

2673 Make Costs of Paths Equal in a Binary Tree

题意：给定一个<b>满二叉树</b>，节点编号`1~n`。每个节点`i+1`有一个代价`cost[i]`。如果你可以对任意节点的代价`cost[i]`执行+1。请判断至少多少次，能让所有<b>根到叶的路径和</b>相等。

难度：medium

解法：我们先<b>遍历一次</b>，求出最大的路径和`max_sm`，同是<b>递归向上返回</b>，并记录每个节点<b>r所在子树</b>的<b>最大根到叶路径和</b>。那么对于每个节点r，我考虑r所在子树的最大路径和`max_val[r]`，执行`r.val+=max_sm-max_val[r]`。为什么这么做？因为我在<b>越上面</b>执行+1，下面受影响的节点就越多，这样能保证<b>+1的总次数最小</b>。递归向下执行这个逻辑即可。这个思路描述起来有点复杂，代码也一样复杂。但你想明白的话，就不算很难。<b>难和繁琐</b>不是一个概念。这题比较繁琐。总代价`O(n)`。

<hr>

2678 Number of Senior Citizens

题意：给定每个乘客的身份信息，其中某两位是年龄。请返回年龄大于60岁的乘客数量。

难度：easy

解法：水题，字符串处理。

<hr>

2679 Sum in a Matrix

题意：给定m x n矩阵nums，每次从每行中找出`max`并删除，并把`max(max)`加入总分。请返回最终总分。

难度：medium

解法：对每行执行<b>排序</b>即可。总代价`O(mnlogn+mn)=O(mnlogn)`。

<hr>

2682 Find the Losers of the Circular Game

题意：给定n个人，<b>`1~n`围成一圈</b>，玩传球，从1号开始。在<b>第i轮</b>，传到随后的第i*k个人，<b>本轮结束</b>。如果某人第二次拿到球了，则游戏结束。定义始终拿不到球的人为输家，请返回<b>输家列表</b>，升序排列。

难度：easy

解法：直接<b>按规则模拟</b>即可，总代价`O(n)`。

<hr>

2683 Neighboring Bitwise XOR

题意：给定01数组nums，我们按照`derived[i]=nums[i]^nums[i+1]`计算相邻的异或值。对于`n-1`，则计算`n-1`和`0`的异或。现在给定derived结果，请判断是否存在nums，可以得到这个结果。

难度：medium

解法：分别用`nums[0]=0或者1`去试一遍，看<b>有没有矛盾</b>。如果验证完了没有矛盾，就true；否则false。其实你把每个`nums[i]`<b>都取反</b>，`derived`的结果是完全一样的。因此，01<b>要么都行，要么都不行</b>。总代价`O(n)`。

<hr>

2684 Maximum Number of Moves in a Grid

题意：给定m x n矩阵grid，你可以从任意`(i,j)`出发。可以选择`(i-1,j+1),(i,j+1),(i,j+1)`三个位置。但要求到达的位置，grid值必须<b>比当前值大</b>。请求出你能移动的<b>最大步数</b>。

难度：medium

解法：既然每次都是往右走，<b>右上、右下、右</b>，那么我们执行一个<b>从左往右的DP</b>就行了。思路很简单，就不细说了。总代价`O(mn)`。

<hr>

2685 Count the Number of Complete Components

题意：给定<b>无向图</b>，请求出其中全连通分量的个数。<b>全连通分量</b>，是指任意两个点之间，都有<b>直接连接的边</b>。

难度：medium

解法：先用<b>并查集</b>，把不同的连通分量<b>归类</b>。对于每个连通分量，比如有k个点，那么我们判断关联的边的数量是不是`C(k,2)=k*(k-1)/2`。如果是，则为全连通分量。也可以通过判断<b>点的度数</b>来确定，如果度数都是`k-1`，则为全连通分量。

<hr>

2696 Minimum String Length After Removing Substrings

题意：给定字符串s，你可以不断从中删除`AB`或`CD`。请返回最终<b>剩余结果</b>的长度。

难度：easy

解法：用<b>栈</b>处理，栈顶是AB或者CD则弹出。总代价`O(n)`。

<hr>

2697 Lexicographically Smallest Palindrome

题意：给定字符串s，你可以替换任意字符。请用最少的替换次数，把s变成回文串。返回<b>字典序最小</b>的结果。

难度：easy

解法：按照对称位置`s[i]`和`s[n-1-i]`比较，取两者中<b>较小的一个</b>。总代价`O(n)`。

<hr>

2698 Find the Punishment Number of an Integer

题意：给定整数x，如果str(x*x)可以划分成几个值，这些整数值加起来恰好等于x，我不知道管x叫什么，因为<b>题目也没没告诉我</b>。现在给定整数n，请求出`[1,n]`范围内，满足这样条件的i，求`sum(i*i)`。

难度：medium

解法：这个条件<b>很奇怪，也很苛刻</b>。因此<b>满足要求的数不会很多</b>。对于给定的`[1,1000]`范围，可以直接<b>暴力搜索+保存预计算结果</b>。对于一个数x，暴力搜索的代价是`O(2^log10(x))=O(x^log10(2))`。那么总代价就是`O(n^(1+log10(2)))~=O(n^1.3)`，其实也不用深究这个。

## 2701 - 2800

2706 Buy Two Chocolates

题意：给定数组prices和金额money，从prices中选出最小的两个值x、y。如果`x+y<=money`，则返回减去后的剩余值`money-x-y`，否则返回`money`。

难度：easy

解法：水题。

<hr>

2707 Extra Characters in a String

题意：给定字符串s和一个词表dictionary。你需要把s<b>划分</b>为多个子串，使得其中某些子串在词表中。请求出剩余不在词表的子串的<b>最小长度和</b>。

难度：medium

解法：题意希望剩余部分尽可能少，那么我们可以先用`O(n^2)`代价（算上字符串匹配，其实是`O(n^3)`），检查每个`s[i:j+1]`是否在词表中。然后我们可以用<b>DP思路</b>解决。定义`dp[i]`为`s[0:i+1]`部分的最小剩余长度。那么枚举`j=[0,i]`，如果`s[j:i+1]`在词表中，则`dp[i]=min(dp[i],dp[j-1])`；如果不在词表中，则`dp[i]=min(dp[i],dp[j-1]+i-j+1)`。这样可以`O(n^2)`代价求出结果。最终答案就是`dp[n-1]`。按照给定数据量，最多可以接受`O(n^3)`的代价，对于总代价`O(n^2)`的解法，显然是OK的。

<hr>

2710 Remove Trailing Zeros From a String

题意：给定数组串num，把末尾0去掉。

难度：easy

解法：水题。

<hr>

2711 Difference of Number of Distinct Values on Diagonals

题意：给定m x n矩阵，对应每个位置`grid[i][j]`，我们分别考虑沿对角线方向，往<b>左上、右下</b>走。定义`la[i][j]`为左上不包括自身的唯一值个数；定义`rb[i][j]`为右下不包括自身的唯一值个数。对每个(i,j)位置，请求出`|la-rb|`的差值。

难度：medium

解法：首先，每条对角线是<b>互不相干</b>的。那么我们可以考虑，对于一个数组nums，我求`|left-right|`的唯一值个数的差值。我可以用ml、mr两个哈希表，一边移动一边<b>更新哈希计数</b>。那么`len(ml)-len(mr)`就是唯一值个数的差值。因此，处理一个对角线的代价是`O(n)`。总共有`O(n)`个对角线，总代价`O(n^2)`。这题并不难，但<b>比较繁琐</b>。注意仔细实现，不要出bug。

<hr>

2712 Minimum Cost to Make All Characters Equal

题意：给定一个01串s，每次操作，你可以选择反转`s[0:i+1]`，代价为`i+1`；或者反转`s[i:n]`，代价为`n-i`。请求出把所有值变为相等的最小总代价。

难度：medium

解法：第一步，我们要考虑<b>全0还是全1</b>。比如全0，第二步，我们要考虑<b>左反转还是右反转</b>。比如我定一个分界线`i`。那么`s[0:i+1]`我采取从左反转，`s[i+1:n]`我采取从右反转。第三步，就考虑是<b>贪心还是DP</b>？想了下，应该是<b>贪心</b>。既然全0或者全1都可以，那我只要用<b>尽量少</b>的反转个数，总代价就<b>一定最小</b>。这个反转的方式，是<b>从两端</b>，因此我可以用一个<b>双向队列deque</b>。每次都取<b>较短的一边</b>进行反转。思路到这儿，就算<b>完整了</b>，实现吧。总代价`O(n)`。

<hr>

2716 Minimize String Length

题意：给定字符串s，请求出<b>唯一值</b>的个数。

难度：easy

解法：原题不是这么说的，但翻译过来就是这样。

<hr>

2717 Semi-Ordered Permutation

题意：给定一个`1~n`的排列nums，每次允许你交换相邻元素。请问至少多少次交换后，`nums[0]=1,nums[n-1]=n`？

难度：easy

解法：执行交换即可，总代价`O(n)`。当然，你不交换，找到<b>1和n的位置</b>后，<b>直接计算</b>也可以。

<hr>

2729 Check if The Number is Fascinating

题意：给定整数n，如果(n,2n,3n)数位连起来，恰好是`1~9`的一个<b>排列</b>，则称为<b>有魅力</b>。请判断n有没有魅力。

难度：easy

解法：水题，按题意判断即可。

<hr>

2733 Neither Minimum nor Maximum

题意：给定数组，请随意返回一个<b>不等于max或min</b>的元素。如果不存在则返回-1。

难度：easy

解法：水题。

<hr>

2739 Total Distance Traveled

题意：有一辆卡车，每1升油10公里。有主副油箱，主油箱每耗油5升，则副油箱会向其中补充1升。给定初始的主副油箱存量`main、additional`，请求出你能行进的<b>最大里程数</b>。

难度：easy

解法：水题，`/5`做一下换算。不断换算，直到<b>不够除</b>为止。总代价`O(logn)`。

<hr>

2740 Find the Value of the Partition

题意：给定数组nums，请将其划分为两个数组`nums1、nums2`。要求不能有<b>剩余元素</b>，划分方式<b>不用连续</b>。请求出`|max(nums1)-min(nums2)|`的最小值。

难度：medium

解法：既然希望`max-min`最小，也就是尽可能接近。那我们把nums<b>排序</b>。显然，这个<b>最接近的值</b>一定出现在某个<b>相邻位置</b>。因此，我们检查`sorted_nums[i]-sorted_nums[i-1]`即可。总代价`O(nlogn)`。

<hr>

2744 Find Maximum Number of String Pairs

题意：给定一个词表words，元素各不相同。如果`words[i]`恰好等于`reversed(words[j])`，则可以进行配对。请求出能找出的<b>最大对数</b>。

难度：easy

解法：虽然数据量很小，随便怎么做都行，但我们还是可以<b>动动脑子</b>。比如我们把`reversed(words[i])`存入<b>哈希表</b>，这样可以快速查到。注意，对于<b>回文串</b>的情况，则要<b>排除掉</b>。最后记得把总结果`/2`。总代价`O(n)`。

<hr>

2745 Construct the Longest New String

题意：你有`AA、BB、AB`三种串各`x、y、z`个。你可以选其中若干个，连成一个长串。要求长串里不能包含`AAA、BBB`。请求出这个长串的<b>最大长度</b>。

难度：medium

解法：有种<b>分情况讨论</b>的感觉。比如ABAA，之后必须是BB。比如BBAB，之后必须是AA。因此，<b>关键在于AB</b>。最后我想了个<b>比较繁琐</b>的思路。首先按照`BBABAA`，用完`min(x,y,z)`次。然后对剩下的分情况讨论。很麻烦，但<b>好歹结果是对的</b>。总代价`O(1)`。

<hr>

2748 Number of Beautiful Pairs

题意：给定数组，对于任意位置`i<j`，请求出`nums[i]`最高位和`nums[j]`最低位<b>互质</b>的`(i,j)`对数。

难度：easy

解法：水题，题目要求很<b>稀奇古怪</b>，但仍然是个水题。

<hr>

2760 Longest Even Odd Subarray With Threshold

题意：给定数组nums，请求出符合`偶奇偶奇...`交替变换，且值不超过`threshold`的最长子数组的<b>长度</b>。

难度：easy

解法：水题。

<hr>

2762 Continuous Subarrays

题意：给定数组nums，如果某个子数组的所有元素<b>相差都不超过2</b>，则称为<b>连续子数组</b>。请求出连续子数组的个数。

难度：medium

解法：非常典型的<b>滑动窗口+双指针</b>解法，熟悉这种玩法的话，很快就有思路了。为了计算<b>最大的差值</b>，我们需要用`SortedDict`，而不是<b>哈希表</b>。总代价`O(nlogn)`。

<hr>

2765 Longest Alternating Subarray

题意：给定数组，请找出公差在`+1、-1`间<b>交替变化</b>的最长子数组，返回长度。

难度：easy

解法：水题。

<hr>

2766 Relocate Marbles

题意：给定nums，表示一些小球的<b>初始位置</b>。你需要执行m次操作`[from,to]`，每次把from位置的所有球，移动到to位置。执行完成后，返回所有存在小球的<b>位置</b>，升序排列。

难度：medium

解法：这题不难，我们把小球位置存入<b>哈希表</b>，用`位置->小球个数`来表示。那么当我<b>移动x到y</b>时，则执行`mm[y]+=mm[x]; del mm[x];`即可。最后把key值升序返回。总代价`O(n+m+nlogn)=O(nlogn)`。

<hr>

2767 Partition String Into Minimum Beautiful Substrings

题意：给定一个01串s，我们将其<b>划分</b>为多个子串。要求每个子串都<b>以1开头</b>，且对应的值是<b>5的幂</b>。请返回<b>最小的划分个数</b>。

难度：medium

解法：按照给定数据量，直接暴力搜也是可以的。但我们可以用`O(n^2)`代价，判断<b>每一个子串</b>是不是<b>5的幂</b>。很容易想出一个<b>DP解法</b>，定义`dp[i]`为`s[0:i+1]`的最小划分次数，-1表示<b>无法完成划分</b>。那么，如果`dp[j-1]!=-1`，且`s[j:i+1]`是<b>5的幂</b>，则`dp[i]=min(dp[i],dp[j-1]+1)`。最终答案就是`dp[n-1]`，总代价`O(n^2)`。

<hr>

2769 Find the Maximum Achievable Number

题意：给定x、y，每次你可以选择x+1或者x-1，可以同时选择y+1或者y-1。如果要求<b>至多t次</b>把x变成y，给定y，请求出最大的x。

难度：easy

解法：这题的评论区有两百多个<b>愤怒的网友</b>。答案就是`y+2t`。如果<b>你没看懂题目</b>，那就正常。这就是网友愤怒的原因。

<hr>

2778 Sum of Squares of Special Elements 

题意：给定数组nums，长度n。对于`n%i==0`的位置i，请返回`sum(nums[i]**2)`。

难度：easy

解法：水题。

<hr>

2779 Maximum Beauty of an Array After Applying Operation

题意：给定数组nums，你对<b>每个位置</b>至多可以执行<b>一次操作</b>。操作是把`nums[i]`替换为`[nums[i]-k,nums[i]+k]`范围的任意值。请求出最终能得到的<b>最长单值子序列</b>的长度。

难度：medium

解法：<b>最长单值子序列</b>，看起来很复杂，其实还好。比如我们选一个值x，如果`nums[i]`在`[x-k,x+k]`范围内，我就可以<b>把它变成x</b>。那么对于任何值x，一次判断的代价是`O(n)`。那么，我可以通过<b>二分搜索</b>，以总代价`O(nlogn)`完成这题。还有一种解法，我把nums<b>排序</b>。对于每个`nums[i]`，我都找出<b>上下界位置jk</b>，使得它们处在`[nums[i]-k,nums[i]+k]`范围内。这个代价也是`O(nlogn)`。两种方法都可以，而且都不算难。

<hr>

2780 Minimum Index of a Valid Split

题意：如果一个数组有某个值x存在超过一半，则称为主值（其实是<b>众数</b>）。现在我们将nums划分为`nums[0:i+1]`和`nums[i+1:n]`，使得两个数组的主值和nums的<b>主值相同</b>。请求出<b>最小的i</b>，如果不存在则返回-1。

难度：medium

解法：先以`O(n)`代价做一次<b>哈希计数</b>，找出`nums`的主值`d`。定义`d`的总次数为`nd`，那么对于每个位置`i`，我们用一个计数`cc`，表示`nums[0:i+1]`中`d`的个数。则前半段个数是`cc`，后半段个数是`nd-cc`。当两边同时满足`cc>(i+1)/2`且`nd-cc>(n-i)/2`时，符合条件的`i`就找到了。总代价`O(n)`。

<hr>

2784 Check if Array is Good

题意：给定数组nums，请判断nums经过<b>排序</b>后，能否变成`[1,2,3,...,n-1,n,n]`，也就是`1~n`还多个n。

难度：easy

解法：那就<b>排序</b>。

<hr>

2785 Sort Vowels in a String

题意：给定字符串s，请将其中辅音保持原位，元音`aeiouAEIOU`则按ASCII码排序。

难度：medium

解法：这题很直白，应该定级为easy。找出所有元音并<b>排序</b>，得到sv。然后遍历一次s，<b>每遇到元音</b>，就取`s[i]=sv[j++]`。总代价`O(nlogn)`。对了，其实这题可以在`O(n)`时间解决。方法很容易想，不细说了。毕竟总共就<b>10种字母</b>。

<hr>

2788 Split Strings by Separator

题意：给定词表words和分隔符separator。请把所有词切分，结果在一个数组中返回，去掉其中的<b>空串</b>。

难度：easy

解法：水题，`split()`之后都<b>加一起</b>，过滤空串即可。

<hr>

2798 Number of Employees Who Met the Target

题意：给定数组hours，请求出`hours[i]>=target`的个数。

难度：easy

解法：水题。

<hr>

2799 Count Complete Subarrays in an Array

题意：给定数组nums，如果一个子数组的<b>唯一值个数</b>，等于nums的唯一值个数，则称为<b>完整子数组</b>。请求出完整子数组的个数。

难度：medium

解法：第一念头当然是<b>滑动窗口+双指针</b>。想了想，确实是。我以`i`在前，每次前进1步；我以`j`在后，如果`nums[j:i+1]`<b>完整了</b>，则j前进到<b>恰好变得不完整</b>为止。那么每次<b>i到达完整位置</b>时，则`res+=j`。滑动窗口里的一个重要思路，就是当我<b>满足条件</b>时，则我需要<b>移动窗口</b>，导致<b>恰好破坏条件</b>。这就是在<b>有效的边缘</b>试探。总代价`O(n)`。

## 2801 - 2900

2806 Account Balance After Rounded Purchase

题意：给定x，请求出`100-(x+5)//10*10`。

难度：easy

解法：水题。

<hr>

2807 Insert Greatest Common Divisors in Linked List

题意：给定链表，在每两个相邻节点之间，插入它们<b>最大公约数</b>的值。

难度：medium

解法：写一个`gcd()`函数，按要求插入即可。总代价`O(n)`。

<hr>

2810 Faulty Keyboard

题意：给定字符串s，依次输出其中的字符，如果遇到`i`则<b>反转当前输出内容</b>。

难度：easy

解法：水题。

<hr>

2815 Max Pair Sum in an Array

题意：给定数组nums，请从中找出两个元素x、y，使得x和y的最大数位相同，求出`max(x+y)`。如果不存在，则返回-1。

难度：easy

解法：水题，按照<b>最大数位</b>归类即可。

<hr>

2816 Double a Number Represented as a Linked List

题意：给定一个用<b>链表</b>表示的大数，请乘以2。

难度：medium

解法：可以把链表先反转一下再`*2`，如果有<b>进位</b>，则需要添加一个节点。总代价`O(n)`。

<hr>

2824 Count Pairs Whose Sum is Less than Target

题意：给定数组nums，请求出`i<j, nums[i]+nums[j]<target`的`(i,j)`对数。

难度：easy

解法：先把nums<b>排序</b>，然后枚举`nums[i]`，对`nums[j]`执行<b>二分搜索</b>。总代价`O(nlogn)`。也可以先排序，然后<b>双指针</b>`O(n)`代价解决。复杂度是一样的，都取决于排序。

<hr>

2825 Make String a Subsequence Using Cyclic Increments

题意：给定字符串s1、s2，你可以选s1中的<b>任意多个字符</b>，执行循环右移，比如`a->b,b->c,...,z->a`。请问经过至多一次操作后，能否让s2变成s1的子序列。

难度：medium

解法：<b>匹配子序列</b>的思路是贪心的，加上这个操作后，<b>依然是贪心的</b>。只不过我们匹配的<b>条件更宽了</b>。之前是要求`s1[i]==s2[j]`，现在变成了`s1[i]==s2[j] or shift(s1[i])==s2[j]`。其余逻辑完全相同。总代价`O(n1+n2)`。

<hr>

2828 Check if a String Is an Acronym of Words

题意：给定字符串s和词表words，如果s可以由words每个单词首字母<，则称为<b>依次拼成</b>，则称为<b>缩写</b>。请判断s是否为words的缩写。

难度：easy

解法：水题。

<hr>

2829 Determine the Minimum Sum of a k-avoiding Array

题意：请找出一个长度为n，元素都是<b>正数，不含重复值</b>，且不存在任何两元素`x+y==k`的数组nums，返回最小的数组和`min(sum(nums))`。

难度：medium

解法：数据范围很小，那我可以<b>直接枚举</b>。从1开始，比如当前尝试值是x，则查找`k-x`是否在数组中。如果是，则`x+=1`；否，则`nums.append(x)`。这题如果数据范围很大，则需要动动脑子。数据小的话，随便怎么处理都行的。生成了数组nums之后，返回`sum(nums)`。总代价是`O(n^2)`。

<hr>

2833 Furthest Point From Origin

题意：给定字符串s，其中包含`LR_`三种字符。表示左移、右移、左或右移。从0位置出发，左移、右移都按<b>1格</b>处理。请求出<b>移动结束之后</b>，你能到达的，距离0点的<b>最大距离</b>。

难度：easy

解法：`abs(L的数量-R的数量)+_的数量`。注意读题，是<b>移动完了之后</b>，不是过程中。

<hr>

2839 Check if Strings Can be Made Equal With Operations I

题意：两个长度为4的串s1、s2。你可以对其中任意串，交换相隔2位的字符。可以交换<b>任意次</b>，请问能否让`s1==s2`？

难度：easy

解法：水题。

<hr>

2840 Check if Strings Can be Made Equal With Operations II

题意：2839的变体。有两个长度为n的串s1、s2，你可以任选一个串，交换相隔距离是<b>偶数</b>的字符。可以交换<b>任意次</b>，请问能否让`s1==s2`？

难度：medium

解法：其实依然很简单，我们只要把<b>奇偶位置</b>分开比较即可。`sorted(s1[0::2])==sorted(s2[0::2])`，就这么搞。总代价`O(nlogn)`。

<hr>

2843 Count Symmetric Integers

题意：给定范围`[low,high]`，请求出范围内的<b>对称数</b>的个数。对称数的要求是，2n位且<b>前n位和后n位</b>的数位和相等。<b>奇数位</b>的数不是对称数。

难度：easy

解法：范围很小，<b>直接枚举</b>即可。如果范围大的话，则要考虑DP思路了。

<hr>

2848 Points That Intersect With Cars

题意：给定一些闭区间`[x,y]`，求<b>并集</b>里的<b>整点</b>个数。

难度：easy

解法：题目翻译过来就是这个意思。做区间合并，然后统计`sum(y-x+1)`。

<hr>

2855 Minimum Right Shifts to Sort the Array

题意：给定数组nums，如果经过<b>循环右移</b>可以使nums变得有序，请求出移位次数。如果不能则返回-1。

难度：easy

解法：可以找出第一个`nums[i]>nums[i+1]`的位置，在这个位置移位，把`nums[i+1]`移到`nums[0]`位置。检查移位后的结果是否有序。总代价`O(n)`。

<hr>

2859 Sum of Values at Indices With K Set Bits

题意：给定数组nums，请返回`sum(nums[i]), countOnes(i)==k`，下标i的二进制表示有k个1。

难度：easy

解法：水题。

<hr>

2860 Happy Students

题意：给定数组nums，你需要选一些学生。比如有k个学生被选中，那么，<b>费解的部分来了</b>。如果i学生被选中，则`k>nums[i]`；如果i学生没被选中，则`k<nums[i]`。请求出能满足这两条要求的选法。

难度：medium

解法：这题是<b>真看不懂</b>，不知道出题者怎么想出来的。首先，这个选择<b>和顺序无关</b>，我们可以随意排序。我们把nums<b>排序</b>，那么比如`nums[i]`被选中了，我有可能不选`nums[i-1]`吗？不可能的，必须选中。因此，我必须<b>选中一个前缀`nums[0:i+1]`</b>。按照这个逻辑，枚举所有位置i，检查题目给的那个<b>很难懂的条件</b>。总代价`O(nlogn)`。鉴定为<b>智力题+阅读理解题</b>。

<hr>

2864 Maximum Odd Binary Number

题意：给定01串s，请重排数位，使得结果是一个<b>最大的奇数</b>。返回结果。

难度：easy

解法：水题，拿出一个1，剩下部分倒序排列。

<hr>

2869 Minimum Operations to Collect Elements

题意：给定数组nums，每次你可以拿出最后一个元素。请问多少次可以凑齐`1~k`？

难度：easy

解法：水题。

<hr>

2870 Minimum Number of Operations to Make Array Empty

题意：给定数组nums，每次你可以选<b>2个或3个相同值</b>删除。请求出把数组<b>清空</b>的最小次数。如果做不到，则返回-1。

难度：medium

解法：对nums做<b>哈希计数</b>，对于每个唯一值的个数`cc`，我们考虑<b>删光的次数</b>。其实次数就是`(cc+2)//3`，但如果`cc==1`，则无法删除。所有次数求和，就是最终结果。总代价`O(n)`。

<hr>

2872 Maximum Number of K-Divisible Components

题意：有一个n节点的<b>无向图</b>，构成了<b>一棵树</b>。点集是`0~n-1`，边集是`[x,y]`形式。每个节点有分值`values[i]`。现在允许你删掉一些边，使得每个连通分量的<b>节点分值之和</b>是<b>k的倍数</b>。请求出最大的<b>连通分量个数</b>。

难度：hard

解法：我们先做第一个检查：`sum(values)%k==0`。所有加起来必须是k的倍数，否则无解。这是一棵<b>无根树</b>，根节点可以是任意点。我们可以随意选一个点作为根，进行<b>后序遍历</b>。遍历的重点是，求子树和，判断<b>子树和</b>是否`%k==0`。比如对于节点x，父节点是`p->x`，子树和是sm。那么，如果`sm%k==0`，我就应该切断`p->x`这条边。因为是<b>后序遍历</b>，我们在访问完这个子树后，才会<b>判断+切断</b>。这个方法可以保证<b>不论从哪个点出发</b>，能得到的划分都是最优的。关于<b>“切断边”</b>，其实你也可以通过`子树和=0`这种<b>赋值</b>，把这个子树给<b>丢弃了</b>。这就等价于<b>切断了这条边</b>。总代价`O(n)`。最终的答案就是`切断次数+1`。

<hr>

2873 Maximum Value of an Ordered Triplet I

题意：给定数组，请任选3个元素，求`max((nums[i]-nums[j])*nums[k])`。

难度：easy

解法：不用单独考虑<b>正负</b>的情况，我们可以枚举`nums[k]`，同时知道`nums[0:k]`范围内，同时求出`max(nums[i]-nums[j])`的值。那么这个`max_diff`怎么求呢？可以枚举`nums[j]`，然后求出`max(nums[i])`的值。`max(nums[i])`就是前缀max，可以O(n)代价求出。之后的两步也可以O(n)代价求出。而且这三件事，可以<b>一件一件做</b>。因此总代价还是`O(n)`的，而不是`O(n^3)`。想出这个`O(n)`解法，还是<b>有一定难度</b>的。

<hr>

2894 Divisible and Non-divisible Sums Difference

题意：给定整数n和m，请求出`[1,n]`范围内，m的倍数之和n1，其余数之和n2。返回`n1-n2`。

难度：easy

解法：<b>数学题</b>，总和是`n*(n+1)/2`，倍数和是`(n//m)*(n//m+1)/2*m`。

<hr>

2895 Minimum Processing Time

题意：你有n个处理器，每个有4核。现在给定m个单核任务，需要分配被处理器，处理过程中<b>不会切换核</b>。已知每个处理器有个<b>就绪时间`processorTime[i]`</b>，在这个时间之前不能处理任务。每个任务的耗时为`tasks[j]`。请求出完成所有任务的<b>最早时间</b>。

难度：medium

解法：第一念头，应该是<b>排序+贪心策略</b>。关键在于<b>怎么排序</b>。处理器时间肯定应该<b>升序排列</b>，这样<b>最早空闲</b>的，也<b>最早开始干活</b>。至于任务，则按照<b>长任务优先</b>，也就是<b>降序</b>。这样两者的匹配是最好的，<b>最终完成时间</b>可以做到<b>尽量平均</b>。这个思路是<b>出于直觉</b>，试了下确实OK。总代价`O(nlogn)`。

<hr>

2899 Last Visited Integers

题意：不知道在讲什么。

难度：easy

解法：水题，题目<b>非常难懂</b>。终于读懂之后，发现<b>确实很水</b>。

<hr>

2900 Longest Unequal Adjacent Groups Subsequence I

题意：给定长度为n的词表words和01数组groups。请选出一个最长的子序列`{i0,i1,...,ik}`，使得对应位置的groups元素按照`0101...`或者`1010...`<b>交替变化</b>。返回对应的words子序列。

难度：easy

解法：水题。对于groups，直接按照01交替，用<b>贪心原则</b>找出最长的子序列。把对应的<b>下标</b>记下来，返回`words[i]`子序列作为结果。总代价`O(n)`。
