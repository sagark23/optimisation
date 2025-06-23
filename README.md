# Optimisation problem

This codebase demonstrates different optimisation techniques, including linear programming (LP), mixed-integer linear programming (MILP). It is used for educational purposes and accompanies a talk given at various conferences.

## One time setup 

```shell
brew install uv
```

## How to run

```shell
# Farmers Problem (LP and MILP)
uv run farmers_problem/optimise.py  # Simple LP version (potato & carrot)
uv run farmers_problem/optimise_milp.py  # Extended MILP version (multiple crops, more constraints)

```

## Problems Included

- **Problem 1:** Simple and extensible LP models for resource allocation
- **Farmers Problem:**
    - LP model for two crops (see `farmers_problem/optimise.py`)
    - MILP model for multiple crops and constraints (see `farmers_problem/optimise_milp.py`)

See individual problem folders for detailed descriptions and mathematical formulations.

