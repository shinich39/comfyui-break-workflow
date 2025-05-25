"""
@author: shinich39
@title: comfyui-break-workflow
@nickname: comfyui-break-workflow
@version: 1.0.0
@description: Break the execution, save the incompleted image then continue later.
"""

from .nodes import *

NODE_CLASS_MAPPINGS = {
  "BreakWorkflow": BreakWorkflow,
}

NODE_DISPLAY_NAME_MAPPINGS = {
  "BreakWorkflow": "Break",
}

WEB_DIRECTORY = "./js"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]