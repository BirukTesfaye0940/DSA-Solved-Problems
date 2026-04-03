def activity_selection(start, finish):
    n = len(start)
    
    # Combine and sort by finish time
    activities = sorted(zip(start, finish), key=lambda x: x[1])
    
    selected = []
    
    # Pick first activity
    last_finish = activities[0][1]
    selected.append(activities[0])
    
    # Check remaining activities
    for i in range(1, n):
        if activities[i][0] >= last_finish:
            selected.append(activities[i])
            last_finish = activities[i][1]
    
    return selected


# Example
start = [1,2,4,1,5,8,9,11,13]
finish = [3,5,7,8,9,10,11,14,16]

print(activity_selection(start, finish))