class UnsafeMetricsRegistry:
    """
    Version without locking to demonstrate race conditions.
    """

    def __init__(self):
        self.total_spells_cast = 0
        self.total_damage = 0

    def record_spell(self, damage: int) -> None:
        self.total_spells_cast += 1
        self.total_damage += damage