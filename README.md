# Reachy Mini — HRI Lab 1

**Course:** INFO 5356-030 — Introduction to Human-Robot Interaction  
**Semester:** Fall 2026  
**Author:** Nai Chun Chen  
**Submission Type:** Individual

## Overview

This private repository contains my work for Lab 1: Introduction to Reachy Mini.

The lab includes:

- Setting up Reachy Mini Control and the MuJoCo simulation environment.
- Running and observing a Reachy Mini community application.
- Teleoperating Reachy Mini in simulation.
- Developing and testing a custom `team_greeting_app`.
- Conducting controlled interaction tests using baseline, moderate-challenge, and boundary conditions.
- Documenting observations, limitations, failure analysis, and simulation evidence.

## Repository Structure

```text
reachyrobotic_lab1/
├── apps/
│   └── team_greeting_app/
│       ├── pyproject.toml
│       └── src/
├── evidence/
│   ├── images/
│   └── video/
├── README.md
└── .gitignore
- Do not commit credentials, tokens, SSH private keys, or `.env` files.
- Exclude local virtual environments and generated caches.
- Commit actual progress with descriptive messages.
- Include only relevant source files, documentation, and evidence.
- Verify installation and run instructions before final submission.
