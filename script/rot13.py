


'''
加密
'''


def encrypt_rot13(option):
    if(option == "1"):
        src=input("输入加密字符串:")
    else:
        src=input("输入解密字符串:")
    result = ""
    for x in src:
        if(x.isalpha()):
            if(x.isupper()):
                x = ord(x)+13
                if(x>90):
                    x=x-26
            else:
                x = ord(x)+13
                if(x>122):
                    x=x-26
            result = result + chr(x)
        else:
            result = result + x
    return result





'''
解密与加密是统一过程,调用加密程序就行
'''



if __name__ == '__main__':
    while True:
        print("---------------------#------------------------")
        print("----------------------#-----------------------")
        print("--------------------###-----------------------")
        print("使用rot13加密或解密,选项1 加密 || 选项2 解密 || 选项其他 退出脚本\n")
        option = input("请输入:")
        if(option == "1"):
            print(encrypt_rot13(option))
        elif(option == "2"):
            print(encrypt_rot13(option))
        else:
            print("已退出")
            break

