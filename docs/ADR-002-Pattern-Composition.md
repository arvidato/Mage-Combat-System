# ADR-002: Pattern Composition

## Status

Accepted

## Context

The combat system must support reusable character templates, interchangeable spell behaviors, and runtime spell enhancement without tightly coupling these concerns into a single class hierarchy.

## Decision

The system uses exactly three GoF design patterns:

### Prototype

Used to clone reusable character templates such as `Mage` and `Monster`.

### Strategy

Used to define interchangeable spell behaviors such as `ShortRangeSpell`, `LongRangeSpell`, and `BarrageSpell`.

### Decorator

Used to dynamically modify spell behavior through `SpellBoostDecorator` without modifying the base `Mage` class.

These patterns are used together:

- Prototype creates reusable combat entities
- Strategy defines how spells behave at runtime
- Decorator enhances selected spell execution dynamically

## Consequences

### Advantages

- Clear separation of responsibilities
- Easy addition of new spell types
- Easy reuse of entity templates
- Runtime behavior can be extended without modifying core classes

### Disadvantages

- More classes and indirection
- Slightly higher conceptual complexity than a simpler inheritance-only design
