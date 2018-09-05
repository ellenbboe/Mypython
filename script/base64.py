
array=[
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
        'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
        'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
        'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z', '0', '1', '2', '3',
        '4', '5', '6', '7', '8', '9', '+', '/'
]

'''
使用base64方式加密
'''
def encrypt_base64():
    src=input("加密字符串:")
    tmp = ""
    result=""
    eqcount=0
    for char in src:
        char = ord(char) #turn to the ascii
        char = bin(char) #turn to the bin(二进制)
        char = char.replace("0b","")
        if(len(char) != 8):
            char = (8-len(char))*"0"+char
        tmp = tmp + char
    if(len(tmp)%6!= 0):
        eqcount = 6 - len(tmp)%6
        tmp = tmp + (6-len(tmp)%6)*"0"
    for i in range(0,len(tmp),6):
        base64bin=tmp[i:i+6]
        base64bin=int(base64bin,2)
        result=result + array[base64bin]
    result = result + int(eqcount/2)*"="
    return result

#-------------------------------------
'''
使用base64方式解密
'''
def decrypt_base64():
    src=input("解密字符串")
    eqcount = 0
    for i in src:
        if(i == "="):
            eqcount=eqcount+1
    src = src.replace("=",'')
    tmp = ""
    result = ""
    for char in src:
        for i in range(len(array)):
            if(array[i] == char):
                tmpbin=bin(i).replace("0b","")
                if(len(tmpbin) !=6):
                    tmpbin = (6-len(tmpbin))*"0" + tmpbin
                tmp = tmp + tmpbin

    for i in range(0,len(tmp)-eqcount*2,8):
       result=result + chr(int(tmp[i:i+8],2))
    return result

#---------------------------------------

if __name__ == '__main__':
    while True:
        print("-------------------------------------------")
        print("-------------------------------------------")
        print("使用base64加密或解密,选项1 加密 || 选项2 解密 || 选项其他 退出脚本\n")
        option = input("请输入:")
        if(option == "1"):
            print(encrypt_base64())
        elif(option == "2"):
            print(decrypt_base64())
        else:
            print("已退出")
            break

