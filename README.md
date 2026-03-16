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

## GoF Pattern Principles

This project uses three Gang of Four (GoF) design patterns to keep the combat system modular, flexible, and easier to extend.

### Prototype

Prototype is used when object creation should happen by cloning an existing template instead of rebuilding a new object from scratch each time.

In this project:

- `Mage` and `Monster` support `clone()`
- reusable templates can be defined once, then copied for new battles

Principle:

- create new objects by copying an existing instance

### Strategy

Strategy is used when one part of the system should support multiple interchangeable behaviors without changing the main class that uses them.

In this project:

- `Mage` delegates spell behavior to a `SpellStrategy`
- different strategies implement different spell behavior:
  - `ShortRangeSpell`
  - `LongRangeSpell`
  - `BarrageSpell`

Principle:

- define a family of algorithms or behaviors, place them behind a common interface, and make them interchangeable

### Decorator

Decorator is used when behavior should be added dynamically to an existing object without modifying the original class.

In this project:

- `SpellBoostDecorator` wraps a mage-like character
- it temporarily increases spell power only during the spell cast
- after the cast, the original state is restored

Principle:

- extend object behavior by wrapping the object instead of modifying or subclassing it directly

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

