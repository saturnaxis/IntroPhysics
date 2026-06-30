# Chapter 12 Revision Report

Revised file: `static-equilibrium-elasticity_revised-etamu-dropdown.ipynb`

## Phase summary

### Phase 0: Baseline
- Treated the uploaded `static-equilibrium-elasticity.ipynb` as the current baseline.
- Preserved the existing chapter structure, section order, example sequence, in-class problems, and homework sections.

### Phase 0.5: Chapter roadmap
- Added a `Chapter roadmap` admonition immediately after the chapter title.
- Used `:class: tip` and the required structure: short opening paragraph, three focus questions, and a closing sentence.

### Phase 1: Main text typo and surface-error pass
- Corrected clear typos and small technical surface errors, including:
  - `\sum_j \vec{F}_k` corrected to `\sum_j \vec{F}_j`.
  - `whin` corrected to `when`.
  - `on longer linear` corrected to `no longer linear`.
  - `tectonic planets` corrected to `tectonic plates`.
  - `bulk*` fixed to `**bulk**`.
  - Removed `\[6pt]` line-spacing syntax so no `\[` remains.
- Avoided broad rewriting of the main explanatory text.

### Phase 2: Worked examples and etamu-exercise pass
- Verified all 10 worked examples use the canonical `etamu-exercise` structure.
- Verified every worked example has the required order:
  1. **The Problem**
  2. **The Model**
  3. **The Math**
  4. **The Conclusion**
  5. **The Verification**
- Verified every worked example uses `Show worked solution` dropdowns with:
  - `:color: secondary`
  - `:icon: pencil`
  - `:class-container: etamu-dropdown`
  - `:class-title: etamu-dropdown-title`
  - `:class-body: etamu-dropdown-body`
- Confirmed no dropdown uses the `:open:` option.
- Ensured examples containing Python verification use five-backtick exercise fences, four-backtick dropdown fences, and three-backtick Python fences.
- Improved the pillar verification text and Python comments so the computational verification mirrors the analytic method more clearly.

### Phase 3: Figure and caption pass
- Updated OpenStax figure captions to be more descriptive and instructional.
- Added direct OpenStax section links to figure credits.
- Improved figure alt text for the main chapter figures.
- Converted in-class and homework images from centered raw HTML blocks into valid nested `figure-md` blocks.
- Added descriptive captions to the in-class and homework figures.

### Phase 4: Checkpoint pass
- Added five short student-facing checkpoint questions using:
  ```markdown
  ```{admonition} Checkpoint
  :class: tip margin checkpoint
  ```
  ```
- Checkpoints target static equilibrium, pivot choice, stress, Young's modulus, and elastic versus plastic behavior.

### Phase 5: Video and interactive suggestion pass
- Did not insert new videos or interactives directly into the notebook to avoid overloading the chapter.
- Suggested two videos and one interactive below with ready-to-paste blocks and recommended insertion points.

### Phase 6: Previous-chapter connection pass
- Added a short connection in the static-equilibrium problem-solving strategy section noting that the chapter reuses free-body diagrams and force-component reasoning from Newton's laws, then adds torque balance for extended objects.

## Validation pass

Completed checks:

- Notebook validates with `nbformat`.
- Notebook exports to Markdown with `jupyter nbconvert --to markdown`.
- All Python code fences parse with Python `ast.parse`.
- No `import NumPy as np` remains.
- No `\vec{v}` remains.
- No `\[` remains.
- No dropdown contains `:open:`.
- All worked examples contain the required Problem → Model → Math → Conclusion → Verification order.
- All worked examples include the required dropdown.
- Figure captions are no longer bare `Image Credit: OpenStax.` captions.

## Suggested videos and interactives

### Suggested insertion point: after the `Problem Solving Strategy` admonition in `Examples of Static Equilibrium`

`````markdown
````{admonition} [**Khan Academy**](https://www.youtube.com/khanacademy)
:class: tip

```{youtube} TQQXpFhACSU
:width: 720
:height: 405
:align: center
```

As you watch, focus on how the same force can produce different torques depending on where it acts relative to the pivot. Pay attention to the lever arm idea, because that is the step that usually determines whether a static-equilibrium setup is correct.
````
`````

### Suggested insertion point: after the discussion of torque balance or before the meter-stick example

````markdown
````{admonition} [**PhET Interactive Simulations**](https://phet.colorado.edu/)
:class: tip

<iframe src="https://phet.colorado.edu/sims/html/balancing-act/latest/balancing-act_en.html" width="720" height="405" allowfullscreen></iframe>

Use the Balance Lab to move objects to different distances from the pivot. Compare cases where a lighter object farther from the pivot balances a heavier object closer to the pivot, and connect what you see to the torque condition for static equilibrium.
````
````

### Suggested insertion point: after Table 12.1 or before the `Stretching a Rod` example

`````markdown
````{admonition} [**The Organic Chemistry Tutor**](https://www.youtube.com/@TheOrganicChemistryTutor)
:class: tip

```{youtube} DLE-ieOVFjI
:width: 720
:height: 405
:align: center
```

As you watch, focus on the distinction between stress, strain, and Young's modulus. The key idea is that stress describes the applied force per area, strain describes the fractional deformation, and Young's modulus describes how strongly the material resists that deformation.
````
`````
