# 	YOLOX for myself

# #待做实验 Resnet finetune50 / 100#

## Sixed （finetune50）

### baseline

| AP/AR                  | DATA                                                    |
| ---------------------- | ------------------------------------------------------- |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.378  |
| Average Precision (AP) | [ IoU=0.50   \| area=  all \| maxDets=100 ] = 0.570     |
| Average Precision (AP) | [ IoU=0.75   \| area=  all \| maxDets=100 ] = 0.410     |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.211 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.429 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.503 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 1 ] = 0.312   |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 10 ] = 0.511  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.554  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.353 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.614 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.684 |

### 1 backbone

| AP/AR                  | DATA                                                    |
| ---------------------- | ------------------------------------------------------- |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.364  |
| Average Precision (AP) | [ IoU=0.50   \| area=  all \| maxDets=100 ] = 0.554     |
| Average Precision (AP) | [ IoU=0.75   \| area=  all \| maxDets=100 ] = 0.395     |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.201 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.429 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.496 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 1 ] = 0.307   |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 10 ] = 0.501  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.544  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.344 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.606 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.683 |

### 3 backbone

| AP/AR                  | DATA                                                    |
| ---------------------- | ------------------------------------------------------- |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.375  |
| Average Precision (AP) | [ IoU=0.50   \| area=  all \| maxDets=100 ] = 0.567     |
| Average Precision (AP) | [ IoU=0.75   \| area=  all \| maxDets=100 ] = 0.405     |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.210 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.425 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.501 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 1 ] = 0.311   |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 10 ] = 0.508  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.551  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.350 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.612 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.682 |



## Fifth

### Baseline

| AP/AR                  | DATA                                                    |
| ---------------------- | ------------------------------------------------------- |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= all \| maxDets=100 ] = 0.184   |
| Average Precision (AP) | [ IoU=0.50 \| area= all \| maxDets=100 ] = 0.319        |
| Average Precision (AP) | [ IoU=0.75 \| area= all \| maxDets=100 ] = 0.190        |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.092 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.203 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.243 |
| Average Recall (AR)    | [ IoU=0.50:0.95 \| area= all \| maxDets= 1 ] = 0.201    |
| Average Recall (AR)    | [ IoU=0.50:0.95 \| area= all \| maxDets= 10 ] = 0.322   |
| Average Recall (AR)    | [ IoU=0.50:0.95 \| area= all \| maxDets=100 ] = 0.342   |
| Average Recall (AR)    | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.166 |
| Average Recall (AR)    | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.370 |
| Average Recall (AR)    | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.442 |

### 1 backbone

params：d1 b2 e100

| AP/AR                  | DATA                                                    |
| ---------------------- | ------------------------------------------------------- |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.186  |
| Average Precision (AP) | [ IoU=0.50   \| area=  all \| maxDets=100 ] = 0.326     |
| Average Precision (AP) | [ IoU=0.75   \| area=  all \| maxDets=100 ] = 0.191     |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.083 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.207 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.250 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 1 ] = 0.207   |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 10 ] = 0.351  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.386  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.188 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.430 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.490 |

### 3 backbone

| AP/AR                  | DATA                                                    |
| ---------------------- | ------------------------------------------------------- |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.188  |
| Average Precision (AP) | [ IoU=0.50   \| area=  all \| maxDets=100 ] = 0.329     |
| Average Precision (AP) | [ IoU=0.75   \| area=  all \| maxDets=100 ] = 0.195     |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.088 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.208 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.251 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 1 ] = 0.206   |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 10 ] = 0.350  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.385  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.195 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.431 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.482 |

## Forth

**本次主要是对比1个backbone和3个backbone的区别**

### 3 backbone

params：device1 batchsize2 epochs30

baseline:5 gt_data, 30 epochs, mosaic, device 1, batchsize2,modify ==》 3 * process_backbone

exp: 5 process_data, 30 epochs, mosaic, device 1, batchsize2,modify ==》 3 * process_backbone

| AP/AR                  | DATA                                                    |
| ---------------------- | ------------------------------------------------------- |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.067  |
| Average Precision (AP) | [ IoU=0.50   \| area=  all \| maxDets=100 ] = 0.131     |
| Average Precision (AP) | [ IoU=0.75   \| area=  all \| maxDets=100 ] = 0.063     |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.024 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.076 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.094 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 1 ] = 0.125   |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 10 ] = 0.215  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.237  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.074 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.250 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.316 |

