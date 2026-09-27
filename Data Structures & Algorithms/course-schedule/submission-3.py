class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # record the indegree of each course
        # if the indegree is 0, means this course could be taken
        # after taken the course, decrease other courses indegree
        # if finally the output length is same as numCourses, means True
        # else false
        indegree = [0] * numCourses
        relation = {}
        for r in prerequisites:
            i, j = r[0],r[1]
            indegree[i] += 1
            if j not in relation:
                relation[j] = []
            relation[j].append(i)
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        res = []
        while queue:
            cur = queue.popleft()
            res.append(cur)
            if cur in relation:
                for c in relation[cur]:
                    indegree[c] -= 1
                    if indegree[c] == 0:
                        queue.append(c)
        if len(res) == numCourses:
            return True
        else:
            return False
        
