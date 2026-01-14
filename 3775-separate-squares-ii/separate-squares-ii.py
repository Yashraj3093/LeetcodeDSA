class SegmentTree:
    def __init__(self, xs):
        self.xs = xs
        self.n = len(xs) - 1
        self.count = [0] * (4 * self.n)
        self.covered = [0] * (4 * self.n)

    def update(self, ql, qr, val, l, r, pos):
        if self.xs[r + 1] <= ql or self.xs[l] >= qr:
            return
        
        if ql <= self.xs[l] and self.xs[r + 1] <= qr:
            self.count[pos] += val
        else:
            mid = (l + r) // 2
            self.update(ql, qr, val, l, mid, pos*2+1)
            self.update(ql, qr, val, mid+1, r, pos*2+2)
        
        if self.count[pos] > 0:
            self.covered[pos] = self.xs[r + 1] - self.xs[l]
        else:
            if l == r:
                self.covered[pos] = 0
            else:
                self.covered[pos] = self.covered[pos*2+1] + self.covered[pos*2+2]


class Solution:
    def separateSquares(self, squares):
        # ---- Coordinate Compression ----
        xs = set()
        events = []
        
        for x, y, l in squares:
            xs.add(x)
            xs.add(x + l)
            events.append((y, +1, x, x + l))
            events.append((y + l, -1, x, x + l))
        
        xs = sorted(xs)
        st = SegmentTree(xs)
        events.sort()
        
        # ---- First Sweep : Compute total area ----
        totalArea = 0
        prev_y = events[0][0]
        
        for y, typ, x1, x2 in events:
            width = st.covered[0]
            totalArea += width * (y - prev_y)
            st.update(x1, x2, typ, 0, st.n - 1, 0)
            prev_y = y
        
        half = totalArea / 2.0
        
        # ---- Second Sweep : Find answer Y ----
        st = SegmentTree(xs)  # reset tree
        currArea = 0
        prev_y = events[0][0]
        
        for y, typ, x1, x2 in events:
            width = st.covered[0]
            sliceArea = width * (y - prev_y)
            
            if currArea + sliceArea >= half:
                return prev_y + (half - currArea) / width
            
            currArea += sliceArea
            st.update(x1, x2, typ, 0, st.n - 1, 0)
            prev_y = y
        
        return float(prev_y)
