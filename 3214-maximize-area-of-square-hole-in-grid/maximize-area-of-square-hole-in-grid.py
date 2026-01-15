class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        hmax, vmax = 1, 1
        hcurr, vcurr = 1, 1
        for i in range(1, len(hBars)):
            if hBars[i] == hBars[i - 1] + 1:
                hcurr += 1
            else:
                hcurr = 1
            hmax = max(hmax, hcurr)
        
        for i in range(1, len(vBars)):
            if vBars[i] == vBars[i - 1] + 1:
                vcurr += 1
            else:
                vcurr = 1
            vmax = max(vmax, vcurr)
        
        side = min(hmax,vmax) + 1
        return side * side
