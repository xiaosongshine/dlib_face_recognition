# [深度应用]·实战掌握Dlib人脸识别开发教程
个人网站--> http://www.yansongsong.cn/

项目GitHub地址--> https://github.com/xiaosongshine/dlib_face_recognition

项目教程地址--> https://xiaosongshine.blog.csdn.net/article/details/117073052

### 1.背景介绍
Dlib是一个深度学习开源工具，基于C++开发，也支持Python开发接口，功能类似于TensorFlow与PyTorch。但是由于Dlib对于人脸特征提取支持很好，有很多训练好的人脸特征提取模型供开发者使用，所以Dlib人脸识别开发很适合做人脸项目开发。

上面所说的人脸识别开发，主要是指人脸验证，就是输入两张人脸照片，系统会对比输出0或者1，代表判断是否是同一个人。一般的人脸识别开发可以简单分为1.人脸特征建模与2.使用人脸特征模型进行验证（其实还应包括人脸对齐等,这些也可以划分到1中）。使用Dlib进行开发时，我们直接可以使用训练好的人脸特征提取模型，主要的工作就变成了如何进行人脸的验证。

人脸的验证其实就是计算相似度，同一个人的相似度就会大，不同的人就会比较小。可以采用余弦相似度或者欧式距离来计算相似度。其中余弦相似度就是计算角度，欧式距离就是指平方差。都可以用来表示两个特征的相似度（距离）。


### 2.环境搭建
安装可以参考我的这篇博客：[深度学习工具]·极简安装Dlib人脸识别库，下面说一下需要注意的点:：

此博文针对Windows10安装，其他平台可以仿照这个步骤来安装

安装Miniconda
使用conda指令来安装Dlib库，使用Miniconda与Anaconda都可以，我习惯用Miniconda，简单占用内存小。
推荐使用清华源，下载安装，选择合适的平台版本。python==3.6

安装dlib
注意一定要以管理员身份进入CMD，执行（如果是Linux Mac 就使用 sudo）
conda install -c conda-forge dlib
需要imageio 库，可以使用下述命令安装
conda install imageio
