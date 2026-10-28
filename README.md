# ML Problem Framing & Responsible Data Card

A starter repository for deciding whether machine learning is justified for a real-world decision **before training a model**. It documents the decision, data risks, evaluation costs, human review, monitoring, and rollback.

> **Project status:** In mentor review. This repository is a starter implementation and example template, not a completed or validated ML system.

## Objectives

- Define the decision, prediction target, unit of observation, action window, and non-ML baseline.
- Document data provenance, consent, sensitive attributes, missingness, and leakage risks.
- Select business and model metrics with explicit false-positive and false-negative costs.
- Design abstention, human-review, monitoring, and rollback conditions.

## Repository contents

```text
ml_problem_framing_responsible_data_card/
├── README.md
├── problem_framing_memo.md
├── responsible_data_card.md
├── risk_register.csv
├── baseline.py
├── baseline_notebook.ipynb
├── requirements.txt
└── .gitignore
```

## Quick start

This starter baseline uses only Python's standard library.

```bash
python baseline.py
```

It prints a simple majority-class baseline on a small **synthetic example dataset**. You can also open `baseline_notebook.ipynb` in Jupyter or Google Colab. The example is for demonstrating a baseline approach only; it is not evidence that ML is appropriate for any real use case.

## How to use this repository

1. Choose a real decision and identify who is affected.
2. Complete `problem_framing_memo.md`.
3. Complete `responsible_data_card.md` using verified information about your actual data.
4. Update `risk_register.csv` with project-specific risks, owners, and mitigations.
5. Establish an appropriate non-ML baseline before training a model.
6. Agree on metrics, review thresholds, monitoring, and rollback criteria with stakeholders.
7. Do not use real or sensitive personal data in this starter example.

## Important limitations

- No real dataset is included.
- The sample data in `baseline.py` is synthetic and intentionally tiny.
- No trained ML model is included.
- The example thresholds and costs must be decided with domain experts; they are not universal recommendations.
- Do not deploy a model or use its output to make consequential decisions without appropriate validation, privacy/security review, and human oversight.

## Expected proof

- ML problem-framing memo
- Responsible data card
- Baseline notebook or script (this repository includes a baseline script; you can add a notebook later)
- Risk register

## License

Choose a license before sharing or reusing this repository (for example, MIT if appropriate for your project).
