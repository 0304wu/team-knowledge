# 团队科研 Wiki

这是一个基于 GitHub 的团队科研资料库，用来保存论文原文、讲解笔记、项目资料和实验记录。成员使用自己熟悉的 AI 工具阅读和整理资料，再把 Markdown 笔记同步到仓库。

## 核心原则

- GitHub 保存共享资料和版本记录。
- Markdown 笔记是主要知识载体。
- AI 工作规范统一记录格式、分类和引用方式。
- 脚本只用于维护，不是使用前提。
- 当前不提供服务器端 RAG 或知识图谱服务。

## 目录

- `00_index/`：目录和更新日志
- `01_papers/`：论文原文和讲解笔记
- `02_projects/`：项目资料
- `03_experiments/`：实验记录
- `04_code/`：代码和环境说明
- `07_faq/`：常见问题
- `99_archive/`：旧版本
- `PORTABLE_WORKFLOW.md`：通用 AI 工作规范
- `skills/`：可选的结构化 skills
- `optional-tools/`：可选维护脚本

## 上传论文

在支持文件上传的 AI 工具中上传论文和已有讲解，输入：

```text
把我刚上传的论文和已有讲解加入团队科研 Wiki，放到合适的主题目录，更新 00_index/catalog.md 和 00_index/update-log.md，不需要重新分析论文。
```

AI 应做到：

1. 保留原始 PDF 和已有讲解；
2. 补充标题、作者、年份、DOI、主题、贡献者和日期；
3. 更新目录和日志；
4. 检查重复文件和 DOI；
5. 报告保存路径。

## 查询资料

```text
查找团队科研 Wiki 中与单细胞扰动预测相关的论文，列出标题、主题、年份、原文和讲解路径。
```

回答时先读 `00_index/catalog.md`，再读相关 Markdown 笔记，必要时核对 PDF 页码。不要一次读取整个仓库。没有证据时说明 Wiki 中没有找到。

## 同步

修改完成后提交并 Push 到 GitHub。只有 Push 成功，其他成员才能看到更新。

## AI 工作规范

- 支持 Agent Skills 的平台：使用 `skills/` 中的 `SKILL.md`。
- 支持系统提示词的 AI：使用 `PORTABLE_WORKFLOW.md`。
- 只支持普通聊天的 AI：提供 `PORTABLE_WORKFLOW.md` 和相关 Markdown 文件。

不同平台的安装方式可能不同，但资料目录和记录规则保持一致。

## 可选脚本

`optional-tools/` 包含扫描、搜索、去重和安装脚本。没有脚本也可以通过 GitHub、Markdown 模板和 AI 工作规范维护 Wiki。

## 文件要求

- 不提交密码、Token、患者隐私或未经授权的数据。
- 大文件先评估 Git LFS 或其他存储方式。
- 不直接删除重要原文，旧版本放入 `99_archive/`。
- 重要结论保留来源文件、页码、DOI 或实验记录。
