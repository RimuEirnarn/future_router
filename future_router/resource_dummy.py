"""Resource Dummy"""
from typing import Protocol
from .funcs import static_notimplemented


class ResourceDummy(Protocol):
    """Resource Dummy"""

    @static_notimplemented
    def index():
        """Index all the resource available."""

    @static_notimplemented
    def create():
        """Show the user/form response"""

    @static_notimplemented
    def store():
        """Store user request"""

    @static_notimplemented
    def edit(res_id):
        """Show user edit form response."""

    @static_notimplemented
    def update(res_id):
        """Update user request"""

    @static_notimplemented
    def destroy(res_id):
        """Delete user request"""

    @static_notimplemented
    def show(res_id):
        """Return resource from id"""
