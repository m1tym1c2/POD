_base_ = 'mmdetection\configs\\faster_rcnn\\faster_rcnn_r50_fpn_1x_coco.py'
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes = 4)))
dataset_type = 'COCODataset'
evaluation = dict(interval = 1, metric = 'bbox', save_best = 'bbox_mAP')
classes = ('caption', 'figure', 'table', 'formula')