from keras.layers import Dense,Conv2D,Dropout
import cv2 as cv
path='/home/li/zoulb/datasets/datasets/train/'

def showimage(im_name,points):
    im=cv.imread(path+im_name)
    print (points)
    cv.rectangle(im,points[0],points[1],(255, 0, 0))
    cv.imshow('im',im)
    cv.waitKey(1000)

def yoloFormatC(file):
    print ('begin convert format')
    f = open(file)

    lines = f.readlines()
    pre = '';
    pre_pic=''
    tmp=''

    results=list()
    im=None
    for str in lines:
        #print(str)
        strs=str.split()
        if(pre_pic==strs[0]):
            tmp=tmp+' '+strs[2]+','+strs[3]+','+strs[4]+','+strs[5]+','+strs[1]
            cv.rectangle(im, (int(strs[2]), int(strs[3])), (int(strs[4]), int(strs[5])), (255, 0, 0))
        else:
            if len(tmp)>10:
                #print(tmp)
                results.append(tmp+'\r')
                tmp=''
                cv.imshow('im', im)
                cv.waitKey(1000)
            tmp=strs[0]+' '+strs[2]+','+strs[3]+','+strs[4]+','+strs[5]+','+strs[1]
            pre_pic=strs[0]
            im = cv.imread(path + pre_pic)
            cv.rectangle(im, (int(strs[2]),int(strs[3])),(int(strs[4]),int(strs[5])), (255, 0, 0))

    return results




def loadDatas(file,isshow):
    f=open(file)
    pics=list()
    lines=f.readlines()
    pre='';

    for str in lines:
        print(str)
        strs=str.split()
        if isshow:
            pics.append(str)
            lrs=[(int(strs[2]),int(strs[3])),(int(strs[4]),int(strs[5]))]
            showimage(strs[0],lrs)
    return pics










if __name__ == '__main__':
    #pics=loadDatas('/home/li/zoulb/datasets/datasets/train.txt',True)
    pics = yoloFormatC('/home/li/zoulb/datasets/datasets/train.txt')
    for info in pics:
        print (info)

