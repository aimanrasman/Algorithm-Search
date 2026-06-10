import time

def dfs_live():
    adj = {"Library": ["Admin", "Cafeteria"], "Admin": ["Library", "Lab"], "Lab": ["Admin"],
           "Cafeteria": ["Library", "Student Center", "Mosque"], "Student Center": ["Cafeteria", "Lecture Hall", "Mosque"],
           "Lecture Hall": ["Student Center"], "Mosque": ["Cafeteria", "Student Center", "Main Hall"], "Main Hall": ["Mosque"]}

    stack = [("Library", ["Library"])]
    visited = set()

    print("--- DFS START ---")
    while stack:
        current, path = stack.pop()
        print(f"Diving into: {current:15} | Path: {' -> '.join(path)}")
        time.sleep(0.6)

        if current == "Main Hall":
            print(f"\nGOAL FOUND! Final Path: {' -> '.join(path)}")
            return

        if current not in visited:
            visited.add(current)
            # Reverse for a more natural "Left-to-Right" check
            for neighbor in reversed(adj[current]):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

dfs_live()