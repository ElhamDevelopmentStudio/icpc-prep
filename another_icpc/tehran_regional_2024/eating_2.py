import sys, math

# This function computes the minimum x (>= r1) needed so that
# after merging “step 1” with value x1 (i.e. x -> x XOR x1),
# we have (x XOR x1) >= r2.
# (We use a 32-bit loop – adjust if your numbers are larger.)
def combine_req(r1, x1, r2):
    L = 32
    res = 0
    # f1 and f2 indicate whether the inequality
    # x >= r1 or (x XOR x1) >= r2 is already “loosened”
    # (i.e. we are already strictly greater than the requirement)
    f1 = 0  
    f2 = 0  
    for i in range(L-1, -1, -1):
        br1 = (r1 >> i) & 1
        bx1 = (x1 >> i) & 1
        br2 = (r2 >> i) & 1
        if f1:
            min_b1 = 0
        else:
            min_b1 = br1
        if f2:
            forced = None
        else:
            # If r2 has a 1 at this bit, then (x XOR x1) must be 1;
            # that forces the bit b to be (1 - bx1).
            if br2 == 1:
                forced = 1 - bx1
            else:
                forced = None
        if forced is not None:
            if forced < min_b1:
                # If the forced value is less than the lower bound from r1,
                # there is no valid x here. (Return a very high requirement.)
                return 1 << 30
            b = forced
        else:
            b = min_b1
        if not f1 and b > br1:
            f1 = 1
        if not f2 and ((b ^ bx1) > br2):
            f2 = 1
        res |= (b << i)
    return res

# Given two segments seg1 and seg2 (each a tuple (req, xor)),
# their combination represents the effect of applying first seg1 then seg2.
def combine(seg1, seg2):
    r1, x1 = seg1
    r2, x2 = seg2
    return (combine_req(r1, x1, r2), x1 ^ x2)

# Build a sparse table (binary-lifting table) for the reversed array B.
# ST[k][i] will represent the merged segment starting at i of length 2^k.
def build_sparse_table(B):
    N = len(B)
    max_k = (N).bit_length()
    ST = [ [None] * N for _ in range(max_k) ]
    for i in range(N):
        ST[0][i] = (B[i], B[i])
    for k in range(1, max_k):
        step = 1 << (k-1)
        for i in range(N - (1 << k) + 1):
            ST[k][i] = combine(ST[k-1][i], ST[k-1][i+step])
    return ST

# Given a starting value cur, use binary lifting on ST to “jump”
# as far as possible (i.e. process as many merges in one go) 
# and return the total number of merges.
def process_query(cur, ST, N, max_k):
    pos = 0
    cnt = 0
    for k in range(max_k-1, -1, -1):
        jump = 1 << k
        if pos + jump <= N:
            seg_req, seg_xor = ST[k][pos]
            if cur >= seg_req:
                cur ^= seg_xor
                pos += jump
                cnt += jump
    return cnt

def main():
    data = sys.stdin.read().strip().split()
    if not data: 
        return
    t = int(data[0])
    index = 1
    out_lines = []
    for _ in range(t):
        n = int(data[index]); q = int(data[index+1]); index += 2
        mars = list(map(int, data[index:index+n])); index += n
        # Rather than copying mars for every query, notice that the merge process 
        # only “works” on the suffix. So let B be the reversed array.
        B = mars[::-1]
        N_val = len(B)
        ST = build_sparse_table(B)
        max_k = (N_val).bit_length()
        res = []
        for _ in range(q):
            x = int(data[index]); index += 1
            merges = process_query(x, ST, N_val, max_k)
            res.append(str(merges))
        out_lines.append(" ".join(res))
    sys.stdout.write("\n".join(out_lines))
    
if __name__ == '__main__':
    main()

