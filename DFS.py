def solve(a, n):
    # Tạo danh sách kề:
    # adj[u] sẽ chứa tất cả các đỉnh kề với u
    adj = [[] for _ in range(n + 1)]

    # Duyệt từng cạnh trong danh sách a
    for edge in a:
        # edge là 1 cặp [u, v]
        u, v = edge

        # Vì đây là cây vô hướng nên phải thêm 2 chiều
        adj[u].append(v)
        adj[v].append(u)

    # visited[i] = True nếu đỉnh i đã được thăm
    visited = [False] * (n + 1)

    # Chiều sâu lớn nhất tìm được
    max_depth = 0

    # Số lá
    leaf_count = 0

    # Bậc lớn nhất
    max_degree = 0

    # Stack để DFS, bắt đầu từ đỉnh 1, độ sâu 0
    stack = [(1, 0)]
    visited[1] = True

    # Trong khi stack còn phần tử
    while stack:
        # Lấy phần tử trên cùng ra
        u, depth = stack.pop()

        # Cập nhật chiều sâu lớn nhất
        if depth > max_depth:
            max_depth = depth

        # Số đỉnh kề của u
        degree = len(adj[u])

        # Cập nhật bậc lớn nhất
        if degree > max_degree:
            max_degree = degree

        # Nếu u không phải root và chỉ có 1 cạnh kề
        # thì u là lá
        if u != 1 and degree == 1:
            leaf_count += 1

        # Duyệt các đỉnh kề
        for v in adj[u]:
            # Nếu chưa thăm thì cho vào stack
            if not visited[v]:
                visited[v] = True
                stack.append((v, depth + 1))

    # Trả về chuỗi kết quả
    return f"{max_depth} {leaf_count} {max_degree}"
