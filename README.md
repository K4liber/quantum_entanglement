## 1. Problem description

What is an example of a simple quantum experiment that disagree with a classical intuition implying local realism?

Such an experiment could be CHSH game[1].

We consider a maximally entangled pair of qubits (EPR pair). The probability of finding both qubits with the same state depends on the angle between measurement settings.

Why this dependency is described by the following equation?

`P(same spin) = P(↑₁↑₂) + P(↓₁↓₂) = sin²(θ/2)`

![alt text](./img/probability.png)

## 2. Glossary

`Spin`: Electrons (and many other fundamental particles) possess an intrinsic angular momentum called spin. Spin is a quantum mechanical property, and for electrons, it can have two possible values: spin-up (|↑⟩) or spin-down (|↓⟩).

`Superposition`: A fundamental principle in quantum mechanics is superposition. A particle can exist in multiple states simultaneously.

`Entanglement`: Two or more particles can become interconnected in a way that their states are no longer independent. They are said to be entangled.

`Tensor Product (⊗)`: The tensor product is used to describe combined quantum systems. For example, |↑⟩₁|↓⟩₂ represents a two-electron system where electron 1 is spin-up and electron 2 is spin-down.

`Two-electron system`: Consider a system of two electrons. Each electron can be in either the spin-up or spin-down state, resulting in four possible combinations for the system.

`Entangled Singlet State`: The entangled state of the two electrons is represented by the singlet state. This state has an interesting property: if you measure the spin of one electron, you instantly know the spin of the other (with opposite direction).

`Spin Angular Momentum (S)`: An intrinsic property of particles, independent of their spatial motion. It's like a particle spinning around its own axis. 

`Spin operator`: describes the spin angular momentum of a particle. Such an operator is applied to a mathematical representation of the physical state of a system and yields an angular momentum value if the state has a definite value for it.

`Spin Rotation operator R(θ)`: It represents a rotation of the spin state of the particle by an angle θ about an axis in the x-y plane. This rotation doesn't change the overall magnitude of the spin, but it changes its orientation in space. The specific form of R(θ) follows from the general principles of how rotations are represented in quantum mechanics. For spin-1/2 systems, 2x2 matrices act on the two-dimensional state vector.

`Unitary Operation`: The rotation operator is a unitary operator. This means that it preserves the normalization of the quantum state (i.e., the probability of finding the particle in a particular state remains 1).

## 3. CHSH game optimal strategy derivation

### Entangled Singlet State

Electrons are fermions, which means they obey the Pauli Exclusion Principle. This fundamental principle states that no two identical fermions can occupy the same quantum state simultaneously.

The quantum state of a particle encompasses not only its position but also intrinsic properties like spin.  So, two electrons cannot be in the same location and have the same spin state.

The Pauli Exclusion Principle translates into a mathematical requirement for the wavefunction describing a system of fermions: it must be antisymmetric under the exchange of particles.

Each electron in our system can exist in a superposition of spin-up (`|↑⟩`) and spin-down (`|↓⟩`) states. For two electrons, the possible combined states are:

- `|↑₁⟩|↑₂⟩` (Both spin-up)
- `|↑₁⟩|↓₂⟩` (Electron 1 spin-up, Electron 2 spin-down)
- `|↓₁⟩|↑₂⟩` (Electron 1 spin-down, Electron 2 spin-up)
- `|↓₁⟩|↓₂⟩` (Both spin-down)

The singlet state is defined by having a total spin of zero. Because electron spins have values of 1/2,  the only way to combine their spins to get zero is if they're in opposite states. This eliminates the first and last possibilities from the list above.

The quantum state of a singlet is antisymmetric under exchange. What does "antisymmetric under exchange" mean? If you swap the labels of the two electrons (1 and 2) in the wavefunction, the wavefunction changes its sign.

Now, we need to combine the remaining two possible states in a way that makes the wavefunction antisymmetric:

