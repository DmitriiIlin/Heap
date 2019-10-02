
class Heap:
    def __init__(self):
        self.HeapArray = []
        self.Root=None

    def MaxElement(self,i,a):
        #Возвращает индекс максимального элемента среди родителя и двух детей
        if len(a)!=0:
            if a[i]!=None:
                leftchild=2*i+1
                rightchild=2*i+2
            else:
                return -1
        else:
            return -1
        #Ищем максимальный элемент среди родителя и его детей
        directionleft=None
        if leftchild<len(a):
            if rightchild<len(a):
                if a[leftchild]>=a[rightchild]:
                    maxelement=a[leftchild]
                    directionleft=True
                elif a[leftchild]<a[rightchild]:
                    maxelement=a[rightchild]
                    directionleft=False
            else:
                maxelement=a[leftchild]
                directionleft=True
        else:
                maxelement=a[i]
        data=a[i]
        if data>=maxelement:
            return i
        else:
            if directionleft==True:
                return 2*i+1
            else:
                return 2*i+2

    
    def GetMax(self):
        #Вернуть значение корня и перестроить кучу
        #Если куча пуста вернуть -1
        """
        level=0
        if len(self.HeapArray)==0:
            return -1
        else:
            pass
        #Расчет кол-ва уровней в куче 
        """
        size=len(self.HeapArray)
        """
        pos=len(self.HeapArray)
        while pos//2!=0:
            level+=1
            pos=pos//2
        """
        #Присвоение максимального элемента 
        max=self.HeapArray.pop(0)
        #Поиск позиции последнего элемента не равного None
        # и удаление всех элементов со значением None
        None_in_array=False
        for i in range(0,len(self.HeapArray)):
            if self.HeapArray[i]==None:
                None_in_array=True
                number=i
                break
        if None_in_array==False:
            number=len(self.HeapArray)
        while len(self.HeapArray)-number>0:
            self.HeapArray.pop()
        # Если после удалениея в куче не осталось элементов!=None
        #Вернуть max
            if len(self.HeapArray)==0:
                return max
        #Вставка последнего элемента в нулевую позицию
        self.HeapArray.insert(0,self.HeapArray.pop())
        #print(self.HeapArray)
        
        current_number=0
        number_for_change=self.MaxElement(current_number,self.HeapArray)
        while current_number!=number_for_change:
            data=self.HeapArray[current_number]
            self.HeapArray[current_number]=self.HeapArray[number_for_change]
            self.HeapArray[number_for_change]=data
            current_number=number_for_change
            number_for_change=self.MaxElement(current_number,self.HeapArray)
        #print(self.HeapArray)    
        while size-len(self.HeapArray)>0:
            self.HeapArray.append(None)
        #print(self.HeapArray)
        return max
    

    def ChangePosition(self,i,a):
        #Метод всплытия / погружения ключа
        q_ty=len(a)
        if self.HeapArray[i]<0 or self.HeapArray[i] is None:
            return None
        for element in range(0,q_ty):
            leftchild=2*element+1
            rightchild=2*element+2
            child=None
            if leftchild<q_ty and self.HeapArray[leftchild]!=None:
                if rightchild<q_ty and self.HeapArray[rightchild]!=None:
                    if self.HeapArray[leftchild]>self.HeapArray[rightchild]:
                        maxchild=self.HeapArray[leftchild]
                        child=False
                    else: 
                        maxchild=self.HeapArray[rightchild]
                        child=True
                else: 
                    maxchild=self.HeapArray[leftchild]
                    child=False
                if self.HeapArray[element]<maxchild:
                    data=self.HeapArray[element]
                    self.HeapArray[element]=maxchild
                    if child==False:
                        self.HeapArray[2*element+1]=data
                        element=2*element+1
                    else:
                        self.HeapArray[2*element+2]=data
                        element=2*element+2
            else:
                element+=1
    
    def MakeHeap(self, a, depth=0):
	# создаём массив кучи HeapArray из заданного
    # размер массива выбираем на основе глубины depth
        q_ty=0
        if depth<0:
            return None
        for i in range(0,depth+1):
            q_ty=q_ty+2**i
        #print(len(a),q_ty)
        if len(a)>q_ty:
            size=q_ty
        else:
            size=len(a)
        for key in range(0,size):
            self.HeapArray.append(a[key])
            for everykey in range(0,len(self.HeapArray)):
                self.ChangePosition(everykey,self.HeapArray)
        if q_ty-len(self.HeapArray)>0:
            while q_ty-len(self.HeapArray)>0:
                self.HeapArray.append(None)
        self.Root=self.HeapArray[0]


    def Add(self, key):
	# добавляем новый элемент key в кучу и перестраиваем её
        a=[]     
        if key!=None and key>0:
            pass
        else:
            return None
        if len(self.HeapArray)==0:
            a=[]
            a.append(key)
            self.MakeHeap(a)
        else:
            level=0
            pos=len(self.HeapArray)
            while pos//2!=0:
                level+=1
                pos=pos//2
            for everyelement in range(0,len(self.HeapArray)):
                if self.HeapArray[everyelement]==None:
                    break
            #print(everyelement)
            if self.HeapArray[everyelement]==None:
                self.HeapArray[everyelement]=key
                while len(self.HeapArray)-everyelement-1>0:
                    self.HeapArray.pop()
                for i in range(0,len(self.HeapArray)):
                    a.append(self.HeapArray[i])
                while len(self.HeapArray)!=0:    
                    self.HeapArray.pop()
                #print(self.HeapArray)
                #print(a)
                self.MakeHeap(a,level)
            else:
                return False

class HeapSort:
    def __init__(self,array):
        self.HeapSort=Heap()
        lenarray=len(array)
        q_ty=0
        i=0
        while q_ty<=lenarray:
            q_ty=q_ty+2**i
            i+=1
        if lenarray==0:
            self.HeapSort.MakeHeap(array,0)
        else: 
            self.HeapSort.MakeHeap(array,i-1)
        print(self.HeapSort.HeapArray)
    
    def GetNextMax(self):
        #Выдаёт максимальный элемент кучи, если куча пуста то -1
        return self.HeapSort.GetMax()



            
        
"""
a=[2,4,5,6,1]
z=HeapSort(a)
print(z.GetNextMax())
print(z.HeapSort.HeapArray)
print(z.HeapArray)
z.Add(86000)
print(z.HeapArray)
print(z.GetMax())
print(z.HeapArray)
print(z.GetMax())
print(z.HeapArray)
z.Add(23)
z.Add(None)
z.Add(40)
print(z.HeapArray)
print(z.Root)
z.GetMax()
print(z.HeapArray)
print(z.Root)
"""

