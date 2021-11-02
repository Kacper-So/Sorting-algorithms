#IS,SS,HS,MS
#losowa,rosnąca,malejąca,stała,v kształtna,A kształtna

import random
import time

def dp(x):
    for i in range(len(x)):
        print(x[i])
    print(len(x))

def gen(input):
    n=20000
    n2=10000
    #zwraca 300 liczb losowych z zakresu od 0 do 299
    if input == "los":
        losowe = []
        for i in range(n):
            losowe.append(random.randint(0,n))
        file = open("los.txt", "w+")
        for i in range(len(losowe)):
            file.readline()
            file.write('%d' % losowe[i] + '\n')
        file.close
        return losowe

    #zwraca 300 rosnących od 0 do 299 liczb
    if input == "ros":
        rosnace = []
        for i in range(n):
            rosnace.append(i)
        return rosnace

    #zwraca 300 malejących od 299 do 0 liczb
    if input == "mal":
        malejace = []
        for i in range(n):
            malejace.append(n-1-i)
        return malejace

    #zwraca 300 liczb każda o wartości 1
    if input == "st":
        stale = []
        for i in range(n):
            stale.append(1)
        return stale

    #zwraca 300 liczb ułożonych w v z zakresu 0 do 299
    if input == "vksz":
        vksz = []
        val = n-1
        for i in range(n2):
            vksz.append(val-(i*2))
        val = 0
        for i in range(n2):
            vksz.append(val+(i*2))
        return vksz

    #zwraca 300 liczb ułożonych w A z zakresu 0 do 299
    if input == "aksz":
        aksz = []
        val = 0
        for i in range(n2):
            aksz.append(val+(i*2))
        val = n-1
        for i in range(n2):
            aksz.append(val-(i*2))
    return aksz

def IS(x):
    time_vector = []
    start = time.time()
    time_vector.append(start-start)
    for i in range(1,len(x)):
        key = x[i]
        j = i - 1
        while j >= 0 and key < x[j]:
            x[j+1] = x[j]
            j -= 1
        x[j+1] = key
        time_vector.append(time.time() - start)
    return [x,time_vector]

def SS(x):
    time_vector = []
    start = time.time()
    time_vector.append(start - start)
    for j in range(len(x)-1,0,-1):
        max = j
        for i in range(j - 1,0,-1):
            if x[max] < x[i]:
                max = i
        x[j], x[max] = x[max], x[j]
        time_vector.append(time.time() - start)
    return [x,time_vector]

def heapify(x,i,n,time_vector,start):
    left = 2 * i +1
    right = 2 * i + 2
    if left < n and x[left] > x[i]:
        max = left
    else:
        max = i
    if right < n and x[right] > x[max]:
        max = right
    if max != i:
        x[i],x[max] = x[max],x[i]
        heapify(x,max,n,time_vector,start)

