# Design Patterns Combat System Prototype

## Problem Statement

Many games require flexible combat systems that support different abilities, temporary upgrades, reusable enemy templates, and scalable execution. This project demonstrates how design patterns can be used to build a modular and extensible combat system.

## Scope

Included:

- Text-based combat demo
- Mage and monster combat entities
- Runtime-selectable spell behaviors
- Temporary spell enhancement using a decorator
- Character cloning through templates
- Bounded concurrency for spell execution
- Unit and integration tests
- Performance benchmarking

Not included:

- GUI
- Networking
- Database/storage
- Full game engine features

## Constraints

- Exactly three GoF patterns are used
- Python implementation
- Bounded concurrency using a fixed-size thread pool
- Shared state must be protected where needed
- In-memory execution only

## Quickstart

Build / setup:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

Test:

```bash
pytest
```

Coverage:

```bash
pytest --cov=core --cov=concurrency
```

Benchmark:

```bash
python -m benchmarks.performance_benchmark
```

## Pattern Map

- Prototype → `core/prototype.py`, `Mage.clone()`, `Monster.clone()`
- Strategy → `core/strategy.py`, spell selection in `Mage`
- Decorator → `core/decorator.py`, `SpellBoostDecorator`

## Interaction Diagram

```text
User -> main.py -> Mage
              -> choose monster template -> clone monster
              -> choose spell strategy
Mage -> Strategy.cast(target)
BarrageSpell -> CombatExecutor -> target.take_damage()
SpellBoostDecorator -> wraps Mage.cast_spell()
MetricsRegistry -> records shared combat metrics
```

