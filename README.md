<div align="center">
<h1>TinyViM </h1>
<h3>TinyViM: Frequency Decoupling for Tiny Hybrid Vision Mamba</h3>

[Xiaowen Ma](https://scholar.google.com/citations?hl=zh-CN&user=UXj8Q6kAAAAJ),  [Zhenliang Ni](https://scholar.google.com/citations?user=2urTmpkAAAAJ&hl=zh-CN&oi=sra), [Xinghao Chen](https://scholar.google.com/citations?user=tuGWUVIAAAAJ&hl=zh-CN&oi=ao)

Huawei Noah’s Ark Lab

 [[Paper Link](https://arxiv.org/abs/2411.17473)]

</div>

## 🔥 News

- **`2024/11/27`**: **TinyViM is available at [Arxiv](https://arxiv.org/abs/2411.17473).**

## 📷 Introduction

<img src="fig/comp.png"  />

<img src="fig/whole.png"  />

We build a series of tiny hybrid vision Mamba called **TinyViM** by integrating mobile-friendly convolution and efficient Laplace mixer. The proposed TinyViM achieves impressive performance on several downstream tasks including image classification, semantic segmentation, object detection and instance segmentation. In particular, TinyViM outperforms Convolution, Transformer and Mamba-based models with similar scales, and the throughput is about 2-3 times higher than that of other Mamba-based models.

## 🏆 Performance

### 1️⃣ Classification

| Model |                           Type                           | Params (M) | GMACs | Throughput (im/s) | Top-1 |
| :------------: | :----------------------------------------------------------: | ---------- | :-------: | :-------: | --------- |
|   TinyViM-S   | CNN-Mamba | 5.6     |    0.9    |    2563    |   79.2   |
|  TinyViM-B  | CNN-Mamba | 11.0     |    1.5    |    1851    |   81.2   |
|   TinyViM-L   | CNN-Mamba | 31.7    |    4.7    |    843    |   83.3   |

### 2️⃣  Detection & Instance Segmentation

| Model |                           Head                           | AP-box | AP-mask |
| :------------: | :----------------------------------------------------------: | :----------: | ---------- |
|     TinyViM-B     | Mask RCNN |     42.3     | 38.7       |
| TinyViM-L | Mask RCNN |     44.5     | 40.7    |

### 3️⃣ Segmentation

|   Model   | Head | Throughput | mIoU |
| :-------: | :--: | :--------: | ---- |
| TinyViM-B | FPN  |    180     | 41.9 |
| TinyViM-L | FPN  |    111     | 44.2 |



## 📚 Use example

- **Environment**

  ```shell
  conda create --name tinyvim python=3.9.11 -y
  conda activate tinyvim
  conda install pytorch==2.0.0 torchvision==0.15.0 torchaudio==2.0.0 pytorch-cuda=11.7 -c pytorch -c nvidia
  pip install timm==0.5.4
  ```
  
- **Train**

  ```shell
  bash train.sh
  ```
  
- **Test**

  ```shell
  bash eval.sh
  ```
  
- **speed**

  ```shell
  python speed_gpu.py --model TinyViM_S --resolution 224 --batch 2048
  ```



## 🌟 Citation

If you are interested in our work, please consider giving a 🌟 and citing our work below. 

```
@misc{tinyvim,
      title={TinyViM: Frequency Decoupling for Tiny Hybrid Vision Mamba}, 
      author={Xiaowen Ma and Zhenliang Ni and Xinghao Chen},
      year={2024},
      eprint={2411.17473},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2411.17473}, 
}
```



## 💡Acknowledgment

Thanks to previous open-sourced repo: [Efficientformer](https://github.com/snap-research/EfficientFormer), [Swiftformer](https://github.com/Amshaker/SwiftFormer), [mmsegmentation](https://github.com/open-mmlab/mmsegmentation/tree/v0.30.0), [mmdetection](https://github.com/open-mmlab/mmdetection/tree/v2.28.2)

