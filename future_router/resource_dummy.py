"""Resource Dummy"""
from typing import Protocol
from .funcs import notimplemented


class ResourceDummy(Protocol):
    """Resource Dummy"""

    @notimplemented
    @staticmethod
    def index():
        """Index all the resource available."""

    @notimplemented
    @staticmethod
    def create():
        """Show the user/form response"""

    @notimplemented
    @staticmethod
    def store():
        """Store user request"""

    @notimplemented
    @staticmethod
    def edit(id):
        """Show user edit form response."""

    @notimplemented
    @staticmethod
    def update(id):
        """Update user request"""

    @notimplemented
    @staticmethod
    def destroy(id):
        """Delete user request"""

    @notimplemented
    @staticmethod
    def show(id):
        """Return"""
