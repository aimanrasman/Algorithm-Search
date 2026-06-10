import time, heapq

def greedy_live():
    nodes = {"Library": (0,0), "Admin": (4,0), "Lab": (8,0), "Cafeteria": (1,3), 
             "Student Center": (4,2), "Lecture Hall": (8,2), "Mosque": (4,5), "Main Hall": (8,5)}
    adj = {"Library": ["Admin", "Cafeteria"], "Admin": ["Library", "Lab"], "Lab": ["Admin"],
           "Cafeteria": ["Library", "Student Center", "Mosque"], "Student Center": ["Cafeteria", "Lecture Hall", "Mosque"],
           "Lecture Hall": ["Student Center"], "Mosque": ["Cafeteria", "Student Center", "Main Hall"], "Main Hall": ["Mosque"]}

    def h(n): return abs(8 - nodes[n][0]) + abs(5 - nodes[n][1])

    pq = [(h("Library"), "Library", ["Library"])]
    visited = set()

    print("--- GREEDY START ---")
    while pq:
        h_val, current, path = heapq.heappop(pq)
        print(f"Greedy Pick: {current:15} | h(n)={h_val:2} | Path: {' -> '.join(path)}")
        time.sleep(0.7)

        if current == "Main Hall":
            print(f"\nGOAL FOUND! Final Path: {' -> '.join(path)}")
            return

        visited.add(current)
        for neighbor in adj[current]:
            if neighbor not in visited:
                heapq.heappush(pq, (h(neighbor), neighbor, path + [neighbor]))

greedy_live()