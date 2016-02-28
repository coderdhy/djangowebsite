from django.test import TestCase
import os

# 获取当前脚本文件路径
print('\r\n')
print('\r\n')
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
# 获取当前路径的上级目录
print(os.path.dirname(__file__))
print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
print(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
UPLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'public', 'uploads')
print(UPLOAD_DIR)


print('\r\n')
