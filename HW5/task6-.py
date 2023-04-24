# Дана строка (возможно, пустая),состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28

def string_conv (some_str):
    count = 0
    conv_str=[]
    if len(some_str)<=1:
        return (some_str)
    else:
        conv_str.append(some_str[0])

    for i  in range (1, len(some_str)):
        if some_str[i] == some_str[i-1]:
            count+=1
        else:
            if count > 0:
                conv_str.append(count+1)
            count=0
            conv_str.append(some_str[i])
    if count > 0:
         conv_str.append(count+1)
    return conv_str



flag = False

while (not flag):
    test_string = input("Введите строку из символов A-Z: ")
    for i in range (0,len(test_string)):
        if (test_string[i] < 'A') or (test_string[i] > 'Z'):
            print ("Ошибочная строка!")
            break
    else: flag = True

print (*(string_conv (test_string)), sep="")

