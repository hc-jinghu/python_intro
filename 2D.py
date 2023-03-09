# 巢狀迴圈(nested loop), meaning while/for in while/for
# 2維列表, 2D list (similar concept to 2D array in C++)
nums = [
    [0,1,2,3],
    [7,4,3,5],
    [10,9,7,8],
    [6]
]

print(nums[1][1]) # 4
#print(nums[3][2]) # error. Index out of range

# print the whole list
for row in nums:
    for col in row:
        print(col)