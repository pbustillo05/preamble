def d(x, y, mod):
    """Calculates the cyclic distance on the modulo torus."""
    diff = abs(x - y)
    return min(diff, mod - diff)

def generate_table(n):
    """Generates the LaTeX array for E_n."""
    rows = 2**n       # i goes from 0 to 2^n - 1
    cols = 2**(n+1)   # j goes from 0 to 2^{n+1} - 1
    
    latex_table = []
    latex_table.append("\\begin{array}{" + "c" * cols + "}")
    
    for i in range(rows):
        row_str = []
        for j in range(cols):
            # L1 product distance from (0,0)
            d1 = d(i, 0, rows) + d(j, 0, cols)
            # L1 product distance from (2^{n-1}, 2^n)
            # Note: For n=0, 2^{n-1} would be a fraction, but the prompt says n >= 0. 
            # Given n=1,2,3 we use integer powers.
            d2 = d(i, 2**(n-1), rows) + d(j, 2**n, cols)
            
            # Distance constraint
            if d1 >= 2**(n-1) and d2 >= 2**(n-1):
                row_str.append("\\bullet")
            else:
                row_str.append("\\circ")
        latex_table.append(" & ".join(row_str) + " \\\\")
        
    latex_table.append("\\end{array}")
    return "\n".join(latex_table)

for n in [1, 2, 3]:
    print(f"n = {n}")
    print(generate_table(n))
    print("\n")