from concurrency.metrics_registry import MetricsRegistry


def test_metrics_registry_records_spells():
    registry = MetricsRegistry()

    registry.record_spell(10)
    registry.record_spell(20)

    assert registry.total_spells_cast == 2
    assert registry.total_damage == 30