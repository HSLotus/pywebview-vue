import axios from 'axios'
import { ElMessage } from 'element-plus'
import { useAppStore } from '@/stores/app'

// 创建 axios 实例
const service = axios.create({
  baseURL: 'http://127.0.0.1:8000/api', // API 的 base_url
  timeout: 5000 // 请求超时时间
})

// 请求拦截器
service.interceptors.request.use(
  config => {
    const appStore = useAppStore()
    appStore.setLoading(true)
    return config
  },
  error => {
    console.error('Request Error:', error) // for debug
    return Promise.reject(error)
  }
)

// 响应拦截器
service.interceptors.response.use(
  response => {
    const appStore = useAppStore()
    appStore.setLoading(false)
    return response.data
  },
  error => {
    const appStore = useAppStore()
    appStore.setLoading(false)
    ElMessage({
      message: error.message,
      type: 'error',
      duration: 5 * 1000
    })
    return Promise.reject(error)
  }
)

export default service