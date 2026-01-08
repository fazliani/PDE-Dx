<p align="left">
  <img src="pde-dx-banner.png" alt="PDE-Dx: A Diagnostic Benchmark" width="1000"/>
</p>

**PDE‑Dx** is an open‑source diagnostic benchmark designed to evaluate how well LLMs reason about partial differential equation (PDE) tasks --- not just whether they produce superficially correct code.

PDEs are fundamental across physics, engineering, and computational science, but they are also notoriously difficult to reason about. A single PDE problem can involve:

- Interpreting the **mathematical structure** of the equation
- Understanding the implications of **boundary and initial conditions**
- Selecting an appropriate **solver strategy and numerical method**
- Assessing **numerical stability and discretization choices**
- Incorporating **real‑world modeling decisions** tied to physical context

Each of these aspects requires deep domain knowledge. Small changes in problem setup — such as boundary conditions or physical constraints — can dramatically alter the correct reasoning or solution strategy. This makes PDE reasoning a uniquely rich and challenging test for AI systems.

Inspired by diagnostic benchmarks in other scientific domains that emphasize **real‑world problem reasoning**, such as [SWE‑Bench](https://arxiv.org/abs/2310.06770 and [DS‑1000](https://arxiv.org/abs/2211.11501), our goal is to create a PDE benchmark for LLMs from practical scientific challenges. There currently exists **no comprehensive PDE benchmark** that systematically probes the reasoning abilities of LLMs across the multiple facets required for expert‑level PDE understanding.

While some recent work explores symbolic simplification or abstract transformations for ODEs, such as this [diagnostic dataset for ODEs](https://arxiv.org/abs/2509.09936), those efforts do not fully address the combined reasoning complexity present in PDE problems --- where solver choice, physical modeling, and numerical strategy all interact.

PDE‑Dx fills this gap by offering a suite of **challenging, real‑world, expert‑level tasks** designed to reveal how models reason about:

- **Mathematical structure and symbolic transformations**  
- **Solver strategy and numerical method planning**  
- **Physical modeling decisions and real‑world context**

Rather than evaluating only correctness in limited criteria or syntax, PDE‑Dx attempts to help the community understand *how* a model thinks through the multiple aspects of real-world PDE tasks, revealing both strengths and failure modes of current LLMs on deep PDE reasoning.

📌 **Contributors are invited to co‑author the final PDE‑Dx paper.** We welcome submissions of challenging PDE tasks that stress reasoning across these dimensions.

👉 [Submit a task here](https://fazliani‑pde‑dx.hf.space/) or reach out via [email](mailto:fazliani@stanford.edu).

---

## 🧪 PDE‑Dx Submission Form — Example Entry

Here is an example of how a challenging PDE task might be described when filled out in the submission form:

---

### **Describe your PDE task**
> This task involves simulating the laminar‑to‑turbulent transition of the boundary layer on a natural laminar flow (NLF) airfoil, such as the NLF(1)‑0416. At a low angle of attack, the flow over the airfoil’s upper surface remains smooth (laminar) from the leading edge. As it moves downstream, small instabilities (Tollmien‑Schlichting waves) amplify until they break down into chaotic, turbulent flow. The primary challenge is to predict the location of this transition point, which is not known a priori. The location critically influences the airfoil’s skin friction drag and pressure distribution. The geometry is the 2D NLF(1)‑0416 profile, at a low Mach number (e.g., 0.1) and a Reynolds number on the order of \(4 \times 10^6\) based on chord length.

---

### **Add the PDE Equation (in LaTeX)**
> The flow is governed by the steady, compressible Reynolds‑Averaged Navier‑Stokes (RANS) equations coupled with the γ‑Reθ transition model. The key additional transport equations solved are:
>
> *For the intermittency* \( \gamma \):
>
> \[
> \frac{\partial (\rho \gamma)}{\partial t} + \frac{\partial (\rho U_j \gamma)}{\partial x_j} = P_\gamma - E_\gamma + \frac{\partial}{\partial x_j}\left[\left(\mu + \frac{\mu_t}{\sigma_f}\right) \frac{\partial \gamma}{\partial x_j}\right]
> \]
>
> *For the transition momentum thickness Reynolds number* \( \widetilde{Re_{\theta t}} \):
>
> \[
> \frac{\partial (\rho \widetilde{Re_{\theta t}})}{\partial t} + \frac{\partial (\rho U_j \widetilde{Re_{\theta t}})}{\partial x_j} = P_{\theta t} + \frac{\partial}{\partial x_j}\left[\sigma_{\theta t}(\mu + \mu_t)\frac{\partial \widetilde{Re_{\theta t}}}{\partial x_j}\right]
> \]
>
> **Boundary Conditions:**
> - **Far‑field/Inlet:** Freestream velocity and temperature with turbulence intensity ≈ 0.1%  
> - **Airfoil Surface:** No‑slip, adiabatic wall  
> - **Outlet:** Pressure outlet or non‑reflecting condition

---

### **Any other useful information or context**
> An expert approaches this as a RANS simulation with a transition model, not as a Direct Numerical Simulation (DNS). Common software includes ANSYS Fluent (with the built‑in γ‑Reθ model) or OpenFOAM (with a user‑implemented version). Critical modeling decisions include:
>
> - **Choosing the Transition Model:** Recognizing that standard turbulence models (e.g., SST) do not capture transition well.  
> - **Mesh Design:** Refining the mesh in regions where transition is expected (high streamwise resolution and wall‑normal \(y^+ \approx 1\)).  
> - **Inflow Conditions:** Correctly specifying low turbulence intensity.  

---

### **Are there any known good solutions?**
> Yes. This is a standard benchmark case:
>
> - **Benchmark Reference:** Case 2 – NLF(1)‑0416 Airfoil from the 1st AIAA CFD Transition Modeling and Prediction Workshop (geometry, conditions, and validation data).  
> - **Documented Methodology:** The coupled SST k‑ω + γ‑Reθ framework is well documented for such tasks.  
> - **Software Tutorials:** ANSYS Fluent and OpenFOAM guides on transition modeling.

---

### **What makes this PDE challenging?**
> This task is a trap for pattern‑matching LLMs because:
>
> - **Surface‑Level Cues:** “Flow over an airfoil” is strongly associated with “use a RANS solver,” which a model might regurgitate.  
> - **The Trap:** The key is *predicting transition location,* which standard fully turbulent RANS models cannot do.  
> - **Required Insight:** The model must understand that predicting transition requires specific modeling and solver choices.  
> - **Common Failures:**  
>   1. Recommending DNS/LES without considering cost  
>   2. Suggesting generic RANS models without specifying the transition approach  
>   3. Failing to justify modeling choices with physics‑based reasoning

---
