# Gravitation chapter revision report

## Phase summary

**Phase 0 — Baseline**
- Treated the uploaded `gravitation.ipynb` as the current baseline.
- Preserved the existing chapter structure, section order, headings, examples, figures, and problem sets.

**Phase 0.5 — Chapter roadmap**
- Added a `Chapter roadmap` admonition immediately after the chapter title using `:class: tip`.
- The roadmap uses one short opening paragraph, three student-facing focus questions, and one closing sentence.

**Phase 1 — Main text typo and syntax pass**
- Corrected limited surface issues such as obvious grammar/typo errors.
- Converted unstarred `align` environments to `align*`.
- Removed `\\[6pt]` spacing commands so no `\[...\]`-style pattern remains.
- Preserved the main explanatory text and author voice.

**Phase 2 — Worked example pass**
- Verified all 15 worked examples use the canonical `etamu-exercise` structure.
- Confirmed each worked example follows the required order: Problem → Model → Math → Conclusion → Verification.
- Updated the "Escape from Earth" worked example to start from the standard escape-speed equation and emphasize that mass and radius/distance must correspond to the same central body.
- Updated notation in the escape-speed example to use $a_\oplus$ for Earth’s semimajor axis so students can distinguish it from $R_\oplus$.
- Updated the "Comparing Tidal Forces" worked example to show how the near-side/far-side force difference is simplified into the $M/d^3$ tidal scaling.
- Kept Math sections condensed where practical while still developing general equations before numerical substitution.
- Improved verification code comments where needed and preserved complete explanatory print statements.

**Phase 3 — Figure and caption pass**
- Replaced minimal image-credit-only captions with student-facing captions for all `figure-md` blocks.
- Added direct OpenStax section links to OpenStax figure captions.
- Preserved existing image URLs and responsive image sizing.

**Phase 4 — Checkpoint pass**
- Added four short conceptual checkpoint admonitions using `:class: tip margin checkpoint`.
- Checkpoints target inverse-square scaling, gravity in low Earth orbit, centripetal force in circular orbit, and the distinction between overall gravity and tidal effects.

**Phase 5 — Video and interactive suggestions**
- Did not insert new videos directly into the notebook to avoid overloading the chapter.
- Suggested a small set of videos/interactives below with ready-to-paste blocks and recommended insertion points.

**Phase 6 — Previous-chapter connection pass**
- Existing short connections to Newton’s laws, circular motion, energy, and angular momentum were preserved.
- No long review paragraphs were added.

## Validation checks

- `nbformat.validate` passed.
- All 15 worked examples contain the required dropdown.
- All worked examples with Python verification use five-backtick outer exercise fences, four-backtick dropdown fences, and three-backtick Python fences.
- No `import NumPy as np` remains.
- No `\vec{v}` occurrences remain.
- No `\[...\]` pattern remains.
- No `:open: false` remains in solution dropdowns.
- All code cells and Python verification fences passed Python syntax checks.
- All code cells and Python verification fences executed successfully in the sandbox after adding fallbacks for optional local image/glue dependencies.
- A Markdown export was generated with `jupyter-nbconvert` for practical syntax inspection.

## Suggested videos and interactives

### 1. Newton’s law of gravitation
**Recommended insertion point:** after the `Newton's Law of Universal Gravitation (Defined)` subsection and before the first worked example.

`````markdown
````{admonition} [**Khan Academy**](https://www.youtube.com/@khanacademy)
:class: tip

```{youtube} PIpnGilqefE
:width: 720
:height: 405
:align: center
```

As you watch, focus on how mass and distance affect the gravitational force. Pay special attention to the inverse-square dependence: doubling the distance does not cut the force in half, it reduces it by a factor of four.
````
`````

### 2. Satellite energy and escape speed
**Recommended insertion point:** after the `Energy in Circular Orbits` subsection or after the `Energy Required to Orbit` worked example.

`````markdown
````{admonition} [**Khan Academy**](https://www.youtube.com/@khanacademy)
:class: tip

```{youtube} A-YeMNeq55E
:width: 720
:height: 405
:align: center
```

As you watch, focus on how kinetic energy, gravitational potential energy, and total energy fit together for a satellite. This helps explain why putting a spacecraft into orbit requires much more than simply lifting it upward.
````
`````

### 3. Kepler’s laws and orbital motion
**Recommended insertion point:** after the introduction to Kepler’s laws and before the Halley’s comet worked example.

`````markdown
````{admonition} [**Khan Academy**](https://www.youtube.com/@khanacademy)
:class: tip

```{youtube} zPHnZFoiO0E
:width: 720
:height: 405
:align: center
```

As you watch, focus on how the shape of an orbit, the speed of the orbiting body, and the orbital period are connected. This is the conceptual bridge between ellipse geometry and Kepler’s third law.
````
`````

### 4. Tidal forces
**Recommended insertion point:** after `The Magnitude of the Tides` and before the tidal-force worked example.

`````markdown
````{admonition} [**CrashCourse**](https://www.youtube.com/@crashcourse)
:class: tip

```{youtube} KlWpFLfLFBI
:width: 720
:height: 405
:align: center
```

As you watch, focus on the difference between a gravitational force and a tidal force. The key idea is that tides come from how gravity changes across Earth, not just from how strong gravity is at Earth’s center.
````
`````

### 5. PhET Gravity and Orbits interactive
**Recommended insertion point:** after the circular-orbit derivation, near the existing interactive simulation block.

`````markdown
````{admonition} PhET: Gravity and Orbits
:class: tip

<iframe src="https://phet.colorado.edu/sims/html/gravity-and-orbits/latest/gravity-and-orbits_all.html"
        width="720"
        height="405"
        allowfullscreen>
</iframe>

Use the simulation to compare how changing mass, distance, and speed changes the orbit. Turn on the force arrows and path traces, then compare what happens when the object has too little speed, circular-orbit speed, and too much speed.
````
`````