### 1 backbone

params：device1 batchsize2 epochs30

baseline: 5 gt_data, 30 epochs, mosaic, device 1, batchsize2,modify ==》 1 * process_backbone

| AP/AR                  | DATA                                                    |
| ---------------------- | ------------------------------------------------------- |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.068  |
| Average Precision (AP) | [ IoU=0.50   \| area=  all \| maxDets=100 ] = 0.132     |
| Average Precision (AP) | [ IoU=0.75   \| area=  all \| maxDets=100 ] = 0.064     |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.025 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.078 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.092 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 1 ] = 0.124   |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 10 ] = 0.213  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.234  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.073 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.252 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.308 |

exp:  process_data, 30 epochs, mosaic, device 1, batchsize2,modify ==》 1 * process_backbone

| AP/AR                  | DATA                                                    |
| ---------------------- | ------------------------------------------------------- |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.072  |
| Average Precision (AP) | [ IoU=0.50   \| area=  all \| maxDets=100 ] = 0.136     |
| Average Precision (AP) | [ IoU=0.75   \| area=  all \| maxDets=100 ] = 0.069     |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.026 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.080 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.102 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 1 ] = 0.129   |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 10 ] = 0.219  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.242  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.078 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.257 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.324 |



---

## 验证修改网络合理性实验

baseline0：30 epoches, mosaic aug, device 1, batchsize 2

| AP/AR                  | DATA                                                    |
| ---------------------- | ------------------------------------------------------- |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.072  |
| Average Precision (AP) | [ IoU=0.50   \| area=  all \| maxDets=100 ] = 0.138     |
| Average Precision (AP) | [ IoU=0.75   \| area=  all \| maxDets=100 ] = 0.067     |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.026 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.082 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.100 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 1 ] = 0.129   |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 10 ] = 0.220  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.241  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.076 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.257 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.316 |

baseline：30 epoches, no mosaic aug, device 1, batchsize 2

| AP/AR                  | DATA                                                    |
| ---------------------- | ------------------------------------------------------- |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.045  |
| Average Precision (AP) | [ IoU=0.50   \| area=  all \| maxDets=100 ] = 0.087     |
| Average Precision (AP) | [ IoU=0.75   \| area=  all \| maxDets=100 ] = 0.042     |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.013 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.049 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.065 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 1 ] = 0.093   |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 10 ] = 0.136  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.140  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.029 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.132 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.201 |

exp1: 5 gt_input, 30 epochs, no mosaic, device 1, batchsize 2, process_backbone only conv

| AP/AR                  | DATA                                                    |
| ---------------------- | ------------------------------------------------------- |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.042  |
| Average Precision (AP) | [ IoU=0.50   \| area=  all \| maxDets=100 ] = 0.083     |
| Average Precision (AP) | [ IoU=0.75   \| area=  all \| maxDets=100 ] = 0.038     |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.013 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.047 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.063 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 1 ] = 0.096   |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 10 ] = 0.162  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.175  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.043 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.171 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.250 |

exp2: 5 process_data, 30 epochs, no mosaic, device 1, batchsize 2

| AP/AR                  | DATA                                                    |
| ---------------------- | ------------------------------------------------------- |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.038  |
| Average Precision (AP) | [ IoU=0.50   \| area=  all \| maxDets=100 ] = 0.076     |
| Average Precision (AP) | [ IoU=0.75   \| area=  all \| maxDets=100 ] = 0.035     |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.013 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.042 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.056 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 1 ] = 0.092   |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 10 ] = 0.153  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.165  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.042 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.162 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.227 |

exp3: 5 process_data, 30 epochs, mosaic, device 1, batchsize2

| AP/AR                  | DATA                                                    |
| ---------------------- | ------------------------------------------------------- |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.057  |
| Average Precision (AP) | [ IoU=0.50   \| area=  all \| maxDets=100 ] = 0.113     |
| Average Precision (AP) | [ IoU=0.75   \| area=  all \| maxDets=100 ] = 0.054     |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.023 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.066 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.078 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 1 ] = 0.117   |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 10 ] = 0.198  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.215  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.067 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.222 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.289 |

