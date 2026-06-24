# Narrative Check Report: Fixed-Axis Rotation Examples

## Scope

Checked the **Model**, **Math**, **Conclusion**, and **Verification** sections of all 19 `etamu-exercise` worked examples in `fixed-axis-rotation_revised_dropdowns.ipynb` against the narrative requirements in the chapter revision rules.

## Rules Checked

- The Model should describe the physical system and assumptions, but should not include equations, calculations, or references to problem parts.
- The Math section should use narrative-first derivations, with complete declarative sentences before displayed equations.
- The Math section should avoid vague connector phrases such as “Substituting values,” “Substituting the given values,” and “Substituting the numerical values gives.”
- The Conclusion should state the final result, include units and significant figures, and provide a brief physical interpretation.
- The Verification section should give a high-level computational confirmation, mirror the analytical method, avoid new physics, and include complete-sentence outputs in code.

## Issues Found and Corrected

### Model sections

Revised Model sections that contained inline equations or formula-like statements. The affected examples were:

- Rotation of a Flywheel
- Torque on Particles
- Torque on a Rigid Body
- Effect of Mass Distribution on a Merry-Go-Round
- Torque on a Boat Propeller

These were rewritten so the Model describes the governing framework and assumptions without equations or calculations.

### Math sections

Revised Math sections that used fragment-style or vague equation introductions. Common replacements included:

- “Solving this expression…” → “We solve this expression…”
- “Substituting these values gives…” → a full sentence naming the physical quantity being evaluated
- “Using the given values gives…” → a full declarative sentence naming the relevant quantity and relationship

The affected examples included:

- Spinning Bicycle Wheel
- Energy in a Boomerang
- Helicopter Energies
- Effect of Mass Distribution on a Merry-Go-Round
- Rotational Work and Energy
- Rotational Work: A Pulley
- Torque on a Boat Propeller

### Conclusion sections

Checked that each Conclusion includes both the numerical result and a short physical interpretation. The centrifuge example was strengthened with an additional interpretive sentence emphasizing that the centripetal component dominates near the end of the spin-down.

### Verification sections

Checked that Verification sections describe the computational method at a high level rather than restating only the numerical result. The centrifuge Verification was expanded to explicitly state that the computational calculation reproduces the analytical solution.

## Validation

- All 19 worked examples were checked.
- No Model section still contains equation-like math or references to problem parts.
- No Math section still contains the flagged phrases:
  - “Substituting values”
  - “Substituting these values”
  - “Substituting the given values”
  - “Substituting the numerical values gives”
  - “Solving this expression”
  - “Using the ... gives”
- All Markdown Python code blocks parse successfully with Python `ast`.
- All code cells parse successfully with Python `ast`.
- The revised notebook validates with `nbformat`.
- Markdown export with `jupyter nbconvert --to markdown` completed successfully.

## Output File

The revised notebook is:

`fixed-axis-rotation_revised_narrative_checked.ipynb`
