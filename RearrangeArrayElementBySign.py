def rearrange_by_sign(A):
    n = len(A)
    ans = [0] * n

    pos_index = 0
    neg_index = 1

    for i in range(n):
        if A[i] < 0:
            ans[neg_index] = A[i]
            neg_index += 2
        else:
            ans[pos_index] = A[i]
            pos_index += 2

    return ans



A = [-1, 2, -3, 4]
print(rearrange_by_sign(A))
