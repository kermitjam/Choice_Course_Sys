


from conf import settings
import os,pickle

def select(name,cls_name):
    path = os.path.join(settings.DB_PATH,cls_name)
    if not os.path.isdir(path):
        os.mkdir(path)
    file_path = os.path.join(path,name)
    if os.path.exists(file_path):
        with open(file_path,'rb') as f:
            return pickle.load(f)



def save(obj):
    path = os.path.join(settings.DB_PATH,obj.__class__.__name__.lower())
    if not os.path.isdir(path):
        os.mkdir(path)

    file_path = os.path.join(path,obj.name)

    with open(file_path,'wb') as f:
        pickle.dump(obj,f)
