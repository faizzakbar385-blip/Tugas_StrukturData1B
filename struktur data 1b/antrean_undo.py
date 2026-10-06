"""Tugas Mandiri 1b - Struktur Data Linear (Queue dan Stack)
Nama : Faiz Akbar | NIM : 12550110321

Fitur 1: Antrean layanan mahasiswa  -> QUEUE (FIFO)
Fitur 2: Undo aktivitas petugas     -> STACK (LIFO)
"""
from collections import deque


class Queue:
    """Antrean (FIFO): yang masuk pertama, keluar pertama."""

    def __init__(self):
        self.data = deque()

    def is_empty(self):
        return len(self.data) == 0

    def enqueue(self, item):          # penambahan di belakang: O(1)
        self.data.append(item)

    def dequeue(self):                # penghapusan di depan: O(1)
        if self.is_empty():
            raise IndexError("Antrean kosong")
        return self.data.popleft()

    def peek(self):                   # lihat terdepan: O(1)
        if self.is_empty():
            raise IndexError("Antrean kosong")
        return self.data[0]

    def tampil(self):
        return list(self.data)


class Stack:
    """Tumpukan (LIFO): yang masuk terakhir, keluar pertama."""

    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def push(self, item):             # penambahan di puncak: O(1)
        self.data.append(item)

    def pop(self):                    # penghapusan di puncak: O(1)
        if self.is_empty():
            raise IndexError("Tumpukan kosong")
        return self.data.pop()

    def peek(self):                   # lihat puncak (terbaru): O(1)
        if self.is_empty():
            raise IndexError("Tumpukan kosong")
        return self.data[-1]

    def tampil(self):
        return list(self.data)


def simulasi_antrean():
    print("=== SIMULASI ANTREAN (QUEUE / FIFO) ===")
    q = Queue()
    print("Langkah 1 | enqueue Faiz Akbar     ->", end=" "); q.enqueue("Faiz Akbar"); print(q.tampil())
    print("Langkah 2 | enqueue Siti Aisyah    ->", end=" "); q.enqueue("Siti Aisyah"); print(q.tampil())
    print("Langkah 3 | enqueue Budi Santoso   ->", end=" "); q.enqueue("Budi Santoso"); print(q.tampil())
    print("Langkah 4 | peek (lihat terdepan)  ->", q.peek(), "| antrean:", q.tampil())
    print("Langkah 5 | dequeue (dilayani)     ->", q.dequeue(), "| antrean:", q.tampil())
    print("Langkah 6 | enqueue Dewi Lestari   ->", end=" "); q.enqueue("Dewi Lestari"); print(q.tampil())
    print("Langkah 7 | enqueue Rizki Ramadhan ->", end=" "); q.enqueue("Rizki Ramadhan"); print(q.tampil())
    print("Langkah 8 | dequeue (dilayani)     ->", q.dequeue(), "| antrean:", q.tampil())
    print("Langkah 9 | is_empty?              ->", q.is_empty())


def simulasi_undo():
    print("\n=== SIMULASI UNDO (STACK / LIFO) ===")
    s = Stack()
    print("Langkah 1 | push Input nilai Algoritma  ->", end=" "); s.push("Input nilai Algoritma"); print(s.tampil())
    print("Langkah 2 | push Edit data mahasiswa    ->", end=" "); s.push("Edit data mahasiswa"); print(s.tampil())
    print("Langkah 3 | push Hapus data KRS         ->", end=" "); s.push("Hapus data KRS"); print(s.tampil())
    print("Langkah 4 | peek (aktivitas terbaru)    ->", s.peek(), "| tumpukan:", s.tampil())
    print("Langkah 5 | pop (undo)                  ->", s.pop(), "| tumpukan:", s.tampil())
    print("Langkah 6 | push Tambah data mahasiswa   ->", end=" "); s.push("Tambah data mahasiswa"); print(s.tampil())
    print("Langkah 7 | pop (undo)                  ->", s.pop(), "| tumpukan:", s.tampil())
    print("Langkah 8 | is_empty?                   ->", s.is_empty())


if __name__ == "__main__":
    simulasi_antrean()
    simulasi_undo()