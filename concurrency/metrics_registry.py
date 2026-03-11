import threading


class MetricsRegistry:
    """
    Thread-safe registry that tracks combat metrics.
    """

    def __init__(self):
        self.total_spells_cast = 0
        self.total_damage = 0
        self._lock = threading.Lock()

    def record_spell(self, damage: int) -> None:
        """
        Safely update shared metrics.
        """

        with self._lock:
            self.total_spells_cast += 1
            self.total_damage += damage