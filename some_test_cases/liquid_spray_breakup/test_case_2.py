test_case_2 = '''
1. Background & Problem Motivation  
After primary atomization, droplets are subjected to the continuous aerodynamic force of the surrounding gas. If the relative velocity is high enough, these parent droplets can further deform and undergo secondary breakup, reducing the droplet size and increasing evaporation surface area. This process is governed by the competition between disruptive aerodynamic pressure and restorative surface tension and viscous forces. Simulating a single droplet breakup is a fundamental benchmark for validating multiphase codes and understanding the physical regimes (bag, multimode, shear, or catastrophic breakup).

2. Problem Specification  
Your task is to plan a Direct Numerical Simulation (DNS) to investigate the deformation and secondary breakup of a single liquid droplet suddenly exposed to a high-speed continuous gas flow.

**Governing Equations**:  
The governing equations are the incompressible (or low-Mach) multiphase Navier-Stokes equations with interface tracking, identical in form to those used for primary atomization. Due to the focus on a single droplet, a Level Set method or a high-order Volume-of-Fluid (VOF) method is often preferred for more accurate curvature calculation. The equations must resolve the boundary layer around the deforming droplet and the interface dynamics.

**Geometry**:  
A 3D domain containing a single spherical liquid droplet initially at rest, placed in a uniform gas flow. The domain size must be sufficiently large to avoid boundary influence on the droplet wake and deformation.

**Flow Conditions**:  
Conditions are predefined to target a specific breakup regime (e.g., bag breakup or shear breakup).

**Key Dimensionless Numbers**:
- Weber Number:
\\[
We = \\frac{\\rho_g U_{rel}^2 D_d}{\\sigma}
\\]
This is the primary controlling parameter (e.g., \\( We = 20 \\) for bag breakup, \\( We > 100 \\) for shear breakup).

- Reynolds Number:
\\[
Re_d = \\frac{\\rho_g U_{rel} D_d}{\\mu_g}
\\]

- Ohnesorge Number:
\\[
Oh_d = \\frac{\\mu_l}{\\sqrt{\\rho_l \\sigma D_d}}
\\]

- Density and Viscosity Ratios:
\\[
\\frac{\\rho_l}{\\rho_g}, \\quad \\frac{\\mu_l}{\\mu_g}
\\]
These ratios are critical and are set to match a real fluid pair (e.g., water/air).

**Primary Objective**:  
To capture the temporal evolution of droplet morphology and the onset of fragmentation. Key deliverables include:

- Quantification of droplet deformation (e.g., time history of aspect ratio)  
- Identification of the breakup regime and the breakup time  
- For bag breakup: analysis of bag growth, rim formation, and child droplet generation

3. Computational Domain & Boundary Conditions  

**Domain**:  
A 3D rectangular domain. Depending on symmetry assumptions, a quarter-domain with symmetry planes may be used to reduce computational cost, but full 3D simulations are required for asymmetric breakup regimes.

**Boundary Conditions**:
- **Inflow**: Uniform gas velocity  
- **Outflow**: Pressure outlet or convective boundary condition  
- **Other Boundaries**: Symmetry or far-field pressure conditions  
- **Initial Condition**: A spherical droplet with a smoothed interface function used to initialize the volume fraction or level set field

4. Task Requirements & Deliverables  
Do not write the actual code. Your task is to produce a **DNS Plan for Droplet Breakup**. This plan must address:

- **Numerical Method for Sharp Interface**: Justify the choice of interface method (e.g., Coupled Level Set–VOF). Emphasize the need for high-order spatial discretization to minimize parasitic currents and accurately resolve the thinning liquid membrane during bag formation.

- **Mesh Resolution Strategy**: Define the global and local (adaptive) mesh resolution. The mesh must resolve the droplet boundary layer (on both gas and liquid sides) and the thin bag film, which can be orders of magnitude smaller than the initial droplet diameter. Propose a total cell count estimate.

- **Temporal Resolution & Scaling**: Discuss the time-step constraints imposed by the acoustic CFL condition (due to high liquid density) and the capillary time scale. Explain the impact of these constraints on computational cost.

- **Analysis & Benchmarking**: Detail the post-processing steps, including how to track droplet centroid and interface evolution, compute volume and surface area, and identify child droplets. Specify that results must be validated against classic breakup regime maps and correlations (e.g., Pilch–Erdman breakup time) as well as qualitative experimental imagery.
'''
