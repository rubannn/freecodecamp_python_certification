def hanoi_solver(n):
    # Initialize rods
    A = list(range(n, 0, -1))
    B = []
    C = []

    # Store all states as strings
    moves = []

    # Helper to record the current state
    def record_state():
        moves.append(f"{A} {B} {C}")

    # Recursive Hanoi solution
    def solve(disks, a, b, c):
        if disks == 1:
            c.append(a.pop())
            record_state()
        else:
            solve(disks - 1, a, c, b)
            c.append(a.pop())
            record_state()
            solve(disks - 1, b, a, c)

    # Record starting arrangement
    record_state()

    # Solve the puzzle
    solve(n, A, B, C)

    # Return all moves as a single string
    return "\n".join(moves)


print(hanoi_solver(2))
