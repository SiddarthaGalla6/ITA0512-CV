models = {"A": {"train": 97, "test": 75}, "B": {"train": 90, "test": 88}}
print(f"{'Model':<8}{'Train%':<10}{'Test%':<10}{'Gap':<8}{'Overfit Risk'}")
for m, v in models.items():
gap = v["train"] - v["test"]
risk = "HIGH" if gap > 10 else ("MODERATE" if gap > 5 else "LOW")
print(f"{m:<8}{v['train']:<10}{v['test']:<10}{gap:<8}{risk}")
print("\nDeployment score = test_accuracy - 0.5 * gap")
for m, v in models.items():
gap = v["train"] - v["test"]
score = v["test"] - 0.5*gap
print(f" Model {m}: {v['test']} - 0.5*{gap} = {score:.1f}")
best = max(models, key=lambda m: models[m]["test"] - 0.5*(models[m]["train"]-models[m]["test"]))
print(f"\nRecommended for deployment: Model {best}")


Output :
Model   Train%   Test%   Gap   Overfit Risk
A         97      75     22       HIGH
B         90      88      2       LOW
Deployment score = test_accuracy - 0.5 * gap
Model A: 75 - 0.5*22 = 64.0
Model B: 88 - 0.5*2 = 87.0
Recommended for deployment: Model B
