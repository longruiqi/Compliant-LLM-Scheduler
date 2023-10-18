import os
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

@dataclass(frozen=True)
class Config:
    hostname: Optional[str] = None
    
