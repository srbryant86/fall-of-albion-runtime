# Fall of Albion Runtime

**ICS-Certified Tactical Runtime Environment for Simulation and Agent Execution**

This repository contains the full runtime system for the *Fall of Albion* project, a modular, CLI-activated game framework designed for real-time tactical simulations, GUI bridging, and solo developer execution workflows. This runtime is fully ICS-certified and vault-sealed.

---

## 📦 Core Components

### `runtime_bridge.py`
Manages CLI-triggered agent execution via a JSON command map. Acts as the central control bridge between manual calls and automated logic sequences.

### `solodev_portable_launcher.sh`
A portable, shell-based launcher for initializing the runtime system in environments without full IDE overhead. Designed for Unix-based execution.

### `gui_stub.py`
A minimal Tkinter-based graphical interface used to prototype frontend behavior, user input hooks, and visual scenario control.

### `agent_trigger_map.json`
Defines mappings between agent names and their respective system commands, supporting modular invocation of behaviors and subsystems.

### `vault/`
Contains the ICS metadata, convergence seals, and certification tag for this release. This is used to validate payload fidelity and runtime integrity across deployments.

---

## 🚀 Quick Start

```bash
# Launch the system (Unix/macOS):
sh solodev_portable_launcher.sh

# Or trigger an agent manually:
python3 runtime_bridge.py <agent_name>
```

---

## 🔐 ICS Certification

This runtime is certified under the **CertNode ICS Seal** system, version `v1.0.0`.  
Included vault metadata confirms structural convergence, logic slope resolution, and execution integrity.

---

## 🌐 Repository Status

- Version: `v1.0.0`
- Status: Stable
- Runtime Integrity: Verified
- GUI Status: Stub/Prototype
- ICS: ✅ Locked and Sealed

---

## 📄 License

© 2025 SRB Creative Holdings LLC. All rights reserved. Runtime distribution permitted under licensed deployments or internal use.

---