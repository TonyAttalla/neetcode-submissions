class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    # cycle detection
    # prereqs is a directed graph, [x,y] means y is a prereq for x , which means y points to x
    # build a map that maps all courses to its prereqs
    # run dfs from each course, and maintain a map of visited courses, if we reach a point where the 
    # course is already in the map, we found a cycle, return false
    # [0,1] = 0<-1
    # 0 -> numCourses - 1
        courses_to_prereqs = defaultdict(list)

        for i in range(numCourses):
            courses_to_prereqs[i] = []
        
        for (course, prereq) in prerequisites:
            courses_to_prereqs[course].append(prereq)
            if course == prereq:
                return False
        print(courses_to_prereqs)
        # run detect_cycles on each course with an initially empty courses_to_visited
        # return true if a cycle is detected, else return false
        def detect_cycles(course, courses_to_visited: set):
            if courses_to_prereqs[course] == []:
                return False
            # already been here
            if course in courses_to_visited:
                return True
            courses_to_visited.add(course)
            for prereq in courses_to_prereqs[course]:
                if detect_cycles(prereq, courses_to_visited):
                    return True
            return False
        
        for course in courses_to_prereqs:
            if detect_cycles(course, set()):
                return False
        return True
        
