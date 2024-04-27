class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        prereq_count = [0] * numCourses #number of prereqs
        
        
        for crs, pre in prerequisites:
            graph[pre].append(crs) #add course to pre's list
            prereq_count[crs] += 1 #incremening prereq count of course

        #queue with courses that have no prerequisites
        queue = deque([i for i in range(numCourses) if prereq_count[i] == 0])
        top_order = [] #storing order of courses
        
        while queue:
            course = queue.popleft() #get course with no remaining prereqs
            top_order.append(course) 
            #traverse all courses dependent on current course 
            for neighbor in graph[course]:
                prereq_count[neighbor] -= 1 #reduce the prerequisite count
                if prereq_count[neighbor] == 0: #if no more prereqs
                    queue.append(neighbor)
        
        return top_order if len(top_order) == numCourses else []




#dfs
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        #states: 0 = unvisited, 1 = visiting, 2 = visited
        visit = [0] * numCourses
        top_order = []
        
        for crs, pre in prerequisites:
            graph[pre].append(crs)
            
        def dfs(crs):
            if visit[crs] == 1:  #cycle detected
                return False
            if visit[crs] == 2:  #already processed
                return True
            
            visit[crs] = 1  #mrk the course as visiting for cycle detection
            for next_course in graph[crs]:
                if not dfs(next_course):
                    return False
            visit[crs] = 2  #mark the course as visited
            top_order.append(crs)  #add the course to the topological order
            return True
        
        #visit each course
        for crs in range(numCourses):
            if visit[crs] == 0:  # Unvisited
                if not dfs(crs):
                    return []  #if a cycle is detected, return an empty list
        
        # courses were added in reverse topological order, so returning inverse
        return top_order[::-1]  


      
