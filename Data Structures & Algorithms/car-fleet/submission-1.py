class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        distance_left_arr = [target - x for x in position]
        hours_taken = [distance_left_arr[i] / speed[i] for i in range(len(position))]
        cars = [(position[i], hours_taken[i]) for i in range(len(position))]
        cars.sort(key=lambda x: x[0], reverse=True)
        stack = []
        curr_max = 0
        result = 0
        for i in cars:
            if not stack:
                curr_max = max(i[1], curr_max)
            elif i[1] > curr_max:
                stack.clear()
                result += 1
                curr_max = i[1]
            stack.append(i)
        if stack:
            result += 1
        return result
