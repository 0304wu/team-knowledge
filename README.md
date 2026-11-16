# AI Team Knowledge Base 使用说明

本仓库用于保存团队论文、笔记、项目文档、实验记录和 Prompt，并配合 Codex 的科学研究 skills 使用。

## 这是什么

本项目由三部分组成：**团队知识库**保存论文原文、讲解笔记、目录和标签；**Codex skills**规定 AI 如何整理、检索和回答；**工具脚本**负责扫描、搜索、去重和安装。严格来说，这是一个“团队科研知识库 + 一组 AI skills + 配套工具”的工作流项目，`team-knowledge-base` 是其中负责知识库维护和问答的主要 skill。

## 目录

- `00_index/`：论文目录、术语表、更新日志、扫描报告
- `01_papers/`：论文原文和论文笔记
- `02_projects/`：项目说明、决策和里程碑
- `03_experiments/`：实验记录、结果和失败分析
- `04_code/`：代码、环境和 API 说明
- `05_datasets/`：数据集卡片、字段和预处理说明
- `06_prompts/`：可复用 Prompt 和评测样例
- `07_faq/`：经过确认的常见问题答案
- `99_archive/`：已经过时但需要保留的资料
- `tools/`：索引、检索、去重和安装工具
- `skills/`：可一次安装的团队 skills bundle，结构参考 scientific-agent-skills
- `plugin.json`：skills 清单和版本信息
- `tests/`：不依赖第三方包的结构检查

## 一次安装全部 skills

这是一个可复制的 skills bundle。成员不需要逐个复制文件：获取仓库后，在仓库根目录打开 PowerShell，运行：

```powershell
.\tools\install-skills.ps1
```

脚本会一次安装 `team-knowledge-base`、`paper-reading`、`experiment-record` 和 `technical-flowchart` 到当前电脑的 Codex skills 目录。安装后重启 Codex 或新建聊天即可发现它们。

如果使用支持插件安装的 Codex 版本，也可以在仓库根目录尝试：

```powershell
codex plugins install .
```

若该命令不可用，使用上面的 PowerShell 脚本即可；知识库文件仍然保存在 GitHub 仓库中，安装 skill 不会复制全部论文到聊天里。

## 能否用于其他 AI

这些文件首先按照 Codex skill 规范编写，因此在 Codex 中可以被自动发现或通过 `$team-knowledge-base` 等名称调用。不同 AI 产品对 skill 的格式和安装方式并不统一：支持 Markdown 自定义指令的工具可以参考 `skills/*/SKILL.md`；支持插件或 agent skill 目录的工具可以复制对应文件夹；只支持普通聊天的工具可以复制其中的工作流和提示词，但不会自动获得 Codex 的调用机制。任何 AI 都需要获得 GitHub 仓库权限，才能读取私有资料。

因此，论文、笔记和目录具有较好的跨工具可迁移性，skill 的自动安装和调用方式取决于具体 AI 平台。本仓库不会自动把私有 GitHub 内容开放给其他 AI，也不等于一个共享网页问答服务。

## 一般的 skill 用在哪里

Skill 是给 AI 使用的可复用工作规范，通常包含一个 `SKILL.md`，必要时还包含脚本、模板和参考资料。它适合固定文献阅读、实验记录、数据分析、幻灯片制作、代码审查和团队知识库维护等重复任务。Skill 规定 AI 如何工作，仓库中的论文和笔记才是实际被检索的知识内容。

检查打包结构：

```powershell
python .\tests\validate_package.py
```

## 五步工作流

### 1. 上传论文

可以直接在 Codex 中上传附件，并用自然语言要求保存。例如：

```text
把我刚上传的论文和已有讲解加入团队知识库，保存到合适的主题目录，更新 catalog.md 和 update-log.md，不需要重新分析论文。
```

Codex 会把附件复制到知识库目录，保留原文件，补充必要的标题、作者、年份、DOI、主题和来源链接。之后仍需要提交并推送到 GitHub，其他成员才能看到。只上传到聊天窗口而没有保存到仓库的附件不会自动成为团队资料。

