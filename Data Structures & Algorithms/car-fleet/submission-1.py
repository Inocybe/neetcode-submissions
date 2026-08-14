class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = sorted(zip(position, speed), reverse=True)
        stack = []

        for p, s in combined:
            time = (target - p) / s

            if not stack:
                stack.append(time)
                continue

            if stack[-1] < time:
                stack.append(time)
        
        return len(stack)

