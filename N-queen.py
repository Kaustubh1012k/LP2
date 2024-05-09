def solve_n_queens(n):
    """Solve the N-Queens problem and return a list of solutions."""
    solutions = []  # List to store solutions

    def is_safe(board, row, col):
        """Check if it's safe to place a queen at (row, col)."""
        # Check the column
        for i in range(row):
            if board[i] == col:
                return False
        
        # Check the diagonals
        for i in range(row):
            if abs(board[i] - col) == abs(i - row):
                return False
        
        return True

    def solve(row, board):
        """Recursive function to solve the N-Queens problem."""
        # If all queens are placed, add the solution
        if row == n:
            solutions.append(board[:])
            return
        
        # Try placing a queen in each column of the current row
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col  # Place the queen
                solve(row + 1, board)  # Move to the next row
                # Backtrack: Remove the queen
                board[row] = -1

    # Initialize the board with -1, representing an empty board
    board = [-1] * n
    # Start solving from the first row
    solve(0, board)
    return solutions

def print_solutions(solutions):
    """Print the solutions in a readable format."""
    for idx, solution in enumerate(solutions, start=1):
        print(f"Solution {idx}:")
        for row in range(len(solution)):
            line = ""
            for col in range(len(solution)):
                if solution[row] == col:
                    line += "Q "  # Queen
                else:
                    line += ". "  # Empty cell
            print(line)
        print()  # Blank line for separation

def main():
    """Main function to take input from the user and solve the N-Queens problem."""
    # Read the number of queens from the user
    n = int(input("Enter the number of queens: "))
    
    # Solve the N-Queens problem
    solutions = solve_n_queens(n)
    
    # Print the solutions
    print(f"\nTotal solutions found: {len(solutions)}")
    print_solutions(solutions)

if __name__ == "__main__":
    main()
