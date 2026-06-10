n=int(input())
nums=list(map(int,input().split()))
max_val=0
max_index=0
for i,num in enumerate(nums):
    if num>max_val:
        max_val=num
        max_index=i
print(max_val,max_index+1)
