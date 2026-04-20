# | 📊 文本统计分析 | 文本分析与统计 | 中英文统计、常用词、行分析 |
HTML 工具箱

<p align="center">
  <img src="https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white" alt="CSS3">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/tangguo95/html-tools?style=flat-square" alt="Stars">
  <img src="https://img.shields.io/github/commit-activity/m/tangguo95/html-tools?style=flat-square" alt="Commits">
  <img src="https://img.shields.io/github/last-commit/tangguo95/html-tools?style=flat-square" alt="Last Commit">
</p>

<p align="center">
  <b>🇨🇳 中文</b> | <a href="#features">特性</a> | <a href="#tools">工具列表</a> | <a href="#usage">使用方式</a>
</p>

---

<p align="center">
  <b>🔧 一个纯前端实现的在线工具集合</b><br>
  无需后端服务，完全离线可用，即开即用
</p>

## ✨ 特性

- 🚀 **纯前端实现** - 仅需浏览器，无需服务器
- 💻 **完全离线** - 下载后可在无网络环境使用
- 📱 **响应式设计** - 支持桌面端和移动端
- 🔒 **隐私安全** - 所有数据处理在本地完成
- ⚡ **即开即用** - 单个 HTML 文件，双击打开

## 🛠️ 工具列表

| 工具 | 功能说明 | 技术亮点 |
|------|----------|----------|
| 🔐 密码生成器 | 生成安全随机密码 | 强度评估、批量生成 |
| 📝 文本比对 | 文本差异对比 | LCS 算法、高亮显示 |
| 🧹 JSON 格式化 | JSON 格式化/压缩/验证 | 语法高亮、错误提示 |
| 🔗 Base64 编码 | Base64 编解码 | URL 安全模式、UTF-8 |
| #️⃣ MD5 加密 | 生成 MD5 哈希 | 纯 JS 实现、32/16位 |
| 🔒 AES 加密 | AES 加解密 | Web Crypto API、GCM/CBC/CTR |
| 📁 文件 Base64 | 文件与 Base64 互转 | 任意文件类型支持 |
| 🌐 URL 编解码 | URL 编码/解码 | encodeURI/Component |
| 🗄️ SQL IN 助手 | Excel 数据转 SQL | 自动去重、转义处理 |
| ⏰ 时间戳转换 | Unix 时间戳转换 | 多时区、相对时间 |
| 🎯 正则测试 | 正则表达式测试 | 实时匹配、常用示例 |
| 📄 HTML 提取器 | HTML 内容提取 | 提取文本/链接/图片 |
| 🎨 颜色转换 | 颜色格式转换 | HEX/RGB/HSL互转、预览 |
| 🆔 UUID 生成器 | 生成 UUID/GUID | v4/v7 支持、格式自定义、批量生成 |
| 📊 文本统计分析 | 文本分析与统计 | 中英文统计、常用词、行分析 |

## 🚀 快速开始

### 方式一：在线使用

直接访问 GitHub Pages：
👉 [https://tangguo95.github.io/html-tools/toolbox.html](https://tangguo95.github.io/html-tools/toolbox.html)

### 方式二：本地使用

```bash
# 克隆项目
git clone https://github.com/tangguo95/html-tools.git

# 进入目录
cd html-tools

# 用浏览器打开
toolbox.html
```

或者直接在浏览器中打开文件：`file:///path/to/html-tools/toolbox.html`

## 📸 界面预览

<p align="center">
  <img src="screenshots/preview.png" alt="工具箱界面" width="80%">
</p>

## 📖 功能详情

### 🔐 密码生成器
- 自定义长度（4-128 位）
- 字符类型：大写/小写/数字/符号
- 排除相似字符（0O, 1lI）
- 批量生成（最多 20 个）
- 密码强度评估

### 📝 文本比对
- LCS（最长公共子序列）算法
- 忽略大小写/空白字符
- 高亮显示差异

### 🧹 JSON 格式化
- 格式化（2/4 空格/Tab）
- 压缩
- 语法验证

### 🔗 Base64 编码
- 编码/解码
- URL 安全模式
- 支持 UTF-8

### #️⃣ MD5 加密
- 纯 JS 实现，无依赖
- 32 位/16 位输出
- 大小写切换

### 🔒 AES 加密
- 使用 Web Crypto API
- 支持 GCM/CBC/CTR 模式
- PBKDF2 密钥派生
- 随机密钥生成

### 📁 文件 Base64
- 文件转 Base64 编码
- Base64 转文件下载
- 支持任意文件类型

### 🌐 URL 编解码
- 支持 encodeURI/encodeURIComponent
- 编码/解码切换

### 🗄️ SQL IN 助手
- 自动解析 Excel 复制数据
- 自动去重、转义单引号
- 输出 SQL IN 格式

### ⏰ 时间戳转换器
- 实时显示当前时间戳
- 时间戳转日期（自动识别秒/毫秒级）
- 日期转时间戳（支持本地/UTC 时区）
- 相对时间计算（如"3天前"）
- 多时区显示（北京、东京、纽约、伦敦等 10 个主要城市）

### 📄 HTML 提取器
- 提取纯文本内容（移除HTML标签）
- 提取所有链接（带链接文本）
- 提取图片URL
- 移除 script/style 标签
- 清理多余空白/保留换行
- 下载为TXT文件
- 示例HTML输入助手

## 🛠️ 技术栈

<p align="center">
  <img src="https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white" alt="CSS3">
  <img src="https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Web%20Crypto%20API-Supported-4285F4" alt="Web Crypto API">
</p>

## 📝 更新日志

### 2026-04-16
- ✨ 新增 HTML 提取器功能
- 📝 提取纯文本、链接、图片URL
- 🧹 移除 script/style 标签
- 🎨 清理空白、保留换行控制
- 💾 下载为TXT文件

### 2026-04-14
- ✨ 新增时间戳转换器功能
- 🌍 支持 Unix 时间戳与日期时间互转
- 🌐 添加多时区显示功能（10 个主要城市）
- ⏱️ 支持相对时间计算

### 更早版本
- 🔐 密码生成器
- 📝 文本比对
- 🧹 JSON 格式化
- 🔗 Base64 编码
- #️⃣ MD5 加密
- 🔒 AES 加密
- 📁 文件 Base64
- 🌐 URL 编解码
- 🗄️ SQL IN 助手

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

[MIT](LICENSE) © tangguo95

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/tangguo95">tangguo95</a>
</p>
