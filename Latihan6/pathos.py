print('Lala Adilah\n 210511117 \nT121C(R3)\n')
from pathos.multiprocessing import ProcessPool

def worker(num):
    """Fungsi untuk menjalankan tugas pada proses multiprocessing"""
    print('Worker', num)
if __name__ == '__main__':
# Buat ProcessPool dengan 2 proses
    pool = ProcessPool(2)
# Panggil fungsi worker pada setiap item secara parallel
    pool.map(worker, range(5))