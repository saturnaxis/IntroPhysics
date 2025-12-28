# etamu-exercise Template

Use this template for **all worked examples** in JupyterBook using the **etamu-exercise** style.  
Replace bracketed placeholders with your content. Do not remove required sections.

---

````{`exercise}
:class: etamu-exercise

**The Problem**

> [COPY THE PROBLEM VERBATIM HERE.]  
>  
> [All values, symbols, and vectors must be written in math mode using $ $.
> Do not paraphrase. Preserve wording and structure.]

---

**The Model**

[Describe the physical model and assumptions.
Focus on how the system is idealized, not how it is solved.
State reference frames, forces, constraints, and approximations.
No numerical substitution here.]

---

**The Math**

[Introduce the governing principles in words before writing equations.]

[If two or more equations appear consecutively, use an align block:]

\begin{align*}
[First equation] \\
[Second equation]
\end{align*}

[Continue the derivation in a narrative style.
Define symbols at first use.
Use $\hat{i}$, $\hat{j}$, $\hat{k}$ for unit vectors.
Apply significant figures based on measurement precision, not convention.]

[End this section with the fully evaluated result(s), including units.]

---

**The Conclusion**

[State the final numerical result(s) clearly.
Explain what the result means physically.
Connect back to the model and assumptions.
No new calculations here.]

---

**The Verification**

[Briefly explain what is being verified numerically.]

```python
# Verification code
# Use NumPy and Matplotlib as needed
# Recompute the result numerically
# Print labeled values for comparison

import numpy as np
import matplotlib.pyplot as plt

# [Define parameters]
# [Compute quantities]
# [Print results]

# Optional minimal figure (geometry, vectors, or trajectory)
fig = plt.figure(figsize=(5,4), dpi=120)
ax = fig.add_subplot(111)

# [Plot minimal sketch or vectors]
# Prefer annotate arrows over ax.arrow when aspect distortion matters
# Do not have a plot title; Annotations, labels, and legend provides context
ax.set_xticks([])
ax.set_yticks([])

plt.tight_layout()
plt.show()
```
````