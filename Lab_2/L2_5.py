from mpi4py import MPI
from sys import getsizeof
import time

# Get info
rank = MPI.COMM_WORLD.Get_rank()
size = MPI.COMM_WORLD.Get_size()

N = 10
if rank == 0:
    for i in range(51):
        obj = [666]*(1000 * i + 1)
        L = getsizeof(obj) # size in bytes
        T = time.time()
        for j in range(N):
            MPI.COMM_WORLD.send(obj, dest=1, tag=1000 * i+j)
            obj = MPI.COMM_WORLD.recv(source=1, tag=1000*i+j+1)
        T = time.time() - T
        R = (2 * N * L) / T
        print(f"Iter {i}: Object {L} size (bytes): {R} MB/s")
elif rank == 1:
    # only one worker
    for i in range(51):
        for j in range(N):
            mes = MPI.COMM_WORLD.recv(source=0, tag=1000*i+j)
            MPI.COMM_WORLD.send(mes, dest=0, tag=1000*i+j+1)
