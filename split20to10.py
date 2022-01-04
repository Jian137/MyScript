import os
import shutil
from tqdm import tqdm
from glob import glob

FileFolderPath = "/data/hj/mmediting-master/hlm2_track3/*"
SavePath = "/data/hj/mmediting-master/hlm_track3_7/"
FileFolders = sorted(glob(FileFolderPath))

if __name__=="__main__":
    i = 0
    for n,FileFolder in enumerate(tqdm(FileFolders)):
        Files = sorted(glob(os.path.join(FileFolder,"*.png")))
        for m,File in enumerate(Files):
            if m%7 == 0:
                i=i+1
                TmpPath = os.path.join(SavePath,str(i).zfill(4))
                if not os.path.exists(TmpPath):
                    os.mkdir(TmpPath)
                shutil.copy(File,os.path.join(TmpPath,str(m%7).zfill(8)+".png"))
            else :
                shutil.copy(File,os.path.join(TmpPath,str(m%7).zfill(8)+".png"))      
