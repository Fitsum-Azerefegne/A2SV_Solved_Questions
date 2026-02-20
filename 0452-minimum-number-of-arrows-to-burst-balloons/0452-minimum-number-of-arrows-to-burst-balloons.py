class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0    
        points.sort(key=lambda x: x[1])       
        arrows = 1
        arrow_position = points[0][1]      
        for x_start, x_end in points[1:]:
            if x_start > arrow_position:
                arrows += 1
                arrow_position = x_end
                
        return arrows