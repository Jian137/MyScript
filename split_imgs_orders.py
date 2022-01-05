import cv2
import os
import shutil
from glob import glob

DstPath = r".\wzt\*.png"
SavePath = r".\wzt1"
os.chdir(r"F:\Onedrive\OneDrive - business\超分辨率\laopianxiufu")
imgs = sorted(glob(DstPath))

if __name__ == "__main__":
    Num = 0
    i = 0
    start = 0
    end = 0
    while True:
        if i >= len(imgs):
            cv2.destroyAllWindows()
            break
        img = cv2.imread(imgs[i])
        cv2.imshow("image", img)
        print("show {}/{} img".format(i,len(imgs)))
        k = cv2.waitKey()
        if i == 0 and k == ord('a'):
            continue
        elif i == len(imgs) - 1 and k == ord('d'):
            continue
        elif k == ord('a'):
            i = i - 1
            continue
        elif k == ord('d'):
            i = i + 1
        elif k == ord('s'):
            end = i
            OrdFolder = os.path.join(SavePath,str(Num).zfill(4))
            Num=Num+1
            if not os.path.exists(OrdFolder):
                os.mkdir(OrdFolder)
            for l in range(start,end+1):
                shutil.copy(imgs[l],os.path.join(OrdFolder,str(l).zfill(4)+".png"))
            start = end+1
            i = i+1
        elif k == ord('q'):
            cv2.destroyAllWindows()
            break