exp4: 5 process_data, 30 epochs, mosaic, device 1, batchsize2,fix mixup bug(感觉没收敛好)

| AP/AR                  | DATA                                                    |
| ---------------------- | ------------------------------------------------------- |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.063  |
| Average Precision (AP) | [ IoU=0.50   \| area=  all \| maxDets=100 ] = 0.123     |
| Average Precision (AP) | [ IoU=0.75   \| area=  all \| maxDets=100 ] = 0.057     |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.024 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.072 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.083 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 1 ] = 0.121   |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 10 ] = 0.206  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.225  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.072 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.237 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.296 |

exp5: 5 process_data, 30 epochs, mosaic, device 1, batchsize2,modify ==》 3 * process_backbone

| AP/AR                  | DATA                                                    |
| ---------------------- | ------------------------------------------------------- |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.067  |
| Average Precision (AP) | [ IoU=0.50   \| area=  all \| maxDets=100 ] = 0.131     |
| Average Precision (AP) | [ IoU=0.75   \| area=  all \| maxDets=100 ] = 0.063     |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.024 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.076 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.094 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 1 ] = 0.125   |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 10 ] = 0.215  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.237  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.074 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.250 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.316 |

exp6：5 process_data, 30 epochs, mosaic, device 1, batchsize2,modify ==》 1 * process_backbone

| AP/AR                  | DATA                                                    |
| ---------------------- | ------------------------------------------------------- |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.072  |
| Average Precision (AP) | [ IoU=0.50   \| area=  all \| maxDets=100 ] = 0.136     |
| Average Precision (AP) | [ IoU=0.75   \| area=  all \| maxDets=100 ] = 0.069     |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.026 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.080 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.102 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 1 ] = 0.129   |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 10 ] = 0.219  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.242  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.078 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.257 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.324 |

---

## EXP

### expv2

- batch size:2
- device:1
- yolox-s
- epochs:100
- no aug:15
- no shuffle +  mosaic aug

| AP/AR                  | DATA                                                    |
| ---------------------- | ------------------------------------------------------- |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.153  |
| Average Precision (AP) | [ IoU=0.50   \| area=  all \| maxDets=100 ] = 0.270     |
| Average Precision (AP) | [ IoU=0.75   \| area=  all \| maxDets=100 ] = 0.156     |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.063 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.171 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.210 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 1 ] = 0.192   |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 10 ] = 0.319  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.347  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.150 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.381 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.453 |

### expv1

- batch size:2
- device:1
- yolox-s
- epochs:100
- no aug:15
- shuffle mosaic aug

| AP/AR                  | DATA                                                    |
| ---------------------- | ------------------------------------------------------- |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.160  |
| Average Precision (AP) | [ IoU=0.50   \| area=  all \| maxDets=100 ] = 0.278     |
| Average Precision (AP) | [ IoU=0.75   \| area=  all \| maxDets=100 ] = 0.165     |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.068 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.177 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.219 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 1 ] = 0.194   |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 10 ] = 0.326  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.354  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.159 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.390 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.464 |

### baseline

- batch size:2
- device:1
- yolox-s
- epochs:100
- no aug:15
- 2022-03-21 22:00:44 - 2022-03-22 17:32:05

| AP/AR                  | DATA                                                    |
| ---------------------- | ------------------------------------------------------- |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= all \| maxDets=100 ] = 0.184   |
| Average Precision (AP) | [ IoU=0.50 \| area= all \| maxDets=100 ] = 0.319        |
| Average Precision (AP) | [ IoU=0.75 \| area= all \| maxDets=100 ] = 0.190        |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.092 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.203 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.243 |
| Average Recall (AR)    | [ IoU=0.50:0.95 \| area= all \| maxDets= 1 ] = 0.201    |
| Average Recall (AR)    | [ IoU=0.50:0.95 \| area= all \| maxDets= 10 ] = 0.322   |
| Average Recall (AR)    | [ IoU=0.50:0.95 \| area= all \| maxDets=100 ] = 0.342   |
| Average Recall (AR)    | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.166 |
| Average Recall (AR)    | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.370 |
| Average Recall (AR)    | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.442 |

## Third version.v3

