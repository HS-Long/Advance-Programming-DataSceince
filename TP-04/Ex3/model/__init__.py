import torch.nn as nn
import sys
from pathlib import Path

# Import Net from the model.py file at root level
root_path = Path(__file__).parent.parent
sys.path.insert(0, str(root_path))

# This will import from model.py in the root directory
import importlib.util
spec = importlib.util.spec_from_file_location("model_file", root_path / "model.py")
model_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(model_module)

Net = model_module.Net

__all__ = ['Net']