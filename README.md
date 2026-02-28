# 多源融合鞋靴类电商详情页生成系统 (Multi-Source Footwear System)

本系统整合了四个核心模块，提供从图像处理到详情页生成的全流程解决方案。

## 📦 子模块介绍

### 1. 🎭 鞋子掩码生成器 (`shoe-mask-generator`)
基于阿里云imageseg20191230Client 图像分割模型生成鞋靴遮罩图。
- **功能**: 自动识别鞋子并生成分割掩码。
- **适用**: 需要去除背景或提取鞋子主体的场景。
- [👉 查看详细文档](./shoe-mask-generator/README.md)

### 2. 📐 批量图片缩放 (`batch-resize-images`)
智能调整图片尺寸比例，保持内容不变。
- **功能**: 支持 3:4, 9:16 等电商常用比例。
- **适用**: 统一素材库图片规格。
- [👉 查看详细文档](./batch-resize-images/README.md)

### 3. ✨ 融合详情页生成 (`fusion-footwear-detail-page-batch-gen`)
基于火山引擎视觉模型 + nano banana pro 模型 + 预置信息 融合的详情页生成工具。
- **功能**: 两种生成模式：自动设计详情页分屏详情 和 本地模板库分页设计详情，调用 Nano Banana模型生成创意详情页。
- **适用**: 快速生成高质量营销素材。
- [👉 查看详细文档](./fusion-footwear-detail-page-batch-gen/README.md)

### 4. 🔄 详情页批量复刻 (`shoe-detail-page-batch-raplicate`)
针对鞋靴类电商详情页的自动化复刻流程。建立专属详情页模板库。
- **功能**: 基于火山引擎视觉模型，基于参考图，仅通过「背景、构图、模特、光影 / 布光」视觉元素，客观精准推导并明确原图对鞋子设计 / 细节的展示逻辑、核心维度与视线落点，逐张独立拆解为一段式精简总结，拆解结果直接落地服务于鞋类电商视觉复刻、详情页 / 主图 / 拍摄的视觉布局。
- **适用**: 创建品牌专属详情页模板库，针对不同类型的产品创建不同视觉特征的详情页。
- [👉 查看详细文档](./shoe-detail-page-batch-raplicate/README.md)

## 🚀 快速开始

每个子模块都是独立运行的 Python 项目。请进入对应的文件夹，按照其内部的 `README.md` 进行安装和配置。

```bash
# 示例：运行鞋子掩码生成器
cd shoe-mask-generator
pip install -r requirements.txt
修改config.py中的配置参数
执行  python main.py <图片路径> [类别] [返回形式]

## 注意
每个子模块可能需要不同的 API Key (阿里云 、火山引擎、api聚合网站)，请分别配置。
所有子模块建议使用 Python 3.12。