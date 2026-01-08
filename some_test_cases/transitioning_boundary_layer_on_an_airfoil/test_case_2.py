test_case_2 = '''
1. Problem Statement: The "Natural Laminar Flow" Airfoil  
You are tasked with planning a simulation to predict the aerodynamic performance of a Natural Laminar Flow airfoil, NLF(1)-0416. The key requirement is to accurately predict the location where the boundary layer transitions from laminar to turbulent on the upper surface. This location is not known beforehand and is highly sensitive to the flow environment and numerical method.

**Objective**:  
Determine the transition location and compute the lift and drag coefficients.

2. Problem Specification  

**Geometry**:  
NLF(1)-0416 airfoil.

**Flow Conditions**:
- Freestream Mach number: \\( M_\\infty = 0.1 \\) (low-speed).
- Reynolds number based on chord: \\( Re_c = 4 \\times 10^6 \\)
- Freestream turbulence intensity: Very low (~0.1%) to promote natural transition.
- The flow is considered isothermal.

**Governing Equations**:  
The flow is governed by the 2D, unsteady, compressible Navier-Stokes equations:

\\[
\\frac{\\partial Q}{\\partial t} + \\frac{\\partial F}{\\partial x} + \\frac{\\partial G}{\\partial y} = \\frac{1}{Re} \\left( \\frac{\\partial F_v}{\\partial x} + \\frac{\\partial G_v}{\\partial y} \\right)
\\]

where

\\[
Q = 
\\begin{bmatrix}
\\rho \\\\
\\rho u \\\\
\\rho v \\\\
E
\\end{bmatrix}
\\]

is the vector of conservative variables representing density, momentum components, and total energy.

3. Computational Domain & Boundary Conditions  

**Domain**:  
A C-grid or O-grid topology extending sufficiently far from the airfoil to ensure accurate capture of boundary layer development and far-field behavior. Suggested: 10 chord lengths upstream, downstream, and normal to the airfoil surface.

**Boundary Conditions**:
- **Far-field Inflow/Outflow**: Characteristic-based non-reflecting conditions using freestream values.
- **Airfoil Surface**: No-slip, adiabatic wall condition.
- **Wake Cut (if applicable)**: Symmetry or periodic condition.

4. Primary Objective & Evaluation Criteria  

- **Transition Location**:  
  Accurately identify the transition point on the upper surface of the airfoil. This can be inferred from a sudden rise in skin friction coefficient \\( C_f \\) or breakdown of laminar boundary layer profiles.

- **Lift and Drag Coefficients**:  
  Compute the time-averaged lift (\\( C_L \\)) and drag (\\( C_D \\)) coefficients over the airfoil surface.

5. Task Requirements & Deliverables  
Do not write the actual code. Your task is to produce a **Solver Strategy Document** that outlines the numerical approach to achieve the simulation objectives. This should include:

- Discretization method for the Navier-Stokes equations.
- Grid resolution and clustering strategy near the wall.
- Transition modeling approach (if any).
- Temporal integration strategy.
- Post-processing methodology for identifying transition and computing \\( C_L \\), \\( C_D \\), and \\( C_f \\).
'''
