# LeetCode 一句话题解 - 2501-3000

[返回目录](./README.md)

- [LeetCode 一句话题解 - 2501-3000](#leetcode-一句话题解---2501-3000)
  - [2501 - 2600](#2501---2600)

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

解法：这是什么<b>诡异的位运算</b>？共有`n^3`种组合，求异或。这题我卡了很久，想了半天想不出什么巧妙的思路。但我肯定这题是个<b>智力题</b>。最后<b>瞎猜</b>`xor(nums)`，猜对了。我没法解释，就是猜的。总代价`O(n)`。我觉得出题人应该<b>及时就医</b>。

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
