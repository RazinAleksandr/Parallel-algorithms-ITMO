from mpi4py import MPI
import numpy as np

# Get my rank
rank = MPI.COMM_WORLD.Get_rank()
size = MPI.COMM_WORLD.Get_size()

# Define class object
class simple_obj:
    def __init__(self, obj_1, obj_2):
        self.obj_1 = obj_1
        self.obj_2 = obj_2

    def production(self):
        return self.obj_1 * self.obj_2

# Define all data for sending
data_0 = list(range(100))
data_1 = simple_obj(np.random.randint(100), np.random.randint(100))
data_2 = np.random.randint(0, 100, size=(2, size))

list_of_objects = [data_0, data_1, data_2]

if rank == 0:
    data = list_of_objects

else:
    data = None


data = MPI.COMM_WORLD.scatter(data, root=0)
print(f"Rank {rank} shows data:\n{data}\n")
