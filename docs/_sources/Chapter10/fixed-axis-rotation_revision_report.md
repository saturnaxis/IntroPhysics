# Revision Report: fixed-axis-rotation.ipynb

## Baseline and workflow

The uploaded `fixed-axis-rotation.ipynb` was treated as the current baseline. The revised notebook was saved with a descriptive suffix:

- `fixed-axis-rotation_revised_dropdowns.ipynb`

## Phase summary

### Phase 0: Baseline
- Preserved the chapter structure, section order, examples, in-class problems, homework blocks, and author voice.
- Did not reorganize the chapter or revert to earlier drafts.

### Phase 0.5: Chapter roadmap
- Added a `Chapter roadmap` admonition immediately after the chapter title.
- Used `:class: tip`.
- Followed the required structure: short opening paragraph, three focus questions, and a closing preview sentence.

### Phase 1: Main text typo and surface-error pass
- Corrected surface typos and clear technical slips only.
- Fixed broken or inconsistent math notation where it affected correctness.
- Repaired the time-independent rotational kinematics derivation so it gives
  `\omega_f^2 = \omega_0^2 + 2\alpha(\Delta \theta)`.
- Removed `\[...\]`-style patterns from the notebook.
- Preserved `$\vec{\rm v}$` for velocity vectors.

### Phase 2: Worked example / etamu-exercise pass
- Converted all 19 worked examples to the canonical `etamu-exercise` dropdown structure.
- Kept the Problem visible.
- Moved the Model, Math, Conclusion, and Verification sections inside `Show worked solution` dropdowns.
- Used:
  - five backticks for the outer `{exercise}` block,
  - four backticks for the `{dropdown}` block,
  - three backticks for Python fences.
- Updated dropdown metadata:
  - `:color: secondary`
  - `:icon: pencil`
  - `:class-container: etamu-dropdown`
  - `:class-title: etamu-dropdown-title`
  - `:class-body: etamu-dropdown-body`
- Verified that all worked examples follow:
  Problem → Model → Math → Conclusion → Verification.

### Phase 3: Figure and caption pass
- Checked all `figure-md` blocks for valid image syntax.
- Verified descriptive alt text, responsive sizing, and direct image URLs.
- Replaced generic `Image Credit: Openstax.` captions with OpenStax credits linked to the relevant direct OpenStax section or the Chapter 10 Problems page.

### Phase 4: Checkpoint pass
- Added five short, conceptual, student-facing checkpoints using:
  ```markdown
  ```{admonition} Checkpoint
  :class: tip margin checkpoint
  ```
  ```
- Checkpoints were placed near major conceptual transitions:
  - tangential speed vs. radius,
  - angular acceleration direction,
  - mass distribution and moment of inertia,
  - torque and lever arm,
  - rotational work and angular displacement.

### Phase 5: Video and interactive suggestion pass
Suggested resources are listed below. I did not insert them into the notebook to avoid overloading the chapter.

### Phase 6: Previous-chapter connection pass
- Preserved existing previous-chapter links where they directly supported the current material.
- Did not add broad review paragraphs.

## Final validation

Completed checks:

- Notebook validates with `nbformat`.
- Markdown export with `jupyter nbconvert --to markdown` completed successfully.
- All 19 worked examples have the required section order.
- All 19 worked examples have the required dropdown.
- All worked-example fences use the required nesting depth.
- No `import NumPy as np` remains.
- No `\vec{v}` remains.
- No `\[...\]` remains.
- All Markdown Python code fences parse with Python `ast`.
- All code cells parse with Python `ast`.
- All 19 Verification Python snippets executed successfully in isolation.
- Figure blocks include `<img>` tags with `src`, `alt`, and responsive `style` attributes.

I did not execute the full notebook end-to-end in the sandbox because the local environment does not include `myst_nb`, which the notebook uses for `glue`. The Verification snippets themselves were executed successfully.

---

# Suggested videos and interactive

## Suggested insertion point 1

Place after the right-hand rule / angular velocity vector discussion, before the first worked example.

````markdown
````{admonition} [**Khan Academy**](https://www.youtube.com/@khanacademy)
:class: tip

```{youtube} garegCgMxxg
:width: 720
:height: 405
:align: center
```

As you watch, focus on the difference between angular displacement, angular velocity, and angular acceleration. Pay attention to how the same circular motion can be described with both linear quantities and angular quantities.
````
````

## Suggested insertion point 2

Place after the section introducing rotational work and power, before the worked pulley example.

````markdown
````{admonition} [**The Organic Chemistry Tutor**](https://www.youtube.com/@TheOrganicChemistryTutor)
:class: tip

```{youtube} KbYejyiRsFw
:width: 720
:height: 405
:align: center
```

As you watch, focus on how torque, rotational work, rotational kinetic energy, and power fit together. Compare each rotational equation to the linear work-energy equations you already know.
````
````

## Suggested interactive

Place after the table connecting angular and translational quantities.

````markdown
```{admonition} [**PhET Interactive Simulations: Ladybug Revolution**](https://phet.colorado.edu/en/simulations/rotation/)
:class: tip

Open the Ladybug Revolution simulation and switch the angle units to radians. Move the ladybug to different radii while keeping the angular velocity fixed, then compare the angular velocity, tangential velocity, and acceleration vectors. Focus on which quantities change with radius and which stay the same for a rigid rotating platform.
```
````

