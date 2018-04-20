#--coding:utf-8--
import torch.nn as nn
import torch
import math

def conv3x3(in_planes, out_planes, stride=1):
    "3x3 convolution with padding"
    return nn.Conv2d(in_planes, out_planes, kernel_size=3, stride=stride,
                     padding=1, bias=False)

#import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        # nn.Module子类的函数必须在构造函数中执行父类的构造函数
        # 下式等价于nn.Module.__init__(self)
        super(Net, self).__init__()
        
        self.conv1 = conv3x3(3, 16, 2) 
        self.conv2a1 = conv3x3(16, 16, 2)
        self.conv2a2 = conv3x3(16,8)
        self.conv2a3 = conv3x3(8,4)
        self.conv2a4 = conv3x3(4,4)
        self.conv2a_strided = conv3x3(32,32,2)
        self.conv3 = conv3x3(32,32,2)
        self.conv4 = conv3x3(32,32,1)
        self.conv6 = conv3x3(32,64,2)
        self.conv8 = conv3x3(64,64,1)
        self.conv9 = conv3x3(64,128,2)
        self.conv11 = conv3x3(128,128,1)
        self.conv11_1 = conv3x3(128,32,1)
        self.conv11_2 = conv3x3(128,32,1)
        self.conv11_3 = conv3x3(128,32,1)
        self.conv11_4 = conv3x3(32,64,1)
        self.conv11_6 = conv3x3(32,64,1)
        self.conv11_5 = conv3x3(64,128,1)
        self.conv11_7 = conv3x3(224,128,1)
        self.conv11_8 = conv3x3(128,128,1)
        self.conv11_9 = conv3x3(128,128,1)
        self.conv12 = conv3x3(128,16,1)
        self.conv13 = conv3x3(16,8,1)
        self.conv14 = nn.Conv2d(8, 5, 1,stride = 1,padding = 0, bias=False)
        self.bn1 = nn.BatchNorm2d(16)
        self.bn2 = nn.BatchNorm2d(16)
        self.bn3 = nn.BatchNorm2d(8)
        self.bn4 = nn.BatchNorm2d(4)
        self.bn5 = nn.BatchNorm2d(4)
        self.bn6 = nn.BatchNorm2d(32)
        self.bn7 = nn.BatchNorm2d(32)
        self.bn8 = nn.BatchNorm2d(32)
        self.bn9 = nn.BatchNorm2d(64)
        self.bn10 = nn.BatchNorm2d(64)
        self.bn11 = nn.BatchNorm2d(128)
        self.bn12 = nn.BatchNorm2d(128)
        self.bn13 = nn.BatchNorm2d(32)
        self.bn14 = nn.BatchNorm2d(32)
        self.bn15 = nn.BatchNorm2d(32)
        self.bn16 = nn.BatchNorm2d(64)
        self.bn17 = nn.BatchNorm2d(64)
        self.bn18 = nn.BatchNorm2d(128)
        self.bn19 = nn.BatchNorm2d(128)
        self.bn20 = nn.BatchNorm2d(128)
        self.bn21 = nn.BatchNorm2d(128)
        self.bn22 = nn.BatchNorm2d(16)
        self.bn23 = nn.BatchNorm2d(8)

    def forward(self, x): 
        x = nn.ReLU(inplace=True)(self.bn1(self.conv1(x)))
        x1 = nn.ReLU(inplace=True)(self.bn2(self.conv2a1(x)))
        x2 = nn.ReLU(inplace=True)(self.bn3(self.conv2a2(x1)))
        x3 = nn.ReLU(inplace=True)(self.bn4(self.conv2a3(x2)))
        x4 = nn.ReLU(inplace=True)(self.bn5(self.conv2a4(x3)))
        x = torch.cat([x1, x2, x3, x4], dim = 1)
        x = nn.ReLU(inplace=True)(self.bn6(self.conv2a_strided(x)))
        x = nn.ReLU(inplace=True)(self.bn7(self.conv3(x)))
        x = nn.ReLU(inplace=True)(self.bn8(self.conv4(x)))
        x = nn.ReLU(inplace=True)(self.bn9(self.conv6(x)))
        x = nn.ReLU(inplace=True)(self.bn10(self.conv8(x)))
        x = nn.ReLU(inplace=True)(self.bn11(self.conv9(x)))
        x = nn.ReLU(inplace=True)(self.bn12(self.conv11(x)))
        x1= nn.ReLU(inplace=True)(self.bn13(self.conv11_1(x)))
        x2= nn.ReLU(inplace=True)(self.bn14(self.conv11_2(x)))
        x3= nn.ReLU(inplace=True)(self.bn15(self.conv11_3(x)))
        x4= nn.ReLU(inplace=True)(self.bn16(self.conv11_4(x3)))
        x6= nn.ReLU(inplace=True)(self.bn17(self.conv11_6(x2)))
        x5= nn.ReLU(inplace=True)(self.bn18(self.conv11_5(x4)))
        x = torch.cat([x1, x5, x6], dim = 1)
        x = nn.ReLU(inplace=True)(self.bn19(self.conv11_7(x)))
        x = nn.ReLU(inplace=True)(self.bn20(self.conv11_8(x)))
        x = nn.ReLU(inplace=True)(self.bn21(self.conv11_9(x)))
        x = nn.Upsample(size=(45,53),mode='bilinear')(x)
        x = nn.ReLU(inplace=True)(self.bn22(self.conv12(x)))
        x = nn.Upsample(size=(177,209),mode='bilinear')(x)
        x = nn.ReLU(inplace=True)(self.bn23(self.conv13(x)))
        x = self.conv14(x)
        return x

#net = Net()
#print(net)