/**
 * 应用状态管理
 */
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useAppStore = defineStore('app', () => {
  // 应用标题
  const title = ref('PyWebView + Vue3 + FastAPI')
  
  // 加载状态
  const loading = ref(false)
  
  // 设置标题
  const setTitle = (newTitle: string) => {
    title.value = newTitle
  }
  
  // 设置加载状态
  const setLoading = (status: boolean) => {
    loading.value = status
  }
  
  return {
    title,
    loading,
    setTitle,
    setLoading
  }
})