def find_even_index(arr):
    xt = 0;
    xid = -1;

    end = len(arr) - 1;
    while xid <= end :
        yid = end
        yt = 0;
        while yid != xid + 1 and yid >= 0 :
            yt += arr[yid]
            yid -= 1;
        if xt == yt :
            return yid
        xid += 1
        xt += arr[xid]
    return -1


a = [1,2,3,4,3,2,1]
print(find_even_index(a))