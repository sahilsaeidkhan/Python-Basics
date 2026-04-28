class UltimateDataSCienceBatch:

    def __init__(self , batch_id):
        self.batch_id = batch_id
        self.student_list = []

    def add_student(self,name,email):
        self.student = {"name":name,"email":email}
        self.student_list.append(self.student)
        print(f"Added {name} to  Batch {self.batch_id}")

    def student_names(self):
        for self.student in self.student_list:
            print(f"Student lists for Batch {self.batch_id} - {self.student}")


batch_1 = UltimateDataSCienceBatch(1)
batch_1.add_student("Krishna","krishna@gmail.com")
batch_1.student_names()

print("\n")

batch_2 = UltimateDataSCienceBatch(2)
batch_2.add_student("Radha","Radha@gmail.com")
batch_2.student_names()
        

