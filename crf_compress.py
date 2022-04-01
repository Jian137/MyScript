import os
import os.path as osp
from multiprocessing.dummy import Pool as ThreadPool

def process(file):
    # img_name = osp.join(submit,osp.basename(file))
    # save_path = osp.joion(submit,osp.basename()
    img_name = ""
    save_path = ""
    os.system("ffmpeg -i "+file+ " -c:v libx264 -crf 10 -pix_fmt yuv444p -vf scale=iw/2:ih/2 "+save_path+ ' -y -vsync 0')
    os.system("ffmpeg -i "+save_path+' -vsync 0  -f image2 -y '+img_name)

    if os.path.exists(save_path):
        os.unlink(save_path)

if __name__=="__main__":
    sourcedir = ''
    submit = ' '
    os.makedirs(submit,exist_ok=True)

    files = ''
    pool = ThreadPool(8)

    pool.map(process,files)
    pool.close()
    pool.join()
