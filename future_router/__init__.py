"""future_router

This package may be used to handle a possibly future routers, this can be used to 'avoid'
problematic imports.

For Router class, you can use function 'notimplemented' as a decorator to un-use specific
methods."""

from .router import Router
from .resource_dummy import ResourceDummy
from .funcs import *

__version__ = '0.0.4'
