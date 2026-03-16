from concurrent.futures import ThreadPoolExecutor


class CombatExecutor:
    """Executes combat actions using a bounded thread pool."""

    def __init__(self, max_workers: int = 4):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)

    def submit_spell(self, caster, target):
        return self.executor.submit(caster.cast_spell, target)

    def submit_callable(self, func, *args, **kwargs):
        return self.executor.submit(func, *args, **kwargs)

    def shutdown(self):
        self.executor.shutdown(wait=True)

