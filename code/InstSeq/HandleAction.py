class HandleAction:
    def __init__(self, time, listCompName):
        self._initTime = time
        self._lCompNames = []
        self._isCompleted = False
        for compName in listCompName
            self._lCompNames.append({ compName : { 'time' : -1 } })

    def updateComponent(self, nameComp, t_end):
       for comp in self._lCompNames:
          for name in comp:
             if name == nameComp
                 com[name]['time'] = t_end
                 return True
       return False


    def completed(self, nameComp, t_end):
        if self._isCompleted:
            return True

        if (! updateComponent(nameComp, t_end)):
           raise Exception(f'The {nameComp} is not valid, please check your program. The expected components names are: {self._lCompNames}')
        
        for comp in self._lCompNames:
            for name in comp:
                if com[name]['time'] == -1:
                    return False

        self._isCompleted = True
        return True



