def maxSlidingWindow(nums, k):
        max_upto =[0 for i in range(len(nums))]
        s = []
        s.append(0)
        for i in range(1, len(nums)):
            while(len(s)> 0 and nums[s[-1]]<nums[i]):
                max_upto[s[-1]]= i-1
                del s[-1]
            s.append(i)
        while (len(s)>0):
            max_upto[s[-1]]= len(nums)-1
            del s[-1]
        j=0
        mylist=[]
        for i in range(len(nums)-k+1):
            while(j<i or max_upto[j]< i+k-1):
                j+=1

            mylist.append(nums[j])
        return mylist
        
nums = [9, 7, 2, 4, 6, 8, 2, 1, 5] 
k = 3
print(maxSlidingWindow(nums,k)) 