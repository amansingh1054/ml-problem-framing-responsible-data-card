# ML Problem-Framing Memo

**Project:** ML Problem Framing & Responsible Data Card  
**Status:** In mentor review  
**Owner:** [Your name]  
**Last updated:** [YYYY-MM-DD]

## 1. Decision to support

- **Real-world decision:** [Describe the decision a person or organization needs to make.]
- **Decision-maker:** [Who makes the final decision?]
- **People affected:** [Who may benefit or be harmed?]
- **Purpose:** [What outcome should improve?]
- **Out of scope:** [What must this system not decide or do?]

## 2. Prediction target

- **Target to predict:** [Define the outcome precisely.]
- **Label definition:** [How is the target measured and by whom?]
- **Prediction time:** [When would a prediction be generated?]
- **Unit of observation:** [For example, one transaction, one application, or one device-hour.]
- **Action window:** [How long after prediction can an action be taken usefully?]
- **Label availability delay:** [When does the true outcome become known?]

## 3. Is machine learning justified?

- **Current process:** [Describe today's workflow.]
- **Non-ML baseline:** [Simple rule, current policy, or majority-class baseline.]
- **Why the baseline may be insufficient:** [Evidence, not assumption.]
- **Why ML may help:** [Expected benefit and how it will be tested.]
- **Reasons not to use ML:** [Low data volume, unstable labels, high error costs, simpler rule sufficient, etc.]
- **Go/no-go criteria:** [Conditions that must be met before model training.]

## 4. Error costs and metrics

| Error or outcome | Cost / impact | Who bears the cost? | Mitigation |
|---|---|---|---|
| False positive | [Specify] | [Specify] | [Specify] |
| False negative | [Specify] | [Specify] | [Specify] |
| True positive | [Specify benefit] | [Specify] | [Specify] |
| True negative | [Specify benefit] | [Specify] | [Specify] |

- **Business metric:** [For example, time saved, avoidable loss, or service quality.]
- **Model metrics:** [Choose metrics suitable for the task and class balance.]
- **Minimum acceptable performance:** [Set with stakeholders.]
- **Subgroup checks:** [Define appropriate and lawful checks.]

## 5. Human review and abstention

- **Abstain when:** [Low confidence, missing critical fields, out-of-distribution input, conflicting signals, etc.]
- **Human-review queue:** [Which cases go to a qualified reviewer?]
- **Reviewer authority:** [Can the reviewer override the system?]
- **Appeal/correction path:** [How can affected people correct errors?]

## 6. Monitoring and rollback

- **Monitoring frequency:** [Specify.]
- **Data-quality checks:** [Specify.]
- **Performance/drift checks:** [Specify.]
- **Incident owner:** [Specify.]
- **Rollback trigger:** [Pre-agreed measurable condition.]
- **Fallback process:** [What happens if the model is unavailable or unsafe?]

## 7. Decision

- [ ] Proceed to data validation
- [ ] Collect more evidence
- [ ] Use a non-ML solution
- [ ] Stop the project

**Rationale:** [Summarize evidence and open questions.]
