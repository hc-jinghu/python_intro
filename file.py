# read, write files

# Notes:
# open("file path", mode="something")
# file path can be absolute or relative
# mode parameter
# mode="r" read
# mode="w" rewrite
# mode="a" add-on


# Example:
#file = open("123.txt", mode="r")
#print(file.read())

file = open("/Users/jhu/repo/python_repo/123.txt", mode="a", encoding="utf-8") # utf-8 支援中文編碼方式
file.write("\n媽媽木賽高！") # rewrites the file content

file.close() # essential for saving PC memory

# this method allows us to not close file2, it will close it for us
with open("456.txt", mode="a", encoding="utf-8") as file2:
    file2.write("I say MAMA MAMA MOO~")