- If we simply add them, the wavefunction is symmetric: `|↑₁⟩|↓₂⟩` + `|↓₁⟩|↑₂⟩` (Doesn't change sign if we swap 1 and 2)
- To make it antisymmetric, we subtract them: `|↑₁⟩|↓₂⟩` - `|↓₁⟩|↑₂⟩`.  Now, swapping the electron labels changes the sign of the wavefunction.

The only way to construct a valid wavefunction with opposite spins and satisfy the antisymmetry requirement is by making a linear combination where the two possible configurations have opposite signs.

Finally, in Dirac notation the state has the following representation:
```
|Ψ⟩ = (1/√2) ( |↑₁⟩|↓₂⟩ -  |↓₁⟩|↑₂⟩)
```

### Rotated Spin Measurement

Unlike in more complicated quantum mechanical systems, the spin of a spin-1/2 particle can be expressed as a linear combination of just two eigenstates, or eigenspinors. These are traditionally labeled spin up and spin down.

The Pauli matrices are a set of three 2x2 matrices that are essential in describing the spin of particles like electrons:
```
σx = ( [0 1] [1 0] )
σy = ( [0 -i] [i 0] )
σz = ( [1 0] [0 -1] )
```

If we use the column vector representation of the various spin eigenstates, then we can use the following representation for the spin operators:
```
Sz = (ħ/2)σz = (ħ/2) * ( [1  0]
                         [0 -1] )

Sₓ = (ħ/2)σx = (ħ/2) * ( [0  1]
                         [1  0] )
```

#### Rotation Operator (in the x-y plane)

Rotations are intricately linked to angular momentum. The angular momentum operators (Sx, Sy, Sz for spin systems) are considered the 'generators'  of rotations. This means infinitesimal rotations around a specific axis can be expressed in terms of the corresponding angular momentum operator.

A powerful mathematical result tells us how to build a finite rotation from infinitesimal ones: If we have a generator of rotations, G, then a rotation by an angle θ around the axis associated with G can be represented as:

```
R(θ) = exp(-iθG / ħ)
```

The angular momentum operator for the z-axis is Sz. Similarly, the rotation operators about the x-axis and y-axis can be derived using their corresponding angular momentum operators (Sx and Sy):

```
Rz(θ) = exp(-iθσz / 2)
Rx(θ) = exp(-iθσx / 2)
Ry(θ) = exp(-iθσy / 2)
```

To get the rotation operator in the x-y plane, we need a combination of rotations about different axes.  One way to achieve this is:

Rotate about the z-axis by an angle of π/2.  
Rotate about the y-axis by an angle of θ.  
Rotate about the z-axis by an angle of -π/2.  

The combined rotation operator is the product of these individual rotation operators:
```
R(θ) = Rz(-π/2) Ry(θ) Rz(π/2)
```
If you calculate the matrix multiplications (using the exponential forms of the rotation matrices and the properties of Pauli matrices), you will arrive at exactly the structure shown:

```
R(θ) =  [ cos(θ/2) -sin(θ/2) ]
        [ sin(θ/2)  cos(θ/2) ]
```

#### Spin Operator Along Rotated Axis (Sθ)
```
Sθ = R(θ) Sz R⁻¹(θ) 

Sθ =  (ħ/2) * [ cos(θ/2)  sin(θ/2) ]
              [ sin(θ/2) -cos(θ/2) ]
```
#### Eigenstates of Sθ
```
|↑(θ)⟩ = [ cos(θ/2) ]
         [ sin(θ/2) ]

|↓(θ)⟩ = [-sin(θ/2) ]
         [ cos(θ/2) ]  
```

### Probability of 'Up-Up' Result
```
P(↑₁↑₂) = |⟨↑₁(θ) ⊗ ↑₂ |Ψ⟩|² 
```
### Tensor product of individual states
Individual states of particles `1` and `2`:
```
|↑₁(θ)⟩ = cos(θ/2)|↑₁⟩ + sin(θ/2)|↓₁⟩

|↑₂⟩ = 1 |↑₂⟩ + 0|↓₂⟩
```

```
⟨↑₁(θ)| ⊗ ⟨↑₂|
```

### P(up-up)
```
I. P(up-up) = |(⟨↑₁(θ)| ⊗ ⟨↑₂|)|Ψ⟩|² 

II. ... TODO step by step calculations
```
Finally:
```

P(up-up) =  1/2 * sin²(θ)

```
### P(same spin)
```
I. P(same spin) = P(up-up) + P(down-down) = 2 * 1/2 * sin²(θ)

II. P(same spin) = sin²(θ)

```

## 4. Intepretation

Our physical world is at least four-dimensional (3D space + 1D time, + maybe more) Mandelbrot set like. It has a relatively simple definition that exhibits great complexity, especially as it is magnified. Due to the not locality of the reality coming from the quantum mechanics theory, the set seems to be calculated up front. Such interpretation allows the present to be determined not only by the past, but by the future as well. Time is not a special dimension. It seems special because of how a human brain works.

Such interpretation is close to the "pilot wave theory" (https://en.wikipedia.org/wiki/De_Broglie%E2%80%93Bohm_theory).

## 5. Bibliography

1. "CHSH (Clauser-Horne-Shimony-Holt) game", 1969, https://en.wikipedia.org/wiki/CHSH_inequality#CHSH_game

2. "Einstein–Podolsky–Rosen paradox", 1935, https://en.wikipedia.org/wiki/Einstein%E2%80%93Podolsky%E2%80%93Rosen_paradox

3. "Bell's theorem", John Stewart Bell, 1964,  https://en.wikipedia.org/wiki/Bell%27s_theorem

4. "Experimental Test of Local Hidden-Variable Theories", Stuart J. Freedman and John F. Clauser, https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.28.938

5. "Testing Superdeterministic Conspiracy", Sabine Hossenfelder, https://www.youtube.com/watch?v=cbSc-PLGU8o
