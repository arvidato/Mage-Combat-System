# Performance Report

## Hot Path

The most frequently executed operation in the system is:

Mage.cast_spell()

This method calculates spell damage and applies it to a target.

## Benchmark Method

A benchmark was implemented that executes 100,000 spell casts using the combat system.

The benchmark measures total execution time and throughput.

## Results

Example output:

Total spells cast: 100000
Execution time: ~0.59 seconds
Throughput: ~168,000 spells per second

## Interpretation

The results demonstrate that the combat system performs efficiently even when executing a large number of spells. The use of lightweight objects and simple algorithms allows high throughput.
