# -*- coding: utf-8 -*-
import os
import json
import uuid
from io import BytesIO
import urllib.request
from alibabacloud_imageseg20191230 import models as imageseg_20191230_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_imageseg20191230.client import Client as imageseg20191230Client
from client import create_client

# ---下载图片的函数 ---
def download_image(url: str, save_dir: str = "./output", filename: str = None):
    """
    下载图片并保存到本地
    :param url: 图片的URL
    :param save_dir: 保存的目录
    :param filename: 保存的文件名 (如果为None，则自动生成)
    :return: 本地保存路径
    """
    try:
        # 创建目录
        os.makedirs(save_dir, exist_ok=True)
        
        # 如果没有指定文件名，从 URL 中提取或生成
        if filename is None:
            # 尝试从 URL 提取文件名，或者用 UUID 防止冲突
            ext = os.path.splitext(url)[1]
            if not ext:
                ext = '.png'
            filename = f"seg_result_{uuid.uuid4()}{ext}"
        
        save_path = os.path.join(save_dir, filename)
        
        # 下载文件
        print(f"⬇️ 正在下载: {url}")
        urllib.request.urlretrieve(url, save_path)
        print(f"✅ 下载完成: {save_path}")
        return save_path
        
    except Exception as e:
        print(f"❌ 下载失败 {url}: {str(e)}")
        return None

class ImageSegService:
    def __init__(self):
        self.client = create_client()

    def segment_cloth(self, image_path_or_url: str, cloth_class: str = 'shoes', return_form: str = 'mask'):
        """
        执行服饰分割，并支持传入 return_form 参数
        """
        print(f"📂 处理文件: {image_path_or_url}")
        print(f"👗 类别: {cloth_class} | 格式: {return_form}")

        # 检查文件是否存在（如果是本地路径）
        if not image_path_or_url.startswith('http') and not os.path.exists(image_path_or_url):
            raise FileNotFoundError(f"错误：文件 {image_path_or_url} 不存在。")

        # --- 构建 Advance 请求 ---
        request = imageseg_20191230_models.SegmentClothAdvanceRequest()
        
        # 判断是本地文件还是网络URL
        if image_path_or_url.startswith('http'):
            request.image_url = image_path_or_url
        else:
            # 读取文件流
            with open(image_path_or_url, 'rb') as f:
                request.image_urlobject = BytesIO(f.read())
        
        # 设置核心参数
        request.out_mode = 1
        request.cloth_class = [cloth_class]
        request.return_form = return_form  # <--- 关键：接收外部传入的参数

        # --- 调用 API ---
        runtime = util_models.RuntimeOptions()
        try:
            response = self.client.segment_cloth_advance(request, runtime)
            result_dict = response.body.to_map() if hasattr(response.body, 'to_map') else str(response.body)
            
            # --- 解析并下载结果 ---
            print("\n" + "="*50)
            print("API 调用成功，正在处理返回结果...")
            
            # 遍历 Elements 列表
            for idx, element in enumerate(result_dict['Data']['Elements']):
                image_url = None
                suffix = f"_{idx}"
                
                # 情况1：直接是 ImageURL
                if 'ImageURL' in element:
                    image_url = element['ImageURL']
                    suffix += "_full"
                
                # 情况2：是 ClassUrl 字典 (如 shoes)
                elif 'ClassUrl' in element:
                    class_dict = element['ClassUrl']
                    # 假设只有一个类别，取它的名字和链接
                    class_name = list(class_dict.keys())[0]
                    image_url = class_dict[class_name]
                    suffix = f"_{class_name}"
                
                # 执行下载
                if image_url:
                    # 生成文件名，包含原图名和类别信息
                    base_name = os.path.splitext(os.path.basename(image_path_or_url))[0]
                    # 如果是URL，用UUID作为名字
                    if image_path_or_url.startswith('http'):
                        base_name = "web_image"
                    filename = f"{base_name}_mask{suffix}.png"
                    download_image(image_url, "./output", filename)
            
            print("="*50)
            return result_dict
            
        except Exception as error:
            print(f"❌ API 调用失败: {str(error)}")
            if hasattr(error, 'data') and error.data:
                print(f"💡 诊断建议: {error.data.get('Recommend')}")
            return None