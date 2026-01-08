test_case_2 = '''
1. Background & Problem Motivation  
At high hypersonic speeds with laminar inflow, shock-wave/boundary-layer interaction (SBLI) can lead to large, dynamically unsteady separation bubbles. The low-frequency "breathing" of these bubbles causes dramatic fluctuations in surface heating and skin friction, posing a severe design challenge. This unsteadiness is not driven by external turbulence but by a self-sustained mechanism intrinsic to the interaction dynamics. Simulating this phenomenon requires high-fidelity methods to capture the instability and coupling between the separation shock, the shear layer, and the reattachment region.

2. Problem Specification  
Your task is to plan a high-fidelity simulation to investigate the unsteady mechanics of a laminar separation bubble induced by a shock impinging on a flat plate boundary layer.

**Governing Equations**:  
The 3D, unsteady, compressible Navier-Stokes equations without turbulence modeling (Direct Numerical Simulation - DNS) or with a scale-resolving method (LES):

\\[
\\frac{\\partial Q}{\\partial t}
+ \\frac{\\partial F}{\\partial x}
+ \\frac{\\partial G}{\\partial y}
+ \\frac{\\partial H}{\\partial z}
= \\frac{1}{Re}
\\left(
\\frac{\\partial F_v}{\\partial x}
+ \\frac{\\partial G_v}{\\partial y}
+ \\frac{\\partial H_v}{\\partial z}
\\right)
\\]

where

\\[
Q = 
\\begin{bmatrix}
\\rho \\\\
\\rho u \\\\
\\rho v \\\\
\\rho w \\\\
E
\\end{bmatrix}
\\]

is the vector of conservative variables.

**Geometry**:  
A flat plate with an impinging oblique shock generated either by a shock generator placed above the plate or by simulating a compression corner. The spanwise width of the domain must be sufficient to allow three-dimensional structures to develop.

**Flow Conditions**:
- Freestream Mach number: \\( M_\\infty = 7.7 \\)  
- Reynolds number based on plate length or momentum thickness: Laminar regime  
- Incoming boundary layer state: Laminar (Blasius profile)  
- High wall-to-recovery temperature ratio, making wall cooling effects significant

**Primary Objective**:  
To capture the self-sustained unsteadiness of the separation bubble. Key deliverables include:

- Quantification of the low-frequency fluctuation in wall heat flux and skin friction at reattachment (reported to vary by over 20% and 26%, respectively)  
- Identification of the dominant temporal frequency and spanwise length scale of the unsteadiness  
- Analysis of the vortex dynamics (baroclinic generation, pairing of quasi-streamwise vortices) that drive the cyclic motion

3. Computational Domain & Boundary Conditions  

**Domain**:  
A high-resolution structured mesh. Extreme grid clustering is needed in the wall-normal direction to resolve the laminar sublayer and in the streamwise direction around the interaction zone. The spanwise direction requires enough points to resolve developing vortical structures.

**Boundary Conditions**:
- **Inflow**: Laminar Blasius boundary layer profile  
- **Plate Surface**: No-slip, isothermal (cold wall)  
- **Top Boundary**: Condition to enforce the impinging shock wave (e.g., a symmetry boundary with an inclined shock, or a specified inviscid shock profile)  
- **Spanwise Boundaries**: Periodic boundary conditions  
- **Outflow**: Supersonic outflow or characteristic-based non-reflecting conditions

4. Task Requirements & Deliverables  
Do not write the actual code. Your task is to produce a **High-Fidelity Simulation Plan**. This plan must address:

- **Fidelity & Method Selection**: Justify the choice of DNS over RANS/LES, or a specific LES approach, based on the need to resolve the intrinsic instability mechanisms. Discuss the profound computational cost implications.

- **Temporal & Spatial Resolution Requirements**: Define criteria for temporal resolution (time step based on acoustic CFL and instability frequencies) and spatial resolution (grid spacing in inner wall units and in the shear layer). Estimate the total grid point and core-hour requirements.

- **Algorithmic Choices for Unsteadiness**: Specify time-integration schemes suitable for long-duration simulations to capture low-frequency cycles (e.g., high-order implicit or hybrid schemes). Discuss the need for spectral analysis tools (FFT, DMD) within the post-processing plan.

- **Initialization & Data Collection Strategy**: Describe how to establish the initial flow field (e.g., from a steady RANS solution). Detail what flow data must be sampled (e.g., time histories of surface quantities, volumetric snapshots) and at what frequency to properly analyze the unsteadiness.
'''
