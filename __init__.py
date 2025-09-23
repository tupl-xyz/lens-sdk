"""
Lens Reasoning SDK

A Python SDK for the Lens Reasoning System that provides two focused SDKs:
- LensQueryProcessor: Query processing and reasoning
- LensSteeringManager: Steering directive management and guided reasoning
"""

from query_processor import LensQueryProcessor
from steering_manager import LensSteeringManager
from exceptions import LensError, ContractNotFoundError, ProcessingError, SteeringError

__version__ = "1.0.0"
__all__ = [
    "LensQueryProcessor",   # Focused SDK for query processing
    "LensSteeringManager",  # Focused SDK for steering directives
    "LensError",
    "ContractNotFoundError",
    "ProcessingError",
    "SteeringError"
]