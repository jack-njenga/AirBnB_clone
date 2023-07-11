from .engine import FileStorage

__all__ = ["base_model"]

storage = FileStorage()

storage.reload()
