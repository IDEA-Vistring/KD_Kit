# -*- coding: utf-8 -*-

import torch
import argparse
from collections import OrderedDict

def change_model(args):
    dis_model = torch.load(args.dis_path)
    all_name = []
    for name, v in dis_model["state_dict"].items():
        if name.startswith("student."):
            all_name.append((name[8:], v))
        else:
            continue
    state_dict = OrderedDict(all_name)
    dis_model['state_dict'] = state_dict
    dis_model.pop('optimizer')
    torch.save(dis_model, args.output_path) 

           
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Transfer CKPT')
    parser.add_argument('--dis_path', type=str, default='work_dirs/res34_distill_res18_img/latest.pth', 
                        metavar='N',help='dis_model path')
    parser.add_argument('--output_path', type=str, default='res18_new.pth',metavar='N', 
                        help = 'output path')
    args = parser.parse_args()
    change_model(args)
