AWS will run [[kubernetes pieces | control plane]] in its own managed VPC while the worker nodes run in the customers VPC.  In order to communicate between the two you can traverse the public, private (through a ENI) or hybrid internet.

In all three versions `kubelet` communicates with the master through the ENI.  Only in the public model do the worker nodes `kube proxy` communicate with the API server through the IGW attached to the managed VPC (xxx.eks.aws.com).  In the private and hybrid models you stand up a hosted zone inside your vpc which routes all worker traffic through the ENI.  Finally in the private model the `kubectl` commands only work from inside that VPC.


Source:
[De-mystifying cluster networking for Amazon EKS worker nodes | Containers](https://aws.amazon.com/blogs/containers/de-mystifying-cluster-networking-for-amazon-eks-worker-nodes/)

#kubernetes #networking