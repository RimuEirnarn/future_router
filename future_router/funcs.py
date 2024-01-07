"""funcs"""

def notimplemented(func):
    """Set route method as Not Implemented, this would make sure that certain function is
    striped."""
    setattr(func, '_notimplemented', True)
    return func

def static_notimplemented(func):
    """Set route method as Not Implemented, by default not requiring @staticmethod"""
    return staticmethod(notimplemented(func))
