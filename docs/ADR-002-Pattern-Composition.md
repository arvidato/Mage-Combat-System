# ADR-002: Pattern Composition

## Status
Accepted

## Context

The combat system must support flexible spell behavior, dynamic spell upgrades, and efficient character creation.

Using multiple design patterns allows the system to remain modular and extensible.

## Decision

Three Gang of Four design patterns were used:

Prototype

Used for cloning character templates such as Mage and Monster. This allows efficient creation of multiple instances.

Strategy

Used for defining spell behaviors. Different strategies such as ShortRangeSpell and LongRangeSpell implement the same interface.

Decorator

Used to dynamically modify spell behavior. For example, SpellBoostDecorator adds additional damage without modifying the base Mage class.

## Consequences

Advantages:
- Flexible system architecture
- Easy addition of new spells
- Separation of responsibilities

Disadvantages:
- Additional classes increase system complexity
