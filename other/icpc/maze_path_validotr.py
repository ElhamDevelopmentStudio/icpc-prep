from collections import deque
def solve(maze,start,end,row_,col_):
    queue = deque(
        [(start[0],start[1])]
         )
    visisted = set()

    visisted.add((start[0],start[1]))

    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    while queue:
        row,col = queue.popleft()
        print("\n")
        print(f"now at row {row} and col of {col}")
        if row == end[0] and col == end[1]:
            return True
    
        
        for direct in directions:
            #print(f"direction : {direct}")
            new_row,new_col = row+direct[0],col+direct[1]
            while 0 <= new_row < row_ and 0 <= new_col < col_ and maze[new_row][new_col] != 1:
                new_row += direct[0]
                new_col += direct[1]

            new_row -= direct[0]
            new_col -= direct[1]
            #print(f"new row : {new_row} and new_col : {new_col}")
            if (new_row,new_col) not in visisted:
                visisted.add((new_row,new_col))
                queue.append((new_row,new_col))
    return False


if __name__ == "__main__":
    row,col = 5,5
    start_row,start_col =0,4
    end_row,end_col = 3,2
    maze = [
        [0,0,1,0,0],
        [0,0,0,0,0],
        [0,0,0,1,0],
        [1,1,0,1,1],
        [0,0,0,0,0]
    ]




    res = solve(
        maze,(start_row,start_col),(end_row,end_col),row,col
    )

    print(res)
