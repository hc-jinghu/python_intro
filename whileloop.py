# while迴圈
# examples to show while loop in python syntax

# practice: 寫出一串星期幾跟Erin吃飯的string
#   1. using match and case to setup the correct Day in a week
j=0
day="ㄧ"
while j<=7:
    match j:
        case 1:
            day = "一"
        case 2:
            day = "二"
        case 3:
            day = "三"
        case 4:
            day = "四"
        case 5:
            day = "五"
        case 6:
            day = "六"
        case 7:
            day = "日"
        case 0:
            "invalid kkk"
    print("星期"+day+"跟Erin吃飯~")
    j+=1
        


#   2. using dictionary to setup the correct Day in a week 
days = {1:"一", 2:"二", 3:"三", 4:"四", 5:"五", 6:"六", 7:"日"}

i = 1
while i>0 and i<=7:
    print("星期"+days[i]+"跟Erin吃飯~")
    i+=1
print("嘿嘿嘿kkkkk")