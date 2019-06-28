
if __name__ == '__main__':
    import multiprocessing
    import cpuinfo
    import os
    from psutil import virtual_memory
    import psutil
    # Call freeze_support or Pyinstaller will recursively fork infinite processes forever
    multiprocessing.freeze_support()
    computername = os.environ['COMPUTERNAME']
    user = os.getlogin()
    ram = virtual_memory()
    processor = cpuinfo.get_cpu_info()['brand']
    cores = psutil.cpu_count(logical=False)
    disk = psutil.disk_usage('/')

    print('\nComputer name: ' + computername)
    print('\nUser: ' + user)
    print('\nTotal RAM:')
    print(ram.total / (1024.0 ** 3),'GB')
    print('\nProcessor: ' + processor)
    print('\nCores: ' + str(cores))
    print('\nFree space:')
    print(disk.free / (1024.0 ** 3),'GB')
    print('\nTotal space:')
    print(disk.total / (1024.0 ** 3),'GB')

    input('\nPress any key to exit')
