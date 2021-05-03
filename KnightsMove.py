'''
Created on 03-May-2021

@author: Dinesh Thilagar
'''
dlist = [[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]

def ispossible(visited,x,y):
   if x<0 or y<0 or x>=len(visited) or y>=len(visited[0]) or visited[x][y]==1:
      return False
   return True

def possiblePath(visited,distance,s,e):
    que= [s]
    sx,sy=s[0],s[1]
    visited[sx][sy]= 1
    while que:
        temp= que.pop(0)
        x,y=temp[0],temp[1]
        dist=distance[x][y]

        for (u,v) in dlist:
            if ispossible(visited,x+u,y+v):
                que.append([x+u,y+v])
                visited[x+u][y+v] = 1
                distance[x+u][y+v] = dist+1
    ex,ey=e[0],e[1]
    if distance[ex][ey] <=10:
        print(distance[ex][ey])
    else:
        print("No path is possible")
N=8
visited = [[0 for x in range(N)] for y in range(N)]
distance = [[0 for x in range(N)] for y in range(N)]
s=[2,2]
e=[5,1]
possiblePath(visited,distance,s,e)
