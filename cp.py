import os
'''
check kinds of subtrainset
'''
# import json
# from tqdm import trange
# annfile = "datasets/COCO/annotations/instances_train2017-orig.json"
# namefile = "datasets/COCO/names.txt"
# namelst = {}
# jsonlst = {}
# with open(namefile, 'r') as f:
#     names = f.readlines()
#     for name in names:
#         namelst[name[:-1]] = 1
#
# with open(annfile, 'r') as f:
#     jsonlst = json.load(f)
#
# jsonlst['subimages'] = []
# jsonlst['subanno'] = []
#
# for i in trange(len(jsonlst['images'])):
#     if namelst.get(jsonlst['images'][i]['file_name'], 0):
#         jsonlst['subimages'].append(jsonlst['images'][i])
#
# cnt = {}
#
# for i in trange(len(jsonlst['annotations'])):
#     if namelst.get(str(jsonlst['annotations'][i]['image_id']).zfill(12)+'.jpg', 0):
#         jsonlst['subanno'].append(jsonlst['annotations'][i])
#         cnt[jsonlst['subanno'][-1]['category_id']] = 1
#
# for x in jsonlst:
#     print(x, len(jsonlst[x]))
#
# print("-----------")
#
#
#
# subjsonlst = {}
# for x in jsonlst:
#     if x == 'subimages' or x == 'subanno':
#         continue
#     elif x == 'images':
#         subjsonlst[x] = jsonlst['subimages']
#     elif x == 'annotations':
#         subjsonlst[x] = jsonlst['subanno']
#     else:
#         subjsonlst[x] = jsonlst[x]
#     print(x, len(subjsonlst[x]))
#
# print(len(cnt), cnt)
#
# with open("instances_train2017.json", 'w') as f:
#     f.write(json.dumps(subjsonlst))



'''
check subtrainset
'''
# print("RUNNING")
# from tqdm import trange
# dir = './datasets/COCO/val2017'
# filenames = os.listdir(dir)
#
# need_img_names = ["gt_input.png"] + ["retrain_structure_" + "{:.2f}".format(0.2 + i * 0.4) + ".png" for i in range(0, 4)]
# need_img_names.sort()
# errors = []
# for i in trange(len(filenames)):
#     filename = filenames[i]
#     filedir = os.path.join(dir, filename)
#     all_image_names = os.listdir(filedir)
#     all_image_names.sort()
#     if all_image_names != need_img_names:
#         print(filedir)



'''
delete useless images
'''
# dir = './datasets/COCO/val2017'
# filenames = os.listdir(dir)
#
# need_img_names = ["gt_input.png"] + ["retrain_structure_" + "{:.2f}".format(0.2 + i * 0.4) + ".png" for i in range(0, 4)]
# errors = []
# for i in range(len(filenames)):
#     filename = filenames[i]
#     filedir = os.path.join(dir, filename)
#     all_image_names = os.listdir(filedir)
#     for img_name in all_image_names:
#         if img_name not in need_img_names:
#             target = os.path.join(filedir, img_name)
#             if os.path.exists(target):
#                 print("os remove {}\t{} / {}".format(target, i, len(filenames)))
#                 os.remove(target)
#             else:
#                 print("{} not exist".format(target))
#                 with open("notExist.txt", "a+") as f:
#                     f.write("{} not exist".format(target))

'''
create subtrainset annotation
'''
# import json
# from tqdm import trange
# annfile = "/home/tuf/Calculus/yolox/datasets/COCO/annotations/instances_train2017.json"
# namefile = "/home/tuf/Calculus/yolox/datasets/COCO/names.txt"
# namelst = {}
# jsonlst = {}
# with open(namefile, 'r') as f:
#     names = f.readlines()
#     for name in names:
#         namelst[name[:-1]] = 1
#
# with open(annfile, 'r') as f:
#     jsonlst = json.load(f)
#
# jsonlst['subimages'] = []
#
# for i in trange(len(jsonlst['images'])):
#     if namelst.get(jsonlst['images'][i]['file_name'], 0):
#         jsonlst['subimages'].append(jsonlst['images'][i])
#
# for x in jsonlst:
#     print(x, len(jsonlst[x]))
#
# subjsonlst = {}
# for x in jsonlst:
#     if x == 'subimages':
#         continue
#     elif x == 'images':
#         subjsonlst[x] = jsonlst['subimages']
#     else:
#         subjsonlst[x] = jsonlst[x]
#     print(x, len(subjsonlst[x]))
#
# with open("/home/tuf/Calculus/yolox/datasets/COCO/annotations/instances_subtrain2017.json", 'w') as f:
#     f.write(json.dumps(subjsonlst))


'''
check introsmooth results
'''
# import cv2
# from tqdm import trange
# dir = './datasets/COCO/train2017smo'
# filenames = os.listdir(dir)
#
# img_names = ["gt_input.png"] + ["retrain_structure_" + "{:.2f}".format(0.2 + i * 0.4) + ".png" for i in range(0, 4)]
# errors = []
# for i in trange(len(filenames)):
#     filename = filenames[i]
#     filedir = os.path.join(dir, filename)
#     for img_name in img_names:
#         target = os.path.join(filedir, img_name)
#         image = cv2.imread(target)
#         # print("{} : ".format(target), end='')
#         try:
#             num = image.shape
#             # print("{}\t{} / {}".format(image.shape, i+1, len(filenames)))
#         except AttributeError:
#             print(target)
#             errors.append(target)
# print(len(errors))
# for error in errors:
#     print(error)



'''
check coco
'''
# import numpy as np
# from pycocotools.coco import COCO
# annfile = "datasets/COCO/annotations/instances_train2017.json"
# print(annfile)
# coco = COCO(annfile)
#
# catids = coco.getCatIds()
# print(catids)
#
# imgIds = coco.getImgIds()
# print(len(imgIds))
# print(imgIds[:10])
# img = coco.loadImgs(imgIds)
# print(len(img))


'''
move subtrainset
'''
# from tqdm import trange
# import shutil
# srcdir = os.getcwd() + "/datasets/COCO"
# filename = os.listdir(srcdir)
# targetdir = os.getcwd() + "/datasets/COCO/train2017"
# if not os.path.isdir(targetdir):
#     os.makedirs(targetdir)
# filename.sort()
# for i in trange(len(filename)):
#     if(filename[i][-3:] == "jpg"):
#         shutil.move(srcdir + '/' + filename[i], targetdir)

