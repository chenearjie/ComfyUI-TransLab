"""Top-level package for ComfyUI_TransLab."""

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
    "WEB_DIRECTORY",
]

__author__ = """chenear"""
__email__ = "chen3059445287@qq.com"
__version__ = "0.0.1"

from .src.ComfyUI_TransLab.nodes import NODE_CLASS_MAPPINGS
from .src.ComfyUI_TransLab.nodes import NODE_DISPLAY_NAME_MAPPINGS

WEB_DIRECTORY = "./web"
