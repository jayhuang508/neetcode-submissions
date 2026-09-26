class Solution:
    def jump(self, nums: List[int]) -> int:
        # because it always has valid result
        # from the begining and count the rounds to reach the end
        # the queue
        steps = 0
        if len(nums) == 1:
            return steps
        goal = len(nums) - 1
        queue = deque()
        queue.append(0)
        while True:
            steps += 1
            t = len(queue)
            for _ in range(t):
                idx = queue.popleft()
                if idx + nums[idx] >= goal:
                    return steps
                else:
                    for j in range(idx+1,idx+nums[idx]+1):
                        if j not in queue:
                            queue.append(j)
            # sorted(queue,reverse = True)

        