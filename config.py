icdar17_mlt_img_dir = 'images/'
icdar17_mlt_gt_dir = 'annotations/'

anchor_scale = 16
IOU_NEGATIVE = 0.3
IOU_POSITIVE = 0.7
IOU_SELECT = 0.7

RPN_POSITIVE_NUM = 150
RPN_TOTAL_NUM = 300

# bgr can find from  here: https://github.com/fchollet/deep-learning-models/blob/master/imagenet_utils.py
IMAGE_MEAN = [123.68, 116.779, 103.939]
OHEM = True

pretrained_weights = 'checkpoints/CTPN.pth'
num_workers = 2

checkpoints_dir = './checkpoints'
