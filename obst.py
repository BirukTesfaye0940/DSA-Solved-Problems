def optimal_bst(p, q, n):
    # e[i][j] = minimum expected search cost for keys i to j
    e = [[0] * (n + 2) for _ in range(n + 2)]
    
    # w[i][j] = total probability (p + q) from i to j
    w = [[0] * (n + 2) for _ in range(n + 2)]
    
    # root[i][j] = root of subtree from i to j
    root = [[0] * (n + 1) for _ in range(n + 1)]
    
    # -------------------------------
    # Base case: empty subtree
    # -------------------------------
    # When i > j (i.e., i == j+1), there are no keys
    # Cost is just the probability of unsuccessful search q
    for i in range(1, n + 2):
        e[i][i - 1] = q[i - 1]
        w[i][i - 1] = q[i - 1]
    
    # -------------------------------
    # Build solutions for increasing subtree sizes
    # -------------------------------
    for l in range(1, n + 1):  # l = length of subtree
        for i in range(1, n - l + 2):
            j = i + l - 1  # ending index
            
            # Initialize with infinity (we want minimum)
            e[i][j] = float('inf')
            
            # Compute total probability for this subtree
            # Use previous result to avoid recomputation
            w[i][j] = w[i][j - 1] + p[j] + q[j]
            
            # -------------------------------
            # Try every key as root
            # -------------------------------
            for r in range(i, j + 1):
                
                # Cost if r is chosen as root:
                # left subtree cost + right subtree cost + total weight
                t = e[i][r - 1] + e[r + 1][j] + w[i][j]
                
                # Update if we found a better (smaller) cost
                if t < e[i][j]:
                    e[i][j] = t
                    root[i][j] = r
    
    # Return full tables
    return e, root

p = [0, 0.15, 0.10, 0.05]  # 1-based
q = [0.05, 0.10, 0.05, 0.05]

e, root = optimal_bst(p, q, 3)

print("Minimum cost:", e)
print("Root:", root)