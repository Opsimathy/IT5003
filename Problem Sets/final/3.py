import sys
MOD = 10**9 + 7
CHUNK = 16
MASK = (1 << CHUNK) - 1
it = iter(map(int, sys.stdin.buffer.read().split()))
n0, e, q = next(it), next(it), next(it)
maxn = n0 + q
init_rows = [0] * n0
init_cols = [0] * n0
for _ in range(e):
    a, b = next(it), next(it)
    init_rows[a] |= 1 << b
    init_cols[b] |= 1 << a
birth_time = [0] * maxn
birth_value = [0] * maxn
clear_time = [-1] * maxn
clear_value = [0] * maxn
row_edges = [dict() for _ in range(maxn)]
col_edges = [dict() for _ in range(maxn)]
exact0 = [0] * (q + 1)
exact1 = [0] * (q + 1)
adds_before = [0] * (q + 1)
n = n0
adds = rev = inv = 0
def set_edge(a: int, b: int, time: int, value: int) -> None:
    enc = (time << 1) | value
    row_edges[a][b] = enc
    col_edges[b][a] = enc
def clear_vertex(v: int, time: int, value: int) -> None:
    old = clear_time[v]
    bit = 1 << v
    if old > 0:
        if clear_value[v]:
            exact1[old] &= ~bit
        else:
            exact0[old] &= ~bit
    clear_time[v] = time
    clear_value[v] = value
    if value:
        exact1[time] |= bit
    else:
        exact0[time] |= bit
for t in range(1, q + 1):
    adds_before[t] = adds
    typ = next(it)
    if typ == 1:
        birth_time[n] = t
        birth_value[n] = inv
        n += 1
        adds += 1
    elif typ == 2:
        x, y = next(it), next(it)
        a, b = (y, x) if rev else (x, y)
        set_edge(a, b, t, 1 ^ inv)
    elif typ == 3:
        clear_vertex(next(it), t, inv)
    elif typ == 4:
        x, y = next(it), next(it)
        a, b = (y, x) if rev else (x, y)
        set_edge(a, b, t, inv)
    elif typ == 5:
        rev ^= 1
    else:
        inv ^= 1
birth_time = birth_time[:n]
birth_value = birth_value[:n]
clear_time = clear_time[:n]
clear_value = clear_value[:n]
row_edges = row_edges[:n]
col_edges = col_edges[:n]
after0 = [0] * (q + 1)
after1 = [0] * (q + 1)
run0 = run1 = 0
for t in range(q, -1, -1):
    after0[t] = run0
    after1[t] = run1
    if t:
        run0 |= exact0[t]
        run1 |= exact1[t]
all_mask = (1 << n) - 1
later_birth_1 = 0
later_clear_0 = 0
later_clear_1 = 0
for v in range(n0, n):
    bit = 1 << v
    if birth_value[v]:
        later_birth_1 |= bit
    if clear_time[v] > birth_time[v]:
        if clear_value[v]:
            later_clear_1 |= bit
        else:
            later_clear_0 |= bit
sparse_rows = col_edges if rev else row_edges
init_base = init_cols if rev else init_rows
pow7 = [1] * (max(n, CHUNK) + 1)
for i in range(1, len(pow7)):
    pow7[i] = (pow7[i - 1] * 7) % MOD
cnt = [0] * (1 << CHUNK)
A = [0] * (1 << CHUNK)
B = [0] * (1 << CHUNK)
for mask in range(1, 1 << CHUNK):
    bit = mask.bit_length() - 1
    prev = mask ^ (1 << bit)
    cnt[mask] = cnt[prev] + 1
    A[mask] = (A[prev] + pow7[cnt[prev]]) % MOD
    B[mask] = (B[prev] + pow7[cnt[prev]] * bit) % MOD
chunks = (n + CHUNK - 1) // CHUNK
def row_hash(row: int) -> int:
    h = used = base = 0
    for _ in range(chunks):
        part = row & MASK
        if part:
            h = (h + pow7[used] * ((base * A[part] + B[part]) % MOD)) % MOD
            used += cnt[part]
        row >>= CHUNK
        base += CHUNK
    return h
out = [str(n)]
for i in range(n):
    if i < n0:
        row = init_base[i] | later_birth_1
    else:
        older = (1 << i) - 1 if birth_value[i] else 0
        younger = later_birth_1 & ~((1 << (i + 1)) - 1)
        row = older | younger
    row &= ~(1 << i)
    ti = clear_time[i]
    bi = birth_time[i]
    if ti > bi:
        cut = min(n, n0 + adds_before[ti])
        mask = ((1 << cut) - 1) & ~(1 << i) & ~(after0[ti] | after1[ti])
        if clear_value[i]:
            row |= mask
        else:
            row &= ~mask
    left_threshold = max(bi, ti)
    m1 = ((1 << i) - 1) & after1[left_threshold]
    m0 = ((1 << i) - 1) & after0[left_threshold]
    if i < n0:
        right_init = ((1 << n0) - 1) ^ ((1 << (i + 1)) - 1)
        init_threshold = max(0, ti)
        m1 |= right_init & after1[init_threshold]
        m0 |= right_init & after0[init_threshold]
    start = n0 if i < n0 else i + 1
    cut = min(n, n0 + adds_before[ti]) if ti > 0 else n0
    if cut > start:
        middle = ((1 << cut) - 1) ^ ((1 << start) - 1)
        m1 |= middle & after1[ti]
        m0 |= middle & after0[ti]
    start = max(start, cut)
    if start < n:
        tail = all_mask ^ ((1 << start) - 1)
        m1 |= tail & later_clear_1
        m0 |= tail & later_clear_0
    row |= m1
    row &= ~m0
    for j, enc in sparse_rows[i].items():
        time = enc >> 1
        threshold = max(birth_time[max(i, j)], clear_time[i], clear_time[j])
        if time > threshold:
            if enc & 1:
                row |= 1 << j
            else:
                row &= ~(1 << j)
    row &= ~(1 << i)
    if inv:
        row = (all_mask ^ (1 << i)) ^ row
    out.append(f"{row.bit_count()} {row_hash(row)}")
sys.stdout.write("\n".join(out))