def maxHeap(x,time_vector,start):
    n = len(x)
    for i in range(n//2 - 1,-1,-1):
        heapify(x,i,n,time_vector,start)

def HS(x):
    time_vector = []
    start = time.time()
    time_vector.append(start - start)
    n = len(x)
    maxHeap(x,time_vector,start)
    for i in range(n-1,0,-1):
        x[0],x[i] = x[i],x[0]
        time_vector.append(time.time() - start)
        heapify(x,0,i,time_vector,start)
    return [x,time_vector]

def MS(x):
    time_vector = []
    start = time.time()
    MS1(x,time_vector,start)
    return [x,time_vector]

def MS1(x,time_vector,start):
    if len(x) > 1:
        m = len(x) // 2
        l = x[:m]
        r = x[m:]
        MS(l)
        MS(r)
        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                x[k] = l[i]
                time_vector.append(time.time() - start)
                i += 1
            else:
                x[k] = r[j]
                time_vector.append(time.time() - start)
                j += 1
            k += 1
        while i < len(l):
            x[k] = l[i]
            time_vector.append(time.time() - start)
            i += 1
            k += 1
        while j < len(r):
            x[k] = r[j]
            time_vector.append(time.time() - start)
            j += 1
            k += 1
        return [x,time_vector]

def partition(x, l, h,time_vector,start,pivotPoz):
    i = (l - 1)
    if pivotPoz == 0:
        b = h
    if pivotPoz == 1:
        b = h//2
    if pivotPoz == 2:
        b = random.randint(0,h)
    a = x[b]

    for j in range(l, h):
        if x[j] <= a:
            i = i + 1
            x[i], x[j] = x[j], x[i]

    x[i + 1], x[b] = x[b], x[i + 1]
    return (i + 1)

def QS(x,l,h,pivotPoz):
    time_vector = []
    start = time.time()
    time_vector.append(start - start)

    size = h - l + 1
    stack = [0] * (size)
    top = -1

    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h

    while top >= 0:
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
        p = partition(x, l, h,time_vector,start,pivotPoz)
        time_vector.append(time.time() - start)
        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h
    return [x,time_vector]

if __name__ == '__main__':
    los = gen("los")
    ros = gen("ros")
    mal = gen("mal")
    st = gen("st")
    vksz = gen("vksz")
    aksz = gen("aksz")
    """
    #IS ok
    IS_los=IS(los)
    IS_ros=IS(ros)
    IS_mal=IS(mal)
    IS_st=IS(st)
    IS_vksz=IS(vksz)
    IS_aksz=IS(aksz)
    file = open("results.txt", "w+")
    for i in range(len(IS_los[1])):
        file.readline()
        file.write('%f' % IS_los[1][i] + '\n')
    for i in range(len(IS_los[1])):
        file.readline()
        file.write('%f' % IS_ros[1][i] + '\n')
    for i in range(len(IS_los[1])):
        file.readline()
        file.write('%f' % IS_mal[1][i] + '\n')
    for i in range(len(IS_los[1])):
        file.readline()
        file.write('%f' % IS_st[1][i] + '\n')
    for i in range(len(IS_los[1])):
        file.readline()
        file.write('%f' % IS_vksz[1][i] + '\n')
    for i in range(len(IS_los[1])):
        file.readline()
        file.write('%f' % IS_aksz[1][i] + '\n')
    file.close
    """
    """
    #SS ok
    SS_los = SS(los)
    SS_ros = SS(ros)
    SS_mal = SS(mal)
    SS_st = SS(st)
    SS_vksz = SS(vksz)
    SS_aksz = SS(aksz)
    file = open("results.txt", "w+")
    for i in range(len(SS_los[1])):
        file.readline()
        file.write('%f' % SS_los[1][i] + '\n')
    for i in range(len(SS_los[1])):
        file.readline()
        file.write('%f' % SS_ros[1][i] + '\n')
    for i in range(len(SS_los[1])):
        file.readline()
        file.write('%f' % SS_mal[1][i] + '\n')
    for i in range(len(SS_los[1])):
        file.readline()
        file.write('%f' % SS_st[1][i] + '\n')
    for i in range(len(SS_los[1])):
        file.readline()
        file.write('%f' % SS_vksz[1][i] + '\n')
    for i in range(len(SS_los[1])):
        file.readline()
        file.write('%f' % SS_aksz[1][i] + '\n')
    file.close
    """
    """
    #HS
    HS_los = HS(los)
    HS_ros = HS(ros)
    HS_mal = HS(mal)
    HS_st = HS(st)
    HS_vksz = HS(vksz)
    HS_aksz = HS(aksz)
    file = open("results.txt", "w+")
    for i in range(len(HS_los[1])):
        file.readline()
        file.write('%f' % HS_los[1][i] + '\n')
    for i in range(len(HS_ros[1])):
        file.readline()
        file.write('%f' % HS_ros[1][i] + '\n')
    for i in range(len(HS_mal[1])):
        file.readline()
        file.write('%f' % HS_mal[1][i] + '\n')
    for i in range(len(HS_st[1])):
        file.readline()
        file.write('%f' % HS_st[1][i] + '\n')
    for i in range(len(HS_vksz[1])):
        file.readline()
        file.write('%f' % HS_vksz[1][i] + '\n')
    for i in range(len(HS_aksz[1])):
        file.readline()
        file.write('%f' % HS_aksz[1][i] + '\n')
    file.close
    """
    """
    # MS
    MS_los = MS(los)
    MS_ros = MS(ros)
    MS_mal = MS(mal)
    MS_st = MS(st)
    MS_vksz = MS(vksz)
    MS_aksz = MS(aksz)
    file = open("results.txt", "w+")
    for i in range(len(MS_los[1])):
        file.readline()
        file.write('%f' % MS_los[1][i] + '\n')
    for i in range(len(MS_ros[1])):
        file.readline()
        file.write('%f' % MS_ros[1][i] + '\n')
    for i in range(len(MS_mal[1])):
        file.readline()
        file.write('%f' % MS_mal[1][i] + '\n')
    for i in range(len(MS_st[1])):
        file.readline()
        file.write('%f' % MS_st[1][i] + '\n')
    for i in range(len(MS_vksz[1])):
        file.readline()
        file.write('%f' % MS_vksz[1][i] + '\n')
    for i in range(len(MS_aksz[1])):
        file.readline()
        file.write('%f' % MS_aksz[1][i] + '\n')
    file.close
    """
    # QS
    QS_aksz = QS(aksz,0,len(aksz)-1,0)
    file = open("resultsLP.txt", "w+")
    for i in range(len(QS_aksz[1])):
        file.readline()
        file.write('%f' % QS_aksz[1][i] + '\n')
    file.close
    dp(aksz)
    aksz2 = gen("aksz")
    QS_aksz2 = QS(aksz2, 0, len(aksz2) - 1, 1)
    file = open("resultsSP.txt", "w+")
    for i in range(len(QS_aksz2[1])):
        file.readline()
        file.write('%f' % QS_aksz2[1][i] + '\n')
    file.close
    aksz3 = gen("aksz")
    QS_aksz3 = QS(aksz3, 0, len(aksz3) - 1, 2)
    file = open("resultsLosowyP.txt", "w+")
    for i in range(len(QS_aksz3[1])):
        file.readline()
        file.write('%f' % QS_aksz3[1][i] + '\n')