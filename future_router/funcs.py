
def notimplemented(func):
    """Set route method as Not Implemented, this would make sure that certain function is striped."""
    setattr(func, '_notimplemented', True)
