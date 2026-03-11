# Design Patterns Combat System Prototype

## Overview

This project implements a small combat simulation system using three Gang of Four design patterns:

- Prototype
- Strategy
- Decorator

The system simulates a mage casting spells on monsters while supporting concurrency, performance measurement, and automated testing.

---

# Problem Statement

Many games require flexible combat systems that support multiple abilities, upgrades, and enemy spawning. This project demonstrates how design patterns can be used to build a modular and extensible combat system.

---

# Design Patterns Used

## Prototype Pattern
Used to clone character templates such as monsters or mages.

Example:

skeleton_template = Monster("Skeleton", 50, 5)

skeleton1 = skeleton_template.clone()

This allows efficient creation of many enemies.

---

## Strategy Pattern
Encapsulates different spell behaviors.

Example strategies:

- ShortRangeSpell
- LongRangeSpell

The Mage delegates spell damage calculation to the strategy object.

---

## Decorator Pattern
Allows dynamic modification of spell behavior.

Example decorator:

- SpellBoostDecorator

Decorators wrap characters to add spell modifiers without modifying the base Mage class.

---

# Concurrency Model

The system uses a bounded thread pool to execute spell attacks concurrently.

Key components:

- ThreadPoolExecutor
- CombatExecutor
- MetricsRegistry

Thread safety is ensured using locks to protect shared resources.

---

# Performance Measurement

The hot path of the system is:

Mage.cast_spell()

Benchmark:

100,000 spell executions

Example result:

Execution time: ~0.59 seconds  
Throughput: ~168,000 spells per second

---

# Running the Project

Activate the virtual environment:

source venv/bin/activate

Run tests:

pytest

Run performance benchmark:

python -m benchmarks.performance_benchmark

---

# Test Coverage

Coverage is measured using pytest-cov.

Run:

pytest --cov=core --cov=concurrency

Current coverage: ~86%

---

# Project Structure

core/
- character.py
- mage.py
- monster.py
- strategy.py
- decorator.py
- prototype.py

concurrency/
- combat_executor.py
- metrics_registry.py
- unsafe_metrics_registry.py

benchmarks/
- performance_benchmark.py

tests/
- unit tests
- integration tests

---

# Lessons Learned

This project demonstrates how combining Prototype, Strategy, and Decorator enables flexible system design. The architecture allows new spells, modifiers, and entities to be added without modifying existing core classes.