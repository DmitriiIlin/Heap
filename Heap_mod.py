
class Heap:
    def __init__(self):
        self.HeapArray = []
        self.Root=None

    def Data_Sort(self,data):
        #Сортирует исходный массив по убыванию 
        length=len(data)
        for i in range(0,length):
            for j in range(i,length):
                if data[i]<data[j]:
                    data[i],data[j]=data[j],data[i]
                else:
                    pass
        return data


    def MakeHeap(self, a, depth=0):
	# создаём массив кучи HeapArray из заданного
        # размер массива выбираем на основе глубины depth 
        if not a:
            return None
        if depth==None or depth<0:
            return None
        q_ty=0
        for i in range(0,depth+1):
            q_ty=q_ty+2**i
        a=self.Data_Sort(a)
        len_a=len(a)
        if q_ty>len_a:
            limit=len_a
        else: 
            limit=q_ty
        for j in range(0,limit):
            if a[j]<0:
                return None 
            self.HeapArray.append(a[j])
        if len_a<q_ty:
            delta=q_ty-len_a-1
            while delta>=0:
                self.HeapArray.append(None)
                delta-=1 
        return depth
    
    def Getdepth(self,a):
        # Вернуть значение глубины массива
        if len(a)==0:
            return 0
        depth=0
        array_q_ty=len(a)
        while array_q_ty>0:
            depth+=1
            array_q_ty=array_q_ty//2
        return depth-1


    def GetMax(self):
        # вернуть значение корня и перестроить кучу
        if self.HeapArray[0]<0 or self.HeapArray[0]==None: 
            return -1 # если куча пуста
        else:
            max_key=self.HeapArray.pop(0)
            self.HeapArray.append(None)
            return max_key


    def Add(self, key):
	# добавляем новый элемент key в кучу и перестраиваем её
        if key<0 and key==None:
            return None
        len_heap=len(self.HeapArray)
        if len_heap==0:
            self.HeapArray.append(key)
        else:
            None_id=False
            for i in range(0,len_heap):
                if self.HeapArray[i]==None:
                    self.HeapArray[i]=key
                    None_id=True
                    break
                else:
                    pass
            if None_id==False:
                return False # если куча вся заполнена
            else:
                depth=self.Getdepth(self.HeapArray)
                None_q_ty=0
                for everykey in range(0,len_heap):
                    if self.HeapArray[everykey]==None:
                        None_q_ty+=1
                for _ in range(0,None_q_ty):
                    self.HeapArray.remove(None)
                a=[]
                for key in range(0,len(self.HeapArray)):
                    a.append(self.HeapArray[key])
                self.HeapArray.clear()
                self.MakeHeap(a,depth)

"""
z=Heap()
a=[1,3,5,6,89,0,44,5]

b=[]
print(z.Getdepth(a))
#print(a)
zz=z.MakeHeap(a,2)
print(z.HeapArray)
print(z.Add(55))
print(z.HeapArray)
print(z.GetMax(),z.HeapArray)
"""