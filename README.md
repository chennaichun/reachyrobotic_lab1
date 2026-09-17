# Reachy Mini — HRI Lab 1

Course: INFO 5356-030 — Introduction to Human-Robot Interaction  
Semester: Fall 2026  
Author: Nai Chun Chen  
Submission type: Individual

## Overview

This private repository contains my work for Lab 1:
Introduction to Reachy Mini.

The lab covers setting up the Reachy Mini simulation environment,
observing a community application, developing a greeting application,
and investigating interaction failures through controlled tests.

## Development Status

The repository is being initialized. Environment setup, application
development, and simulation testing have not yet been documented.

Verified software versions, installation commands, run instructions,
and test results will be added as the work is completed.

## Planned Repository Structure

- `apps/team_greeting_app/`: Complete greeting application, including
  source code and `pyproject.toml`.
- `reports/`: Final lab report.
- `evidence/setup/`: Environment setup screenshots.
- `evidence/community_app/`: Community application observations and clips.
- `evidence/greeting_app/`: Greeting application logs and test evidence.
- `evidence/failure_tests/`: Controlled test results and supporting evidence.

Directories will be added when their contents are available.

## Environment Requirements

The lab specifies:

- macOS or Linux.
- Python 3.10–3.12, with Python 3.12 recommended.
- A virtual environment named `reachy_mini_env`.
- Reachy Mini SDK with MuJoCo simulation dependencies.

The operating system, processor architecture, and installed versions of
Python, Reachy Mini, MuJoCo, and Reachy Mini Control will be recorded
after setup.

## Greeting Application Requirements

The application will be named `team_greeting_app` and will:

- Extend `ReachyMiniApp` and implement `run(reachy_mini, stop_event)`.
- Coordinate at least two expressive channels.
- Perform three stages: orient toward an implied user, greet,
  and return to neutral.
- Check `stop_event` during loops and waits and stop gracefully.
- Print timestamped markers for each stage.
- Expose at least two named motion or timing parameters with units.
- Avoid camera, microphone, cloud AI, and personal data collection.

## Validation Plan

### Greeting Application

- Run at least three complete simulation cycles.
- Request a normal stop during each of the three stages.
- Verify clean termination and return to neutral.
- Vary at least two named parameters and record their effects.
- Explain the final parameter choices and anticipated physical-robot risks.

### Community Application

- Define one research question.
- Vary one independent variable across baseline, moderate-challenge,
  and boundary conditions.
- Record expected and observed behavior, measurable outcomes,
  pass/fail results, and timestamped evidence.
- Distinguish observations from interpretations.
- Propose one technical mitigation, one interaction-design mitigation,
  and one follow-up test.

## Repository Practices

- Keep this repository private.
- Do not commit credentials, tokens, SSH private keys, or `.env` files.
- Exclude local virtual environments and generated caches.
- Commit actual progress with descriptive messages.
- Include only relevant source files, documentation, and evidence.
- Verify installation and run instructions before final submission.
