class Vagonas:
    def __init__(self,name, mase, maxMase):
        self.name = name
        self.mase = mase
        self.maxMase = maxMase
        self.id = id
        self.maseKrov = None
        self.foreign_key = None
        
    def getIdVag(self, id):
        return self.id

    def getForeignId(self):
        return self.foreign_key
    
    
    def getVagonai(self):
        return "Vagonas: %s, mase = %s, maksimali mase = %s" %(self.name, self.mase, self.maxMase)

    def __repr__(self):
        return "mase = %s, pavadinimas = %s, maksimali mase= %s" %(self.name, self.mase, self.maxMase)
    
  #  def __str__(self):
   #     return self.name

    def __name__(self):
        return "Vagonas: %s" %(self.name)
        
   # def __unicode__(self):
   #     return self.name

    def __len__(self,):
        return self._len__

    def get_id(self):
        return id


