import paddle
import paddle.nn as nn
import numpy as np
import paddle.fluid as fluid
from paddle.fluid.dygraph import to_variable#TODO
import paddle.nn.functional as F

def conv3x3(in_planes, out_planes, stride=1,type='same'):
    """type:same/downsample/downsamplex2"""
    """3x3 convolution with padding"""
    if type == 'same':
        return nn.Conv2D(in_planes, out_planes, kernel_size=3, stride=1,
                    padding='same', bias_attr=False)
    if type == 'downsample':
        return nn.Conv2D(in_planes,out_planes,kernel_size=3,stride=1,
                    padding=0,bias_attr=False)
    if type == 'downsamplex2':
        return nn.Conv2D(in_planes,out_planes,kernel_size=3,stride=2,
                    padding=1,bias_attr=False)
    # return nn.Conv2D(in_planes,out_planes,kernel_size=3,stride=2,
    #         padding=1,bias_attr=False)

def my_upsample(in_channels,out_channels,in_size,multiple,type='transposeconv',upsample_type='nearest'):
    if type == 'transposeconv':
        return nn.Conv2DTranspose(in_channels,out_channels,4,2,1)
    if type == 'upsample':
        return nn.Upsample(size=[in_size*multiple,in_size*multiple],mode=upsample_type)

class ConvBnRelu(nn.Layer):
    def __init__(self,in_planes,out_planes,type='same'):
        super().__init__()
        self.conv = conv3x3(in_planes,out_planes,stride=1,type=type)
        self.bn = nn.BatchNorm(out_planes)
    
    def forward(self,x):
        out = self.conv(x)
        out = self.bn(out)
        out = F.relu(out)

        return out

class basicblock(nn.Layer):
    def __init__(self):
        super()__init__()
        self.conv1 = 






def main():
    place = paddle.fluid.CPUPlace()
    with fluid.dygraph.guard(place):
        input_data = np.random.rand(1,3,14,14).astype(np.float32)# TODO
        print('Input data shape: ', input_data.shape)
        input_data = to_variable(input_data)# TODO
        conv = my_upsample(3,6,14,2,type='upsample')
        output_data = conv(input_data)
        output_data = output_data.numpy()# TODO
        print('Output data shape: ', output_data.shape)


if __name__ == "__main__":
    main()