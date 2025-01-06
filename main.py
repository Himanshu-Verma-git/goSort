def moveRight(l:list, ind:int, t:int):
    while(l[ind+1] != t):
        l[ind], l[ind+1] = l[ind+1], l[ind]
        ind+=1
    l[ind], l[ind+1] = l[ind+1], l[ind]

def moveLeft(l:list, ind:int, t:int):
    while(l[ind-1] != t):
        l[ind], l[ind-1] = l[ind-1], l[ind]
        ind-=1
    l[ind], l[ind-1] = l[ind-1], l[ind]

def sort(l:list)->list:
    if(len(l) == 0 or len(l) == 1):return l
    mid = len(l)//2
    t = l[mid]
    i = mid-1
    j = mid+1
    
    while(i >= 0):
        if(l[i] > t):moveRight(l, i, t)
        i-=1
    
    while(j <= len(l)-1):
        if(l[j] < t):moveLeft(l, j, t)
        j+=1
    
    ind = l.index(t)
    print(l)
    return sort(l[:ind]) + [t] + sort(l[ind+1:])

def main():
    l = [0, 9, 6, 5, 1, 2, 7, 4, 8]
    print(sort(l))

main()