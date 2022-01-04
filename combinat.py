import glob
import os
import shutil
from tqdm import tqdm
FilePath = "E:\老片修复\hlm2_track3\*\*.png"
SavePath = "E:\老片修复\hlm_track3"
Files = sorted(glob.glob(FilePath))

if __name__ == "__main__":
    for i,File in enumerate(tqdm(Files)):
        FileName = os.path.join(SavePath,str(i).zfill(4)+".png")
        shutil.move(File,FileName)
