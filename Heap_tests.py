import unittest, random, Heap_mod

def Create_masive(massive_size=1):
    # Создание исходного массива для пирамиды
    if massive_size==0:
        return []
    massive=[] 
    for _ in range(0,massive_size):
        massive.append(random.randint(1,100))
    return massive

class Heap_Tests(unittest.TestCase):
    # Тетирование работы пирамиды

    def test_zero(self):
        # Тестирование пустой пирамиды: добавление элемента, получение максимального элемента
        a=[]
        Heap_Test=Heap_mod.Heap()
        new_key=random.randint(1,100)
        Heap_Test.MakeHeap(a,1)
        Heap_Test.Add(new_key)
        self.assertEqual(Heap_Test.GetMax(),new_key)

    
    def test_some_elements(self):
        # Тестирование пиромиды с количеством элементов не равным 0 и 1
        massive_size=random.randint(3,15)
        deep_heap=random.randint(1,3)
        a=Create_masive(massive_size)
        Heap_test=Heap_mod.Heap()
        Heap_test.MakeHeap(a,deep_heap)
        q_ty=0
        for i in range(0,deep_heap+1):
            q_ty=q_ty+2**i
        self.assertEqual(q_ty,len(Heap_test.HeapArray))
        self.assertEqual(max(a),Heap_test.HeapArray[0])
        # Добавление э-та в заполненный массив
        massive_size=15
        deep_heap=3
        b=Create_masive(massive_size)
        Heap_test_2=Heap_mod.Heap()
        Heap_test_2.MakeHeap(b,deep_heap)
        new_key=random.randint(101,200)
        self.assertEqual(Heap_test_2.Add(new_key),False)
        new_key_in_heap=False
        #print(Heap_test_2.HeapArray)
        for j in range(0,len(Heap_test_2.HeapArray)):
            if Heap_test_2.HeapArray[j]==new_key:
                new_key_in_heap=True
                break
        self.assertEqual(False,new_key_in_heap)
    

if __name__ == '__main__':
    try:
        unittest.main()
    except: 
        SystemExit
    input()
