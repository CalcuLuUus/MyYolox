# YOLOX for myself

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