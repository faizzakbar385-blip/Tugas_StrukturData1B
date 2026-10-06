"""Unit testing Queue dan Stack - Tugas Mandiri 1b"""
import unittest
from antrean_undo import Queue, Stack


class TestQueue(unittest.TestCase):
    def test_enqueue(self):
        q = Queue()
        q.enqueue("Faiz")
        q.enqueue("Siti")
        self.assertEqual(q.tampil(), ["Faiz", "Siti"])

    def test_dequeue_fifo(self):
        q = Queue()
        q.enqueue("Faiz")
        q.enqueue("Siti")
        self.assertEqual(q.dequeue(), "Faiz")
        self.assertEqual(q.tampil(), ["Siti"])

    def test_dequeue_antrean_kosong(self):
        q = Queue()
        with self.assertRaises(IndexError):
            q.dequeue()

    def test_peek(self):
        q = Queue()
        q.enqueue("Faiz")
        q.enqueue("Siti")
        self.assertEqual(q.peek(), "Faiz")
        self.assertEqual(len(q.tampil()), 2)   # peek tidak menghapus data

    def test_peek_antrean_kosong(self):
        with self.assertRaises(IndexError):
            Queue().peek()

    def test_is_empty(self):
        q = Queue()
        self.assertTrue(q.is_empty())
        q.enqueue("Faiz")
        self.assertFalse(q.is_empty())
        q.dequeue()
        self.assertTrue(q.is_empty())


class TestStack(unittest.TestCase):
    def test_push(self):
        s = Stack()
        s.push("Aksi 1")
        s.push("Aksi 2")
        self.assertEqual(s.tampil(), ["Aksi 1", "Aksi 2"])

    def test_pop_lifo(self):
        s = Stack()
        s.push("Aksi 1")
        s.push("Aksi 2")
        self.assertEqual(s.pop(), "Aksi 2")
        self.assertEqual(s.tampil(), ["Aksi 1"])

    def test_pop_tumpukan_kosong(self):
        with self.assertRaises(IndexError):
            Stack().pop()

    def test_peek(self):
        s = Stack()
        s.push("Aksi 1")
        s.push("Aksi 2")
        self.assertEqual(s.peek(), "Aksi 2")
        self.assertEqual(len(s.tampil()), 2)   # peek tidak menghapus data

    def test_peek_tumpukan_kosong(self):
        with self.assertRaises(IndexError):
            Stack().peek()

    def test_is_empty(self):
        s = Stack()
        self.assertTrue(s.is_empty())
        s.push("Aksi 1")
        self.assertFalse(s.is_empty())
        s.pop()
        self.assertTrue(s.is_empty())


if __name__ == "__main__":
    unittest.main(verbosity=2)