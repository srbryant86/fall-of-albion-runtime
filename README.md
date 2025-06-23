# Tactical Runtime Core

**ICS-Certified Tactical Runtime Environment for Simulation and Agent Execution**

This repository contains the core runtime system for ICS-certified tactical simulations and agent workflows. It is a modular, CLI-activated framework designed for real-time execution environments, GUI scaffolding, and solo developer workflows. This runtime is fully ICS-certified and vault-sealed under the CertNode protocol.

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


chore: trigger semantic-release