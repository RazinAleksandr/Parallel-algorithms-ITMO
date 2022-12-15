from mpi4py import MPI

comm = MPI.Comm.Get_parent()
rank = comm.Get_rank()

comm.send(rank, dest=0, tag=10)

print(f"Rank of created worker is {rank}")

comm.Disconnect()
