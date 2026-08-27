class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # we'll keep a stack where we store everything that goes right, meaning every asteroid that is positive
        stack = []
        # whenever we encounter a negative number we pop from stack and append the result to stack,
        # if the result is negative we again pop from stack and collide the asteroids
        for n in asteroids:
            stack.append(n)
            if n < 0:
                while len(stack) >= 2 and stack[-1] < 0:
                    colliding = stack.pop()
                    colliding_with = stack.pop()
                    if abs(colliding) > abs(colliding_with):
                        stack.append(colliding)
                    elif abs(colliding) < abs(colliding_with):
                        stack.append(colliding_with)
                    
        return stack
                