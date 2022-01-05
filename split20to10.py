import os
import shutil
from tqdm import tqdm
from glob import glob

FileFolderPath = "/data/hj/mmediting-master/rzwc/*"
SavePath = "/data/hj/mmediting-master/wzt_7/"
FileFolders = sorted(glob(FileFolderPath))
num = 7
if not os.path.exists(SavePath):
    os.mkdir(SavePath)
if __name__=="__main__":
    i = 0
    for n,FileFolder in enumerate(tqdm(FileFolders)):
        Files = sorted(glob(os.path.join(FileFolder,"*.png")))
        for m,File in enumerate(Files):
            if m%num == 0:
                i=i+1
                TmpPath = os.path.join(SavePath,str(i).zfill(4))
                if not os.path.exists(TmpPath):
                    os.mkdir(TmpPath)
                shutil.copy(File,os.path.join(TmpPath,str(m%num).zfill(8)+".png"))
            else :
                shutil.copy(File,os.path.join(TmpPath,str(m%num).zfill(8)+".png"))      
