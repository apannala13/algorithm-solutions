#dfs implementation:









#topological sort implementation:
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #graph to hold lists of courses dependent on each course
        graph = defaultdict(list)

        #array to track # of prereqs needed for each course. serves as indegree
        prereq_count = [0] * numCourses

        #build graph and populate prereq counts
        for crs, pre in prerequisites:
            graph[pre].append(crs) #pre is a prereq for course
            prereq_count[crs] += 1 #increase prereq count for course

        #queue to hold courses with no prerequisite needed
        queue = deque([i for i in range(numCourses) if prereq_count[i] == 0])
        #count of courses that have been processed
        visited = 0 


        while queue:
            current = queue.popleft() #current course being processed
            visited += 1 #increment count of processed courses
            #reduce prereq count of dependent courses
            for neighbor in graph[current]:
                prereq_count[neighbor] -= 1
                #if no more prereqs needed, add to queue to process this course
                if prereq_count[neighbor] == 0:
                    queue.append(neighbor)

        #if all courses were visited, it means courses can be finished.
        return True if visited == numCourses else False 





        
