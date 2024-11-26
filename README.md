<div align="center">
<h1>TinyViM </h1>
<h3>TinyViM: Frequency Decoupling for Tiny Hybrid Vision Mamba</h3>

[Xiaowen Ma](https://scholar.google.com/citations?hl=zh-CN&user=UXj8Q6kAAAAJ),  [Zhenliang Ni](https://scholar.google.com/citations?user=2urTmpkAAAAJ&hl=zh-CN&oi=sra), [Xinghao Chen](https://scholar.google.com/citations?user=tuGWUVIAAAAJ&hl=zh-CN&oi=ao)

Huawei Noah’s Ark Lab

 [[Paper Link]()]

</div>

## 🔥 News

- **`2024/11/27`**: **TinyViM is available at Arxiv.**

## 📷 Introduction





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

- Environment

  ```shell
  
  ```
  
  
  
- Train

  ```shell
  
  ```
  
- Test

  ```shell
  
  ```
  
- speed

  ```shell
  
  ```



## 🌟 Citation

If you are interested in our work, please consider giving a 🌟 and citing our work below. 

```

```



## 💡Acknowledgment



