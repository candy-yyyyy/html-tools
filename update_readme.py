#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
更新 HTML 工具箱 README.md - 添加新工具到表格
"""
import re
from pathlib import Path
import subprocess

# 目标文件路径
repo_root = Path(r"D:\ClawFiles\html-tools")
readme_path = repo_root / "README.md"

# 新工具信息 - 保持 emoji 一致
new_tool = "| 📊 文本统计分析 | 文本分析与统计 | 中英文统计、常用词、行分析 |"

# 读取 README
with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 移除所有文本统计分析条目
content = re.sub(r'\n\|.*?文本统计分析.*?\|\n', '\n', content)

# 查找 UUID 行并插入
lines = content.split('\n')
uuid_line_idx = -1

for i, line in enumerate(lines):
    if ' UUID 生成器 ' in line and '生成 UUID' in line:
        uuid_line_idx = i
        break

if uuid_line_idx >= 0:
    # 在 UUID 生成器后面插入新工具
    lines.insert(uuid_line_idx + 1, new_tool)
    
    # 写回文件
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    
    # 添加文件
    subprocess.run(['git', 'add', 'toolbox.html', 'README.md'], cwd=repo_root)
    
    # 提交
    subprocess.run(['git', 'commit', '-m', 'feat: 新增文本统计分析工具，支持中英文统计、常用词 Top10、行分析'], cwd=repo_root)
    
    # 推送
    subprocess.run(['git', 'push', 'origin', 'main'], cwd=repo_root)
    
    print("Added text stats tool to README.md")
    print(f"Inserted at line {uuid_line_idx + 1}")
    print("Pushed to GitHub")
    
    # 显示 commit hash
    result = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=repo_root, capture_output=True, text=True)
    print(f"Commit hash: {result.stdout.strip()}")
else:
    print("Failed to find UUID tool line")
