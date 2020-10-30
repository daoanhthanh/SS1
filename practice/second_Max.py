if __name__ == "__main__":
    arr = list(map(int, (input("s").split())))
    mx = max(arr[0], arr[1])
    se = min(arr[0], arr[1])
    for i in arr:
        if i > mx:
            se = mx
            mx = i
        elif i > se and i != mx:
            se = i
    print(se)