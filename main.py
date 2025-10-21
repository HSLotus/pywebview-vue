"""
PyWebView + Vue3 + FastAPI 桌面应用主入口
"""
import webview
import sys
import os
from backend.jsApi import Api

def get_frontend_url():
    """获取前端URL"""
    if getattr(sys, "frozen", False):
        # 如果是打包后的可执行文件
        base_path = sys._MEIPASS
        html_file_path = os.path.join(base_path, "dist", "index.html")
        return html_file_path
    else:
        # 开发环境，使用Vite开发服务器
        return "http://localhost:5173"

def main():
    """主函数"""
    # 配置PyWebView中文本地化
    chinese_localization = {
        "global.quitConfirmation": "确定要关闭应用程序吗？",
    }
    
    # 创建API实例
    api = Api()
    
    # 启动FastAPI服务器
    api.start_fastapi_server()
    
    # 创建PyWebView窗口
    window = webview.create_window(
        title="PyWebView + Vue3 + FastAPI",
        url=get_frontend_url(),
        width=1200,
        height=800,
        min_size=(800, 600),
        js_api=api,
        resizable=True,
        shadow=True,
        on_top=False
    )
    
    # 设置窗口引用
    api.set_window(window)
    
    # 启动PyWebView
    webview.start(
        localization=chinese_localization,
        debug=True  # 设为True启用开发者工具，可以打开控制台
    )

if __name__ == "__main__":
    main()