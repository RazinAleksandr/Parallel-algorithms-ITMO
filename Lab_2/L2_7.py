from mpi4py import MPI
import time

def wait(sleeping=25):
    intervals = int(sleeping / 5)
    for i in range(intervals):
        time.sleep(5)
        print(f"WAITING")

# Get my rank
rank = MPI.COMM_WORLD.Get_rank()

if rank == 0:
    # master
    message0 = "Stan"
    MPI.COMM_WORLD.isend(message0, dest=1, tag=0)
    wait()
    message1 = MPI.COMM_WORLD.recv(source=1, tag=1)
    print(f"Master {rank} received Marshall message '{message1}'")
# this program will work only with single worker
if rank == 1:
    # worker
    message0 = MPI.COMM_WORLD.recv(source=0, tag=0)
    print(f"Worker {rank} received Master message '{message0}'")
    message1 = message0 + " back"
    MPI.COMM_WORLD.isend(message1, dest=0, tag=1)
    print(f"Worker {rank} sent message {message1} to Master")
