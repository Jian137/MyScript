import torch
import os
import cv2
import diffjpeg
import numpy as np

jpeger = diffjpeg.DiffJPEG(differentiable=False)

def jpegcompress(imgpath,savepath):
    img = cv2.imread(imgpath)
    cv2.imshow("1", img)
    cv2.waitKey(0)
    img = img/255.0
    img = torch.from_numpy(np.transpose(img[:,:,[2,1,0]],(2,0,1))).float()

    img = img.unsqueeze(0)

    jpeg_p = img.new_zeros(img.size(0)).uniform_(30,95)
    out = torch.clamp(img, 0, 1)
    out = jpeger(out,quality = jpeg_p)
    out = out.squeeze()
    input_tensor = out.mul_(255).add_(0.5).clamp_(0, 255).permute(1, 2, 0).type(torch.uint8).numpy()

    input_tensor = cv2.cvtColor(input_tensor, cv2.COLOR_RGB2BGR)

    """    
    out = torch.clamp((out*255.0).round(), 0, 255)
    out = out.squeeze().float().detach().numpy()
    out = np.transpose(out[[2,1,0],:,:],(1,2,0))
    out = out.round()
    """

    cv2.imwrite(savepath,input_tensor)


if __name__=="__main__":
    jpegcompress("")

