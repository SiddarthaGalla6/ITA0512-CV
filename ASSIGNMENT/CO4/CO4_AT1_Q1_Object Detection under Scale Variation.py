data = {"Large": 94, "Medium": 80, "Small": 55}
drop_lm = data["Large"] - data["Medium"]
drop_ms = data["Medium"] - data["Small"]
avg_accuracy = sum(data.values()) / len(data)
print("Accuracy by object size:", data)
print(f"Drop Large->Medium: {drop_lm} pts | Drop Medium->Small: {drop_ms} pts")
print(f"Unweighted average accuracy: {avg_accuracy:.2f}%")
freq_weights = {"Large": 0.15, "Medium": 0.35, "Small": 0.50}
weighted_accuracy = sum(data[k] * freq_weights[k] for k in data)
print(f"Frequency-weighted deployment accuracy: {weighted_accuracy:.2f}%")
threshold = 70
for size, acc in data.items():
print(f" {size}: {'PASS' if acc >= threshold else 'FAIL'} ({acc}%) vs {threshold}% threshold")


Output :
Accuracy by object size: {'Large': 94, 'Medium': 80, 'Small': 55}
Drop Large->Medium: 14 pts | Drop Medium->Small: 25 pts
Unweighted average accuracy: 76.33%
Frequency-weighted deployment accuracy: 69.60%
Large: PASS (94%) vs 70% threshold
Medium: PASS (80%) vs 70% threshold
Small: FAIL (55%) vs 70% threshold
