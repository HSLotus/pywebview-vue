# PyWebView + Vue3 + FastAPI

基于 PyWebView、Vue3、FastAPI 构建的模板demo


## 项目结构

```
├── backend/                # 后端代码
│   ├── api.py              # FastAPI 应用和 API 接口
│   └── jsApi.py            # PyWebView 与前端交互接口
├── frontend/               # 前端代码
│   ├── public              # 公共资源
│   └── src/
│      ├── App.vue          # 根组件
│      ├── api/             # API 接口封装
│      ├── assets/          # 静态资源
│      ├── components/      # Vue 组件
│      ├── composables/     # 组合式函数
│      ├── router/          # 路由配置
│      ├── stores/          # Pinia 状态管理
│      ├── utils/           # 工具函数
│      ├── views/           # 页面组件
│      └── main.ts          # 应用入口
├── main.py                 # 应用主入口
├── package.json            # 前端依赖配置
├── requirements.txt        # Python 依赖
├── vite.config.ts          # Vite 配置
└── tsconfig.json           # TypeScript 配置
```

## 测试环境启动

### 1. 安装依赖

作者环境：Windows 11
nodejs 版本：22.16.0
python 版本：3.13.5

```bash
# 安装后端依赖
pip install -r requirements.txt
# 安装前端依赖
pnpm i
```

### 2. 开发模式运行

```bash
# 启动前端开发服务器
pnpm dev
# 启动桌面应用
pnpm dev:py
#或
python main.py
```

## 打包

### 1. 构建前端
```bash
pnpm build
```

### 2. 构筑后端
```bash
# pipenv 非必须，但是不使用虚拟环境会导致打包大量本地无用依赖
pnpm install pipenv
pipenv install -r requirements.txt
pipenv shell  # 激活虚拟环境
pnpm build:py # 打包后端

# 不使用虚拟环境打包
pyinstaller --onefile --add-data "webdist;dist" --icon "webdist/favicon.ico" --windowed main.py
```