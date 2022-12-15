from mpi4py import MPI
from sys import getsizeof
import time

# Get info
rank = MPI.COMM_WORLD.Get_rank()
size = MPI.COMM_WORLD.Get_size()

N = 10
assert size == N, f'Number of workers ({size}) != {N}'

circular = list(range(N)) + [0]
message = "My tea's gone cold"

for i in range(N+1):
    if i == rank or i == rank + N:
        if i != 0:
            request = MPI.COMM_WORLD.irecv(source=circular[i-1], tag=i-1)
            message = request.wait()
            print(f'Message '{message}' has been recieved by {rank} from {circular[i-1]}')
        if i != N:
            MPI.COMM_WORLD.send(message, dest=circular[i+1], tag=i)
            print(f'Message was sent from {rank} to {circular[i+1]}')
