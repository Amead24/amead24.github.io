Kubernetes can be first broken down into two pieces.

1. Worker Nodes
2. Control Plane

The worker nodes, are physical machines that need to be configured to communicate with the control plane. 

The control plane is composed of several smaller parts which by default all run in the kube-system namespace:
a. API server
	b. controller manager
	c. scheduler
	d. etcd

The API server communicates with the nodes through `kubelet` which is running on the worker nodes.  The other services (b, c, d) communicate through the same API server.


#kubernetes 