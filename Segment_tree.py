def nhap():
    n, q = map(int, input().split())        # số phần tử, số truy vấn
    a = list(map(int, input().split()))     # mảng ban đầu
    ops = [list(map(int, input().split())) for _ in range(q)]  # danh sách truy vấn
    return n, q, a, ops


def solve(n, q, a, ops):
    tree = [0]*(4*n)   # mảng lưu segment tree (4*n là đủ)
    lazy = [0]*(4*n)   # mảng lazy (trì hoãn cập nhật)

    # BUILD: xây cây từ mảng a
    def build(id, l, r):
        if l == r:                     # nếu là lá (1 phần tử)
            tree[id] = a[l]           # gán trực tiếp
            return
        m = (l+r)//2                  # chia đôi đoạn
        build(id*2, l, m)             # build nhánh trái
        build(id*2+1, m+1, r)         # build nhánh phải
        tree[id] = tree[id*2] + tree[id*2+1]   # gộp lại (sum)

    # PUSH: đẩy lazy xuống 2 con
    def push(id, l, r):
        if lazy[id]:                  # nếu có giá trị chưa đẩy
            m = (l+r)//2

            # đẩy xuống trái
            tree[id*2] += lazy[id]*(m-l+1)
            lazy[id*2] += lazy[id]

            # đẩy xuống phải
            tree[id*2+1] += lazy[id]*(r-m)
            lazy[id*2+1] += lazy[id]

            lazy[id] = 0              # xóa lazy hiện tại

    # UPDATE: cộng val vào đoạn [u, v]
    def update(id, l, r, u, v, val):
        if r < u or l > v:            # không giao
            return

        if u <= l and r <= v:         # nằm hoàn toàn trong
            tree[id] += val*(r-l+1)   # cập nhật luôn
            lazy[id] += val           # đánh dấu lazy
            return

        push(id, l, r)                # trước khi xuống phải push
        m = (l+r)//2
        update(id*2, l, m, u, v, val)       # xuống trái
        update(id*2+1, m+1, r, u, v, val)   # xuống phải
        tree[id] = tree[id*2] + tree[id*2+1]  # cập nhật lại

    # QUERY: lấy tổng đoạn [u, v]
    def query(id, l, r, u, v):
        if r < u or l > v:            # không giao
            return 0

        if u <= l and r <= v:         # nằm hoàn toàn trong
            return tree[id]

        push(id, l, r)                # đảm bảo đúng trước khi đi xuống
        m = (l+r)//2
        return query(id*2, l, m, u, v) + query(id*2+1, m+1, r, u, v)

    build(1, 0, n-1)   # bắt đầu build từ root

    res = []
    for op in ops:
        if op[0] == 1:                # update
            _, l, r, val = op
            update(1, 0, n-1, l, r, val)
        else:                         # query
            _, l, r = op
            res.append(query(1, 0, n-1, l, r))

    return res


if __name__ == '__main__':
    n, q, a, ops = nhap()
    print(*solve(n, q, a, ops))
