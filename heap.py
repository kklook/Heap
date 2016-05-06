# -*- coding:utf-8 -*-


class Heap(object):

    def __init__(self, beforesort):
        self.myheap = beforesort
        self.sorted = []

    def adjheap(self, heap, i, end):
        if heap is None:
            heap = self.myheap
        if not (isinstance(heap, list) and isinstance(i, int) and isinstance(end, int)):
            raise TypeError
        left = i * 2 + 1
        right = i * 2 + 2
        i_max = i
        if i < end / 2:
            if left < end and heap[left] > heap[i_max]:
                i_max = left
            if right < end and heap[right] > heap[i_max]:
                i_max = right
            if i_max != i:
                heap[i_max], heap[i] = heap[i], heap[i_max]
                self.adjheap(None, i_max, end)

    def bulidheap(self, heap):
        if heap is None:
            heap = self.myheap
        for i in range(len(heap) / 2 - 1, -1, -1):
            self.adjheap(heap, i, len(heap))

    def heapsort(self, heap=None):
        if heap is None:
            heap = self.myheap
        else:
            self.myheap = heap
        self.bulidheap(heap)

        for i in range(len(heap) - 1, 0, -1):
            heap[i], heap[0] = heap[0], heap[i]
            self.adjheap(None, 0, i)
        self.sorted = self.myheap[:]
        return self.sorted

    def top(self, k, heap=None):
        re_sign = False
        aim = k
        if not isinstance(k, int):
            raise TypeError
        if heap is None:
            heap = self.myheap
        else:
            self.myheap = heap
        if k < 0:
            k = -k
            aim = -k
            re_sign = not re_sign
        if k >= len(heap):
            aim = len(heap) - 1
        self.bulidheap(heap)

        for i in range(len(heap) - 1, len(heap) - aim - 2, -1):
            heap[0], heap[i] = heap[i], heap[0]
            self.adjheap(None, 0, i)
        self.sorted = self.myheap[-k:]
        if not re_sign:
            self.sorted.reverse()
        return self.sorted


def main():
    mylist = [2, 1, 3, 5, 7, 5, 4, 5]
    heapsort = Heap(mylist)
    print heapsort.heapsort()
    print heapsort.sorted
    print heapsort.top(-8)

if __name__ == '__main__':
    main()