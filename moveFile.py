from distutils import extension
import os;
import shutil;

from_dir="C:\Users\Asus\Downloads"
to_dir="C:\Users\Asus\Desktop\Project111"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for i in list_of_files:
    name,extension=os.path.splitext(i)
    print(name)
    print(extension)
    if extension == " ":
       continue
    if extension in [',txt','.docx','.doc','.pdf']:
       path1 = from_dir + '/'+ i 
       path2 = to_dir + '/' + "documentfiles"
       path3 = to_dir + '/' + "documentfiles" + '/' + i
    if os.path.exists(path2):
       print('Moving' + i +'.........')
       shutil.move(path1,path3)
    else:
       os.makedirs(path2)
       print('Moving'+ i + '.......')
       shutil.move(path1,path3) 