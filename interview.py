def belt_rotation(arr):
	counter = 0
	while(counter < len(arr)/2):
		new_len = len(arr) -1 - counter
		if counter % 2 == 0:
			arr = cw_rotate(arr, counter, new_len)
		else:
			arr = ccw_rotate(arr, counter, new_len)
		counter +=1
	return arr

def cw_rotate(arr, counter, new_len):
	print counter, new_len
	ul, ur, dr, dl = arr[counter][counter], arr[counter][new_len], arr[new_len][new_len], arr[new_len ][counter]
	print ul, ur, dr, dl
	arr = l_r(arr, counter, counter, ul, counter, new_len) #(1,4)
	arr = u_d(arr, counter, new_len, ur, counter, new_len) #(1,4)
	arr = r_l(arr, new_len, new_len, dr, counter, new_len) #(1,4)
	arr = d_u(arr, new_len, counter, dl, counter, new_len) #(1,4)
	return arr

def ccw_rotate(arr, counter, new_len):
	print counter, new_len
	ul, ur, dr, dl = arr[counter][counter], arr[counter][new_len], arr[new_len][new_len], arr[new_len ][counter]
	print ul, dl, dr, ur
	arr = u_d(arr, counter, counter, ul, counter, new_len) #(1,4)
	arr = l_r(arr, new_len, counter, dl, counter, new_len) #(1,4)
	arr = d_u(arr, new_len, new_len, dr, counter, new_len) #(1,4)
	arr = r_l(arr, counter, new_len, ur, counter, new_len) #(1,4)
	return arr

def l_r (arr, i, j, ul, counter, new_len):
	temp1 = ul
	while (j < new_len):
		temp2 = arr[i][j+1]
		arr[i][j+1] = temp1
		temp1 = temp2
		j += 1
	return arr

def u_d (arr, i, j, ur, counter, new_len):
	temp1 = ur
	while (i < new_len):
		temp2 = arr[i+1][j]
		arr[i+1][j] = temp1
		temp1 = temp2
		i += 1
	return arr

def r_l (arr, i, j, dr, counter, new_len):
	temp1 = dr
	while (j > counter):
		temp2 = arr[i][j-1]
		arr[i][j-1] = temp1
		temp1 = temp2
		j -= 1
	return arr

def d_u (arr, i, j, dl, counter, new_len):
	temp1 = dl
	while (i > counter):
		temp2 = arr[i-1][j]
		arr[i-1][j] = temp1
		temp1 = temp2
		i -= 1
	return arr

arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
belt_rotation(arr)

#######################################################################################

def all_unique_or_not(line):
	set_=set()
	for i in line:
		if i !='.':
			if int(i) in set_:
				return False
			set_.add(int(i))
	return True

def sudoku2(grid):
	for line in grid:
		if not all_unique_or_not(line):
			return False
	
	for column_num in xrange(9):
		column = [grid[i][column_num] for i in xrange(9)]
		if not all_unique_or_not(column):
			return False
	
	for i in range(0,9,3):
		for j in range(0,9,3):
			if not all_unique_or_not(grid[i][j:j+3]+grid[i+1][j:j+3]+grid[i+2][j:j+3]):
				return False    
	return True

grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
		['.', '.', '6', '.', '.', '.', '.', '.', '.'],
		['.', '.', '.', '.', '.', '.', '.', '.', '.'],
		['.', '.', '1', '.', '.', '.', '.', '.', '.'],
		['.', '6', '7', '.', '.', '.', '.', '.', '9'],
		['.', '.', '.', '.', '.', '.', '8', '1', '.'],
		['.', '3', '.', '.', '.', '.', '.', '.', '6'],
		['.', '.', '.', '.', '.', '7', '.', '.', '.'],
		['.', '.', '.', '5', '.', '.', '.', '7', '.']]
sudoku2(grid)

#######################################################################################

# Failed_over_time_limit version 
def sumInRange(nums, queries):
	nums_count = [0 for i in xrange(len(nums))]
	
	for q in queries:
		for increment_index  in range(q[0],q[1]+1):
			nums_count[increment_index] += 1
	
	sum_ = 0
	for _ in xrange(len(nums)):
		sum_ += nums[_]*nums_count[_]

	return sum_%(1000000007)


# Success!
def sumInRange(nums, queries):
	prefix_sum=[0]
	sum_so_far = 0
	for num in nums:
		sum_so_far += num
		prefix_sum.append(sum_so_far)
		
	total_sum = 0
	for qurie_set in queries:
		start = qurie_set[0]
		end = qurie_set[1] + 1
		total_sum += prefix_sum[end] - prefix_sum[start]
	return total_sum % 1000000007

#######################################################################################

def findLongestSubarrayBySum(s, arr):
	i, j, longest_length, temp_sum = 0,0,0,0
	while (j<len(arr) and i <len(arr)):
		if temp_sum < s:
			temp_sum += arr[j]
			j+=1
		if temp_sum > s:
			temp_sum -= arr[i]
			i+=1
		if temp_sum == s:
			print "i:", i,"j:", j 
			if j - i > longest_length:
				longest_length = j - i 
				longest_set = [i+1,j]
			if j < len(arr):
				temp_sum += arr[j]
				j+=1
	if longest_length == 0:
		return [-1]   
	return longest_set

