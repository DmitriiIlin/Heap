
class Heap:
    def __init__(self):
        self.HeapArray = []
        self.Root=None
    
    def GetMax(self):
        #Вернуть значение корня и перестроить кучу
        level=0
        a=[]
        if len(self.HeapArray)==0:
            return -1
        else:
            pass
        pos=len(self.HeapArray)
        #pos_for_none=pos
        while pos//2!=0:
            level+=1
            pos=pos//2
        max=self.HeapArray.pop(0)
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
            if len(self.HeapArray)==0:
                """
                for _ in range(0,pos_for_none):
                    self.HeapArray.append(None)
                """    
                return max
        self.HeapArray.insert(0,self.HeapArray.pop())
        for j in range(0,len(self.HeapArray)):
            a.append(self.HeapArray[j])
        while len(self.HeapArray)!=0:
            self.HeapArray.pop()
        self.MakeHeap(a,level)
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


            
        
"""
z=Heap()
a=[]
z.MakeHeap(a,2)
print(z.HeapArray)
#z.Add(86000)
print(z.HeapArray)
z.GetMax()
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
