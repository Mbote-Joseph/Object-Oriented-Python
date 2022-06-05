def lambdaMap(arr):
    ans = map(
        lambda x: x * 2,
        filter(
            lambda x: x % 2 == 0
            

            


# Complete the lambda function below.  It begins in the non-alterable code above

, arr))
    return ans



if __name__ == '__main__':
    n = int(raw_input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, raw_input().split())))
    
    ans = lambdaMap(arr)
    for row in ans:
        print(' '.join(map(str, row)))
