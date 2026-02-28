# Alibaba imageseg20191230Client 图像分割模型生成鞋类遮罩

基于阿里云 imageseg20191230Client 图像分割模型 的 Python 命令行工具，支持对服饰（如鞋子、衣服等）进行智能分割，并保存分割后的掩码（Mask。

## ✨ 功能特点

- 🚀 **快速分割**：支持本地图片路径和网络图片 URL。
- 👗 **多类别支持**：支持指定服饰类别（默认 shoes）。
- 🖼️ **多种输出**：支持返回掩码（mask）或边缘（edge）形式。
- 💾 **自动保存**：自动下载并保存分割结果到 `./output` 目录。

## 🛠️ 环境要求

- Python 3.6+
- 阿里云账号及 AccessKey (需开通图像分割服务)

## 📦 安装使用步骤

1. **克隆项目**
   ```bash
   git clone https://github.com/yanshizhao/shoe-mask-generator.git
   cd <项目文件夹>
   修改config.py中的ACCESS_KEY_ID和ACCESS_KEY_SECRET
   执行  python main.py <图片路径> [类别] [返回形式]
