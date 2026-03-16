from concurrent.futures import ThreadPoolExecutor

from concurrency.metrics_registry import MetricsRegistry


def test_metrics_registry_thread_safe_updates():
    registry = MetricsRegistry()
    task_count = 1000

    def worker():
        registry.record_spell(1)

    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = [executor.submit(worker) for _ in range(task_count)]
        for future in futures:
            future.result()

    assert registry.total_spells_cast == task_count
    assert registry.total_damage == task_count
