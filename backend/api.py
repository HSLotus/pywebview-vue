"""
FastAPI后端应用
"""
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3
import os
from typing import List, Optional

# 创建FastAPI应用
app = FastAPI(
    title="PyWebView FastAPI Backend",
    description="基于FastAPI的后端API服务",
    version="1.0.0"
)

# 添加CORS中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 数据库文件路径
DB_PATH = "app.db"

# Pydantic模型
class MessageModel(BaseModel):
    id: Optional[int] = None
    content: str
    timestamp: Optional[str] = None

class ResponseModel(BaseModel):
    success: bool
    message: str
    data: Optional[dict] = None

# 初始化数据库
def init_database():
    """初始化SQLite数据库"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # 创建消息表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

# 启动时初始化数据库
@app.on_event("startup")
async def startup_event():
    init_database()

# API路由
@app.get("/")
async def root():
    """根路径"""
    return {
        "message": "PyWebView FastAPI Backend is running!",
        "docs_url": "/docs",
        "redoc_url": "/redoc"
    }

@app.get("/api/info")
async def get_info():
    """获取应用信息"""
    return {
        "version": "1.0.0",
        "description": "PyWebView + Vue3 + FastAPI 桌面应用",
        "environment": "pywebview+vue3+fastapi",
        "database": "SQLite"
    }

@app.get("/api/messages", response_model=List[MessageModel])
async def get_messages():
    """获取所有消息"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, content, timestamp FROM messages ORDER BY timestamp DESC")
        rows = cursor.fetchall()
        
        messages = []
        for row in rows:
            messages.append({
                "id": row[0],
                "content": row[1],
                "timestamp": row[2]
            })
        
        conn.close()
        return messages
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/messages", response_model=ResponseModel)
async def create_message(message: MessageModel):
    """创建新消息"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO messages (content) VALUES (?)",
            (message.content,)
        )
        
        conn.commit()
        message_id = cursor.lastrowid
        conn.close()
        
        return ResponseModel(
            success=True,
            message="消息创建成功",
            data={"id": message_id}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/messages/{message_id}", response_model=ResponseModel)
async def delete_message(message_id: int):
    """删除消息"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM messages WHERE id = ?", (message_id,))
        
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="消息不存在")
        
        conn.commit()
        conn.close()
        
        return ResponseModel(
            success=True,
            message="消息删除成功"
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)