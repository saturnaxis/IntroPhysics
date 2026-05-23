# PHYS 2425 Chapter 5 Revised Example Problems, Canonical Dropdown Style (v4)
These revised markdown blocks preserve the original problem statements and figure directives from the Chapter 5 notebook while applying the canonical `etamu-exercise` dropdown rules. The solution sections are written to keep the Model free of algebra and numerical substitution, move coordinate choices into the Model, and make the Math section narrative-first.

---

#### **Example Problem**: Applying Newton's 1st Law to your car

`````{exercise}
:class: etamu-exercise

**The Problem**

> Newton's laws can be applied to all physical processes involving force and motion, including something as mundane as driving a car.
>
> (a) Your car is parked outside your house. Does Newton's first law apply in this situation? Why or why not?
>
> (b) Your car moves at constant velocity down the street. Does Newton's first law apply in this situation? Why or why not?

````{dropdown} Show worked solution
:color: secondary
:icon: pencil
:class-container: etamu-dropdown
:class-title: etamu-dropdown-title
:class-body: etamu-dropdown-body

**The Model**

The car is modeled as a single object observed from the ground, which we treat as an inertial reference frame. For the parked car, the coordinate system has $+\hat{j}$ upward. For the moving car, $+\hat{i}$ points in the direction of motion and $+\hat{j}$ points upward. In both cases, the question is not whether forces exist, but whether the vector sum of the external forces is zero.

For the parked car, the only forces that need to be considered are the downward weight and the upward contact force from the ground. For the car moving at constant velocity, the vertical forces still balance, and the horizontal driving force from the road balances the resistive forces from air drag and rolling resistance.

---

**The Math**

Newton's first law applies when the net external force on an object is zero. Under that condition, the acceleration is zero, so the object remains at rest or moves with constant velocity,

$$
\sum \vec{F}_{\rm ext} = \vec{0} \quad \Rightarrow \quad \vec{a}=\vec{0}.
$$

For the parked car, the weight acts downward and the ground exerts an upward contact force. Writing these qualitatively as $\vec{W}=-w\,\hat{j}$ and $\vec{N}=n\,\hat{j}$, the force sum is

\begin{align*}
\sum \vec{F}_{\rm ext} &= \vec{N}+\vec{W},\\
&= n\,\hat{j}-w\,\hat{j},\\
&= (n-w)\,\hat{j}.
\end{align*}

Since the parked car is not accelerating, the net force is zero and $n=w$. Newton's first law therefore applies.

For the car moving at constant velocity, the acceleration is still zero. The vertical forces balance as before. In the horizontal direction, the forward force from the road on the tires must balance the backward resistive force. If $\vec{F}_{\rm road}=f\,\hat{i}$ and $\vec{F}_{\rm res}=-f\,\hat{i}$, then

$$
\vec{F}_{\rm road}+\vec{F}_{\rm res}=\vec{0}.
$$

The total net force is zero, so Newton's first law applies in this case as well.

---

**The Conclusion**

Newton's first law applies in both situations. For the parked car, the upward contact force from the ground balances the downward weight. For the car moving at constant velocity, the vertical forces balance and the horizontal driving and resistive forces also balance. The important point is that zero net force means zero acceleration, not necessarily zero velocity.

---

**The Verification**

The Python check in the next cell represents each force as a vector and confirms that the net force is zero in both cases. The free-body diagrams are schematic and are used to show balanced forces, not to represent a specific car or numerical force scale.

````
`````

---

#### **Example Problem**: Pushing a Lawnmower

`````{exercise}
:class: etamu-exercise

**The Problem**

> Suppose that the net external force (push minus friction) exerted on a lawn mower is $51\ \text{N}$ (about $11\ \text{lb}.)$ parallel to the ground (Figure {numref}`{number}<mower-force-fig>`). The mass of the mower is $24\ \text{kg}$. What is its acceleration?

```{figure-md} mower-force-fig
<img src="https://openstax.org/apps/image-cdn/v1/f=webp/apps/archive/20251118.192121/resources/301730c548a739c3cc3e4830700fe6ef50e7aedd" alt="net force on mower"  style="max-width:70%; height:auto;">

