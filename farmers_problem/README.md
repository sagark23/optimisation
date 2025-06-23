# Farmers Problem

This problem involves optimizing crop planting decisions to maximize profit while considering resource constraints using linear and mixed-integer linear programming (MILP).

## Problem Description

A farmer has limited resources (seeds, fertilizer, land, labor, equipment) and must decide how much of each crop to plant to maximize profit. The problem is modeled as a MILP with:
- Crop-specific profit margins, setup costs, and resource requirements
- Constraints on available fertilizer, labor, land, and equipment
- Binary variables to represent whether a crop is planted
- Optionally, soft constraints (e.g., labor penalties)

## Example: Simple Problem

A farmer has:
- 3 tons of potato seeds
- 4 tons of carrot seeds
- 5 tons of fertilizer

Fertilizer must be used in a 1:1 ratio with seeds (1 kg of seeds requires 1 kg of fertilizer).

Profit margins:
- Potato seeds: $1.2/kg
- Carrot seeds: $1.7/kg

### Objective
Maximize the total profit by determining the optimal amount of potato and carrot seeds to plant, while respecting the resource constraints.

### Mathematical Formulation

#### Decision Variables
- x₁: Amount of potato seeds to plant (in tons)
- x₂: Amount of carrot seeds to plant (in tons)

#### Objective Function
Maximize: 1200x₁ + 1700x₂

#### Constraints
1. Potato seeds available: x₁ ≤ 3
2. Carrot seeds available: x₂ ≤ 4
3. Fertilizer constraint: x₁ + x₂ ≤ 5
4. Non-negativity: x₁, x₂ ≥ 0

## How to Run

- **Simple LP version:**
  ```sh
  uv run optimise.py
  ```
  Solves the basic problem with two crops (potato and carrot) and simple resource constraints.

- **Extended MILP version:**
  ```sh
  uv run optimise_milp.py
  ```
  Solves the extended problem with multiple crops, setup costs, and additional constraints (fertilizer, labour, land, equipment, binary crop selection, and soft constraints).

## Example: Extended Problem (MILP)

- Multiple crops (potato, carrot, lettuce, tomato)
- Each crop has profit, setup cost, and resource requirements
- Constraints on fertilizer, labor, land, and equipment
- Binary variables for crop selection

## Files
- `optimise.py`: Simple LP model for two crops
- `optimise_milp.py`: Extended MILP model for multiple crops and constraints

## Solution

Implemented using [PuLP](https://coin-or.github.io/pulp/), a linear programming library for Python. The implementation includes:
- Model definition using dataclasses
- Constraint formulation (including hard and soft constraints)
- Solution using the CBC solver
- Output analysis and infeasibility detection

See `optimise_milp.py` for the extended MILP model.

