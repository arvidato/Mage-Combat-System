# Performance Report

## Hot Path

The hot path of the system is repeated spell execution through `Mage.cast_spell()`.

## Performance Budget

- Throughput target: at least **X** spell executions per second on the development machine.

## Benchmark Methodology

Main benchmark:

- Command: `python -m benchmarks.performance_benchmark`
- Workload: 100,000 spell executions
- Timer: `time.perf_counter()`
- Metric: throughput computed as `spell_count / duration`

## Benchmark Result

- Execution time: 0.3804 seconds
- Throughput: 262868.13 spells per second

## Budget Evaluation

- Result: Met

## Optimization Attempt

`BarrageSpell` was optimized by reusing a `CombatExecutor` instead of creating and shutting down a new one on every cast.

## Comparison

Before optimization:

- Execution time: 0.9573 seconds
- Throughput: 10445.79 barrage casts/sec

After optimization:

- Execution time: 0.3666 seconds
- Throughput: 27276.51 barrage casts/sec

## Lessons Learned

Reusing the executor reduced concurrency overhead and improved barrage performance significantly.
