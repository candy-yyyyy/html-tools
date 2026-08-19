# HTML Tools

<p align="center">
  <img src="https://img.shields.io/badge/HTML-Single%20File-E34F26?logo=html5&logoColor=white" alt="HTML Single File">
  <img src="https://img.shields.io/badge/Runtime-Browser-4285F4?logo=googlechrome&logoColor=white" alt="Browser">
  <img src="https://img.shields.io/badge/Mode-Frontend%20Only-0F766E" alt="Frontend Only">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/tangguo95/html-tools?style=flat-square" alt="Stars">
  <img src="https://img.shields.io/github/commit-activity/m/tangguo95/html-tools?style=flat-square" alt="Commits">
  <img src="https://img.shields.io/github/last-commit/tangguo95/html-tools?style=flat-square" alt="Last Commit">
</p>

<p align="center">
  <b>🇨🇳 中文</b> | <a href="#features">特性</a> | <a href="#tool-list">工具列表</a> | <a href="#usage">使用方法</a> | <a href="#notes">说明</a>
</p>

---

`HTML Tools` 是一个纯前端本地工具页，直接打开 `toolbox.html` 即可使用。所有处理都在浏览器内完成，不依赖后端服务，不需要额外安装运行环境。

## ✨ 特性

- 🧩 **单文件工具页** - 核心能力集中在 `toolbox.html`
- 🔒 **本地处理** - 默认不经过服务端，适合日常敏感文本处理
- 📱 **响应式布局** - 桌面和移动端都可用
- 📋 **一键复制** - 常见结果支持快速复制
- 🧰 **覆盖常用开发场景** - 编解码、格式化、哈希、转换、文本处理

## 🛠️ 工具列表

| 工具 | 说明 |
|------|------|
| 🔐 密码生成器 | 批量生成随机密码，可控制长度和字符类型 |
| 📝 文本比对 | 按行比较两段文本，支持忽略大小写和去空格 |
| 🧹 JSON 格式化 | JSON 格式化和压缩 |
| 📊 JSON 转 CSV | JSON 数组转 CSV，支持自定义分隔符和 BOM |
| 🔗 Base64 编解码 | 文本 Base64 编码和解码，支持 URL 安全模式 |
| 📁 文件 Base64 转换 | 文件与 Base64/Data URL 互转 |
| #️⃣ MD5 | 纯前端 MD5 计算，支持 32 位和 16 位输出 |
| 🔒 AES 加解密 | 基于 Web Crypto API 的 AES-GCM / AES-CBC |
| 🌐 URL 编解码 | URL 编码和解码 |
| 🗄️ SQL IN 助手 | 多行文本转 SQL `IN (...)` 列表，支持去重和转义 |
| ⏰ 时间戳转换 | 时间戳与日期时间互转 |
| 🎯 正则测试 | 正则表达式匹配测试 |
| 📄 HTML 提取器 | 提取 HTML 中的文本、链接和图片地址 |
| 🎨 颜色转换 | 颜色解析和 HEX / RGB 展示 |
| 🔐 SHA 哈希 | 基于 Web Crypto API 的 SHA-256 / SHA-384 / SHA-512 |
| 🆔 UUID 生成器 | UUID v4 / v7 批量生成，支持格式调整 |
| 🔢 进制转换 | 十进制、十六进制、二进制、八进制互转 |
| 🔤 大小写转换 | `camelCase` / `PascalCase` / `snake_case` / `kebab-case` |
| 📘 YAML 格式化 | 简单 YAML / JSON 转换与格式化 |
| ⚙️ Nginx 格式化 | nginx 配置文件格式化，支持注释、正则、多级块 |
| 🌍 IP 地址计算器 | IPv4 子网基础计算 |
| 🔄 单位转换器 | 长度、重量、温度、体积、时间转换 |
| ✂️ 文本分隔合并 | 按分隔符拆分、合并、去重 |
| 📈 文本统计 | 字符、行数、段落、英文词数、汉字数统计 |
| 📋 剪贴板历史 | 读取并保存剪贴板文本到本地历史 |

## 🚀 使用方法

1. 直接在浏览器中打开 `toolbox.html`
2. 在左侧切换需要的工具
3. 输入内容并执行操作
4. 复制或导出结果

## 📁 文件说明

```text
html-tools/
├── toolbox.html    # 主工具页
├── README.md       # 项目说明
├── LICENSE         # MIT 许可证
└── todo.md         # 记录文件
```

## 📝 说明

- `AES`、`SHA`、剪贴板读取等功能依赖浏览器能力，建议使用现代浏览器。
- `YAML` 功能使用轻量解析逻辑，适合简单结构；复杂 YAML 不保证完整兼容。
- 当前版本不包含 QR 码功能。

## AI 辅助开发与免责声明

本项目 99% 以上的代码、文档与细节打磨均在作者主导与审阅下，借助 AI 编程工具完成。

本项目按“现状”提供，主要用于学习、实验和个人使用。项目未经过专门的专业安全审计、漏洞扫描或合规性审查；如需用于生产环境、公开网络或任何安全敏感场景，请先自行完成代码审查、测试与加固。因使用本项目造成的安全问题、数据丢失、服务中断或其他风险，作者不承担相关责任。

## 📄 许可证

[MIT](LICENSE) © tangguo95

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/tangguo95">tangguo95</a>
</p>
