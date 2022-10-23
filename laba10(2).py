import os
import shutil
path = 'Python_docs'
end_path = 'RESULTS'
files = os.listdir(path)
print(files)
for file in files[:2]:
   os.makedirs(end_path, exist_ok=True)
   shutil.copy(os.path.join(path, file), end_path)