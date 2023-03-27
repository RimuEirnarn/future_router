# Future Router

A wrapper for Flask app (or blueprint) that can be initialised later.

## Overview

```python
from flask import Flask
from future_router import Router

app = Flask(__name__)
route = Router()

@route.get("/")
def root():
    return "Hello, World"

route.init_app(app)
```

It can also use Blueprint. Like above, just with this different

```python
from flask import Flask, Blueprint
from future_router import Router

app = Flask(__name__)
blueprint = Blueprint("name", __name__, url_prefix="/name")
route = Router(blueprint)

@route.get("/")
def root():
    return "Hello, World"
```

### Using `.resource`

```python
from flask import Flask
from future_router import Router, ResourceDummy

route = Router()
app = Flask(__name__)


@route.resource('/users')
class TestResource(ResourceDummy):
    """Test Resource"""

    def index(self):
        return "Index"

    def update(self, id):
        return "Update"

    def destroy(self, id):
        return "Destroy"

    def store(self):
        return "Store"

    def show(self, id):
        return "Show"

    def create(self):
        return "Create"

    def edit(self):
        return "Edit"


route.init_app(app)
```

# License

This repo is licensed in BSD-3 Clause
