import numpy as np
import os
import h5py

'''
def saveNodule(noduleLabel, img, label, outDir, total_nod_count):
    x,y,z = np.nonzero(noduleLabel)
    x1 = np.min(x)-5
    x2 = np.max(x)+5
    y1 = np.min(y)-5
    y2 = np.max(y)+5
    z1 = np.min(z)-5
    z2 = np.max(z)+5
    nodVol = (img[x1:x2, y1:y2, z1:z2]).astype(np.float32)

    path_vol_save = os.path.join(outDir['testing'], '{}.h5'.format(total_nod_count))
    with h5py.File(path_vol_save, 'w') as h5f:
        h5f.create_dataset('data', data=nodVol, dtype=np.float32)
    path_label_save = os.path.join(outDir['testing'], '{}.txt'.format(total_nod_count))
    with open(path_label_save, 'w+') as f:
        f.write(str(label))
        f.close()

def saveNodule(noduleLabel, img, label, outDir, total_nod_count):
    x,y,z = np.nonzero(noduleLabel)
    if (np.max(x)-np.min(x)+20)>48:
        temp = int((np.max(x)+np.min(x))/2)
        x1 = temp-24
        x2 = temp+24
    else:
        x1 = np.min(x)-10
        x2 = np.max(x)+10

    if (np.max(y)-np.min(y)+20)>48:
        temp = int((np.max(y)+np.min(y))/2)
        y1 = temp-24
        y2 = temp+24
    else:
        y1 = np.min(y)-10
        y2 = np.max(y)+10
        
    if (np.max(z)-np.min(z)+20)>48:
        temp = int((np.max(z)+np.min(z))/2)
        z1 = temp-24
        z2 = temp+24
    else:
        z1 = np.min(z)-10
        z2 = np.max(z)+10
        
    nodVol = (img[x1:x2, y1:y2, z1:z2]).astype(np.float32)
    
    path_vol_save = os.path.join(outDir['testing'], '{}.h5'.format(total_nod_count))
    with h5py.File(path_vol_save, 'w') as h5f:
        h5f.create_dataset('data', data=nodVol, dtype=np.float32)
    path_label_save = os.path.join(outDir['testing'], '{}.txt'.format(total_nod_count))
    with open(path_label_save, 'w+') as f:
        f.write(str(label))
        f.close()
'''

def saveNodule(noduleLabel, img, label, outDir, total_nod_count):
    x,y,z = np.nonzero(noduleLabel)
        
    temp = int((np.max(x)+np.min(x))/2)
    x1 = temp-24
    x2 = temp+24

    temp = int((np.max(y)+np.min(y))/2)
    y1 = temp-24
    y2 = temp+24

    temp = int((np.max(z)+np.min(z))/2)
    z1 = temp-24
    z2 = temp+24

    nodVol = (img[x1:x2, y1:y2, z1:z2]).astype(np.float32)

    path_vol_save = os.path.join(outDir['testing'], '{}.h5'.format(total_nod_count))
    with h5py.File(path_vol_save, 'w') as h5f:
        h5f.create_dataset('data', data=nodVol, dtype=np.float32)
    path_label_save = os.path.join(outDir['testing'], '{}.txt'.format(total_nod_count))
    with open(path_label_save, 'w+') as f:
        f.write(str(label))
        f.close()