(a) The net force on a lawn mower is 51 N to the right. At what rate does the lawn mower accelerate to the right? (b) The free-body diagram for this problem is shown. Figure Credit: OpenStax: [Newton's Second Law](https://openstax.org/books/university-physics-volume-1/pages/5-3-newtons-second-law)
```

````{dropdown} Show worked solution
:color: secondary
:icon: pencil
:class-container: etamu-dropdown
:class-title: etamu-dropdown-title
:class-body: etamu-dropdown-body

**The Model**

The lawn mower is modeled as a particle moving on level ground. The positive $x$ direction is chosen parallel to the ground in the direction of the stated net force, and the positive $y$ direction is upward. The problem already gives the net horizontal force, so the individual push and friction forces do not need to be modeled separately. The vertical forces balance and do not affect the horizontal acceleration.

---

**The Math**

Newton's second law relates the net external force to the acceleration of the mower. With the net force and acceleration both along $+\hat{i}$, we can write $\vec{F}_{\rm net}=(51\ {\rm N})\hat{i}$ and $\vec{a}=a\hat{i}$. We substitute the force vector and acceleration vector into Newton's second law to obtain

\begin{align*}
\sum \vec{F}_{\rm ext} &= m\vec{a},\\
(51\ {\rm N})\hat{i} &= (24\ {\rm kg})(a\hat{i}).
\end{align*}

Because both sides point in the same direction, the scalar magnitudes satisfy

\begin{align*}
51\ {\rm N} &= (24\ {\rm kg})a,\\
a &= \frac{51\ {\rm N}}{24\ {\rm kg}},\\
&= 2.1\ {\rm m/s^2}.
\end{align*}

---

**The Conclusion**

The lawn mower accelerates at $2.1\ {\rm m/s^2}$ in the direction of the net force. This result uses the net external force, not the applied push alone, because friction has already been subtracted from the push in the given force.

---

**The Verification**

The Python check in the next cell recomputes $a=F_{\rm net}/m$ and checks that $ma$ reproduces the given net force. The accompanying free-body diagram shows the net horizontal force used in the calculation.

````
`````

---

#### **Example Problem**: Comparing Forces

`````{exercise}
:class: etamu-exercise

**The Problem**

> (a) The car shown in Figure {numref}`{number}<car-force-fig>` is moving at a constant speed. Which force is bigger, $\vec{F}_{\text{friction}}$ or $\vec{F}_{\text{drag}}$? Explain.
>
> (b) The same car is now accelerating to the right. Which force is bigger, $\vec{F}_{\text{friction}}$ or $\vec{F}_{\text{drag}}$? Explain.

```{figure-md} car-force-fig
<img src="https://openstax.org/apps/image-cdn/v1/f=webp/apps/archive/20251118.192121/resources/4208aa77e974f170b705874223ddfa5927e09929" alt="comparing forces on car"  style="max-width:70%; height:auto;">

A car is shown (a) moving at constant speed and (b) accelerating. How do the forces acting on the car compare in each case? (a) What does the knowledge that the car is moving at constant velocity tell us about the net horizontal force on the car compared to the friction force? (b) What does the knowledge that the car is accelerating tell us about the horizontal force on the car compared to the friction force? Figure Credit: OpenStax: [Newton's Second Law](https://openstax.org/books/university-physics-volume-1/pages/5-3-newtons-second-law)
```

````{dropdown} Show worked solution
:color: secondary
:icon: pencil
:class-container: etamu-dropdown
:class-title: etamu-dropdown-title
:class-body: etamu-dropdown-body

**The Model**

The car is modeled as a particle moving horizontally. The positive $x$ direction is chosen to the right, in the direction of motion. The forward force $\vec{F}_{\rm friction}$ is the static friction force exerted by the road on the tires, while $\vec{F}_{\rm drag}$ represents resistive forces such as air drag and rolling resistance acting opposite the motion. Vertical forces balance and are not needed for the horizontal comparison.

---

**The Math**

**(a)** For the constant-speed case, the car moves in a straight line with zero acceleration. Newton's second law then requires the horizontal net force to be zero. Taking right as positive,

\begin{align*}
\sum F_x &= 0,\\
F_{\rm friction}-F_{\rm drag} &= 0.
\end{align*}

Thus the two forces have equal magnitudes.

**(b)** For the accelerating case, the car accelerates to the right. Newton's second law requires the net horizontal force to point to the right, so

\begin{align*}
\sum F_x &= ma_x,\\
F_{\rm friction}-F_{\rm drag} &> 0.
\end{align*}

This inequality means that the forward static friction force must be larger than the backward drag force.

---

**The Conclusion**

For constant-speed motion, $\vec{F}_{\rm friction}$ and $\vec{F}_{\rm drag}$ have equal magnitudes and opposite directions. When the car accelerates to the right, the forward friction force is larger than the backward drag force. The distinction is not whether the car is moving, but whether its velocity is changing.

---

**The Verification**

The Python check in the next cell draws schematic free-body diagrams for the two cases. In the constant-speed case, the horizontal force vectors are equal in length; in the accelerating case, the forward force is longer, producing a net force to the right.

````
`````

---

#### **Example Problem**: Thrust on a Sled

`````{exercise}
:class: etamu-exercise

**The Problem**

> Before space flights carrying astronauts, rocket sleds were used to test aircraft, missile equipment, and physiological effects on human subjects at high speeds. They consisted of a platform that was mounted on one or two rails and propelled by several rockets.
>
> Calculate the magnitude of force exerted by each rocket, called its thrust $T$, for the four-rocket propulsion system shown in Figure {numref}`{number}<sled-force-fig>`. The sled's initial acceleration is $49\ \text{m/s}^2$, the mass of the system is $2100\ \text{kg}$, and the force of friction opposing the motion is $650\ \text{N}$.

```{figure-md} sled-force-fig
<img src="https://openstax.org/apps/image-cdn/v1/f=webp/apps/archive/20251118.192121/resources/af7c2b785de4e2c3ce7256ee0e357cb2c7e32fcd" alt="forces on rocket sled"  style="max-width:65%; height:auto;">

A sled experiences a rocket thrust that accelerates it to the right. Each rocket creates an identical thrust T. The system here is the sled, its rockets, and its rider, so none of the forces between these objects are considered. Figure Credit: OpenStax: [Newton's Second Law](https://openstax.org/books/university-physics-volume-1/pages/5-3-newtons-second-law)
```

````{dropdown} Show worked solution
:color: secondary
:icon: pencil
:class-container: etamu-dropdown
:class-title: etamu-dropdown-title
:class-body: etamu-dropdown-body

**The Model**

The system is the rocket sled, rockets, and rider treated as one object moving horizontally. The positive $x$ direction is chosen in the direction of the sled's acceleration, and the positive $y$ direction is upward. Four identical rockets exert equal thrusts in the positive $x$ direction, while friction acts in the negative $x$ direction. The normal force and weight balance vertically, so the acceleration is entirely horizontal.

---

**The Math**

Newton's second law is applied along the horizontal direction. The total forward thrust from the four rockets is $4T$, and the friction force of magnitude $f$ opposes the motion. The corresponding force equation is

\begin{align*}
\sum F_x &= ma,\\
4T-f &= ma.
\end{align*}

We solve the horizontal force equation for the thrust from one rocket because $T$ is the requested unknown quantity.

\begin{align*}
4T &= ma+f,\\
T &= \frac{ma+f}{4}.
\end{align*}

We now substitute the sled mass, acceleration, and friction force into the expression for the thrust from one rocket:

\begin{align*}
T &= \frac{(2100\ {\rm kg})(49\ {\rm m/s^2})+650\ {\rm N}}{4},\\
&= 2.6\times10^4\ {\rm N}.
\end{align*}

The result is reported to two significant figures because the acceleration is given as $49\ {\rm m/s^2}$.

---

**The Conclusion**

Each rocket must exert a thrust of $2.6\times10^4\ {\rm N}$. The total thrust must both overcome friction and provide the net force needed to accelerate the massive sled. The vertical forces are not part of this calculation because they balance and produce no vertical acceleration.

---

**The Verification**

The Python check in the next cell recomputes the total thrust from $4T=ma+f$ and divides by four. The free-body diagram is schematic and shows the four thrust forces acting forward and the friction force acting backward.

````
`````

---

#### **Example Problem**: Force on a Soccer Ball

`````{exercise}
:class: etamu-exercise

**The Problem**

A $0.400\ \text{kg}$ soccer ball is kicked across the field by a player; it undergoes acceleration given by $\vec{a} = 3.00\hat{i} + 7.00\hat{j}\ \text{m/s}^2.$ Find (a) the resultant force acting on the ball and (b) the magnitude and direction of the resultant force.

````{dropdown} Show worked solution
:color: secondary
:icon: pencil
:class-container: etamu-dropdown
:class-title: etamu-dropdown-title
:class-body: etamu-dropdown-body

**The Model**

The soccer ball is modeled as a particle moving in the $x$-$y$ plane. The positive $x$ direction is along $\hat{i}$, and the positive $y$ direction is along $\hat{j}$. The given acceleration already provides the acceleration components in this coordinate system. The net external force represents the combined effect of all interactions acting on the ball during the kick.

---

**The Math**

Newton's second law can be applied directly in vector form because the acceleration is already written in component form. Multiplying the acceleration vector by the mass gives the net force vector,

\begin{align*}
\vec{F}_{\rm net} &= m\vec{a},\\
&= (0.400\ {\rm kg})(3.00\hat{i}+7.00\hat{j})\ {\rm m/s^2},\\
&= (1.20\hat{i}+2.80\hat{j})\ {\rm N}.
\end{align*}

This is the resultant force in component form. The magnitude is found from the components,

\begin{align*}
F_{\rm net} &= \sqrt{F_x^2+F_y^2},\\
&= \sqrt{(1.20\ {\rm N})^2+(2.80\ {\rm N})^2},\\
&= 3.05\ {\rm N}.
\end{align*}

The direction is measured counterclockwise from the $+\hat{i}$ axis. Since both force components are positive, the force lies in the first quadrant,

\begin{align*}
\theta &= \tan^{-1}\!\left(\frac{F_y}{F_x}\right),\\
&= \tan^{-1}\!\left(\frac{2.80}{1.20}\right),\\
&= 66.8^\circ.
\end{align*}

---

**The Conclusion**

The resultant force on the soccer ball is $\vec{F}_{\rm net}=(1.20\hat{i}+2.80\hat{j})\ {\rm N}$. Its magnitude is $3.05\ {\rm N}$, directed $66.8^\circ$ counterclockwise from the $+\hat{i}$ axis. The force points in the same direction as the acceleration because the mass is a positive scalar.

---

**The Verification**

The Python check in the next cell recomputes the force components from $\vec{F}_{\rm net}=m\vec{a}$ and then calculates the magnitude and direction using the same component relationships. The diagram shows the net force vector and its components.

````
`````

---

#### **Example Problem**: Mass of a Car

`````{exercise}
:class: etamu-exercise

**The Problem**

> Find the mass of a car if a net force of $-600.0\,\hat{j}\ \text{N}$ produces an acceleration of $-0.2\,\hat{j}\ \text{m/s}^2$.

````{dropdown} Show worked solution
:color: secondary
:icon: pencil
:class-container: etamu-dropdown
:class-title: etamu-dropdown-title
:class-body: etamu-dropdown-body

**The Model**

The car is modeled as a particle subject to a net external force. The positive $y$ direction is chosen along $+\hat{j}$, so both the given net force and acceleration point in the negative $y$ direction. The force and acceleration are parallel, so a scalar component equation can represent the motion. No other forces need to be modeled separately because the net force is already given.

---

**The Math**

Newton's second law relates the net external force to the acceleration,

$$
\sum \vec{F}_{\rm ext}=m\vec{a}.
$$

Mass is a scalar, so we do not divide vectors. Instead, because the force and acceleration point in the same direction, we compare their magnitudes,

$$
F_{\rm net}=ma.
$$

We solve Newton's second law for the scalar mass because the mass is the requested unknown quantity.

\begin{align*}
m &= \frac{F_{\rm net}}{a},\\
&= \frac{600.0\ {\rm N}}{0.2\ {\rm m/s^2}},\\
&= 3\times10^3\ {\rm kg}.
\end{align*}

The direction signs cancel because the force and acceleration are both in the $-\hat{j}$ direction.

---

**The Conclusion**

The mass of the car is $3\times10^3\ {\rm kg}$. The result is a scalar, so it has no direction. The negative signs in the original vectors tell us that the force and acceleration point in the same direction, not that the mass is negative.

---

**The Verification**

The Python check computes the ratio of the force magnitude to the acceleration magnitude, matching the scalar form of Newton's second law used in the analytical solution. The printed result uses significant-figure-appropriate scientific notation so the output does not imply more precision than the given acceleration supports.

```python
import numpy as np
import matplotlib.pyplot as plt

Fnet = 600.0   # N
a = 0.2        # m/s^2

m = Fnet/a

print(f"The computed mass of the car is {m:.1g} kg.")
```

````
`````

---

#### **Example Problem**: Several Forces

`````{exercise}
:class: etamu-exercise

**The Problem**

> A particle of mass $m = 4.0\ \text{kg}$ is acted upon by four forces of magnitudes $F_1 = 10.0\ \text{N}$, $F_2 = 40.0\ \text{N}$, $F_3 = 5.0\ \text{N}$, and $F_4 = 2.0\ \text{N}$, with the directions as shown in the free-body diagram in Fig. {numref}`{number}<four-forces-fig>`.  What is the acceleration of the particle?

```{figure-md} four-forces-fig
<img src="https://openstax.org/apps/image-cdn/v1/f=webp/apps/archive/20251118.192121/resources/c99b424299139944364181eb0d08967715c107e3" alt="four forces"  style="max-width:70%; height:auto;">

Four forces in the xy-plane are applied to a 4.0-kg particle. Figure Credit: OpenStax: [Newton's Second Law](https://openstax.org/books/university-physics-volume-1/pages/5-3-newtons-second-law)
```

````{dropdown} Show worked solution
:color: secondary
:icon: pencil
:class-container: etamu-dropdown
:class-title: etamu-dropdown-title
:class-body: etamu-dropdown-body

**The Model**

The particle is modeled as a point mass moving in the $x$-$y$ plane. The positive $x$ direction is to the right and the positive $y$ direction is upward, matching the axes shown in the free-body diagram. Each force is treated as an external force acting on the particle. The force $F_1$ has both $x$ and $y$ components, while $F_2$, $F_3$, and $F_4$ act along coordinate axes.

---

**The Math**

Newton's second law is applied independently in the $x$ and $y$ directions,

\begin{align*}
\sum F_x &= ma_x,\\
\sum F_y &= ma_y.
\end{align*}

In the $x$ direction, $F_1$ contributes a positive component $F_1\cos30^\circ$, and $F_3$ acts in the negative $x$ direction. The corresponding force equation is

\begin{align*}
F_1\cos30^\circ - F_3 &= ma_x,\\
a_x &= \frac{F_1\cos30^\circ-F_3}{m}.
\end{align*}

We now substitute the force magnitudes and mass into the expression for the horizontal acceleration:

\begin{align*}
a_x &= \frac{(10.0\ {\rm N})\cos30^\circ - 5.0\ {\rm N}}{4.0\ {\rm kg}},\\
&= 0.92\ {\rm m/s^2}.
\end{align*}

In the $y$ direction, the vertical component of $F_1$ and the force $F_4$ act upward, while $F_2$ acts downward. The corresponding force equation is

\begin{align*}
F_1\sin30^\circ+F_4-F_2 &= ma_y,\\
a_y &= \frac{F_1\sin30^\circ+F_4-F_2}{m}.
\end{align*}

We now substitute the vertical force magnitudes and mass into the expression for the vertical acceleration:

\begin{align*}
a_y &= \frac{(10.0\ {\rm N})\sin30^\circ+2.0\ {\rm N}-40.0\ {\rm N}}{4.0\ {\rm kg}},\\
&= -8.3\ {\rm m/s^2}.
\end{align*}

Combining the components gives the acceleration vector,

$$
\vec{a}=(0.92\hat{i}-8.3\hat{j})\ {\rm m/s^2}.
$$

---

**The Conclusion**

The particle accelerates as $\vec{a}=(0.92\hat{i}-8.3\hat{j})\ {\rm m/s^2}$. The acceleration is mostly downward because the downward force $F_2$ is much larger than the upward forces, while the horizontal forces only partially fail to cancel.

---

**The Verification**

The Python check in the next cell resolves the angled force into components, sums all four force vectors, and divides by the mass. The free-body diagram confirms that the force directions used in the calculation match the diagram.

````
`````

---

#### **Example Problem**: Lifting a Stone

`````{exercise}
:class: etamu-exercise

**The Problem**

>A farmer is lifting some moderately heavy rocks from a field to plant crops.  He lifts a stone that weighs $40.0\ \text{lb}$ (about $180\ \text{N}$). What force does he apply if the stone accelerates upward at a rate of $1.5\ \text{m/s}^2$?

````{dropdown} Show worked solution
:color: secondary
:icon: pencil
:class-container: etamu-dropdown
:class-title: etamu-dropdown-title
:class-body: etamu-dropdown-body

**The Model**

The stone is modeled as a particle moving vertically. The positive $y$ direction is chosen upward, in the direction of the stone's acceleration. The farmer exerts an upward applied force on the stone, while the stone's weight acts downward. Air resistance is neglected. The stated weight is the gravitational force on the stone, not its mass.

---

**The Math**

The stone's weight is related to its mass by $w=mg$. We solve Newton's second law for the scalar mass because the mass is the requested unknown quantity.

$$
m=\frac{w}{g}.
$$

We substitute the given weight and $g=9.81\ {\rm m/s^2}$ into the expression for the mass of the stone.

\begin{align*}
m &= \frac{180\ {\rm N}}{9.81\ {\rm m/s^2}},\\
&= 18.3\ {\rm kg}.
\end{align*}

Newton's second law is applied in the vertical direction. The applied force $F$ is upward and the weight $w$ is downward, so

\begin{align*}
\sum F_y &= ma_y,\\
F-w &= ma.
\end{align*}

We solve the vertical force equation for the applied force because the farmer's force is the requested unknown quantity.

\begin{align*}
F &= ma+w,\\
&= (18.3\ {\rm kg})(1.5\ {\rm m/s^2})+180\ {\rm N},\\
&= 210\ {\rm N}.
\end{align*}

---

**The Conclusion**

The farmer applies an upward force of $210\ {\rm N}$ to the stone. This force is larger than the stone's weight because the stone is accelerating upward; if the applied force equaled the weight, the net force would be zero and the stone would not accelerate.

---

**The Verification**

The Python check in the next cell computes the mass from the given weight and then applies Newton's second law to recover the required applied force. The free-body diagram confirms that the applied force must be larger than the weight for the net force to point upward.

````
`````

---

### **Example Problem**: Forces on a Stationary Object

`````{exercise}
:class: etamu-exercise

**The Problem**

> The package in Figure {numref}`{number}<scale-reaction-fig>` is sitting on a scale. For the scale and package at rest (i.e., not accelerating), show that the scale indicates the weight of the package.

```{figure-md} scale-reaction-fig
<img src="https://openstax.org/apps/image-cdn/v1/f=webp/apps/archive/20251118.192121/resources/00c26de7728563423d12455f471da91123b49cfb" alt="scale reaction force"  style="max-width:55%; height:auto;">

(a) The forces on a package sitting on a scale, along with their reaction forces. The force $\vec{w}$ is the weight of the package (the force due to Earth’s gravity) and $\vec{s}$  is the force of the scale on the package. (b) Isolation of the package-scale system and the package-Earth system makes the action and reaction pairs clear. Figure Credit: OpenStax: [Newton's Third Law](https://openstax.org/books/university-physics-volume-1/pages/5-5-newtons-third-law)
```

````{dropdown} Show worked solution
:color: secondary
:icon: pencil
:class-container: etamu-dropdown
:class-title: etamu-dropdown-title
:class-body: etamu-dropdown-body

**The Model**

The system is the package alone. The positive $y$ direction is chosen upward, so the scale force on the package points in the $+\hat{j}$ direction and the weight points in the $-\hat{j}$ direction. The package is at rest in an inertial frame, so its acceleration is zero. Only vertical forces act on the package; the reaction forces shown in the figure act on other objects and are not included in the free-body diagram of the package.

---

**The Math**

Newton's second law requires the net external force to be zero when the acceleration is zero,

\begin{align*}
\sum \vec{F}_{\rm ext} &= m\vec{a},\\
&= \vec{0}.
\end{align*}

The scale exerts an upward force $\vec{s}=s\,\hat{j}$ on the package, and Earth exerts the downward weight $\vec{w}=-w\,\hat{j}$. The force balance on the package is

\begin{align*}
\vec{s}+\vec{w} &= \vec{0},\\
s\,\hat{j}-w\,\hat{j} &= \vec{0},\\
(s-w)\,\hat{j} &= \vec{0}.
\end{align*}

For this vector to be zero, the scalar magnitudes must be equal,

$$
s=w.
$$

---

**The Conclusion**

The scale reading equals the package's weight when the package is at rest. More precisely, the scale measures the upward contact force it exerts on the package, and in this zero-acceleration case that contact force has the same magnitude as the gravitational force on the package.

---

**The Verification**

The Python check in the next cell represents the scale force and weight as equal and opposite vertical vectors. The resulting net force is zero, and the free-body diagram shows the forces acting on the package.

````
`````

---

### **Example Problem**: Force on the Cart (Part 1)

`````{exercise}
:class: etamu-exercise

**The Problem**

> A physics professor pushes a cart of demonstration equipment to a lecture hall (Figure {numref}`{number}<cart-reaction-fig>`). Her mass is $65\ {\rm kg}$, the cart’s mass is $12\ {\rm kg}$, and the equipment’s mass is $7\ {\rm kg}$. Calculate the acceleration produced when the professor exerts a backward force of $150\ {\rm N}$ on the floor. All forces opposing the motion, such as friction on the cart’s wheels and air resistance, total $24.0\ {\rm N}$.

```{figure-md} cart-reaction-fig
<img src="https://openstax.org/apps/image-cdn/v1/f=webp/apps/archive/20251118.192121/resources/7954635a55ec857e43667d5a90ed1aa42226b970" alt="cart reaction force"  style="max-width:55%; height:auto;">

A professor pushes the cart with her demonstration equipment. The lengths of the arrows are proportional to the magnitudes of the forces (except for $\vec{f}$, because it is too small to be drawn to scale). System 1 is appropriate for this example, because it asks for the acceleration of the entire group of objects. Only $\vec{F}_{\rm floor}$  and $\vec{f}$ are external forces acting on System 1 along the line of motion. All other forces either cancel or act on the outside world. System 2 is chosen for the next example so that $\vec{F}_{\rm prof}$ is an external force and enters into Newton’s second law. The free-body diagrams, which serve as the basis for Newton’s second law, vary with the system chosen. Figure Credit: OpenStax: [Newton's Third Law](https://openstax.org/books/university-physics-volume-1/pages/5-5-newtons-third-law)
```

````{dropdown} Show worked solution
:color: secondary
:icon: pencil
:class-container: etamu-dropdown
:class-title: etamu-dropdown-title
:class-body: etamu-dropdown-body

**The Model**

The system is the professor, cart, and equipment together, corresponding to System 1 in the figure. The positive $x$ direction is chosen forward, in the direction of the motion, and the positive $y$ direction is upward. The floor exerts a forward force on the system because the professor pushes backward on the floor. The total resistive force from wheel friction and air resistance acts backward. The vertical forces balance, and forces between the professor, cart, and equipment are internal to this chosen system.

---

**The Math**

Newton's second law is applied to the external horizontal forces on System 1. The forward force from the floor has magnitude $F_{\rm floor}$, and the total resistive force has magnitude $f$, so

\begin{align*}
\sum F_x &= ma,\\
F_{\rm floor}-f &= ma.
\end{align*}

The mass of the system is the sum of the professor, cart, and equipment masses,

\begin{align*}
m &= 65\ {\rm kg}+12\ {\rm kg}+7\ {\rm kg},\\
&= 84\ {\rm kg}.
\end{align*}

We solve the horizontal force equation for the acceleration because the acceleration is the requested unknown quantity.

\begin{align*}
a &= \frac{F_{\rm floor}-f}{m},\\
&= \frac{150\ {\rm N}-24.0\ {\rm N}}{84\ {\rm kg}},\\
&= 1.5\ {\rm m/s^2}.
\end{align*}

---

**The Conclusion**

The professor, cart, and equipment accelerate forward at $1.5\ {\rm m/s^2}$. This acceleration is determined by the net external horizontal force on System 1, not by the internal forces between the professor and the cart.

---

**The Verification**

The Python check in the next cell recomputes the total system mass, the net external horizontal force, and the acceleration. The free-body diagram shows the external forces on System 1: the forward floor force, the backward resistive force, and the balancing vertical forces.

````
`````

---

### **Example Problem**: Force on the Cart (Part 2)

`````{exercise}
:class: etamu-exercise

**The Problem**

> Calculate the force the professor exerts on the cart in Figure {numref}`{number}<cart-reaction-fig>`, using data from the previous example if needed.

````{dropdown} Show worked solution
:color: secondary
:icon: pencil
:class-container: etamu-dropdown
:class-title: etamu-dropdown-title
:class-body: etamu-dropdown-body

**The Model**

The system is now the cart plus the equipment, corresponding to System 2 in the previous figure. The positive $x$ direction is forward, in the direction of the acceleration found in the previous example, and the positive $y$ direction is upward. The professor's push on the cart is external to this smaller system. The same total resistive force opposes the motion, and the vertical forces balance.

---

**The Math**

For System 2, the horizontal external forces are the professor's forward force and the backward resistive force. Newton's second law gives

\begin{align*}
\sum F_x &= ma,\\
F_{\rm prof}-f &= ma.
\end{align*}

We solve the horizontal force equation for the professor's force on the cart because that force is the requested unknown quantity.

$$
F_{\rm prof}=ma+f.
$$

The mass of System 2 is the cart plus the equipment,

\begin{align*}
m &= 12.0\ {\rm kg}+7.0\ {\rm kg},\\
&= 19.0\ {\rm kg}.
\end{align*}

We now use the acceleration found in the previous example in the expression for the professor's force on System 2:

\begin{align*}
F_{\rm prof} &= (19.0\ {\rm kg})(1.5\ {\rm m/s^2})+24.0\ {\rm N},\\
&= 53\ {\rm N}.
\end{align*}

---

**The Conclusion**

The professor exerts a forward force of $53\ {\rm N}$ on the cart. This is smaller than the $150\ {\rm N}$ interaction with the floor because the floor force accelerates the professor, cart, and equipment together, while $F_{\rm prof}$ only has to accelerate the cart and equipment while overcoming the resistive force on that smaller system.

---

**The Verification**

The Python check in the next cell recomputes $F_{\rm prof}=ma+f$ using the mass of System 2 and the acceleration from the previous example. The free-body diagram shows the external forces on the cart-plus-equipment system.

````
`````

---

#### **Example Problem**: Weight on an incline

`````{exercise}
:class: etamu-exercise

**The Problem**

> Consider the skier on the slope in Figure {numref}`{number}<skier-incline-fig>`. Her mass including equipment is $60.0\ \text{kg}$.
> (a) What is her acceleration if friction is negligible? 
> (b) What is her acceleration if friction is $45.0\ \text{N}$?  

```{figure-md} skier-incline-fig
<img src="https://openstax.org/apps/image-cdn/v1/f=webp/apps/archive/20251118.192121/resources/095c5f6fefc5827b20d2c19a057c48ddb4e0d793" alt="skier incline example"  style="max-width:60%; height:auto;">

Since the acceleration is parallel to the slope and acting down the slope, it is most convenient to project all forces onto a coordinate system where one axis is parallel to the slope and the other is perpendicular to it (axes shown to the left of the skier). $\vec{N}$ is perpendicular to the slope and $\vec{f}$ is parallel to the slope, but $\vec{w}$ has components along both axes, namely, $w_y$ and $w_x$. Here, $\vec{w}$ has a squiggly line to show that it has been replaced by these components. The force $\vec{N}$ is equal in magnitude to $w_y$, so there is no acceleration perpendicular to the slope, but $f$ is less than $w_x$, so there is a downslope acceleration (along the axis parallel to the slope). Figure Credit: OpenStax: [Common Forces](https://openstax.org/books/university-physics-volume-1/pages/5-6-common-forces)
```

````{dropdown} Show worked solution
:color: secondary
:icon: pencil
:class-container: etamu-dropdown
:class-title: etamu-dropdown-title
:class-body: etamu-dropdown-body

**The Model**

The skier and equipment are modeled as one particle moving along a rigid incline. The $x$ axis is chosen parallel to the slope and positive down the slope, while the $y$ axis is chosen perpendicular to the slope and positive away from the surface. With this coordinate choice, the acceleration is along the slope and there is no acceleration perpendicular to the surface. The forces are the weight $\vec{w}$, the normal force $\vec{N}$, and, when present, the friction force $\vec{f}$ acting up the slope.

---

**The Math**

The weight is resolved into components along the incline axes. With the incline angle $\theta$, the component parallel to the slope is $w_x=mg\sin\theta$, and the component perpendicular to the slope is $w_y=mg\cos\theta$. The perpendicular forces balance because $a_y=0$, so $N=w_y$.

**(a)** For the frictionless case, the only force parallel to the slope is $w_x$. Newton's second law along the slope gives

\begin{align*}
\sum F_x &= ma_x,\\
mg\sin\theta &= ma_x.
\end{align*}

The mass cancels, leaving

\begin{align*}
a_x &= g\sin\theta,\\
&= (9.81\ {\rm m/s^2})\sin25^\circ,\\
&= 4.1\ {\rm m/s^2}.
\end{align*}

**(b)** For the case with friction, the friction force acts up the slope, opposite the motion. The net force along the slope is reduced to $mg\sin\theta-f$, so

\begin{align*}
mg\sin\theta-f &= ma_x,\\
a_x &= \frac{mg\sin\theta-f}{m}.
\end{align*}

We now substitute the skier's mass, gravitational acceleration, incline angle, and friction force into the expression for the acceleration along the slope:

\begin{align*}
a_x &= \frac{(60.0\ {\rm kg})(9.81\ {\rm m/s^2})\sin25^\circ-45.0\ {\rm N}}{60.0\ {\rm kg}},\\
&= 3.4\ {\rm m/s^2}.
\end{align*}

---

**The Conclusion**

With negligible friction, the skier accelerates down the slope at $4.1\ {\rm m/s^2}$. When a $45.0\ {\rm N}$ friction force acts up the slope, the acceleration is reduced to $3.4\ {\rm m/s^2}$. Both accelerations are down the slope because the downslope component of weight is still larger than the opposing friction force.

---

**The Verification**

The Python check in the next cell computes $w_x=mg\sin\theta$, evaluates the acceleration with and without friction, and draws a schematic free-body diagram using axes aligned with the incline.

````
`````

---

#### **Example Problem**: Tension in a Tightrope

`````{exercise}
:class: etamu-exercise

**The Problem**

> Calculate the tension in the wire supporting the $70.0\ \mathrm{kg}$ tightrope walker shown in Figure {numref}`{number}<tension-tightrope-fig>`.

```{figure-md} tension-tightrope-FBD-fig
<img src="https://openstax.org/apps/image-cdn/v1/f=webp/apps/archive/20251118.192121/resources/f4d052ad93fc813ea956895cacb8f1f74e44e658" alt="tension tightrope FBD example"  style="max-width:70%; height:auto;">

When the vectors are projected onto vertical and horizontal axes, their components along these axes must add to zero, since the tightrope walker is stationary. The small angle results in $T$ being much greater than $w$. Figure Credit: OpenStax: [Common Forces](https://openstax.org/books/university-physics-volume-1/pages/5-6-common-forces)
```

````{dropdown} Show worked solution
:color: secondary
:icon: pencil
:class-container: etamu-dropdown
:class-title: etamu-dropdown-title
:class-body: etamu-dropdown-body

**The Model**

The system is the tightrope walker, treated as a particle at rest. The positive $x$ direction is horizontal to the right, and the positive $y$ direction is upward. The wire is symmetric about the walker, so the left and right tension magnitudes are equal and are denoted by $T$. Each wire segment makes the same small angle above the horizontal. The walker is stationary, so the net force is zero in both coordinate directions.

---

**The Math**

The horizontal components of the two tensions cancel by symmetry. The vertical components of the two tensions support the weight of the walker. Applying Newton's second law in the vertical direction,

\begin{align*}
\sum F_y &= 0,\\
T\sin\theta+T\sin\theta-w &= 0,\\
2T\sin\theta &= w.
\end{align*}

The weight is $w=mg$, so the tension is

\begin{align*}
T &= \frac{w}{2\sin\theta},\\
&= \frac{mg}{2\sin\theta}.
\end{align*}

We now substitute the walker's mass, gravitational acceleration, and wire angle into the tension equation:

\begin{align*}
T &= \frac{(70.0\ {\rm kg})(9.81\ {\rm m/s^2})}{2\sin5.0^\circ},\\
&= 3.9\times10^3\ {\rm N}.
\end{align*}

---

**The Conclusion**

Each side of the wire has a tension of $3.9\times10^3\ {\rm N}$. This is much larger than the walker's weight because the wire is nearly horizontal, so only a small vertical component of each tension supports the walker.

---

**The Verification**

The Python check following this example evaluates $T=mg/(2\sin\theta)$ and shows that the two vertical components $T\sin\theta$ add to the weight. The accompanying diagram resolves the two tension forces into horizontal and vertical components.

````
`````

---

### **Example Problem**: Two Blocks on an Inclined Plane

`````{exercise}
:class: etamu-exercise

**The Problem**

> Construct the free-body diagram for object A and object B in Figure {numref}`{number}<2blocks-FBD-fig>`.

```{figure-md} 2blocks-FBD-fig
<img src="https://openstax.org/apps/image-cdn/v1/f=webp/apps/archive/20251118.192121/resources/144f787db4c7c97ebb616984e0c0a811d05819b9" alt="2 blocks FBD example"  style="max-width:70%; height:auto;">

(a) The free-body diagram for isolated object A. (b) The free-body diagram for isolated object B. Comparing the two drawings, we see that friction acts in the opposite direction in the two figures. Friction always acts opposite the direction of motion or intended motion. Because object A is moving to the right, friction by B must act to the left. Object B is moving to the left relative to B, so the friction by A on B is to the right. The friction force by object A on object B is the third law pair of the friction force by B on A, and therefore these two forces must be in opposite directions. Because object B is sliding down the incline, the friction force by the ramp must oppose it and act up the ramp. Figure Credit: OpenStax: [Drawing Free-body Diagrams](https://openstax.org/books/university-physics-volume-1/pages/5-7-drawing-free-body-diagrams)
```

````{dropdown} Show worked solution
:color: secondary
:icon: pencil
:class-container: etamu-dropdown
:class-title: etamu-dropdown-title
:class-body: etamu-dropdown-body

**The Model**

Objects A and B are treated as separate particles on an inclined plane. The $x$ axis is chosen parallel to the incline, and the $y$ axis is chosen perpendicular to the incline. Object A is attached to a cord and is in contact with object B. Object B is in contact with both object A and the incline. Normal forces act perpendicular to contact surfaces, friction forces act parallel to contact surfaces, and tension acts along the cord. Each free-body diagram includes only forces acting on the isolated object.

---

**The Math**

For object A, the forces acting on the isolated object are its weight $\vec{w}_A$, the tension $\vec{T}$ from the cord, the normal force $\vec{N}_{BA}$ exerted by B on A, and the friction force $\vec{f}_{BA}$ exerted by B on A.

For object B, the forces acting on the isolated object are its weight $\vec{w}_B$, the normal force $\vec{N}_B$ from the incline, the friction force $\vec{f}_B$ from the incline, the normal force $\vec{N}_{AB}$ exerted by A on B, and the friction force $\vec{f}_{AB}$ exerted by A on B.

The contact forces between A and B occur in third-law pairs. The corresponding force equation is

\begin{align*}
\vec{N}_{AB} &= -\vec{N}_{BA},\\
\vec{f}_{AB} &= -\vec{f}_{BA}.
\end{align*}

These pairs act on different objects, so they appear on different free-body diagrams.

---

**The Conclusion**

The free-body diagram for object A contains $\vec{w}_A$, $\vec{T}$, $\vec{N}_{BA}$, and $\vec{f}_{BA}$. The free-body diagram for object B contains $\vec{w}_B$, $\vec{N}_B$, $\vec{f}_B$, $\vec{N}_{AB}$, and $\vec{f}_{AB}$. Drawing the objects separately is essential because action-reaction pairs do not cancel within a single object's free-body diagram.

---

**The Verification**

The Python check in the next cell draws representative free-body diagrams for both objects. The vectors are schematic and are intended to verify which forces belong on each isolated object.

````
`````

---

### **Example Problem**: Two Blocks in Contact

`````{exercise}
:class: etamu-exercise

**The Problem**

> A force is applied to two blocks in contact, as shown in Fig. {numref}`{number}<2blocks-contact-FBD-fig>`. Draw the reaction forces between the two blocks.

```{figure-md} 2blocks-contact-FBD-fig
<img src="https://openstax.org/apps/image-cdn/v1/f=webp/apps/archive/20251118.192121/resources/7f841e852d86c9170a71c72dc0aff0a013355033" alt="2 blocks contact FBD example"  style="max-width:70%; height:auto;">

Image Credit: OpenStax: [Drawing Free-body Diagrams](https://openstax.org/books/university-physics-volume-1/pages/5-7-drawing-free-body-diagrams)
```

````{dropdown} Show worked solution
:color: secondary
:icon: pencil
:class-container: etamu-dropdown
:class-title: etamu-dropdown-title
:class-body: etamu-dropdown-body

**The Model**

The blocks are treated as two separate systems on a horizontal surface. The positive $x$ direction is chosen to the right, in the direction of the applied force on block $m_1$. At the contact surface, block $m_1$ pushes on block $m_2$ to the right, while block $m_2$ pushes on block $m_1$ to the left. The prompt asks only for the reaction forces between the blocks, so other forces are not required unless drawing complete free-body diagrams.

---

**The Math**

Newton's third law states that the interaction forces between the two blocks have equal magnitude and opposite direction. If $\vec{A}_{12}$ is the force on block $m_2$ due to block $m_1$, and $\vec{A}_{21}$ is the force on block $m_1$ due to block $m_2$, then

$$
\vec{A}_{12}=-\vec{A}_{21}.
$$

Because block $m_1$ pushes block $m_2$ to the right, $\vec{A}_{12}$ points in the $+\hat{i}$ direction. The reaction force $\vec{A}_{21}$ therefore points in the $-\hat{i}$ direction.

---

**The Conclusion**

The reaction-force pair is $\vec{A}_{12}$ on block $m_2$ to the right and $\vec{A}_{21}$ on block $m_1$ to the left. These forces have equal magnitude and opposite direction, but they act on different blocks, so they do not cancel in either block's individual free-body diagram.

---

**The Verification**

The Python check in the next cell draws the interaction forces on separate diagrams for the two blocks. This verifies that the third-law pair acts on different objects.

````
`````

---

### **Example Problem**: Block on the Table

`````{exercise}
:class: etamu-exercise

**The Problem**

> A block rests on the table, as shown in Fig. {numref}`{number}<2blocks-contact-FBD-fig>`. A light rope is attached to it and runs over a pulley. The other end of the rope is attached to a second block. The two blocks are said to be coupled. Block $m_2$ exerts a force due to its weight, which causes the system (two blocks and a string) to accelerate.
>
> We assume that the string has no mass so that we do not have to consider it as a separate object. Draw a free-body diagram for each block.

```{figure-md} 2blocks-pulley-FBD-fig
<img src="https://openstax.org/apps/image-cdn/v1/f=webp/apps/archive/20251118.192121/resources/6074c38d1454c55251b327838e603249a92fd375" alt="2 blocks pulley FBD example"  style="max-width:70%; height:auto;">

Image Credit: OpenStax: [Drawing Free-body Diagrams](https://openstax.org/books/university-physics-volume-1/pages/5-7-drawing-free-body-diagrams)
```

````{dropdown} Show worked solution
:color: secondary
:icon: pencil
:class-container: etamu-dropdown
:class-title: etamu-dropdown-title
:class-body: etamu-dropdown-body

**The Model**

The two blocks are treated as separate systems connected by a taut, massless rope over a frictionless pulley. For block $m_1$, the positive $x$ direction is to the right, toward the pulley, and the positive $y$ direction is upward. For block $m_2$, the positive $y$ direction is upward. The table is treated as frictionless, so no friction force acts on $m_1$. The rope tension has the same magnitude on both blocks.

---

**The Math**

To construct the free-body diagrams, each block is isolated and only forces acting on that block are included.

For block $m_1$, the weight $\vec{w}_1$ acts downward, the normal force $\vec{N}$ from the table acts upward, and the rope tension $\vec{T}$ acts horizontally to the right toward the pulley.

For block $m_2$, the weight $\vec{w}_2$ acts downward and the rope tension $\vec{T}$ acts upward. The tension has the same magnitude in both diagrams because the rope is massless and the pulley is frictionless.

---

**The Conclusion**

The free-body diagram for $m_1$ contains $\vec{N}$ upward, $\vec{w}_1$ downward, and $\vec{T}$ to the right. The free-body diagram for $m_2$ contains $\vec{T}$ upward and $\vec{w}_2$ downward. The two blocks require separate free-body diagrams because the forces acting on each block are different, even though their accelerations are linked by the rope.

---

**The Verification**

The Python check in the next cell draws schematic free-body diagrams for both blocks. The purpose is to verify that the correct forces appear on each isolated block, not to solve for the acceleration or tension.

````
`````
