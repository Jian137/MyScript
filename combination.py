import glob
import os
import shutil
from tqdm import tqdm
FilePath = "/data/hj/mmediting-master/hlmtrack3_hisense_230000/*/*.png"
SavePath = "/data/hj/mmediting-master/hlmtrack3_hisense_230000_combate"
Files = sorted(glob.glob(FilePath))

if __name__ == "__main__":
    for i,File in enumerate(tqdm(Files)):
        FileName = os.path.join(SavePath,str(i).zfill(4)+".png")
        shutil.move(File,FileName)
