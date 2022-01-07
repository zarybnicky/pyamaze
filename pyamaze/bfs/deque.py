from collections import deque
from pyamaze import Maze, Agent, COLOR


def BFS(m, start=None):
    if start is None:
        start = (m.rows, m.cols)
    frontier = deque()
    frontier.append(start)
    bfs_path = {}
    explored = [start]

    while len(frontier) > 0:
        current_cell = frontier.popleft()
        if current_cell == m._goal:
            break
        for d in "ESNW":
            if m.maze_map[current_cell][d] == True:
                if d == "E":
                    child_cell = (current_cell[0], current_cell[1] + 1)
                elif d == "W":
                    child_cell = (current_cell[0], current_cell[1] - 1)
                elif d == "S":
                    child_cell = (current_cell[0] + 1, current_cell[1])
                elif d == "N":
                    child_cell = (current_cell[0] - 1, current_cell[1])
                if child_cell in explored:
                    continue
                frontier.append(child_cell)
                explored.append(child_cell)
                bfs_path[child_cell] = current_cell
    # print(f'{bfs_path}')
    fwd_path = {}
    cell = m._goal
    while cell != (m.rows, m.cols):
        fwd_path[bfs_path[cell]] = cell
        cell = bfs_path[cell]
    return explored, bfs_path, fwd_path


def main():
    # m=maze(5,5)
    # m.CreateMaze(loadMaze='bfs.csv')
    # bSearch,bfs_path,fwd_path=BFS(m)
    # a=agent(m,footprints=True,color=COLOR.green,shape='square')
    # b=agent(m,footprints=True,color=COLOR.yellow,shape='square',filled=False)
    # c=agent(m,1,1,footprints=True,color=COLOR.cyan,shape='square',filled=True,goal=(m.rows,m.cols))
    # m.tracePath({a:bSearch},delay=500)
    # m.tracePath({c:bfs_path})
    # m.tracePath({b:fwd_path})

    # m.run()

    m = Maze(12, 10)
    # m.CreateMaze(5,4,loopPercent=100)
    m.CreateMaze(loopPercent=10, theme="light")
    explored, bfs_path, fwd_path = BFS(m)
    a = Agent(m, footprints=True, color=COLOR.yellow, shape="square", filled=True)
    b = Agent(m, footprints=True, color=COLOR.red, shape="square", filled=False)
    # c=Agent(m,5,4,footprints=True,color=COLOR.cyan,shape='square',filled=True,goal=(m.rows,m.cols))
    c = Agent(m, 1, 1, footprints=True, color=COLOR.cyan, shape="square", filled=True, goal=(m.rows, m.cols))
    m.tracePath({a: explored}, delay=100)
    m.tracePath({c: bfs_path}, delay=100)
    m.tracePath({b: fwd_path}, delay=100)

    m.run()

if __name__ == "__main__":
    main()
