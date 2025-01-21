# Genesis Robot Training Environment

## Overview
This project implements training environments for two robots (KBot and ZBot) using the Genesis simulator. It was developed during the K-Scale Hackathon to create reinforcement learning environments for legged robot control.

## Key Components

### Robot Environments
- **KBot Environment**: A quadruped robot training environment
- **ZBot Environment**: A biped robot training environment

Both environments share similar core functionality:

1. **Observation Space**:
- Robot state information including:
  - Joint positions and velocities
  - Base linear and angular velocities
  - Gravity projection
  - Command signals

2. **Action Space**:
- Joint position control with PD controllers
- Action scaling and clipping for stability
- Simulated action latency (1-step delay)

3. **Reward Functions**:
- Velocity tracking (linear and angular)
- Base stability
- Energy efficiency
- Gait symmetry (for KBot)

### Key Features
- 50Hz control frequency (dt = 0.02s)
- Multiple parallel environments for faster training
- Configurable episode length and resampling times
- MPS/GPU acceleration support
- Integrated with Weights & Biases for experiment tracking

## Technical Details

### Environment Configuration
- Base pose initialization
- PD control parameters (kp, kd)
- Observation scaling factors
- Command ranges for velocity targets

### Dependencies
- Genesis World Simulator
- RSL-RL (Robotic Systems Lab RL framework)
- PyTorch
- TensorBoard for logging

## Usage

1. **Setup Environment**:
