# LeetCode 一句话题解 - 3001-3500

[返回目录](./README.md)

- [LeetCode 一句话题解 - 3001-3500](#leetcode-一句话题解---3001-3500)
  - [3001 - 3100](#3001---3100)
  - [3101 - 3200](#3101---3200)

代码库地址：  
[https://github.com/zhuli19901106/leetcode-zhuli/tree/master/algorithms/3001-3500](https://github.com/zhuli19901106/leetcode-zhuli/tree/master/algorithms/3001-3500)

## 3001 - 3100

3005 Count Elements With Maximum Frequency

题意：给定数组nums，求出<b>频率最大</b>的元素的<b>频率之和</b>。

难度：easy

解法：水题。

<hr>

3010 Divide an Array Into Subarrays With Minimum Cost I

题意：给定数组nums，将其划分为3个子数组。每个数组的代价是<b>第1个元素</b>的值。请求出<b>最小总代价</b>。

难度：easy

解法：`nums[0]`必选，然后从`nums[1:n]`中找出<b>最小的两个值</b>。加起来就是答案。

<hr>

3011 Find if Array Can Be Sorted

题意：给定数组nums，如果两个相邻元素`(nums[i],nums[i+1])`二进制有<b>相同的1个数</b>，则允许交换它们。请问能否经过任意次交换，使得nums变成升序？

难度：medium

解法：先写一个`countOnes()`函数，统计1的个数。相邻交换，那么交换完了<b>还是相邻</b>。也就是说，不论你怎么交换，都是在一个<b>连续的局部范围内</b>。因此，我们可以按照相同的1个数，把nums分成多个<b>连续小组</b>。每个小组内，你都可以<b>升序排列</b>。如果<b>每个小组</b>排序完了之后，<b>整个数组也有序</b>，那就true；否则，false。这题算<b>半个智力题</b>，半个算法题。

<hr>

3014 Minimum Number of Pushes to Type Word I

题意：老式的9键手机键盘，见过吧？类似那种`2->abc`的映射。现在允许你把`a~z`自由分配到`2~9`上，得到一个<b>多对一映射</b>。请设计一个映射，使得输入单词word的<b>按键次数</b>最少。

难度：easy

解法：题目讲得挺啰嗦，但用过<b>九键键盘</b>的人，很容易想明白。比如`2->abc`，那么输入a按1次`2`，输入c则按3次`222`。因此，我把word里的字符尽量<b>分散放在第一位</b>，这就是最优的。如果还有多的，就分散放到第二位，依此类推。这题算是<b>模拟题</b>。

<hr>

3015 Count the Number of Houses at a Certain Distance I

题意：给定n个房子，顺着排成一排，编号`1~n`。每个`[i,i+1]`之间有一条<b>双向边</b>。除此之外，还有一条`[x,y]`双向边。给定`k=[1,n]`，请求出<b>两点最短距离等于k</b>的`(x,y)`的对数。

难度：medium

解法：直接按<b>全最短路径</b>处理就行，跑一个<b>Floyd算法</b>。不过，既然在链式的基础上，只额外添加了<b>一条边</b>，这题肯定有什么<b>巧妙解法</b>。反正我没想出来。看了评论区，好像也没有。

<hr>

3016 Minimum Number of Pushes to Type Word II

题意：3014的变体。题目<b>完全一样</b>，只有数据量不同。

难度：medium

解法：又是<b>改个数据量</b>就算两题的情况。好吧，题目虽然照抄，解法<b>并不完全一样</b>。我们按照字符频率，做个<b>倒序排列</b>。剩下就和3014一样。

<hr>

3019 Number of Changing Keys

题意：给定字符串s，统计`s.lower()`中，字符发生变化的次数。

难度：easy

解法：水题，注意理解题目。比如`abBDdaa`，变化了3次。

<hr>

3024 Type of Triangle

题意：给定三条边长，请判断<b>等边、等腰</b>还是普通三角形。

难度：easy

解法：水题。

<hr>

3028 Ant on the Boundary

题意：一只蚂蚁从0点出发，给定数组nums，每次移动`nums[i]`单位。请求出蚂蚁返回0点的次数，<b>路过不算</b>。

难度：easy

解法：水题，啰嗦且充满迷惑性。

<hr>

3033 Modify the Matrix

题意：给定m x n矩阵mat，把所有-1值的位置，替换为<b>本列的最大值</b>。

难度：easy

解法：水题，不过我读了两遍才搞明白<b>到底在问什么</b>。

<hr>

3034 Number of Subarrays That Match a Pattern I

题意：给定数组nums和一个模式数组pattern。pattern的元素按照`-1、0、+1`表示`降、等、升`。请找出nums中，符合pattern对应模式的子数组的个数。

难度：medium

解法：这题有点意思，既然我们关心的是<b>相邻元素</b>的比较，那我们先进行比较，得到一个`n-1`长的比较数组diff，其中也按照`-1、0、+1`这样取值。然后我们对diff和pattern做字符串匹配即可。没错，就是<b>KMP</b>那样的匹配。显然，与其手写KMP，不如用<b>正则</b>直接搞定。你可以把diff和pattern数组都转为<b>字符串格式</b>，这样就方便调用re模块了。这题出得很好，好在既有<b>算法难度</b>，又考察做事的<b>灵活性</b>。总代价`O(n+np)`。<b>重叠匹配</b>的写法可以记一下，有点巧妙，`re.findall(r'(?=(p))', s)`。

<hr>

3038 Maximum Number of Operations With the Same Score I

题意：给定数组nums，每次删除<b>开头两个元素</b>，并求和作为<b>分数</b>。持续删除，但是要求每次得到的<b>分数必须相同</b>。请求出能执行<b>几次操作</b>。

难度：easy

解法：水题。

<hr>

3039 Apply Operations to Make String Empty

题意：给定`a~z`组成的字符串s，每一轮，我们都找出`a~z`字符的<b>第一个出现位置</b>并删除。经过若干次，可以把s删光。请求出<b>最后一次</b>删除之前，s的值。

难度：medium

解法：这题很简单，你既然每次都是<b>删除“第一个”</b>，那么最后一个自然就是<b>最后删的</b>。我们找出`a~z`每个字符的<b>最后出现位置</b>，按次序拼起来。注意，只保留`频率==max(频率)`的字符。因为频率更小的字符，之前已经删光了，<b>不会留到最后</b>。

<hr>

3042 Count Prefix and Suffix Pairs I

题意：给定词表words，请求出`i<j`的对数，使得`words[i]`同时是`words[j]`的<b>前缀和后缀</b>。

难度：easy

解法：数据量很小，直接`O(n^2)`枚举即可。

<hr>

3043 Find the Length of the Longest Common Prefix

题意：给定两个整数数组arr1、arr2，请找<b>按数位算</b>，所有`(arr1[i],arr2[j])`的<b>最长公共前缀</b>。返回<b>长度</b>。

难度：medium

解法：这题直白的思路就是<b>枚举ij</b>，复杂度是`O(n1*n2)`。数据量告诉你太慢了。怎么优化呢？可以把所有整数都转为字符串，然后<b>存入字典树</b>中。再给字典树加一个arr1、arr2的<b>访问标记</b>。如果某个节点同时具有两个标记，则是一个有效的公共前缀。我们遍历字典树的所有节点，找出<b>具有两个标记</b>的<b>最深节点</b>，就等于找到最大长度了。这样的处理代价，对于<b>时间空间</b>，都是`O(nlogn)`。<b>实现麻烦</b>，但思路还比较容易。还有一种<b>更巧妙的办法</b>，我们把arr1和arr2的值都转为字符串，然后<b>混在一起</b>。按字典序<b>排序</b>，那么如果存在某个最长前缀，一定会发生在两个<b>字典序最接近</b>的<b>相邻元素</b>中。如此，我们只需要把排序后的所有相邻元素`(a[i],a[i+1])`进行比较，而且只比较其中<b>来源不同</b>的相邻元素。这个思路比字典树简单得多，总代价也是`O(nlogn)`。

<hr>

3046 Split the Array

题意：给定数组nums，请将其分为等长的两个数组nums1、nums2，要求两数组都没有<b>重复值</b>。请判断<b>能否做到</b>。

难度：easy

解法：水题，如果有一个值<b>出现超过2次</b>，就做不到。

<hr>

3065 Minimum Operations to Exceed Threshold Value I

题意：给定数组nums，每次你可以删除一个<b>最小值</b>。请问经过多少次，所有值都<b>不小于k</b>？

难度：easy

解法：水题，统计`<=k`的值的个数即可。

<hr>

3067 Count Pairs of Connectable Servers in a Weighted Tree Network

题意：有一个<b>树形的无向图</b>，表示服务器网络。n个点编号`0~n-1`，边的格式为`[x,y,w]`，表示<b>双向带权</b>的一条边。给定整数k，如果`a-c`的距离、`b-c`的距离都是<b>k的倍数</b>，且两<b>路径（可以由多条边构成）</b>没有共同的边，则称为<b>a和b通过c连通</b>。对于每个点`i=[0,n-1]`，请求出<b>通过i连通</b>的`(a,b)`对数。

难度：medium

解法：这是个<b>树形结构</b>，因此我们从某点i出发（作为根节点），通往任意j点的路径都是<b>唯一</b>的。那么，我们可以O(n)代价做一次遍历，统计出距离`dist%k==0`的个数。比如有`cc`个，那么对数就是`C(cc,2)=cc*(cc-1)/2`。对于每个点`i=[0,n-1]`，执行n次这样的遍历，总代价`O(n^2)`。这个思路不算复杂，但实现已经<b>挺麻烦了</b>。就这样吧，我想不出更好的办法了。

<hr>

3068 Find the Maximum Sum of Node Values

题意：有一个<b>树形的无向图</b>，n个点编号`0~n-1`，边的格式为`[x,y]`。每个点有分值`nums[i]`。现在你可以对任意边`[x,y]`执行一个操作，同时把`nums[x]`和`nums[y]`异或一个k值，也就是`^=k`。你可以执行<b>任意次操作</b>，请求出`max(sum(nums))`。

难度：hard

解法：这题其实是个<b>智力题</b>，而且需要按<b>图论的思维</b>先想一下才能发现。比如我对`[x,y]`执行操作，又对`[y,z]`执行操作，是不是<b>等价于</b>对`[x,z]`执行操作？发现了吗，这是<b>传递性</b>。因为一棵树，所有点都是连通的，因此我可以<b>随便传递</b>。也就是可以<b>任选两个元素</b>`(nums[i],nums[j])`，执行`^=k`的操作。那么我检查所有`nums[i]`，统计`nums[i]^k>nums[i]`的个数。如果偶数个，则<b>全部执行</b>；如果奇数个，则最后会<b>多余一个</b>。对多余的这个，还要和其他元素<b>尝试做一次</b>。如果结果变大了，那就做。这题属于中规中矩的hard，<b>脑力+体力并用</b>的一题。总代价`O(n)`。不得不说，这题的出题者，脑洞还是挺大的。

<hr>

3069 Distribute Elements Into Two Arrays I

题意：给定数组nums，你需要把它分成两个数组arr1、arr2。先把0和1元素分到arr1、arr2中。对于之后每个元素`nums[i]`，都把它分到<b>末尾元素更大</b>的那个数组中。最后返回`arr1+arr2`。

难度：easy

解法：水题。

<hr>

3070 Count Submatrices with Top-Left Element and Sum Less Than k

题意：给定m x n矩阵grid，所有元素<b>非负</b>。请求出左上是`(0,0)`，子矩阵和<b>不超过k</b>的所有<b>子矩阵个数</b>。

难度：medium

解法：直接用<b>二维前缀和</b>的思路，可以求出每个右下角为`(i,j)`的子矩阵和。`sm[i][j]=sm[i][j-1]+sm[i-1][j]+grid[i][j]-sm[i-1][j-1]`，总代价`O(mn)`。

<hr>

3071 Minimum Operations to Write the Letter Y on a Grid

题意：有一个n x n矩阵，n是奇数，表示一个<b>像素屏幕</b>。现在你需要画出一个<b>“Y”图案</b>。也就是右下、左下、下这三笔，而且<b>不能旋转</b>。已知屏幕上的像素点有0、1、2三种值。要求Y部分的像素必须取<b>同一值x</b>，非Y部分的像素必须取<b>同一值y</b>，且`x!=y`。每次你可以<b>修改一个像素</b>，请求出最小的修改次数。

难度：medium

解法：很麻烦的一道<b>模拟题</b>。统计<b>Y部分</b>的012个数，再统计<b>非Y部分</b>的012个数。然后选一个<b>修改总和最小</b>的`(x,y)`组合。没有难度，单纯就是麻烦，总代价`O(n^2)`。

<hr>

3074 Apple Redistribution into Boxes

题意：有n包苹果，每包有`apple[i]`个。有m个箱子，每个容量为`capacity[j]`。你需要把苹果撞到箱子里，用尽可能少的箱子。如果苹果包<b>可以拆开</b>，请求出最少的箱子个数。

难度：easy

解法：水题。`sum(apple)`，`capacity.sort(reverse=True)`，然后看看几个箱子能<b>装完</b>。

<hr>

3075 Maximize Happiness of Selected Children

题意：给定n个小朋友，每个的快乐值是`happines[i]`。你需要选k个，每次选择，所有未被选中的小朋友，<b>快乐值`-1`，至多减到0</b>。请求出k人的<b>最大快乐值总和</b>。

难度：medium

解法：显然，按`happiness`<b>降序排列</b>，答案就是最优的。我不知道这题为什么是medium，这个贪心思路<b>100%符合直觉</b>，很容易想到。总代价`O(nlogn)`。

<hr>

3079 Find the Sum of Encrypted Integers

题意：给定nums，把每个元素`nums[i]`的每一位，都换成它的最大位。返回<b>总和</b>。

难度：easy

解法：水题。

<hr>

3083 Existence of a Substring in a String and Its Reverse

题意：给定字符串s，请找出在`s、reverse(s)`中都存在的<b>长度为2</b>的子串。只判断<b>是否存在</b>即可。

难度：easy

解法：水题。

<hr>

3090 Maximum Length Substring With Two Occurrences

题意：给定字符串s，请求出<b>每种字符不超过2个</b>的最长子串的长度。

难度：easy

解法：滑动窗口+双指针，这都<b>贬值到easy难度</b>了？厉害。

<hr>

3095 Shortest Subarray With OR at Least K I

题意：给定数组nums，请找出其中<b>最短的</b>，异或结果`>=k`的子数组的长度。不存在则返回-1。

难度：easy

解法：数据很小，直接`O(n^2)`枚举即可。

<hr>

3097 Shortest Subarray With OR at Least K II

题意：3095的变体。和3095完全一样，就是<b>数据量不同</b>。

难度：medium

解法：我们需要一个`O(n)`的解法。想到一个<b>滑动窗口+双指针</b>的思路，但<b>有点巧妙</b>，因为你<b>不能直接用</b>滑动窗口。为什么？因为<b>按位或</b>这个操作是没有<b>直接逆运算</b>的。没有逆运算，你怎么<b>缩小窗口</b>。那怎么处理？我们可以<b>按位进行计数</b>，每当`0->1`时，则`^`异或一下；每当`1->0`时，也`^`异或一下。这个操作，就<b>等价于</b>给按位或执行了<b>逆运算</b>。这样，总体代价不再是`O(n)`，而是`O(nlog(int))`。至于双指针怎么滑动，很简单。我用i在前、j在后。i扩大窗口，使得`按位或>=k`；j缩小窗口，使得`按位或`<b>恰好</b>`>=k`。这样，得到的窗口就是<b>最小的</b>。这题确实<b>挺难</b>，我也不知道，我以前怎么想到这种<b>诡异思路</b>的。

<hr>

3099 Harshad Number

题意：给定整数x，如果`x%sumDigits(x)==0`，则称为<b>Harshad数</b>。如果是Harshad数，则返回<b>数位和</b>；否则返回-1。

难度：easy

解法：按定义，求<b>数位和</b>，看是否整除即可。

<hr>

3100 Water Bottles II

题意：1518的变体。你有nb瓶汽水，每次你可以用ne个空瓶子换1瓶汽水。但<b>每换1次</b>，则`ne+=1`。如果你可以自由安排<b>喝水、换瓶子的策略</b>，请求出能喝到的<b>最大瓶数</b>。

难度：medium

解法：还是<b>喝汽水、换瓶子</b>的问题。第一念头肯定是<b>模拟</b>，这题的数据量<b>确实很小</b>，直接模拟吧。纯模拟的总代价是`O(sqrt(nb))`。其实<b>数学解法</b>也不难，我们考虑nb和ne，那么我换瓶子的策略总是<b>攒够了就换</b>。于是，我按照`ne,ne+1,ne+2,...`这样求和，直到超过nb为止。等差数列求和，求个数，相当于<b>解一元二次方程</b>，代价为`O(1)`。持续模拟，至多`O(log(nb))`次就能完成。对于很大的`nb、ne`值，也能轻松解决。

## 3101 - 3200

3101 Count Alternating Subarrays

题意：给定01数组nums，对于一个子数组，如果没有相邻元素相等，则称为<b>交替子数组</b>。请求出交替子数组的个数。

难度：medium

解法：扫一次就行了，对于长度为cc的交替子数组，其中包含了`cc*(cc+1)/2`个。找出每段<b>最长的交替长度</b>，求和就是最终答案。总代价`O(n)`。

<hr>

3105 Longest Strictly Increasing or Strictly Decreasing Subarray

题意：给定数组nums，找出最长的<b>单调递增或单调递减</b>子数组的长度。

难度：easy

解法：扫一次就行了。总代价`O(n)`。可以针对递增、递减分别扫，也可以按照当前`(nums[i],nums[i+1])`的大小来决定<b>是递增还是递减</b>。总代价`O(n)`。

<hr>

3106 Lexicographically Smallest String After Operations With Constraint

题意：给定等长的字符串s和t，定义`dist(s,t)=sum(dist(s[i],t[i]))`。单个字符的距离，按照`a~z`的<b>循环最短距离</b>为准。比如`(a,b)`和`(a,z)`的距离都是1。现在给定s，请找出符合`dist(s,t)<=k`的<b>字典序最小</b>的t。

难度：medium

解法：字典序最小，显然你应该从<b>前面</b>开始变，而且要把字符<b>尽量变小</b>。这个可以按<b>贪心原则</b>处理。对于每个位置`s[i]`，如果<b>当前剩余距离</b>是cc，则考虑cc是否<b>足够</b>把`s[i]`变成`a`。如果够，就继续处理<b>下一个字符</b>；如果不够，那么这就是<b>最后一个变化</b>了。总代价`O(n)`。

<hr>

3110 Score of a String

题意：给定字符串s，请求出`sum(|s[i]-s[i+1]|)`。

难度：easy

解法：水题。

<hr>

3111 Minimum Rectangles to Cover Points

题意：给定一些点`[xi,yi]`，你需要用一些矩形来覆盖它们。每个矩形<b>左下角是都在x轴上</b>，右上角任意，但要求`宽度<=w`。点落在内部或者边缘，都算覆盖。请求出覆盖所有点，<b>最少</b>需要的矩形个数。

难度：medium

解法：其实这题是迷惑你的，y坐标根本无所谓，因为题目没有<b>对y做任何限制</b>，你可以认为`y=+inf`。我们只需要考虑<b>所有x坐标</b>，用多少个<b>不超过w宽度的区间</b>，可以包含进去。那么，首先对x坐标<b>升序排列</b>。对于每个起点`x[i]`，我都二分搜索`j=bisect_right(ax,x[i]+w)`。一直这样搜，搜到末尾为止。看总共搜了几段，就需要几个矩形。总代价`O(nlogn)`。<b>ij二分搜索</b>也可以改为<b>ij双指针</b>，结果是一样的，大同小异。

<hr>

3114 Latest Time You Can Obtain After Replacing Characters

题意：给定`HH:MM`格式的时间，<b>12小时制</b>。你需要把其中的`?`换成数字，请求可能得到的最晚时间。

难度：easy

解法：水题。

<hr>

3115 Maximum Prime Difference

题意：给定数组nums，请求出其中两个<b>质数元素</b>的<b>下标之差</b>的最大值。

难度：medium

解法：找出其中<b>所有质数</b>，记录下标。把`最后位置-最前位置`就是答案。其实，找出<b>第一个和最后一个</b>质数就行了。总代价`O(n*sqrt(max(nums)))`。

<hr>

3120 Count the Number of Special Characters I

题意：给定字符串word，如果某字母的大小写都出现了，则称为<b>特别字母</b>。请统计特别字母的个数。

难度：easy

解法：水题。

<hr>

3127 Make a Square with the Same Color

题意：给定一个3 x 3的BW方阵，B黑W白。你可以改变至多1个点的颜色，请问能否得到一个2 x 2的同色方阵？

难度：easy

解法：水题。

<hr>

3131 Find the Integer Added to Array I

题意：给定数组nums1、nums2，已知`sorted(nums1)`和`sorted(nums2)`对应元素都相差同一个值x，请求出x。

难度：easy

解法：水题。排序之后，`sorted_nums2[0]-sorted_nums1[0]`即可。

<hr>

3133 Minimum Array End

题意：给定整数n和x，你需要构造一个严格递增的数组nums。nums的长度为n，且`and(nums)==x`。请求出`nums[n-1]`的最小值。

难度：medium

解法：所有元素的<b>按位与</b>等于x，那么比如x是一个<b>二进制p位数</b>，其中有<b>q个0</b>。我为什么关心这个？因为我知道这些元素在`p-q`位上，必须全取1，在剩下的q位上，则<b>可0可1</b>。q位0，总共有`2**q`种组合。那么如果`n>2**q`，就<b>无解</b>了，因为这<b>不够用</b>。如果`n<=2**q`，我可以`0`枚举到`n-1`。但是我要做个<b>奇怪的事情</b>，就是把这q位数，<b>穿插</b>到<b>对应的位置</b>上去。比如举例子`1001100`，我把`1011`穿插到0位置上去，结果就是`1101111`。这样得到的`nums[n-1]`一定是<b>最小的</b>。总代价`O(logn)`。

<hr>

3136 Valid Word

题意：给定字符串word，请判断是否满足以下条件：至少3字符，只包含数字或字母，有至少一个元音和辅音。

难度：easy

解法：水题。

<hr>

3137 Minimum Number of Operations to Make Word K-Periodic

题意：给定字符串word，长度为n。给定整数k，且`n%k==0`，每次你可以位置`(i,j)`，执行`word[i:i+k]=word[j:j+k]`，也就是替换k长度的一个子串。请问至少多少次操作，能让word变为k周期串，也就是以k长度的子串<b>重复而成</b>。

难度：medium

解法：这题的题目描述很费劲，但读懂题目后会发现<b>其实很简单</b>。我们只要把k长度的子串，视为一个<b>“单值”</b>即可。那么，总共有`n/k`个这样的值，做<b>哈希计数</b>，找出最大频率`max_cc`。为了使所有`n/k`个值相同，我需要改变其他`n/k-max_cc`个值，这就是答案。总代价`O(n)`。

<hr>

3142 Check if Grid Satisfies Conditions

题意：给定m x n矩阵，请检查每一格`grid[i][j]`是否等于<b>下方一格</b>，是否不等于<b>右边一格</b>。请判断是否<b>每格</b>都满足这个条件。

难度：easy

解法：水题。

<hr>

3146 Permutation Difference between Two Strings

题意：给定<b>同一组字符集</b>的两个排列s和t。我们定义<b>排列差值</b>为每个字符在两串中<b>出现位置的差值</b>之和。请求出排列差值。

难度：easy

解法：按题目定义，用<b>哈希表</b>记录字符的<b>出现位置</b>，求差值并求和`sum(abs(ms[c]-mt[c]))`。总代价`O(n)`。

<hr>

3151 Special Array I

题意：给定数组nums，请判断所有<b>相邻元素对</b>，是否<b>奇偶性都不同</b>。

难度：easy

解法：水题。

<hr>

3158 Find the XOR of Numbers Which Appear Twice

题意：给定数组nums，请求出其中<b>出现了2次</b>的元素的<b>异或</b>。

难度：easy

解法：水题。

<hr>

3159 Find Occurrences of an Element in an Array

题意：给定数组nums和整数x，你需要执行m次查询，每次查询给出x值在nums中的第`queries[i]`次出现下标。次数<b>从1算起</b>。如果超出最大次数，则返回-1。

难度：medium

解法：把x的所有出现位置<b>记下来</b>就行了。这题定级medium不合适，思路过于简单了。总代价`O(n+nq)`。

<hr>

3162 Find the Number of Good Pairs I

题意：给定数组nums1、nums2，整数k。请找出符合`nums1[i]%(nums2[j]*k)==0`的`(i,j)`对数。

难度：easy

解法：水题，直接枚举即可。

<hr>

3163 String Compression III

题意：443的变体。还是做类似<b>游程码</b>的压缩，但这次格式为`aaa->3a`，且每次个数<b>至多是9</b>。给定字符串s，请返回压缩结果。

难度：medium

解法：既然还是游程码，只是<b>规则稍微改动</b>，那依然简单。按规则处理即可。总代价`O(n)`。

<hr>

3168 Minimum Number of Chairs in a Waiting Room

题意：给定字符串s，由`EL`组成。`E`表示来人，需要板凳；`L`表示离开，让出板凳。请求出<b>最少需要的</b>板凳数量，保证每个人都<b>有地方坐</b>。

难度：easy

解法：其实就是类似<b>进栈出栈</b>的思维，E进L出，用一个计数`cc`表示就够了。答案就是`max(cc)`。总代价`O(n)`。

<hr>

3174 Clear Digits

题意：给定字符串s，每次你可以删除<b>最左的数字</b>，同时删除它<b>左边最接近</b>的<b>非数字字符</b>。如果找不到这样的组合，则停止。请返回最终结果。

难度：easy

解法：用栈处理，如果`st[-2]`是<b>字母</b>且`st[-1]`是<b>数字</b>，则一起`pop()`。总代价`O(n)`。题目<b>保证</b>可以删光所有数字，因此我们可以不考虑<b>很多边界case</b>。

<hr>

3178 Find the Child Who Has the Ball After K Seconds

题意：n个小朋友，编号`0~n-1`，按照`0->1->...->n-1->n-2->...->0`这样往复传球。请问<b>k步之后</b>，谁拿到球？

难度：easy

解法：水题。这题和2582<b>完全相同</b>，这么<b>抄袭</b>难道不违规吗？

<hr>

3179 Find the N-th Value After K Seconds

题意：给定数组a，初始状态是<b>n个1</b>，`[1,1,...,1]`。每次操作，你把`a[i]`<b>同时变为</b>`sum(a[0:i+1])`，也就是<b>前缀和</b>。经过k步后，请求出`a[n-1]`，结果模`1e9+7`返回。

难度：medium

解法：显然这是个<b>数学题</b>。你看例子，就容易<b>找到规律</b>。结果就是`C(n+k-1,k)=(n+k-1)/((n-1)!(k!)!)`。这个要<b>取模</b>，还得做<b>除法</b>。为计算结果，你至少需要求出`k!`对于`1e9+7`的<b>逆元</b>。如果你不想处理<b>欧几里得算法</b>（很多人会写gcd()，但不会写扩展`gcd()`算法），也可以用常规的<b>递推求和</b>。递推解法，总代价`O(nk)`；数学解法，总代价`O(n+k)`。

<hr>

3184 Count Pairs That Form a Complete Day I

题意：给定数组hours，请找出`(hours[i]+hours[j])%24==0, i<j`的`(i,j)`对数。

难度：easy

解法：水题。

<hr>

3190 Find Minimum Operations to Make All Elements Divisible by Three

题意：给定数组nums，每次你可以任选一个元素，+1或-1。请问多少次操作可以使所有元素都是3的倍数？

难度：easy

解法：水题。余数只能是<b>1或2</b>，对应<b>-1或者+1</b>就可以变成余数0。因此，次数就等于<b>余数不为0的个数</b>。总代价`O(n)`。

<hr>

3191 Minimum Operations to Make Binary Array Elements Equal to One I

题意：给定01数组nums，每次你可以选<b>连续3个值反转</b>。请问至少多少次，能把所有值变成1？如果不可能，则返回-1。

难度：medium

解法：<b>从左到右</b>，按<b>贪心原则</b>处理即可。比如遇到<b>第一个</b>`nums[i]==0`，则反转`(i,i+1,i+2)`。如果反转到最后，恰好变成了<b>全1</b>，则返回<b>反转次数</b>；否则，返回-1。

<hr>

3192 Minimum Operations to Make Binary Array Elements Equal to One II

题意：3191的变体。依然是反转，但这次操作是反转`nums[i:n]`<b>整个后缀</b>。请求出把nums变成全1的最小次数。

难度：medium

解法：其实这题比3191<b>更简单</b>，我只需要从后往前，考虑连续的<b>0段、1段、0段、1段</b>这样交替。而且我不关心<b>每段有多少个0或1</b>，因为不论多少个，都是<b>1次翻转</b>搞定。比如我有`10101`这样5段，除了最左的`1`段，后面4段都要反转，共4次。比如我有`010`这样3段，则<b>从右往左</b>3段都要反转，共3次。反转过程是`010->011->000->111`。总代价`O(n)`。

<hr>

3194 Minimum Average of Smallest and Largest Elements

题意：给定数组nums，长度n为偶数。每次从nums中取出min和max，并把`(min+max)/2`加入结果`res`中。请求出`max(res)`。

难度：easy

解法：水题，对nums<b>排序</b>，从两边向中间靠拢。

<hr>

3195 Find the Minimum Area to Cover All Ones I

题意：给定m x n的01矩阵grid，请找出一个最小的子矩阵，使得子矩阵包含了<b>所有1值</b>。

难度：medium

解法：记录所有<b>1值出现位置`(i,j)`</b>的`min_i、max_i、min_j、max_j`即可。这就是边界，<b>计算面积</b>并返回。

<hr>

3200 Maximum Height of a Triangle

题意：你有red个红球，blue个蓝球。你需要堆一个金字塔，按照每层`1,2,3,...`这样递增。要求<b>单层</b>颜色相同，且<b>相邻层</b>颜色不同。请求出<b>最大层数</b>。

难度：easy

解法：数据量很小，<b>直接模拟</b>即可。按照<b>红蓝红</b>或者<b>蓝红蓝</b>都处理一遍。总代价`O(sqrt(n))`。
