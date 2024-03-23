

## Problem description

The probability of finding both particles from a single with the same spin depends on the angle between measurement settings.

Why this dependency is described by the following equation?

`P(same spin) = sin²(θ/2)`

### 1. Entangled Singlet State
```
|Ψ⟩ = (1/√2) ( |↑⟩₁|↓⟩₂ -  |↓⟩₁|↑⟩₂)
```
### 2. Rotated Spin Measurement

#### a) Spin Operators:
```
Sz = (ħ/2) * ( [1  0]
               [0 -1] )

Sₓ = (ħ/2) * ( [0  1]
               [1  0] )
```

#### b) Rotation Operator:
```
R(θ) =  [ cos(θ/2) -sin(θ/2) ]
        [ sin(θ/2)  cos(θ/2) ]
```

#### c) Spin Operator Along Rotated Axis (Sθ)
```
Sθ = R(θ) Sẑ R⁻¹(θ) 

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
```
|↑(θ)⟩₁ = cos(θ/2)|↑⟩₁ + sin(θ/2)|↓⟩₁

|↑⟩₂ = 1 |↑⟩₂ + 0|↓⟩₂ (it's already an eigenstate of Sz)

I. ⟨↑(θ)₁ ⊗ ↑₂ = ⟨(cos(θ/2)|↑⟩₁ + sin(θ/2)|↓⟩₁) ⊗ (1 |↑⟩₂ + 0|↓⟩₂)

II. ⟨↑(θ)₁ ⊗ ↑₂ = cos(θ/2) ⟨↑₁ ⊗ |↑⟩₂  + sin(θ/2) ⟨↓₁ ⊗ |↑⟩₂

III. ⟨↑(θ)₁ ⊗ ↑₂ = cos(θ/2) |↑⟩₁|↑⟩₂ + sin(θ/2) |↓⟩₁|↑⟩₂

IV. ⟨↑(θ)₁ ⊗ ↑₂ = 1/√2 (cos(θ/2)₁ sin(θ/2)₂)

TODO how do we get from III to IV?
```
### 5. P(up-up) continue (3 + 4)
```
I. P(up-up) = | 1/√2 (cos(θ/2)₁ sin(θ/2)₂)( |↑⟩₁|↓⟩₂ -  |↓⟩₁|↑⟩₂ )|²

II. P(up-up) = |1/√2 (cos(θ/2)sin(θ/2)⟨↑₁|↑⟩₁⟨↓₂|↓⟩₂ - cos(θ/2)sin(θ/2)⟨↑₁|↓⟩₁⟨↓₂|↑⟩₂) |²

III. P(up-up) =  1/2 * cos²(θ/2)sin²(θ/2)

```
### 6. P(same spin)
```
sin(2x) = 2sin(x)cos(x)

I. P(same spin) = P(up-up) + P(down-down) = 2 * 1/2 * cos²(θ/2)sin²(θ/2)

II. P(same spin) = (1/2) * sin²(θ)

TODO why we end up with max(P(same spin)) == 1/2 ? It should be equal to 1 for 180 degrees.
```