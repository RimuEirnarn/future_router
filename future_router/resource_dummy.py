"""Resource Dummy"""
from typing import Protocol


class ResourceDummy(Protocol):
    """Resource Dummy"""

    @staticmethod
    def index():
        """Index all the resource available."""

    @staticmethod
    def create():
        """Show the user/form response"""

    @staticmethod
    def store():
        """Store user request"""

    @staticmethod
    def edit(id):
        """Show user edit form response."""

    @staticmethod
    def update(id):
        """Update user request"""

    @staticmethod
    def destroy(id):
        """Delete user request"""

    @staticmethod
    def show(id):
        """Return"""