也可以直接在 GitHub 网页上传，或把 PDF 放入本地仓库的 `01_papers/`，再通过 GitHub Desktop 提交并推送。

建议每篇论文同时保存：

```text
01_papers/
├── paper-title.pdf
└── paper-title.md
```

笔记中至少记录标题、作者、年份、期刊、DOI、关键词、摘要、主要结论和原文路径。

### 2. 按主题查找论文

在本地仓库根目录运行：

```powershell
python .\tools\search_papers.py . 单细胞 扰动预测
```

也可以直接在 Codex 中说：

```text
使用 $team-knowledge-base，查找团队知识库中与单细胞扰动预测相关的论文。
```

### 3. 定位论文

检索结果会显示文件路径和匹配内容。打开 `01_papers/` 中对应的 Markdown 笔记，可以看到 DOI、原文路径、摘要和标签；再点击或下载对应 PDF。

建议使用稳定文件名，例如：

```text
2026-11-16_Benchmarking-perturbation-prediction.pdf
2026-11-16_Benchmarking-perturbation-prediction.md
```

### 4. 使用 AI 分析论文

把需要分析的 PDF 拖进 Codex，然后输入：

```text
使用 $paper-reading，分析这篇论文，说明研究问题、数据、方法、图表、主要结果、局限性和对我们项目的价值，并注明页码或图表来源。
```

如果希望把结果保存到知识库：

```text
使用 $team-knowledge-base，把刚才的论文分析保存为 01_papers/论文名.md，并更新 catalog.md。
```

### 5. 知识问答

针对团队已经整理的摘要和记录，可以直接提问：

```text
使用 $team-knowledge-base，团队知识库中有哪些关于单细胞扰动响应预测的论文？请按方法类型比较。
```

```text
使用 $team-knowledge-base，根据已有论文回答 scGPT 与 GEARS 的差异，并给出来源文件。
```

资料中没有答案时，AI 应明确说明“知识库中没有找到”，不要自行补充成团队结论。

## 每周更新流程

1. 上传或复制新资料；
2. 运行 `python .\tools\scan_knowledge_base.py .`；
3. 运行 `python .\tools\check_duplicates.py .`；
4. 使用 `$team-knowledge-base` 生成摘要并更新索引；
5. 检查修改内容；
6. GitHub Desktop 中填写提交说明；
7. 点击 `Commit to master`；
8. 点击 `Push origin`。

## 同伴首次安装

同伴先获取仓库，然后在仓库根目录打开 PowerShell：

```powershell
.\tools\install-skills.ps1
```

重启 Codex 或新建聊天后即可使用：

```text
$team-knowledge-base
$paper-reading
$experiment-record
```

## GitHub 操作说明

- `Fetch origin`：获取远程最新状态，不上传本地修改；
- `Pull origin`：获取并合并同伴的更新；
- `Commit to master`：保存本地版本；
- `Push origin`：上传本地提交到 GitHub。

开始修改前先点击 `Fetch origin`。如果同伴已经改过同一个文件，先 `Pull origin`，不要直接覆盖。

## 文件和隐私规则

- 私有仓库用于团队内部资料；
- 不要提交密码、Token、患者隐私或未经授权的数据；
- 单个文件超过 100 MiB 时不要直接提交；
- 不要重复上传同一篇 PDF 的多个副本；
- 原始文件不要随意删除，过期资料放入 `99_archive/`；
- 每条重要结论都应有来源文件、页码、DOI 或实验记录。

## 当前能力边界

当前方案不需要额外服务器，也不要求每个人克隆全部 PDF。GitHub 负责保存和浏览，`search_papers.py` 负责本地索引检索，Codex 负责对选中的论文进行 AI 分析和问答。若希望所有成员直接通过一个网页对远程仓库进行全文 RAG 问答，后续需要部署 Open WebUI、AnythingLLM 或其他共享问答服务。
