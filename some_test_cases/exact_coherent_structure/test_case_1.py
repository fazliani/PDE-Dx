test_case_1 = '''
1. Background & Problem Motivation  
In the study of turbulent shear flows, turbulence is not a featureless, random state but is organized around a dynamical "skeleton" of unstable, non-chaotic solutions to the Navier-Stokes equations, known as Exact Coherent Structures (ECS). One of the simplest is an unstable equilibrium (or fixed point) found in plane Couette flow. This solution represents a precise, steady pattern of streamwise vortices and streaks that is embedded within the chaotic dynamics. It is not observable through direct numerical simulation (DNS) because any infinitesimal perturbation will cause the flow to decay to the laminar state or explode into full turbulence. Computing this ECS is fundamental to understanding the phase-space geometry of shear flows and the onset of turbulence.

2. Problem Specification  
Your task is to formulate a numerical strategy to compute this unstable equilibrium solution.

**Governing Equations**:  
The flow is governed by the incompressible Navier-Stokes and continuity equations:

\\[
\\frac{\\partial \\mathbf{u}}{\\partial t} + (\\mathbf{u} \\cdot \\nabla)\\mathbf{u} = -\\nabla p + \\frac{1}{Re}\\nabla^2 \\mathbf{u}, \\quad \\nabla \\cdot \\mathbf{u} = 0
\\]

where \\( \\mathbf{u} = (u, v, w) \\) is the velocity vector, \\( p \\) is the pressure, and \\( Re \\) is the Reynolds number.

**Geometry**:  
A minimal periodic domain in plane Couette flow. The physical domain is defined by two infinite parallel plates.

- Streamwise (\\( x \\)) length: \\( L_x = 2\\pi \\)  
- Wall-normal (\\( y \\)) height: \\( L_y = 2 \\) (from \\( y = -1 \\) to \\( y = +1 \\))  
- Spanwise (\\( z \\)) length: \\( L_z = \\pi \\)

**Flow Conditions**:

- Reynolds number: \\( Re = 400 \\), based on half the channel height (\\( h = 1 \\)) and half the wall velocity difference.  
- The base flow is linear shear: \\( \\mathbf{u}_B = (y, 0, 0) \\)  
- The solution is sought for the perturbation from this base flow: \\( \\mathbf{u}' = \\mathbf{u} - \\mathbf{u}_B \\)

**Primary Objective**:  
To converge upon and report the key properties of the unstable "lower-branch" equilibrium solution. This includes:

- The converged three-dimensional velocity and vorticity fields.
- The perturbation energy:

\\[
E = \\frac{1}{2V} \\int_V |\\mathbf{u}'|^2 \\, dV
\\]

- The visualization of the characteristic streamwise-invariant vortex roll and the sinuous, streamwise-varying low- and high-speed streaks it induces.

3. Computational Domain & Boundary Conditions  

**Domain**:  
The computational box uses the periodic lengths defined above (\\( L_x, L_y, L_z \\)).

**Boundary Conditions**:

- **Walls** (\\( y = \\pm 1 \\)): No-slip, \\( \\mathbf{u} = (\\pm 1, 0, 0) \\)  
- **Streamwise (x) and Spanwise (z) Directions**: Periodic boundary conditions for all flow variables.

**Symmetry Constraint**:  
The target equilibrium is known to belong to the subspace invariant under the shift-reflect symmetry:

\\[
S: [u, v, w](x, y, z) \\rightarrow [-u, -v, w](x + L_x/2, -y, z + L_z/2)
\\]

This symmetry must be enforced in the discretized equations to simplify the search.

4. Task Requirements & Deliverables  
Do not write the actual code. Your task is to produce a **Numerical Computation Plan** that details the strategy to find this unstable fixed point. This should include:

- Discretization approach and spatial resolution.
- Method for applying the symmetry constraint.
- Initial guess and continuation methods.
- Solver strategy (e.g., Newton-Krylov methods).
- Convergence criteria and validation checks.
'''

