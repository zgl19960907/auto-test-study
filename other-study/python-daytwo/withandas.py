'''
with 代码 as 变量
如果with语句的代码不出错，就会赋值给as后的变量
常用于文件读取 with代码执行完后，自动关闭文件

'''

with open(r'info2', encoding='utf-8') as f:
    line = f.read()
    print(line)