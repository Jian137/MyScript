import glob
import os
import shutil
from tqdm import tqdm
import numpy as np

FilePath = "/data/hj/mmediting-master/wzt_7/*"
SavePath = "/data/hj/mmediting-master/wzt_7_55to61s"
if not os.path.exists(SavePath):
    os.mkdir(SavePath)
StartTime = 55
EndTime = 61
rate = 25
StartFrame = StartTime * rate
EndFrame = EndTime * rate

FileFolders = sorted(glob.glob(FilePath))
FileNums = [len(os.listdir(i)) for i in FileFolders]

FileSumNum = np.array([sum(FileNums[0:i]) for i in range(len(FileFolders)+1)])


StartNum = np.where(FileSumNum<=StartFrame)[0][-1]
EndNum = np.where(FileSumNum>=EndFrame)[0][0]

for i in range(StartNum,EndNum):
    print("copy{}-->{}".format(FileFolders[i],os.path.join(SavePath,FileFolders[i].split("/")[-1])))
    shutil.copytree(FileFolders[i],os.path.join(SavePath,FileFolders[i].split("/")[-1]))

