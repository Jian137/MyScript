import os
import shutil
from tqdm import tqdm
from glob import glob

DstFolders = sorted(glob("/data/hj/mmediting-master/wzt_7/*"))

for i,DstFolder in enumerate(tqdm(DstFolders)):

    Files = sorted(glob(os.path.join(DstFolder,"*.png")))

    if len(Files) == 1:
        print("----------------")
        LastFiles = sorted(glob(os.path.join(DstFolders[i-1],"*.png")))
        shutil.move(Files[0],Files[0].replace("00000000.png","00000003.png"))
        shutil.move(LastFiles[-3],os.path.join(DstFolder,"00000000.png"))
        shutil.move(LastFiles[-2],os.path.join(DstFolder,"00000001.png"))
        shutil.move(LastFiles[-1],os.path.join(DstFolder,"00000002.png"))