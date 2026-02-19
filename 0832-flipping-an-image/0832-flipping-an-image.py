class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i].reverse()
        for r in range(len(image)):
            for c in range(len(image[0])):
                if image[r][c] == 0:
                    image[r][c] = 1
                else:
                    image[r][c] = 0
        return(image)
        