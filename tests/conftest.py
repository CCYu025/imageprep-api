# 余振中 (Yu Chen Chung)
# tests/conftest.py
import os, sys
# 把專案根目錄（往上 1 層）插在最前面
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))