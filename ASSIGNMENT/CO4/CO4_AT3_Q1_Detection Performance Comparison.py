models = {
    "Model A (Viola-Jones)": {"TP": 80, "FP": 20, "FN": 30},
    "Model B (YOLO)":        {"TP": 90, "FP": 15, "FN": 20},
}
def compute_metrics(tp, fp, fn):
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * precision * recall / (precision + recall)
    return precision, recall, f1
print(f"{'Model':<24}{'Precision':<12}{'Recall':<12}{'F1-Score':<10}")
results = {}
for name, m in models.items():
    p, r, f1 = compute_metrics(m["TP"], m["FP"], m["FN"])
    results[name] = (p, r, f1)
    print(f"{name:<24}{p*100:>8.2f}%   {r*100:>8.2f}%   {f1*100:>7.2f}%")
best = max(results, key=lambda n: results[n][2])
print(f"\nBetter Model (highest F1-Score): {best}")


Output:
Model                   Precision   Recall      F1-Score
Model A (Viola-Jones)      80.00%      72.73%     76.19%
Model B (YOLO)             85.71%      81.82%     83.72%

Better Model (highest F1-Score): Model B (YOLO)
