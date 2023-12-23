// solution to the problem no. : 1496
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        s = set()
        t = (x, y)
        s.add(t)

        for c in path:
            if c == 'N':
                y += 1
            elif c == 'S':
                y -= 1
            elif c == 'E':
                x += 1
            elif c == 'W':
                x -= 1
            
            t = (x, y)

            if t in s:
                return True
            else:
                s.add(t)
        else:
            return False