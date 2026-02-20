# -------------------- FAST INPUT --------------------
import sys
import threading

def solve():
    input = sys.stdin.readline
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        arr = list(map(int, input().split()))
        result = sum(arr) 
        print(result)
if __name__ == "__main__":
    solve()
