from pyamaze import Maze, Agent, COLOR, TextLabel


def BFS(m):
    start = (m.rows, m.cols)
    frontier = [start]
    explored = [start]
    bfsPath = {}
    while frontier:
        currCell = frontier.pop(0)
        if currCell == (1, 1):
            break
        for d in "ESNW":
            if m.maze_map[currCell][d]:
                if d == "E":
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == "W":
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == "N":
                    childCell = (currCell[0] - 1, currCell[1])
                elif d == "S":
                    childCell = (currCell[0] + 1, currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell] = currCell
    fwdPath = {}
    cell = (1, 1)
    while cell != start:
        fwdPath[bfsPath[cell]] = cell
        cell = bfsPath[cell]
    return fwdPath


if __name__ == "__main__":
    m = Maze(5, 7)
    m.CreateMaze(loopPercent=40)
    path = BFS(m)

    a = Agent(m, footprints=True, filled=True)
    m.tracePath({a: path})
    l = TextLabel(m, "Length of Shortest Path", len(path) + 1)

    m.run()
