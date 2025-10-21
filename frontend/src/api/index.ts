import request from '@/utils/request'

// 测试连接
export function testConnection() {
  return request({
    url: '/info',
    method: 'get'
  })
}