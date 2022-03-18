# YOLOX for myself

## second version.v1 : success

- upload: 2022-3-17 10:00
- fine tunning on yolox-s.pth / 30 epoches
- add a conv between backbone and head

Average forward time: 25.69 ms, Average NMS time: 1.15 ms, Average inference time: 26.83 ms

| AP/AR                  | data                                                    |
| ---------------------- | ------------------------------------------------------- |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.273  |
| Average Precision (AP) | [ IoU=0.50   \| area=  all \| maxDets=100 ] = 0.448     |
| Average Precision (AP) | [ IoU=0.75   \| area=  all \| maxDets=100 ] = 0.289     |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.116 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.314 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.375 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 1 ] = 0.243   |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 10 ] = 0.386  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.414  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.192 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.454 |


## first version: failed

- upload: 2022-3-10 21:00
- cannot running in the no mosaic aug mode
- rewrite dataloader -> 5 * tensor of images with 1 label
- rewrite mosaic, trainer, evaluator and so on so that can work with new dataloder
- while running trainer.py with no mosaic aug mode(15 / 30 epoches), CUDA error
- error info:
  - CUDA error: device-side assert triggered
  - CUDA kernel errors might be asynchronously reported at some other API call,so the stacktrace below might be incorrect.
    For debugging consider passing CUDA_LAUNCH_BLOCKING=1.

## YOLOX yolox-s.pth eval

| AP/AR                  | data                                                    |
| ---------------------- | ------------------------------------------------------- |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.405  |
| Average Precision (AP) | [ IoU=0.50   \| area=  all \| maxDets=100 ] = 0.593     |
| Average Precision (AP) | [ IoU=0.75   \| area=  all \| maxDets=100 ] = 0.437     |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.232 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.448 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.541 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 1 ] = 0.326   |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 10 ] = 0.531  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.574  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.369 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.634 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.724 |