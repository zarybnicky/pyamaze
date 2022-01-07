# from pyMaze import maze,agent,COLOR,TextLabel
from pyamaze import Maze, Agent, TextLabel, COLOR


def DFS(m, start=None):
    if start is None:
        start = (m.rows, m.cols)
    explored = [start]
    frontier = [start]
    dfsPath = {}
    dSeacrh = []
    while len(frontier) > 0:
        currCell = frontier.pop()
        dSeacrh.append(currCell)
        if currCell == m._goal:
            break
        poss = 0
        for d in "ESNW":
            if m.maze_map[currCell][d]:
                if d == "E":
                    child = (currCell[0], currCell[1] + 1)
                if d == "W":
                    child = (currCell[0], currCell[1] - 1)
                if d == "N":
                    child = (currCell[0] - 1, currCell[1])
                if d == "S":
                    child = (currCell[0] + 1, currCell[1])
                if child in explored:
                    continue
                poss += 1
                explored.append(child)
                frontier.append(child)
                dfsPath[child] = currCell
        if poss > 1:
            m.mark_cells.append(currCell)
    fwdPath = {}
    cell = m._goal
    while cell != start:
        fwdPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]
    return dSeacrh, dfsPath, fwdPath


def main():
    m = Maze(10, 10)  # Change to any size
    m.CreateMaze(2, 4)  # (2,4) is Goal Cell, Change that to any other valid cell

    # (5,1) is Start Cell, Change that to any other valid cell
    dSeacrh, dfsPath, fwdPath = DFS(m, (5, 1))

    a = Agent(m, 5, 1, goal=(2, 4), footprints=True, shape="square", color=COLOR.green)
    b = Agent(m, 2, 4, goal=(5, 1), footprints=True, filled=True)
    c = Agent(m, 5, 1, footprints=True, color=COLOR.yellow)
    m.tracePath({a: dSeacrh}, showMarked=True)
    m.tracePath({b: dfsPath})
    m.tracePath({c: fwdPath})
    m.run()

    ## The code below will generate the maze shown in video

    # m=maze()
    # m.CreateMaze(loadMaze='dfs.csv')

    # dSeacrh,dfsPath,fwdPath=DFS(m)

    # a=agent(m,footprints=True,shape='square',color=COLOR.green)
    # b=agent(m,1,1,goal=(5,5),footprints=True,filled=True,color=COLOR.cyan)
    # c=agent(m,footprints=True,color=COLOR.yellow)
    # m.tracePath({a:dSeacrh},showMarked=True)
    # m.tracePath({b:dfsPath})
    # m.tracePath({c:fwdPath})
    # m.run()

if __name__ == "__main__":
    main()
