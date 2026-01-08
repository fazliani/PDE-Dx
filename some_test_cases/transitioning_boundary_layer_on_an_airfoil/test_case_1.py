test_case_1 = '''
1. Background & Problem Motivation  
Accurately predicting the location of boundary layer transition from laminar to turbulent flow is critical for aerodynamic design, impacting drag, heat transfer, and separation characteristics. Transition is not an instantaneous switch but a complex physical process initiated by the growth of small instabilities (Tollmien-Schlichting waves for low-turbulence environments). This process is inherently unsteady and highly sensitive to disturbances, pressure gradients, and surface properties.

2. Problem Specification  
Your task is to plan a numerical simulation strategy to study the natural transition on a symmetric airfoil.

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

is the vector of conservative variables (density, x/y-momentum, total energy), and \\( Re \\) is the Reynolds number based on chord length.

**Geometry**:  
A NACA 0012 airfoil at zero angle of attack. The chord length is \\( c = 1.0 \\) m.

**Flow Conditions**:
- Freestream Mach number: \\( M_\\infty = 0.2 \\) (low-speed, but compressible formulation is used).
- Reynolds number based on chord: \\( Re_c = 1 \\times 10^6 \\)
- Freestream turbulence intensity: Very low (<0.1%) to promote natural transition.
- The flow is isothermal (constant wall temperature).

**Primary Objective**:  
To capture the spatial evolution of instabilities and identify the location where the flow becomes fully turbulent. This is defined as the point where the skin friction coefficient (\\( C_f \\)) significantly deviates from the laminar theoretical solution and exhibits characteristics of a turbulent boundary layer.

3. Computational Domain & Boundary Conditions  
**Domain**:  
A C-grid topology extending 15 chord lengths upstream, 20 chord lengths downstream, and 15 chord lengths above/below the airfoil.

**Boundary Conditions**:
- **Far-field Inflow/Outflow**: Characteristic-based non-reflecting conditions using freestream values.
- **Airfoil Surface**: No-slip, adiabatic wall condition.
- **Wake Cut**: Periodic or symmetric condition.

4. Task Requirements & Deliverables  
Do not write the actual code. Your task is to produce a **Solver Strategy Document** that outlines the numerical approach to meet the objective.
'''
