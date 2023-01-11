.. right-quote ::
    Simple things should be simple, complex things should be possible
    Alan Key

Quantify is an open-source, Python-based, high-level data acquisition framework for quantum-computing
-----------------------------------------------------------------------------------------------------

At Orange Quantum Systems and Qblox, we are developing Quantify as an open-source framework, together with a growing international community of scientists and engineers. Quantify is built on top of QCoDeS and is the spiritual successor of the extensively used PycQED measurement environment. Quantify currently consists of Quantify-Core and Quantify-Scheduler.

:highlight-red:`Quantify-Core` enables users to quickly set up experiments while taking care of practical aspects such as data storage, live plotting of experiments, monitoring the state of instruments, and data analysis.

:highlight-blue:`Quantify-Scheduler` provides a unique hybrid gate–pulse control model with explicit timing control, allowing users to easily express complex quantum experiments.

.. right-quite ::
   All required tools for pulse-level quantum-computing & solid-state physics experiments

Maintained by Professionals
---------------------------
Many research organizations need similar infrastructure for controlling their experiments. Currently, most organizations develop and maintain their own in-house software frameworks, usually with huge maintenance backlogs. Quantify is a professionally maintained (CI/CD), open-source :highlight-red:`(BSD-4 license)` framework, thus relieving organizations from this need. With Quantify, researchers and developers can focus instead on running experiments and adding advanced functionality.

The API of Quantify is documented with user guides explaining the core concepts and tutorials demonstrating how the code can be used in practice. Tutorials include setting up basic and advanced measurement loops, scheduling of operations, and compilation onto different control hardware. Quantify is compatible with various quantum platforms such as transmon qubits, spin qubits or NV–centers, and can be used with any equipment that supports QCoDeS drivers.

Compatible & Device Agnostic
----------------------------
The API of Quantify is documented with user guides explaining the core concepts and tutorials demonstrating how the code can be used in practice. Tutorials include setting up basic and advanced measurement loops, scheduling of operations, and compilation onto different control hardware. Quantify is compatible with various quantum platforms such as transmon qubits, spin qubits or NV–centers, and can be used with any equipment that supports QCoDeS drivers.

.. right-quote ::
   All required tools for pulse-level quantum-computing & solid-state physics experiments

Join the community today
------------------------
We welcome organizations to add the functionality they need to Quantify, enabling the quantum community to build on each other's work. Let's go open-source and discover the benefits of an actively maintained framework for qubit characterization and advanced qubit measuring.

https://quantify./////// slack.com_test

.. carrousel ::

.. red-section ::
   Quantify-Core

An experiment typically consists of a data-acquisition loop that sets parameters, and then measures the resulting set of parameters.

Quantify-core offers:

- Instruments and Parameters, Settables and Gettables: Multi-dimensional software-controlled looping and sweeping of any QCoDeS instrument parameter;
- Parameter monitoring and live visualization of experiments
- Measurement Control: Adaptive measurements using adaptive sampling and classical minimization algorithms
- Data storage: Data saving, using xarray;
- Analysis: Data analysis and fitting.

https://quantify-quantify-core.readthedocs-hosted.com/e n/latest/api_reference.html

.. blue-section ::
   Quantify-Scheduler

Quantum computing experimentalists often need pulse-level control of their hardware when performing their experiments.

The quantify-scheduler package produces synchronized pulse schedules for qubit operations and readout.

Quantify-core offers:

- Quantum-circuit layer: Hybrid quantum circuit description (quantum-device agnostic) in the form of a schedule of gate instructions, arbitrary pulses, or a combination;
- Quantum-device layer: Instructions become device-aware, gate instructions are converted into pulses and timing information is added, corresponding to the quantum-device under test (transmon, dot, NV center, etc.);
- Control-hardware layer: Compile the schedule into a control-hardware specific executable program.

.. right-quote ::
   All required tools for pulse-level quantum-computing & solid-state physics experiments

Quantify is a collaboration between two of Europe’s leading quantum computing companies.
--------------------------------------------------------------------------------------------

Qblox fully-integrated control stacks combine scalable qubit control and readout equipment from ultrastable DC to 18.5 GHz. The state-of-the-art architecture speeds up calibration routines by orders of magnitude, saving research teams significant amounts of time and money. https://qblox.com


Orange Quantum Systems (OrangeQS) is a systems integrator that is tackling the characterization bottleneck of quantum processing units with products and services ranging from control software to full-stack characterization systems. As a spin-off of QuTech, OrangeQS is part of Quantum Delft’s world-leading ecosystem for innovation in quantum technologies. https://orangeqs.com