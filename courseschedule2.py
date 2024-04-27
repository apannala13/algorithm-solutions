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
                
      
