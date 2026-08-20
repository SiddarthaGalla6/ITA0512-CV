methods = {
"Stereo": {"accuracy": 3, "hardware": 1}, 
"SfM": {"accuracy": 2, "hardware": 3}, 
}
w_acc, w_hw = 0.4, 0.6
print(f"{'Method':<8}{'AccScore':<10}{'HWScore':<10}{'Weighted Suitability'}")
for m, v in methods.items():
score = w_acc*v["accuracy"] + w_hw*v["hardware"]
print(f"{m:<8}{v['accuracy']:<10}{v['hardware']:<10}{score:.2f}")
best = max(methods, key=lambda m: w_acc*methods[m]["accuracy"] + w_hw*methods[m]["hardware"])
print(f"\nRecommended under hardware constraints: {best}")


Output:
Method   AccScore   HWScore     Weighted Suitability
Stereo     3           1               1.80
SfM        2           3               2.60
Recommended under hardware constraints: SfM
