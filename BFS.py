import time
from collections import deque

def bfs_live():
    # 8x5 Coordinates
    nodes = {"Library": (0,0), "Admin": (4,0), "Lab": (8,0), "Cafeteria": (1,3), 
             "Student Center": (4,2), "Lecture Hall": (8,2), "Mosque": (4,5), "Main Hall": (8,5)}
    
    # Adjacency based on your blockages
    adj = {"Library": ["Admin", "Cafeteria"], "Admin": ["Library", "Lab"], "Lab": ["Admin"],
           "Cafeteria": ["Library", "Student Center", "Mosque"], "Student Center": ["Cafeteria", "Lecture Hall", "Mosque"],
           "Lecture Hall": ["Student Center"], "Mosque": ["Cafeteria", "Student Center", "Main Hall"], "Main Hall": ["Mosque"]}

    queue = deque([("Library", ["Library"])])
    visited = set()

    print("--- BFS START ---")
    while queue:
        current, path = queue.popleft()
        print(f"Checking: {current:15} | Path: {' -> '.join(path)}")
        time.sleep(0.6)

        if current == "Main Hall":
            print(f"\nGOAL FOUND! Final Path: {' -> '.join(path)}")
            return

        if current not in visited:
            visited.add(current)
            for neighbor in adj[current]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

bfs_live()