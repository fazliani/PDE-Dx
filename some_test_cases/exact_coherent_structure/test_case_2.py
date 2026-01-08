test_case_2 = '''
1. Background & Problem Motivation  
While equilibria represent steady states in an appropriate frame, turbulent dynamics also organize around repeating cycles known as periodic orbits. In pipe flow, a canonical example is a "relative periodic orbit" (RPO), where the flow repeats itself after a time period \\( T \\) but with a spatial shift along the pipe's axis. This RPO is an Exact Coherent Structure that captures the bursting and regeneration cycle of near-wall turbulent streaks and is believed to be a fundamental building block of turbulence. Computing such an orbit is a more advanced challenge than finding an equilibrium, as it requires solving for both a time-periodic field and an unknown spatial shift.

2. Problem Specification  
Your task is to formulate a numerical strategy to compute a known relative periodic orbit in a short, periodic pipe.

**Governing Equations**:  
The incompressible Navier-Stokes equations in cylindrical coordinates \\( (r, \\theta, z) \\), with constant mass flux enforced:

\\[
\\frac{\\partial \\mathbf{u}}{\\partial t} + (\\mathbf{u} \\cdot \\nabla)\\mathbf{u} = -\\nabla p + \\frac{1}{Re} \\nabla^2 \\mathbf{u}, \\quad \\nabla \\cdot \\mathbf{u} = 0
\\]

where \\( \\mathbf{u} = (u_r, u_\\theta, u_z) \\) is the velocity vector, and \\( p \\) is pressure.

**Geometry**:  
A straight, circular pipe with periodic boundary conditions in the axial direction.

- Pipe radius: \\( R = 1 \\)  
- Pipe length (axial period): \\( L_z = \\frac{2\\pi}{1.7} \\) (designed to fit one streak cycle)

The domain is periodic in the axial (\\( z \\)) and azimuthal (\\( \\theta \\)) directions.

**Flow Conditions**:
- Reynolds number: \\( Re_D = 2400 \\), based on pipe diameter \\( D = 2R \\) and bulk velocity \\( U \\)
- The base flow is the parabolic Hagen-Poiseuille profile:

\\[
u_z(r) = 1 - r^2, \\quad u_r = u_\\theta = 0
\\]

The solution is sought for the full flow field, not a perturbation.

**Primary Objective**:  
To converge upon a known RPO with period \\( T \\approx 80 \\) (in units of \\( R / U \\)). The deliverables are:

- The period \\( T \\) and the axial shift \\( \\Delta z \\) the flow undergoes over one period.  
- The time series of key integrated quantities over one period (e.g., energy dissipation rate, perturbation energy).  
- A phase-space visualization showing the closed loop of the orbit projected onto two meaningful state-space coordinates (e.g., energy vs. dissipation).

3. Computational Domain & Boundary Conditions  

**Domain**:  
The periodic pipe as defined above:

- \\( r \\in [0, 1] \\)  
- \\( \\theta \\in [0, 2\\pi] \\)  
- \\( z \\in [0, L_z] \\)

**Boundary Conditions**:
- **Pipe Wall (\\( r = 1 \\))**: No-slip, \\( \\mathbf{u} = 0 \\)  
- **Axial (\\( z \\)) and Azimuthal (\\( \\theta \\)) Directions**: Periodic boundary conditions for all variables

**Symmetry**:  
The target RPO is known to be invariant under a discrete rotation by \\( \\pi \\) around the pipe axis. This symmetry can be enforced to reduce computational cost by half.

4. Task Requirements & Deliverables  
Do not write the actual code. Your task is to produce a **Numerical Computation Plan** for finding this RPO. This should include:

- Spatial and temporal discretization strategies  
- Enforcing the relative periodicity condition with unknown time period \\( T \\) and spatial shift \\( \\Delta z \\)  
- Initial guess strategy (e.g., using time slices from DNS)  
- Numerical method for solving (e.g., Newton-Krylov shooting method)  
- Convergence criteria and validation
'''
