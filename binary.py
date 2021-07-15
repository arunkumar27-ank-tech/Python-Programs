def search(list, n):
    l = 0
    u = len(list)-1

    while l <= u:
        mid = l+u//2
        if list[mid] == n:
            return True
        else:
            if list[mid]<n:
                l = mid+1
            else:
                u = mid-1
        return False


list = [1,2,3,4,5,6]
n = 5
if search(list, n):
    print('found')
else:
    print('not found')