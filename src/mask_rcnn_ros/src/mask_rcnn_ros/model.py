from torchvision.utils import make_grid
from torchvision.io import read_image
from pathlib import Path
from torchvision.utils import draw_bounding_boxes
from torchvision.models.detection import maskrcnn_resnet50_fpn, MaskRCNN_ResNet50_FPN_Weights
import torch
import numpy as np
import matplotlib.pyplot as plt

import torchvision.transforms.functional as F
from torchvision.utils import draw_segmentation_masks


plt.rcParams["savefig.bbox"] = 'tight'


def show(imgs):
    if not isinstance(imgs, list):
        imgs = [imgs]
    fig, axs = plt.subplots(ncols=len(imgs), squeeze=False)
    for i, img in enumerate(imgs):
        img = img.detach()
        img = F.to_pil_image(img)
        axs[0, i].imshow(np.asarray(img))
        axs[0, i].set(xticklabels=[], yticklabels=[], xticks=[], yticks=[])


device = torch.device('cuda')
class MaskRCNNModel(object):
    def __init__(self,filter_class=None) -> None:
        self.weights = MaskRCNN_ResNet50_FPN_Weights.DEFAULT
        self.transforms = self.weights.transforms()
        self.class_name = self.weights.meta["categories"]
        

        self.model = maskrcnn_resnet50_fpn(weights=self.weights, progress=False)
        self.model = self.model.eval()
        self.model.to(device)
        
        print('MaskRCNN initilized successfully.')
        if filter_class:
            print('Only detect object class in: {}'.format(filter_class))


    def detect(self,img,threshold=0.8,mask_threshold=0.75):
        '''
        Object detection
        Return:
            output: {boxes:tensor,labels:tensor,masks:tensor,scores:tensor}
        '''
        if type(img) is np.ndarray:
            img = torch.from_numpy(img)
            if img.shape[2] == 3:
                img = np.transpose(img,[2,0,1])
        images = self.transforms(img.unsqueeze(0)).to(device)
        
        output = self.model(images)[0]
        idx = output['scores'] > threshold

        # print(output)
        cls_labels = [self.class_name[l] for l in output['labels'][idx]]
        bbs = output['boxes'][idx]
        masks = output['masks'][idx] > mask_threshold
        # print(cls_labels)
        img_with_bb = self.draw_bb(img,bbs,cls_labels)
        img_with_mask = self.draw_mask(img,masks)
        # show(img_with_mask)
        # plt.show()
        # print(type(img_with_bb))
        return output, bbs, cls_labels, img_with_bb.detach().numpy(),img_with_mask.detach().numpy()
        

    def draw_bb(self,img,bb,labels,width=4):
        
        return draw_bounding_boxes(img, boxes=bb, labels=labels, width=width)

    def draw_mask(self,img,masks):

        return draw_segmentation_masks(img, masks.squeeze(1))


def readImg():
    dog1_int = read_image(str(Path('.') / 'images.jpeg'))
    dog_list = [dog1_int, dog1_int]

    grid = make_grid(dog_list)
    # show(grid)
    # plt.show()
    return dog1_int

def main():
    m = MaskRCNNModel()
    img = readImg()
    m.detect(img)
 
if __name__ == '__main__':
    main()