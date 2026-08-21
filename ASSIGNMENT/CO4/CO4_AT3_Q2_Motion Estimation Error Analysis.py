frames = [1, 2, 3]
method_a = [2, 3, 2]
method_b = [3, 5, 4]
avg_a = sum(method_a) / len(method_a)
avg_b = sum(method_b) / len(method_b)
print(f"{'Frame':<8}{'Method A':<12}{'Method B':<12}")
for f, a, b in zip(frames, method_a, method_b):
    print(f"{f:<8}{a:<12}{b:<12}")
print(f"\nAverage Error - Method A: {avg_a:.2f} px")
print(f"Average Error - Method B: {avg_b:.2f} px")
better = "Method A" if avg_a < avg_b else "Method B"
print(f"\nMore Accurate Method (lower average displacement error): {better}")



Output:
Frame   Method A    Method B
1       2           3
2       3           5
3       2           4

Average Error - Method A: 2.33 px
Average Error - Method B: 4.00 px

More Accurate Method (lower average displacement error): Method A
