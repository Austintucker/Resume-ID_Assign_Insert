import os
from shutil import copyfile

resumeDirectory = f"{os.getcwd()}\\Resumes"
os.chdir(resumeDirectory)

for file in os.listdir(resumeDirectory):
    for x in range(1000):
        copyfile(file, f"{x}-File.pdf")
    os.remove(file)