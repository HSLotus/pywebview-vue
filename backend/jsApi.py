"""
PyWebView与前端交互的API接口
"""
import webview
import threading
import uvicorn
from backend.api import app as fastapi_app

class Api:
    """PyWebView API类"""
    
    def __init__(self):
        self._window = None
        self._fastapi_server = None
        
    def set_window(self, window):
        """设置窗口引用"""
        self._window = window
        
    def start_fastapi_server(self):
        """启动FastAPI服务器"""
        def run_server():
            uvicorn.run(
                fastapi_app, 
                host="127.0.0.1", 
                port=8000,
                log_level="info"
            )
        
        # 在新线程中启动FastAPI服务器
        server_thread = threading.Thread(target=run_server, daemon=True)
        server_thread.start()
        
    def get_app_info(self):
        """获取应用信息"""
        return {
            "name": "PyWebView + Vue3 + FastAPI",
            "version": "1.0.0",
            "description": "基于PyWebView、Vue3和FastAPI的桌面应用框架",
            "api_url": "http://127.0.0.1:8000"
        }
        
    def show_message(self, message: str):
        """显示消息"""
        if self._window:
            self._window.evaluate_js(f'console.log("来自Python的消息: {message}")')
        return f"消息已发送: {message}"