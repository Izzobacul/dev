##DONE##

def longest_slide_down(pyramid):
    for i in range(len(pyramid)-2, -1, -1):
        for l in range(len(pyramid[i])):
            pyramid[i][l] += max(pyramid[i+1][l], pyramid[i+1][l+1])
    return(pyramid[0][0])
        
pyramid = [[4],
         [7, 4], 
         [2, 4, 6], 
         [8, 5, 9, 3]]

print(longest_slide_down(pyramid))