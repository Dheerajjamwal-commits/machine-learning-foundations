# This program informs the user before opening and closing a file
class Filemanager:
    def __init__(self,filename,mode):
        self.filename = filename
        self.mode = mode
# __enter__() executes when with is used and prints a message and returns a file
    def __enter__(self):
         print(f"Opening {self.filename}")
         self.file = open(self.filename,self.mode)
         return self.file
# __exit__() executes when you exit the with block printing a closing file message with 3 error parameters
    def __exit__ (self,exc_type, exc_val, exc_tb):
        print(f"Now closing {self.filename}")
        if self.file:
            self.file.close()
# Filemanager is used to open the file executing the methods defined above
with Filemanager ("Practice.txt",'w') as file:
    file.write("This is a sample file created to practice Modifying Dunder methods")

