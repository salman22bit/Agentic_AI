# api_server/main.py
from fastapi import FastAPI
from kubernetes import client, config

#FastAPI is a modern web framework used to build APIs in Python quickly and easily.
#kubernetes.client and kubernetes.config are from the official Kubernetes Python client:
#client lets you interact with Kubernetes objects (pods, nodes, namespaces, etc.)

app = FastAPI()

#What this does:
#1- Initializes your FastAPI application.
#2- This app object will be used to define your API endpoints like /nodes.
# We use client to programmatically interact with Kubernetes. Instead of running: kubectl get nodes
# You do the same thing in Python like this: client.CoreV1Api().list_node()


# Load kubeconfig
config.load_kube_config(config_file="kube_config")

#Loads the kube_config file that contains credentials and cluster details.

@app.get("/nodes")
def get_nodes():
    v1 = client.CoreV1Api()
    nodes = v1.list_node().items
    return [node.metadata.name for node in nodes]

#This line tells FastAPI: “When someone visits /nodes, run the function below it.”

#What this does:
#1-Defines a GET endpoint at /nodes.
#When someone accesses http://localhost:8000/nodes (or your server's IP), this function will run
#@app.get(...) is a decorator that tells FastAPI to treat this function as an API route.
# Think of v1 like your personal kubectl but in Python.

# Basically v1 variable meh client coreapi se communicate karega aur usse hum nodes varaible meh use kar rahe hai for example nodes me hum bol rahe hai
# ki client coreapi k nodes lakar de thats it 

@app.get("/pods")
def get_pods():
    v1 = client.CoreV1Api()
    pods = v1.list_pod_for_all_namespaces().items
    return [f"{pod.metadata.namespace}/{pod.metadata.name}" for pod in pods]

@app.get("/namespaces")
def get_namespaces():
    v1 = client.CoreV1Api()
    namespaces = v1.list_namespace().items
    return [ns.metadata.name for ns in namespaces]
