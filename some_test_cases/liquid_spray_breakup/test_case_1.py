test_case_1 = '''
1. Background & Problem Motivation  
Primary atomization is the process where a coherent liquid stream (a jet or sheet) first destabilizes and fragments into ligaments and droplets. This initial breakup sets the characteristic droplet size distribution for the entire spray, which is critical for applications like fuel injection, coating, and combustion efficiency. The process involves complex interactions between liquid turbulence, aerodynamic forces, and surface tension, creating a multiscale problem with a rapidly deforming liquid-gas interface. Accurately simulating this is a major challenge for multiphase CFD.

2. Problem Specification  
Your task is to plan a high-fidelity numerical simulation to study the primary atomization of a turbulent liquid jet injected into a quiescent gas or a coaxial gas flow.

**Governing Equations**:  
The flow is governed by the incompressible (or low-Mach) Navier-Stokes equations for two immiscible fluids, coupled with an interface tracking/capturing method and surface tension. Using the Volume-of-Fluid (VOF) method with a Continuum Surface Force (CSF) model, the equations are:

\\[
\\nabla \\cdot \\mathbf{u} = 0
\\]

\\[
\\frac{\\partial (\\rho \\mathbf{u})}{\\partial t} + \\nabla \\cdot (\\rho \\mathbf{u} \\mathbf{u}) = 
-\\nabla p + \\nabla \\cdot \\left( \\mu (\\nabla \\mathbf{u} + \\nabla \\mathbf{u}^T) \\right) + \\rho \\mathbf{g} + \\mathbf{F}_{st}
\\]

An additional advection equation is solved for the volume fraction \\( \\alpha \\), where \\( \\alpha = 1 \\) in the liquid and \\( \\alpha = 0 \\) in the gas:

\\[
\\frac{\\partial \\alpha}{\\partial t} + \\nabla \\cdot (\\alpha \\mathbf{u}) = 0
\\]

The surface tension force is modeled as:

\\[
\\mathbf{F}_{st} = \\sigma \\kappa \\delta_s \\mathbf{n}
\\]

where \\( \\sigma \\) is the surface tension coefficient, \\( \\kappa \\) is the interface curvature, \\( \\delta_s \\) is a surface delta function, and \\( \\mathbf{n} \\) is the interface normal.

**Geometry**:  
A cylindrical liquid jet issuing from a circular nozzle into a cylindrical or rectangular computational domain filled with gas. The domain must be large enough to capture the fully developed spray without boundary interference.

**Flow Conditions**:

- **Liquid**: e.g., water or diesel fuel  
- **Gas**: e.g., air under standard conditions

**Key Dimensionless Numbers**:
- Reynolds Number: \\( Re_j = \\frac{\\rho_l U_j D}{\\mu_l} \\sim \\mathcal{O}(10^4) \\) (turbulent jet)  
- Weber Number: \\( We_g = \\frac{\\rho_g U_j^2 D}{\\sigma} \\sim \\mathcal{O}(10^2) \\) (aerodynamic forces dominate surface tension)  
- Ohnesorge Number: \\( Oh = \\frac{\\mu_l}{\\sqrt{\\rho_l \\sigma D}} \\) (relates viscous to surface tension forces)

**Inflow Condition**:  
A turbulent velocity profile with specified turbulence intensity must be prescribed at the liquid inlet.

**Primary Objective**:  
To predict the spray breakup morphology and initial droplet statistics. Key deliverables include:

- The breakup length (distance from nozzle to visible disintegration)  
- The Sauter Mean Diameter (SMD) of droplets in the near-field region  
- Visualization of the interface, showing the formation of waves, ligaments, and droplet pinch-off

3. Computational Domain & Boundary Conditions  

**Domain**:  
A 3D domain, typically a cylinder or rectangle. The mesh must be adaptively refined to sub-cell resolution around the liquid-gas interface to accurately capture curvature and pinch-off.

**Boundary Conditions**:
- **Liquid Inlet (Nozzle)**: Velocity inlet with turbulent fluctuations (synthetic turbulence)  
- **Gas Inlet / Ambient**: Pressure inlet or freestream condition  
- **Walls**: No-slip for nozzle walls  
- **Outflow**: Pressure outlet  
- **Other Boundaries**: Symmetry or periodic (if simulating a sector)

4. Task Requirements & Deliverables  
Do not write the actual code. Your task is to produce a **Multiphase CFD Strategy Document**. This document must address:

- **Interface Resolution Method**: Justify the choice of interface treatment (VOF, Level Set, or a hybrid). Discuss the critical need for interface sharpening and the challenges of maintaining mass conservation.

- **Turbulence Treatment**: Decide between Implicit LES (relying on numerical dissipation) and Explicit LES with a subgrid-scale model for the gas and liquid phases. Justify the choice.

- **Mesh Strategy & Adaptive Refinement**: Detail the adaptive mesh refinement (AMR) criteria (e.g., based on volume fraction gradient). Estimate the required minimum cell size at the interface (often a fraction of the target droplet size).

- **Surface Tension & Discretization**: Discuss the handling of the surface tension term to avoid parasitic currents. Specify the method for calculating interface curvature (e.g., height functions).

- **Validation Metrics**: Define how you would validate the simulation against experimental data (e.g., high-speed shadowgraphy for breakup length, Phase Doppler Interferometry for droplet sizes).
'''
