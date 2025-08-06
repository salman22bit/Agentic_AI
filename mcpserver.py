#make sure file directory should be there you can find it in another file 

# mcpserver.py

from fastapi import FastAPI
from fastmcp.server.fastmcp import FastMCP
import requests

# Step 1: Create FastAPI app
app = FastAPI(title="MCP Kubernetes Tool Server")

# Step 2: Initialize FastMCP
mcp_server = FastMCP(name="kubernetesTools")

# Step 3: Define your tool base URL (main.py service)
URL = "http://127.0.0.1:5002"

# Step 4: Define all MCP tools
@mcp_server.tool()
async def get_pods():
    """Get all pods"""
    try:
        response = requests.get(f"{URL}/pods")
        return response.json()
    except Exception as e:
        return {"error": str(e)}

@mcp_server.tool()
async def get_nodes():
    """Get all nodes"""
    try:
        response = requests.get(f"{URL}/nodes")
        return response.json()
    except Exception as e:
        return {"error": str(e)}

@mcp_server.tool()
async def get_namespaces():
    """Get all namespaces"""
    try:
        response = requests.get(f"{URL}/namespaces")
        return response.json()
    except Exception as e:
        return {"error": str(e)}

@mcp_server.tool()
async def get_pods_in_namespace(namespace: str):
    """Get pods in the given namespace"""
    try:
        response = requests.get(f"{URL}/pods/{namespace}")
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# Step 5: Add health route (optional)
@app.get("/")
def root():
    return {"message": "MCP Server is running!"}

# ✅ Step 6: Mount FastMCP's router to the FastAPI app manually
app.include_router(mcp_server.router, prefix="/tools")

# ✅ This 'app' will be used by Uvicorn
