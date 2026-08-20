models = {
"Model A": {"accuracy": 94, "latency": 60},
"Model B": {"accuracy": 96, "latency": 80},
"Model C": {"accuracy": 95, "latency": 65},
}
MIN_ACCURACY = 95
MAX_LATENCY = 70
def evaluate(models, min_acc, max_lat):
feasible = {}
report = []
for name, m in models.items():
acc_ok = m["accuracy"] >= min_acc
lat_ok = m["latency"] < max_lat
status = "PASS" if (acc_ok and lat_ok) else "FAIL"
reasons = []
if not acc_ok:
reasons.append(f"accuracy {m['accuracy']}% < {min_acc}%")
if not lat_ok:
reasons.append(f"latency {m['latency']}ms >= {max_lat}ms")
reason_text = ", ".join(reasons) if reasons else "meets both constraints"
report.append((name, m["accuracy"], m["latency"], status, reason_text))
if acc_ok and lat_ok:
feasible[name] = m
return feasible, report
feasible, report = evaluate(models, MIN_ACCURACY, MAX_LATENCY)
print("Constraint Evaluation Report:")
for name, acc, lat, status, reason in report:
print(f" {name}: accuracy={acc}%, latency={lat}ms -> {status} ({reason})")
if feasible:
best_name = max(feasible, key=lambda n: feasible[n]["accuracy"])
best = feasible[best_name]
print(f"\nSelected Model: {best_name} (accuracy={best['accuracy']}%, latency={best['laten
cy']}ms)")
else:
print("\nNo model satisfies both constraints.")


Output :
Constraint Evaluation Report:
Model A: accuracy=94%, latency=60ms -> FAIL (accuracy 94% < 95%)
Model B: accuracy=96%, latency=80ms -> FAIL (latency 80ms >= 70ms)
Model C: accuracy=95%, latency=65ms -> PASS (meets both constraints)
Selected Model: Model C (accuracy=95%, latency=65ms)                                                                              
