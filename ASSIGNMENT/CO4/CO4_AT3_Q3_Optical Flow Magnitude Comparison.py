regions = ["R1", "R2", "R3"]
method_a = [5, 6, 5]
method_b = [8, 10, 9]
avg_a = sum(method_a) / len(method_a)
avg_b = sum(method_b) / len(method_b)
print(f"{'Region':<8}{'Method A':<12}{'Method B':<12}")
for r, a, b in zip(regions, method_a, method_b):
    print(f"{r:<8}{a:<12}{b:<12}")
print(f"\nAverage Magnitude - Method A: {avg_a:.2f} px/frame")
print(f"Average Magnitude - Method B: {avg_b:.2f} px/frame")
stronger = "Method A" if avg_a > avg_b else "Method B"
print(f"\nMethod Capturing Stronger Motion (higher average magnitude): {stronger}")


Output:
Region  Method A    Method B
R1      5           8
R2      6           10
R3      5           9
Average Magnitude - Method A: 5.33 px/frame
Average Magnitude - Method B: 9.00 px/frame
Method Capturing Stronger Motion (higher average magnitude): Method B
