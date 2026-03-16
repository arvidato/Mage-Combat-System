from concurrent.futures import ThreadPoolExecutor

from concurrency.unsafe_metrics_registry import UnsafeMetricsRegistry


def test_unsafe_metrics_registry_stress_demo():
    registry = UnsafeMetricsRegistry()
    task_count = 20000

    def worker():
        registry.record_spell(1)

    with ThreadPoolExecutor(max_workers=32) as executor:
        futures = [executor.submit(worker) for _ in range(task_count)]
        for future in futures:
            future.result()

    assert registry.total_spells_cast <= task_count
    assert registry.total_damage <= task_count

