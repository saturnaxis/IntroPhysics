# Computational and Writing Primer

This short primer introduces the tools you will use throughout this course to write, compute, and verify physics problems. It is not a programming course, and you are not expected to become a software developer. Instead, the goal is to give you just enough structure to use computation as a **thinking and verification tool**.

You should return to this chapter whenever you need a refresher.

## Working in Google Colab

### What Is a Jupyter Notebook?

A **Jupyter notebook** is a document that combines explanatory text, mathematical equations, executable code, and output in a single place. In this course, notebooks serve the same role as a lab notebook or worked-solution sheet: they record *what you did*, *why you did it*, and *how you checked it*.

Notebooks are made of **cells**, which come in two main types:
- **Markdown cells**, used for explanations and equations
- **Code cells**, used for calculations and verification

#### Mini Exercise

Create a new notebook cell and change it to a Markdown cell. Write one sentence describing what a Jupyter notebook is used for in this course.

````{admonition} Solution
:class: dropdown

A Jupyter notebook is used to combine written explanations, mathematical equations, and executable code in a single document so that physical reasoning and calculations can be recorded together.
````

### Opening the Book in Google Colab

Each chapter of this book can be opened directly in **Google Colab** by clicking the rocket icon at the top of the page and selecting *Google Colab*. This opens a copy of the notebook in your browser without requiring any local software installation.

#### Mini Exercise

Open any chapter in Google Colab and run one existing code cell.

````{admonition} Solution
:class: dropdown

If the code cell executes without errors and produces output, the notebook is running correctly in the Colab environment.
````

## Python Basics for Physics

### Variables

A **variable** stores a value so that it can be reused later. Variables allow us to name physical quantities and keep track of them symbolically.

```python
distance = 80      # meters
time = 4           # seconds
speed = distance / time
print(speed)
```

#### Mini Exercise

Define variables for a distance of 120 m and a time of 6 s. Compute and print the speed.

````{admonition} Solution
:class: dropdown

```python
distance = 120
time = 6
speed = distance / time
print(speed)
```
````

### Comments

Comments explain *why* a calculation is being performed. They are ignored by Python but essential for readability.

```python
# Convert meters to kilometers
distance_km = distance / 1000
```

#### Mini Exercise

Add a comment explaining what a calculation represents physically.

````{admonition} Solution
:class: dropdown

```python
# This calculation determines the average speed of the object
speed = distance / time
```
````

### Importing Libraries

Scientific calculations commonly rely on external libraries. The most frequently used library in this course is **NumPy**.

```python
import numpy as np
```

NumPy provides mathematical constants, array operations, and numerical functions.

#### Mini Exercise

Use NumPy to compute the area of a circle with radius 3.5 m.

````{admonition} Solution
:class: dropdown

```python
import numpy as np

r = 3.5
area = np.pi * r**2
print(area)
```
````

### Lists and Arrays

A **list** stores multiple values, while a **NumPy array** allows mathematical operations to be applied to all values at once.

```python
measurements = [4.8, 5.3, 4.9, 5.4]
weights = np.array(measurements)
```

#### Mini Exercise

Create a list of four measurements, convert it to a NumPy array, and compute the average.

````{admonition} Solution
:class: dropdown

```python
import numpy as np

measurements = [4.8, 5.3, 4.9, 5.4]
weights = np.array(measurements)
print(np.mean(weights))
```
````

### For Loops

A **for loop** repeats an action for each item in a collection.

```python
for value in measurements:
    print(value)
```

#### Mini Exercise

Write a loop that prints each measurement multiplied by 2.

````{admonition} Solution
:class: dropdown

```python
for value in measurements:
    print(2 * value)
```
````

### Functions

Functions package calculations so they can be reused and clearly named.

```python
def percent_uncertainty(A, dA):
    return (dA / A) * 100
```

#### Mini Exercise

Write a function that computes speed given distance and time.

````{admonition} Solution
:class: dropdown

```python
def speed(distance, time):
    return distance / time
```
````

## Writing in Markdown

Markdown cells are used for **clear scientific writing**, not for computation.

### Headings, Emphasis, and Lists

```md
# Section Title
## Subsection Title

*italic text*  
**bold text**

- first item
- second item
```

#### Mini Exercise

Create a Markdown cell with a heading and a bulleted list describing a problem-solving strategy.

````{admonition} Solution
:class: dropdown

```md
## Strategy
- Identify known quantities
- Choose appropriate equations
- Solve the math
- Verify the result
```
````

### Inline Code

Use backticks to refer to code inside text, such as `np.sqrt()`.

## Mathematics with LaTeX

LaTeX is used to typeset mathematical expressions.

### Inline Mathematics

```md
The area is $A = \pi r^2$.
```

Rendered: The area is $A = \pi r^2$.

### Displayed Equations

```md
$$ A = \pi r^2 $$
```

Rendered: 

$$ A = \pi r^2 $$

### Aligned Equations

```md
\begin{align*}
v &= \frac{d}{t} \\
  &= \frac{80\ \text{m}}{4\ \text{s}} \\
  &= 20\ \text{m/s}.
\end{align*}
```

Rendered:

\begin{align}
v &= \frac{d}{t} \\
  &= \frac{80\ \text{m}}{4\ \text{s}} \\
  &= 20\ \text{m/s}.
\end{align}

#### Mini Exercise

Write the LaTeX expression for average speed.

````{admonition} Solution
:class: dropdown

The average speed is given by $\displaystyle v = \frac{d}{t}$.
````

## How Python Fits into Problem Solving

In this course, Python is used **after** the physics reasoning is complete. It serves as a verification tool, not a substitute for understanding.

The typical workflow is:
1. Build a physical model
2. Solve the math analytically
3. Verify the result using Python

### Example Verification

```python
distance = 80    # meters
time = 4         # seconds

speed = distance / time
print(f"Speed = {speed:.1f} m/s")
```

#### Mini Exercise

Change the distance and time values and observe how the speed changes.

````{admonition} Solution
:class: dropdown

Increasing the distance increases the speed, while increasing the time decreases the speed, consistent with the definition $v = d/t$.
````

## Common Mistakes to Avoid

- Writing explanations in code cells
- Using Python without understanding the physics
- Dropping units during calculations
- Treating Python as a formula lookup tool

Python should support your reasoning, not replace it.

## What You Are Expected to Know

By the end of the semester, you should be comfortable with:
- creating and editing Jupyter notebooks,
- defining variables and functions,
- importing NumPy,
- writing Markdown explanations,
- typesetting equations in LaTeX,
- using Python to verify results.

## Final Advice

A Jupyter notebook is a **record of your thinking**. Someone reading your notebook later should be able to follow your reasoning without additional explanation.
