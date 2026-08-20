models = {
"A": {"accuracy": 82, "latency": 30},
"B": {"accuracy": 90, "latency": 70},
"C": {"accuracy": 95, "latency": 120},
}
def select_under_latency(models, max_latency_ms):
eligible = {m: v for m, v in models.items() if v["latency"] <= max_latency_ms}
if not eligible:
return None, {}
best = max(eligible, key=lambda m: eligible[m]["accuracy"])
return best, eligible
for threshold in [50, 100, 150]:
best, eligible = select_under_latency(models, threshold)
print(f"Latency budget <= {threshold} ms | Eligible: {list(eligible.keys())} | "
f"Selected: {best if best else 'NONE MEET CONSTRAINT'}")


Output:
Latency budget <= 50 ms | Eligible: ['A'] | Selected: A
Latency budget <= 100 ms | Eligible: ['A', 'B'] | Selected: B
Latency budget <= 150 ms | Eligible: ['A', 'B', 'C'] | Selected: C
