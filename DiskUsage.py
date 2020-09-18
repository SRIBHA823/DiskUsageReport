<<<<<<< HEAD
import sys
import os
import pandas as pd

def get_size(path):
    total=0
    for entry in os.scandir(path):
        try:
            if entry.is_dir(follow_symlinks=False):
                total+=get_size(entry.path)
            else:
                total+=entry.stat(follow_symlinks=False).st_size
        except Exception as e:
            print("Exception: ",e)
            total+=0
    return total

if __name__=='__main__':
    path='/home'
    print("Total arguments: ",len(sys.argv))
    directory=sys.argv[1] if len(sys.argv)>=2 else path
    usage=[]
    paths=[]
    for entry in os.scandir(directory):
        print(entry.path)
        if(entry.is_dir(follow_symlinks=False)):
            print(get_size(entry.path))
            total=get_size(entry.path)
            print(total)
            paths.append(entry.path)
            usage.append(total)
        usage_dic={'Directory':path,'Usage':usage}
        df=pd.DataFrame(usage_dic)
        print(df)
        df.to_csv("Disk_Home_Usage.csv")
=======
>>>>>>> 5e2dc908c0f93196e8178a8ed2a4b84495c9dfa5

