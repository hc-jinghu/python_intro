# A simple number guessing game for practice

correct_num = 87
guess_num = int(input("遊戲開始！請猜數字："))  # default data type is string, must convert to int before comparison with integer
count = 1
out_of_limit = False

while not(out_of_limit) and guess_num!=correct_num:
    if guess_num<correct_num:
        guess_num = int(input("大一點："))
    else:
        guess_num = int(input("小一點："))
    count+=1
    if count>3:
        out_of_limit = True
if out_of_limit:
    print("再接再厲！")
else:
    print("恭喜答對！")