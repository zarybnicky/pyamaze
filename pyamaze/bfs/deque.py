from collections import deque

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