- upload: 2022-3-21 6:00
- fine tunning on yolox-s.pth / 30 epoches
- add a conv between backbone and head
- backbone: requires_grad :False
- torch.optim.SGD params: process_backbone and head
- new conv: structure like resnet -> 4 image backbone + 1 gt backbone
- mosaic aug：on

| AP/AR                  | DATA                                                    |
| ---------------------- | ------------------------------------------------------- |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.351  |
| Average Precision (AP) | [ IoU=0.50   \| area=  all \| maxDets=100 ] = 0.536     |
| Average Precision (AP) | [ IoU=0.75   \| area=  all \| maxDets=100 ] = 0.380     |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.182 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.401 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.466 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 1 ] = 0.299   |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 10 ] = 0.485  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.527  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.316 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.587 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.655 |

## Third version.v2

- upload: 2022-3-20 9:00
- fine tunning on yolox-s.pth / 30 epoches
- add a conv between backbone and head
- backbone: requires_grad :False
- torch.optim.SGD params: process_backbone and head
- new conv: structure like resnet -> 4 image backbone + 1 gt backbone
- mosaic aug：on + shuffle images

| AP/AR                  | DATA                                                    |
| ---------------------- | ------------------------------------------------------- |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.349  |
| Average Precision (AP) | [ IoU=0.50   \| area=  all \| maxDets=100 ] = 0.534     |
| Average Precision (AP) | [ IoU=0.75   \| area=  all \| maxDets=100 ] = 0.377     |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.182 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.400 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.465 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 1 ] = 0.298   |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 10 ] = 0.483  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.525  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.322 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.584 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.653 |

## Third version.v1

- upload: 2022-3-20 9:00
- fine tunning on yolox-s.pth / 30 epoches
- add a conv between backbone and head
- backbone: requires_grad :False
- torch.optim.SGD params: process_backbone and head
- new conv: structure like resnet -> 4 image backbone + 1 gt backbone

| AP/AR                  | DATA                                                    |
| ---------------------- | ------------------------------------------------------- |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.353  |
| Average Precision (AP) | [ IoU=0.50   \| area=  all \| maxDets=100 ] = 0.539     |
| Average Precision (AP) | [ IoU=0.75   \| area=  all \| maxDets=100 ] = 0.382     |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.185 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.403 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.470 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 1 ] = 0.300   |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 10 ] = 0.487  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.529  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.322 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.587 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.656 |

## second version.v3

- upload: 2022-3-19 9:00
- fine tunning on yolox-s.pth / 30 epoches
- add a conv between backbone and head
- backbone: requires_grad :False
- torch.optim.SGD params: process_backbone and head

Average forward time: 18.94 ms, Average NMS time: 1.32 ms, Average inference time: 20.26 ms

| AP/AR                  | data                                                    |
| ---------------------- | ------------------------------------------------------- |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.348  |
| Average Precision (AP) | [ IoU=0.50   \| area=  all \| maxDets=100 ] = 0.536     |
| Average Precision (AP) | [ IoU=0.75   \| area=  all \| maxDets=100 ] = 0.377     |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.183 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.397 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.460 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 1 ] = 0.298   |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 10 ] = 0.482  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.524  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.330 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.585 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.647 |

## second version.v2

- upload: 2022-3-18 9:00
- fine tunning on yolox-s.pth / 30 epoches
- add a conv between backbone and head
- backbone: requires_grad :False
- torch.optim.SGD params: only process_backbone

Average forward time: 18.66 ms, Average NMS time: 1.49 ms, Average inference time: 20.15 ms

| AP/AR                  | data                                                    |
| ---------------------- | ------------------------------------------------------- |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.354  |
| Average Precision (AP) | [ IoU=0.50   \| area=  all \| maxDets=100 ] = 0.541     |
| Average Precision (AP) | [ IoU=0.75   \| area=  all \| maxDets=100 ] = 0.380     |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.186 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.400 |
| Average Precision (AP) | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.472 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 1 ] = 0.301   |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets= 10 ] = 0.490  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=  all \| maxDets=100 ] = 0.532  |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= small \| maxDets=100 ] = 0.327 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area=medium \| maxDets=100 ] = 0.590 |
| Average Recall   (AR)  | [ IoU=0.50:0.95 \| area= large \| maxDets=100 ] = 0.669 |

## second version.v1

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