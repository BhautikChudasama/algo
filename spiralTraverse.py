# Time: O(N) and Space: O(N)

def sprialTraverse(array):
    final = []
    spiralHelper(array, 0, len(array)-1, 0, len(array[0])-1, final)
    return final

def spiralHelper(array, sr, er, sc, ec, final):
    if sr > er or sc > ec:
        return 
    for col in range(sc, ec+1):
        final.append(array[sr][col])
    for row in range(sr+1, er+1):
        final.append(array[row][ec])
    for col in reversed(range(sc, ec)):
        final.append(array[er][col])
    for row in reversed(range(sr+1, er)):
        final.append(array[row][sc])

    spiralHelper(array, sr+1, er-1, sc+1, ec-1, final)

arr = [[1, 2, 3], [6, 5, 4]]
        
print(sprialTraverse(arr))