arr = [0,3,0]
s=3
findLongestSubarrayBySum(s, arr)

#######################################################################################

def productExceptSelf(nums, m):
	prefix_prod = [1] * len(nums)
	suffix_prod = [1] * len(nums)
	result = 0
	for i in range(1,len(nums)):
		prefix_prod[i] = (nums[i-1]*prefix_prod[i-1] )%m
		suffix_prod[-i-1] = (nums[-i]*suffix_prod[-i] )%m
	for i in xrange(len(nums)):
		result += (prefix_prod[i]%m * suffix_prod[i]%m) %m
	return result

#######################################################################################

def minSubstringWithAllChars(s, t):
	if len(t)==1 or len(t)==0:
		return t
	check_t_used = [0 for i in xrange(len(t))]
	runner, mark, start, flag=0,0,0,0
	min_len = len(s) +1
	result =""
	while(runner<len(s)):
		if s[runner] in t:
			flag +=1
			check_t_used[t.index(s[runner])] =1
			if flag == 2:
				mark = runner   
		if sum(check_t_used)== len(t):
			print s[start:runner+1], runner-start
			if runner - start < min_len:
				min_len = runner - start
				result = s[start:runner+1]
				print result
			check_t_used = [0 for i in xrange(len(t))]
			runner = mark
			start = mark
			flag =0
			continue
		print start, mark, runner, check_t_used
		runner+=1
	return result


s = "adobecodebanc" 
t = "abc"

s = "adobjcodebanc" 
t = "j"
minSubstringWithAllChars(s, t)

#######################################################################################

def arrayMaxConsecutiveSum2(arr):
	sum_=0
	result = -1001
	for num in arr:
		sum_+=num
		if sum_>result:
			result= sum_
		if sum_<0:
			sum_=0
	return result

#######################################################################################

def arrayMaxConsecutiveSum3(arr):
	sum_=0
	result = -1001
	start_ix = 0
	end_ix = 0
	i = 0
	for num in arr:
		sum_ += num
		if sum_>result:
			result= sum_
			end_ix = i
		if sum_<0:
			sum_=0
			start_ix = i + 1
		i = i+1
	return [result, start_ix, end_ix]

		
#######################################################################################

def sumOfTwo(a, b, v):
	a=set(a)
	b=set(b)
	for num in a:
		if (v-num) in b:
			return True
	return False
		

#######################################################################################
#More efficient method for http://www.geeksforgeeks.org/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri/

def maxIndexDiff(a):
	i=0
	j=len(a)-1
	while (j-i>-len(a)):
		if a[i]<a[j]:
			return (j-i)
		else:
			if a[i]<a[j-1]:
				return j-1-i
			if a[i+1]<a[j]:
				return j-(i+1)
			else:
				i+=1


a=[34, 8, 10, 3, 2, 80, 30, 33, 1]
maxIndexDiff(a)

