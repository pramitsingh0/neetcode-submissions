class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # we'll keep a stack where we store everything that goes right, meaning every asteroid that is positive
        stack = []
        # whenever we encounter a negative number we pop from stack and append the result to stack,
        # if the result is negative we again pop from stack and collide the asteroids
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = stack[-1] + a
                if diff > 0:
                    a = 0
                elif diff < 0:
                    stack.pop()
                else:
                    a = 0
                    stack.pop()
            if a: stack.append(a)
        return stack
                