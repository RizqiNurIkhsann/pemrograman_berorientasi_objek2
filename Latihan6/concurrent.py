print('Lala Adilah\n 210511117 \nT121C(R3)\n')

import concurrent.futures

def worker(num):
        """Fungsi untuk menjalankan tugas pada proses baru"""
        print('Worker', num)
if __name__ == '__main__':
# Membuat objek ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
# Memanggil fungsi worker sebanyak 5 kali
        for i in range(5):
            executor.submit(worker, i)