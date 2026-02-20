# -------------------- FAST INPUT --------------------
import sys
import threading

def solve():
    input = sys.stdin.readline  # Fast input
    
    # Example: single integer
    # n = int(input().strip())
    
    # Example: list of integers
    # arr = list(map(int, input().split()))
    
    # Example: multiple test cases
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        arr = list(map(int, input().split()))
        
        # ---- Your logic here ----
        result = sum(arr)  # Example operation
        
        print(result)

# Required for faster execution in some judges
if __name__ == "__main__":
    solve()
