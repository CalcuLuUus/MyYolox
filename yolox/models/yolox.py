#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Copyright (c) 2014-2021 Megvii Inc. All rights reserved.

import torch
import torch.nn as nn

from .yolo_head import YOLOXHead
from .yolo_pafpn import YOLOPAFPN


class YOLOX(nn.Module):
    """
    YOLOX model module. The module list is defined by create_yolov3_modules function.
    The network returns loss values from three YOLO layers during training
    and detection results during test.
    """

    def __init__(self, backbone=None, head=None):
        super().__init__()
        if backbone is None:
            backbone = YOLOPAFPN()
        if head is None:
            head = YOLOXHead(80)

        self.backbone = backbone

        channels = [128, 256, 512]  # yolox-s 0.5*width
        self.process_backbone = nn.ModuleList()
        for channel in channels:
            self.process_backbone.append(
                nn.Sequential(
                    nn.Conv2d(
                        in_channels=channel * 5,
                        out_channels=channel,
                        kernel_size=1
                    ),
                    nn.BatchNorm2d(channel),
                    nn.SiLU(inplace=True)
                )
            )

        self.head = head



    def forward(self, x, targets=None):
        # fpn output content features of [dark3, dark4, dark5]
        # fpn_outs = self.backbone(x)
        '''
        backbone()
        Args:
            x: tensor (3*640*640)

        Returns: (256, 80, 80) (512, 40, 40) (1024, 20, 20)
        '''
        fpn_outs = [[] for i in range(3)] # 5 * [(256, 80, 80) (512, 40, 40) (1024, 20, 20)]
        for i in range(x.shape[1]): # x.shape[1] : number of images n*[5*(3*640*640)]
            ret1, ret2, ret3 = self.backbone(x[:, i])
            fpn_outs[0].append(ret1)
            fpn_outs[1].append(ret2)
            fpn_outs[2].append(ret3)

        for i in range(3):
            fpn_outs[i] = torch.cat(fpn_outs[i], dim=1)
            fpn_outs[i] = self.process_backbone[i](fpn_outs[i])

        fpn_outs = tuple(fpn_outs)

        if self.training:
            assert targets is not None
            loss, iou_loss, conf_loss, cls_loss, l1_loss, num_fg = self.head(
                fpn_outs, targets, x
            )
            outputs = {
                "total_loss": loss,
                "iou_loss": iou_loss,
                "l1_loss": l1_loss,
                "conf_loss": conf_loss,
                "cls_loss": cls_loss,
                "num_fg": num_fg,
            }
        else:
            outputs = self.head(fpn_outs)

        return outputs
