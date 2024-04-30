class Student:
    count=0
    def __init__(college,name,sem,year):
        college.name=name
        college.sem=sem
        college.year=year
        Student.count+=1
    def displayCount (college):
         print("There are %d student" % Student.count)
    def displayDetails (college):
         print("Name:",college.name,".Designation:",college.sem,",year:",college.year)
e1=Student("Tamim","4sem",2024)
e2=Student("Maibub","4sem",2024)
e3=Student("Prakash","4sem",2024)
e4=Student("Ramesh","4sem",2024)
e4.displayCount ()
print("Detail of all Student:")
e1.displayDetails()
e2.displayDetails()
e3.displayDetails()
e4.displayDetails()