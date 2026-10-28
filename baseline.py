"""Tiny synthetic majority-class baseline for the project starter.

This is an illustrative baseline, not a real-world model or evidence that ML is
justified. Replace the synthetic example only after data permissions and the
problem framing have been reviewed.
"""

from collections import Counter

# Synthetic labels only. These do not represent real people or real outcomes.
y_true = [0, 0, 0, 0, 1, 0, 1, 0, 0, 0]

counts = Counter(y_true)
majority_label, majority_count = counts.most_common(1)[0]
predictions = [majority_label] * len(y_true)

correct = sum(actual == predicted for actual, predicted in zip(y_true, predictions))
accuracy = correct / len(y_true)

print("Synthetic example — majority-class baseline")
print(f"Rows: {len(y_true)}")
print(f"Majority label: {majority_label}")
print(f"Baseline accuracy: {accuracy:.1%}")
print("Reminder: accuracy alone may be misleading, especially with imbalanced classes.")
print("Define false-positive/false-negative costs and suitable metrics with stakeholders.")
