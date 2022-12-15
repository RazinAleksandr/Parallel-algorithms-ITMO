from mpi4py import MPI
import time

# Get my rank
rank = MPI.COMM_WORLD.Get_rank()
size = MPI.COMM_WORLD.Get_size()

if rank == 0:
    for i in range(1, size):
        data = MPI.COMM_WORLD.recv(source=i, tag=i)
        print(f"Time between sending message '{data[0]}' from a worker \
and receiving it at the host from rank {i} is {1000 * (time.time() - data[1]):.4f} ms")
else:
    start = time.time()
    data = ['Stan', start]
    MPI.COMM_WORLD.send(data, dest=0, tag=rank)
