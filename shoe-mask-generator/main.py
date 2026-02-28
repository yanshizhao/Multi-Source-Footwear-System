# -*- coding: utf-8 -*-
import sys
from service import ImageSegService

def main():
    # 检查参数数量
    # sys.argv[0] 是文件名，所以至少要有 1 个参数 (图片路径)
    if len(sys.argv) < 2:
        print("错误：缺少图片路径参数。")
        print("用法: python main.py <图片路径> [类别] [返回形式]")
        print("示例 1 (使用默认值): python main.py C:\\Users\\Lenovo\\Desktop\\test.jpg")
        print("示例 2 (指定类别): python main.py C:\\Users\\Lenovo\\Desktop\\test.jpg shoes")
        print("示例 3 (指定类别和返回形式): python main.py C:\\Users\\Lenovo\\Desktop\\test.jpg shoes edge")
        sys.exit(1)

    # --- 提取参数 ---

    # 1. 图片路径 (必填)
    # sys.argv[1] 是第一个参数（图片路径）
    image_path = sys.argv[1] 
    
    # 2. 服饰类别 (可选)
    # sys.argv[2] 是第二个参数（类别），如果没传，默认为 'shoes'
    cloth_class = sys.argv[2] if len(sys.argv) > 2 else 'shoes'

    # 3. 返回形式 (可选)
    # sys.argv[3] 是第三个参数（返回形式），如果没传，默认为 'mask'
    return_form = sys.argv[3] if len(sys.argv) > 3 else 'mask'

    # --- 打印传入的参数 ---
    print(f"📸 图片路径: {image_path}")
    print(f"👗 服饰类别: {cloth_class}")
    print(f"🖼️  返回形式: {return_form}")

    # --- 调用服务 ---
    service = ImageSegService()
    
    # 将 return_form 作为参数传入 segment_cloth 方法
    service.segment_cloth(image_path, cloth_class, return_form)

if __name__ == '__main__':
    main()