class Assignment2:
    def __init__(self, year):   #constructor
        self.year = int(year)
                
    def tellAge(self, currentYear):  # task 2
        currentYear = int(currentYear)
        age = currentYear - self.year 
        print ("Your age is {}".format(age))

    def listAnniversaries(self):  #task 3
        years = (2022 - self.year)
        aniversaries = []  # list of anniversaries 

        modYears = years % 10 # years % 10
        modYears1 = years - modYears # years - mod
        limit = modYears1 / 10 # new result / 10 
       

        for n in range(1, int(limit)+1):  # the new result will be somehow placed as 10, 20 , limit to muliply by 10 
            n = n*10
            aniversaries.append(n)

        return aniversaries

    def modifyYear(n):   #task 4
        subYear = str(n[0:2])
        print(subYear)

obj = Assignment2(1989)  # must input valid year
obj.tellAge(2022)        # input the  current year
ret = obj.listAnniversaries()
print(ret)        