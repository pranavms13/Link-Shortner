BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
target = []
base = input("Enter Base URL : ")
n = int(input("Enter number of Target URLs : "))
for i in range(n):
    target.append(input("Enter URL " + str(i+1) + " : "))


def conv(s):
    b = bytearray()
    arr=[]
    b.extend(map(ord, s))
    for item in b:
        arr.append(hex(item))
    return arr

def encodeb62(num, alphabet=BASE62):
    
    if num == 0:
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        num, rem = divmod(num, base)
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)


for p in target:
    xored=[]
    last8=[]
    last8str = '0x'
    convertedint = 0

    tarr=conv(p)
    barr=conv(base)
    exlen=len(tarr)-len(barr)    

    cbarr = []
    
    times = int(len(tarr)/len(barr))
    exlen = len(tarr)%len(barr)

    for x in range (times):
        cbarr = cbarr + barr

    if exlen != 0:
        exarr = barr[:exlen]
        cbarr = cbarr + exarr

    for i in range(0,len(cbarr)):
        temp = hex(int(cbarr[i],16) ^ int(tarr[i],16))
        if len(temp) == 3:
            temp1=temp[-1:]
            temp = '0x0' + temp1
            xored.append(temp)
        else:
            xored.append(temp)

    last8 = xored[-8:]

    for i in last8:
        last8str = last8str + i[-2:]

    convertedint = int(last8str,0)
    print()
    print("Shortened URL : " + base + "/" + encodeb62(convertedint))