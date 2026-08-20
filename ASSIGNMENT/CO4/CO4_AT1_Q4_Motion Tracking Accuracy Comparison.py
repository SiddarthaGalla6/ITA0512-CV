label_score = {"High": 90, "Moderate": 65, "Low": 35}
methods = {
"A": {"accuracy": label_score["High"], "stability": label_score["Low"]},
"B": {"accuracy": label_score["Moderate"], "stability": label_score["High"]},
}
w_acc, w_stab = 0.35, 0.65
print(f"{'Method':<8}{'Accuracy':<10}{'Stability':<10}{'Long-term Score'}")
for m, v in methods.items():
score = w_acc*v["accuracy"] + w_stab*v["stability"]
print(f"{m:<8}{v['accuracy']:<10}{v['stability']:<10}{score:.2f}")
best = max(methods, key=lambda m: w_acc*methods[m]["accuracy"] + w_stab*methods[m]["stability"])
print(f"\nRecommended for long-term tracking: Method {best}")


Output:
Method   Accuracy   Stability   Long-term Score
A           90         35           54.25
B           65         90           81.25
Recommended for long-term tracking: Method B
