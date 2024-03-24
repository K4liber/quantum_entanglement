

## Problem description

`Spin`: Electrons (and many other fundamental particles) possess an intrinsic angular momentum called spin. Spin is a quantum mechanical property, and for electrons, it can have two possible values: spin-up (|↑⟩) or spin-down (|↓⟩).

`Superposition`: A fundamental principle in quantum mechanics is superposition. A particle can exist in multiple states simultaneously.

`Entanglement`: Two or more particles can become interconnected in a way that their states are no longer independent. They are said to be entangled.

`Tensor Product (⊗)`: The tensor product is used to describe combined quantum systems. For example, |↑⟩₁|↓⟩₂ represents a two-electron system where electron 1 is spin-up and electron 2 is spin-down.

`Two-electron system`: Consider a system of two electrons. Each electron can be in either the spin-up or spin-down state, resulting in four possible combinations for the system.

`Entangled Singlet State`: The entangled state of the two electrons is represented by the singlet state. This state has an interesting property: if you measure the spin of one electron, you instantly know the spin of the other (with opposite direction).

We consider a maximally entangled pair of electrons. The probability of finding both particles from a singlet with the same spin depends on the angle between measurement settings.

Why this dependency is described by the following equation?

`P(same spin) = sin²(θ/2)`

![alt text](./img/probability.png)

### 1. Entangled Singlet State
Singlet state is anti-symmetric and in Dirac notation  it has the following representation:
```
|Ψ⟩ = (1/√2) ( |↑⟩₁|↓⟩₂ -  |↓⟩₁|↑⟩₂)
```
### 2. Rotated Spin Measurement

`Spin Angular Momentum (S)`: An intrinsic property of particles, independent of their spatial motion. It's like a particle spinning around its own axis. 

`Spin operator`: describes the spin angular momentum of a particle. Such an operator is applied to a mathematical representation of the physical state of a system and yields an angular momentum value if the state has a definite value for it.

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
`Spin Rotation operator R(θ)`: It represents a rotation of the spin state of the particle by an angle θ about an axis in the x-y plane. This rotation doesn't change the overall magnitude of the spin, but it changes its orientation in space. The specific form of R(θ) follows from the general principles of how rotations are represented in quantum mechanics. For spin-1/2 systems, 2x2 matrices act on the two-dimensional state vector.

`Unitary Operation`: The rotation operator is a unitary operator. This means that it preserves the normalization of the quantum state (i.e., the probability of finding the particle in a particular state remains 1).

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

#### c) Spin Operator Along Rotated Axis (Sθ)
```
Sθ = R(θ) Sz R⁻¹(θ) 

Sθ =  (ħ/2) * [ cos(θ)  sin(θ) ]
              [ sin(θ) -cos(θ) ]
```
#### d) Eigenstates of Sθ
```
|↑(θ)⟩ = [ cos(θ/2) ]
         [ sin(θ/2) ]

|↓(θ)⟩ = [-sin(θ/2) ]
         [ cos(θ/2) ]  
```

### 3. Probability of 'Up-Up' Result
```
P(up-up) = |⟨↑(θ)₁ ⊗ ↑₂ |Ψ⟩|² 
```
### 4. Tensor product of individual states
Individual states of particles `1` and `2`:
```
|↑(θ)⟩₁ = cos(θ/2)|↑⟩₁ + sin(θ/2)|↓⟩₁

|↑⟩₂ = 1 |↑⟩₂ + 0|↓⟩₂ (it's already an eigenstate of Sz)
```
```
I. ⟨↑(θ)₁ ⊗ ↑₂ = ⟨(cos(θ/2)|↑⟩₁ + sin(θ/2)|↓⟩₁) ⊗ (1 |↑⟩₂ + 0|↓⟩₂)

II. ⟨↑(θ)₁ ⊗ ↑₂ = cos(θ/2) ⟨↑₁ ⊗ |↑⟩₂  + sin(θ/2) ⟨↓₁ ⊗ |↑⟩₂

III. ⟨↑(θ)₁ ⊗ ↑₂ = cos(θ/2) |↑⟩₁|↑⟩₂ + sin(θ/2) |↓⟩₁|↑⟩₂

IV. ⟨↑(θ)₁ ⊗ ↑₂ = 1/√2 (cos(θ/2)₁ sin(θ/2)₂)

TODO how do we get from III to IV?
```
### 5. P(up-up) continue (3 + 4)
Useful trigonometric identity:
```
sin(2x) = 2sin(x)cos(x)
```

```
I. P(up-up) = | 1/√2 (cos(θ/2)₁ sin(θ/2)₂)( |↑⟩₁|↓⟩₂ -  |↓⟩₁|↑⟩₂ )|²

II. P(up-up) = |1/√2 (cos(θ/2)sin(θ/2)⟨↑₁|↑⟩₁⟨↓₂|↓⟩₂ - cos(θ/2)sin(θ/2)⟨↑₁|↓⟩₁⟨↓₂|↑⟩₂) |²

III. P(up-up) =  1/2 * cos²(θ/2)sin²(θ/2)

IV. P(up-up) =  1/2 * 1/4 * (2cos(θ/2)sin(θ/2))²

V. P(up-up) =  1/8 * sin²(θ)

```
### 6. P(same spin)
```
I. P(same spin) = P(up-up) + P(down-down) = 2 * 1/8 * sin²(θ)

II. P(same spin) = 1/4 * sin²(θ)

TODO why we end up with max(P(same spin)) == 1/4 ? It should be equal to 1 for 180 degrees.
```