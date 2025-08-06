from fastapi import APIRouter

class FastMCP:
    def __init__(self, name: str):
        self.name = name
        self.router = APIRouter()
        self.tools = []

    def tool(self):
        def decorator(func):
            # Add both GET and POST support for flexibility
            self.router.add_api_route(
                f"/{func.__name__}", func, methods=["GET", "POST"]
            )
            self.tools.append(func.__name__)
            return func
        return decorator
