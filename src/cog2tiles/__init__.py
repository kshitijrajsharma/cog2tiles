"""
cog2tiles - High-Performance COG to Web Map Tiles Converter

Author: Kshitij Raj Sharma
Copyright: 2025
License: MIT
"""

__version__ = "1.0.0"
__author__ = "Kshitij Raj Sharma"
__email__ = "your.email@example.com"

from .tiler import COGTiler
from .utils import normalize_array, process_bands

__all__ = ["COGTiler", "normalize_array", "process_bands"]
