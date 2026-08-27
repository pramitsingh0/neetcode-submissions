class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speed_map = {}

        for i in range(len(position)):
            speed_map[position[i]] = speed[i]
        position.sort(reverse = True)

        for i in range(len(position)):
            speed[i] = speed_map[position[i]]
        

        stack = []
        target_distance = target - position[0]
        for i in range(len(position)):
            if not stack or position[i] + (target_distance * speed[i]) < stack[-1]:
                stack.append(position[i] + (target_distance * speed[i]))
        
        return len(stack)