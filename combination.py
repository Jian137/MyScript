import glob
import os
import shutil
from tqdm import tqdm
FilePath = "/data/hj/mmediting-master/wzt_7/*/*.png"
SavePath = "/data/hj/mmediting-master/wzt_7_0to32s"
Files = sorted(glob.glob(FilePath))
if not os.path.exists(SavePath):
    os.mkdir(SavePath)
if __name__ == "__main__":
    for i,File in enumerate(tqdm(Files)):
        FileName = os.path.join(SavePath,str(i).zfill(4)+".png")
        shutil.copy(File,FileName)
