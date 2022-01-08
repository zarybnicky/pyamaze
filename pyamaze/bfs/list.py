from pyamaze import Maze, Agent, COLOR, TextLabel


def BFS(maze, start=None):
    if start is None:
        start = (maze.rows, maze.cols)
    agent_path = []

    # OPEN SET (w/start)
    # CLOSED SET (w/start)
    # MAP DICT
    # AGENT_PATH ARRAY

    # WHILE OPEN
    # POP & RECORD VISITED
    # CHECK GOAL
    # CHECK maze.maze_map[current_cell][d] for d in "ESNW"
    # CHECK CLOSED
    # MARK AS OPEN
    # MAP (next <- current)

    # REVERSE PATH, follow (next <- current) and mark reverse path

    fwd_path = {}
    cell = maze._goal

    return agent_path, fwd_path


if __name__ == "__main__":
    m = Maze(5, 7)
    m.CreateMaze(loopPercent=40)
    search_path, path = BFS(m)

    a = Agent(m, footprints=True, filled=True)
    b = Agent(m, footprints=True, color=COLOR.red, shape="square", filled=False)
    m.tracePath({a: path})
    m.tracePath({b: search_path})
    l = TextLabel(m, "Length of Shortest Path", len(path) + 1)

    m.run()
