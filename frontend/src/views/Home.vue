<!--
 * 首页组件 - 项目演示
-->
<template>
  <div class="home-container">
    <el-card class="header-card">
      <template #header>
        <div class="card-header">
          <el-icon><HomeFilled /></el-icon>
          <span>项目演示</span>
        </div>
      </template>
      
      <div class="header-content">
        <h1>{{ appStore.title }}</h1>
        <p class="description">
          基于 PyWebView + Vue3 + FastAPI + SQLite 的桌面应用模板
        </p>

        <div class="actions">
          <el-button type="primary" size="large" @click="testConnection">
            <el-icon><Connection /></el-icon>
            测试后端连接
          </el-button>
        </div>
      </div>
    </el-card>    
  </div>
</template>

<script setup lang="ts">
import { ElMessage } from 'element-plus'
import { HomeFilled, Connection } from '@element-plus/icons-vue'
import { useAppStore } from '@/stores/app'
import { testConnection as testConnectionApi } from '@/api'

const appStore = useAppStore()

// 测试后端连接
const testConnection = async () => {
  try {
    const response = await testConnectionApi()
    ElMessage.success(`连接成功！${response.description}`)
  } catch (error) {
    ElMessage.error('连接失败，请确保后端服务已启动')
    console.error('Connection test failed:', error)
  }
}
</script>

<style scoped>
.home-container {
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 20px;
}

.header-card {
  max-width: 800px;
  margin: 0 auto 40px;
  border-radius: 12px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}

.card-header {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 18px;
  font-weight: 600;
}

.header-content {
  text-align: center;
  padding: 20px;
}

.header-content h1 {
  font-size: 2.5rem;
  margin-bottom: 16px;
  background: linear-gradient(135deg, #667eea, #764ba2);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.description {
  font-size: 1.2rem;
  color: #666;
  margin-bottom: 30px;
}

.actions {
  display: flex;
  justify-content: center;
  gap: 16px;
  flex-wrap: wrap;
}

@media (max-width: 768px) {
  .home-container {
    padding: 10px;
  }
  
  .header-content h1 {
    font-size: 2rem;
  }
  
  .description {
    font-size: 1rem;
  }
  
  .actions {
    flex-direction: column;
    align-items: center;
  }
  
  .actions .el-button {
    width: 200px;
  }
}
</style>