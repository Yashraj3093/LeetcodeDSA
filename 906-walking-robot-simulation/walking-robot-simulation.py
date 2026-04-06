class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dirs = [(0,1),(1,0), (0,-1),(-1,0)]
        distance = 0
        x,y = 0,0
        result = 0
        obstacle = set()
        for a,b in obstacles: obstacle.add((a,b))

        for c in commands:
            if c == -2: distance = (distance - 1) % 4
            elif c == -1: distance = (distance + 1) % 4
            else:
                for i in range(c):
                    nx, ny = x + dirs[distance][0], y + dirs[distance][1]
                    if (nx, ny) in obstacle: break
                    result = max(result, nx**2 + ny**2)
                    x,y = nx,ny
        
        return result