from mpi4py import MPI
import time


def timer(func):
    def wrapper(*args, **kwargs):
        print('='*50, f'\nRank {args[0]} is - {current_time(time.time())}\n')
        func(*args, **kwargs)
        print(f'\nRank {args[0]} is - {current_time(time.time())}')
        print('='*50, '\n')
    return wrapper

def current_time(t):
    return time.asctime(time.localtime(t))

@timer
def sleeping(rank, pause=5):
    time.sleep(pause)


Em = ['Look',
      'If you had',
      'One shot',
      'Or one opportunity',
      'To seize everything you ever wanted,'
      'In one moment',
      'Would you capture it',
      'Or just let it slip?']

# Get my rank
rank = MPI.COMM_WORLD.Get_rank()

if rank == 0:
    sleeping(rank)

    # get message
    message = MPI.COMM_WORLD.recv(source=1, tag=0)

    print(f"Rank {rank} received message:")
    print(f"'{message}' which is translated to '{current_time(message)}'")
    print(f"from {(time.time() - message):.2f} sec ago")

# this program will work only with single worker
if rank == 1:
    # this is worker
    message = time.time()
    req = MPI.COMM_WORLD.isend(message, dest=0, tag=0)
    for string in Em:
        print(string)
        time.sleep(0.25)