a=[9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
maxIndexDiff(a)

a=[1, 2, 3, 4, 5, 6]
maxIndexDiff(a)

a=[6, 5, 4, 3, 2, 1]
maxIndexDiff(a)


#######################################################################################
def non_adjacent_max_sum(a):
	res=0
	i=0
	sum1=0
	sum2=0

	while (i <= len(a)-4):
		if a[i+3]>a[i+2]+a[i+4]:
			sum1+=a[i+3]
			i=i+3
		else:
			sum1+=a[i+2]
			i=i+2
	if i== len(a)-3:
		sum1+=a[-1]

	i=1
	while (i <= len(a)-4):
		if a[i+3]>a[i+2]+a[i+4]:
			sum2+=a[i+3]
			i=i+3
		else:
			sum2+=a[i+2]
			i=i+2
	if i== len(a)-3:
		sum1+=a[-1]

	return max(sum1,sum2)

arr = [5, 5, 10, 100, 10, 5]
print non_adjacent_max_sum(arr)


#######################################################################################


def mapDecoding(digits):
	if len(digits) == 0:
		return 1
	n = len(digits)
	count = [0] * (n+1)
	count[0] = 1
	count[1] = 1 if int(digits[0]) >= 1 else 0
	if len(digits) == 1:
		return count[1] 
	for i in range(2,n+1):
		if (int(digits[i-1]) > 0):
			count[i] = count[i-1]         
		if (0 < int(digits[i-2]) < 2 or (digits[i-2] == '2' and int(digits[i-1]) < 7)):
			count[i] *= count[i-2]            
		count[i] = count[i] % (10**9 + 7)        
	return count[n]

#######################################################################################


def knapsack_0_1(weight,value,weight_limit):
	num_row = len(weight)
	num_col = weight_limit+1
	value_mat = [[0 for i in xrange(num_col)] for j in xrange(num_row)]

	for i in range(1,num_row):
		for w in range(1,num_col):
			print value_mat
			print i,w
			if weight[i] <= w:
				max(value[i] + value_mat[i-1][w-weight[i]], value_mat[i-1][w])
			else:
				value_mat[i][w] = value_mat[i-1][w]
	print value_mat
	return value_mat[num_row -1][num_col -1]


weight = [0,2,3,4,5]
value = [0,3,4,5,6]
weight_limit = 5 
knapsack_0_1(weight,value,weight_limit)


#######################################################################################


def logNSearchRotatedArr(arr):
	




weight = [0,2,3,4,5]
value = [0,3,4,5,6]
weight_limit = 5 
knapsack_0_1(weight,value,weight_limit)



#############################################################################

"""
The idea is to use modified binary search.
If your arr[mid+1]>arr[mid] then your peak ALWAYS exists on the right half.
If you arr[mid-1]>arr[mid] then your peak ALWAYS exists on the left half.
Because arr[i+1] have only two options, either bigger than arr[i] or smaller than arr[i-1]
"""


def FindAPeak(arr, i, j):
	mid = (i+j)/2
	# if mid element is peak
	if (mid == len(arr)-1 or arr[mid] > arr[mid+1]) and (mid == 0 or arr[mid] > arr[mid-1]):
		return arr[mid]
	# when your peak exists in the right half
	if arr[mid] < arr[mid+1] and mid+1 < len(arr):
		return FindAPeak(arr, mid+1, j)
	# when your peak exists in the left half
	else:
		return FindAPeak(arr, i, mid-1)


arr = [1,2,3,2,1]
FindAPeak(arr, 0, len(arr)-1)


arr = [1,2,3,4,5,6]
FindAPeak(arr, 0, len(arr)-1)


#############################################################################

def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r- m
 
	L = arr[l:m+1]
	R = arr[m+1:r+1]
 
	i = 0     # Initial index of first subarray
	j = 0     # Initial index of second subarray
	k = l     # Initial index of merged subarray

	while i < n1 and j < n2 :
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1
 
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1
 
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1
 

def mergeSort(arr,l,r):
	if l < r:
		m = (l+r)/2
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)
 
arr = [12, 11, 13, 5, 6, 7]
print arr
 
mergeSort(arr,0,len(arr)-1)
print arr
 
#############################################################################

global count
count = 0
def merge(arr, l, m, r):
	global count 
	n1 = m - l + 1
	n2 = r- m
 
	L = arr[l:m+1]
	R = arr[m+1:r+1]
 
	i = 0     # Initial index of first subarray
	j = 0     # Initial index of second subarray
	k = l     # Initial index of merged subarray
	print i,j,k
	while i < n1 and j < n2 :
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			count += len(L)-i
			arr[k] = R[j]
			j += 1
		k += 1
 
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1
 
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1


def countInversion(arr,l,r,ct):
	if l < r:
		m = (l+r)/2
		_ = countInversion(arr, l, m, ct)
		_ = countInversion(arr, m+1, r, ct)
		merge(arr, l, m, r)

 
arr = [12, 11, 13, 5, 6, 7]
countInversion(arr,0,len(arr)-1,0)
count

arr = [4, 1, 3, 2, 9, 5]
countInversion(arr,0,len(arr)-1,0)
 
##################################################################


def fillingBlocks(n):
	memo = {0:1, 1:1, 2:5, 3: 11}
	for i in range(4, n+1):
		memo[i] = memo[i-1]+5*memo[i-2]+memo[i-3]-memo[i-4]
	return memo[n]


##################################################################
"""
For nums = [-1, 0, 1, 2, 6, 7, 9], the output should be
composeRanges(nums) = ["-1->2", "6->7", "9"].
"""
def composeRanges(nums):
	runner, start, end = 0, 0, 0
	res = []
	while runner < len(nums):
		end = runner
		while runner + 1 < len(nums) and nums[runner+1] == nums[runner] + 1:
			runner += 1
		if runner == end:
			res.append(str(nums[runner]))
		else:
			res.append("%d->%d" % (nums[start], nums[runner]))
		start = runner +1
		runner += 1
	return res

##################################################################

def houseRobber(arr):
	if len(arr)==0:
		return 0
	if len(arr)==1:
		return arr[0]
	presum = [0 for i in xrange(len(arr))]
	presum[0]=arr[0]
	for i in xrange(1,len(arr)):
		presum[i] = max(presum[i-2] + arr[i], presum[i-1])
	return presum[-1]

nums = [1, 1, 1]
houseRobber(nums)


##################################################################
def climbingStaircase(n, k):
    res=[]
    CSR(n,k,[],res)
    return res

def CSR(n,k,str_, res):
    if n == 0:
        res.append(str_)
    else:
        for i in range(1,k+1):
            if n-i>=0:
                CSR(n-i,k,str_+[i],res)


##################################################################

def climbingStaircase(n, k, wip):
	if n == 0 :
		print wip
	else:
		for i in range(1,k+1):
			if n>=i:
				wip.append(i)
				climbingStaircase(n-i, k, wip)
				wip.pop()

climbingStaircase(4, 2,[])
