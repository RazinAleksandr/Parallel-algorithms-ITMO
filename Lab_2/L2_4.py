from mpi4py import MPI
import numpy as np

# Get info
rank = MPI.COMM_WORLD.Get_rank()
size = MPI.COMM_WORLD.Get_size()

if rank == 0:
    num = int(10e5)
    
    v_1, v_2 = np.random.random(num), np.random.random(num)
    message_1, message_2 = np.array_split(v_1, size-1), np.array_split(v_2, size-1)
    
    for w in range(size-1):
        req_1 = MPI.COMM_WORLD.isend(message_1[w], dest=w+1, tag=w+1)
        req_2 = MPI.COMM_WORLD.isend(message_2[w], dest=w+1, tag=w+1001)

    dot_prod = 0
    for w in range(size-1):
        dot_prod += MPI.COMM_WORLD.recv(source=w+1, tag=w+2001)
    print(f"Total product is {dot_prod:.3f}")

else:
    # workers
    arr_1, arr_2 = MPI.COMM_WORLD.recv(source=0, tag=rank), MPI.COMM_WORLD.recv(source=0, tag=rank+1000)
    result = np.dot(arr_1, arr_2)
    
    print(f"Worker {rank} sum is {result:.4f}")
    res = MPI.COMM_WORLD.isend(result, dest=0, tag=rank+2000)
