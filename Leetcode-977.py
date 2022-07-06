nums = list(map(int,input().split()))
for i in range(len(nums)):
            nums[i] = nums[i]*nums[i]
print(sorted(nums))