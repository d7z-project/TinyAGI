# 文档构建、公开范围与 GitHub Pages

用途：文档发布维护｜更新：2026-09-21。

[项目入口](../README.md) · [文档索引](README.md) · [文档规范](documentation-guide.md)

目录：[公开范围](#public-scope) · [本地材料](#local-materials) · [本地构建](#local-build) · [工作流](#github-pages) · [检查边界](#checks)

<a id="public-scope"></a>

## 公开文档与唯一来源

公开网站包含项目介绍、总设计、六份逻辑专题、工程与库参考、决策和证据索引、文档维护说明、整理后的实验报告及历史设计参考。根目录 `SUMMARY.md` 是 mdBook 章节清单，正文仍维护于原文件，不手工维护另一份书稿。

构建脚本只将清单中的 Markdown 复制到生成目录 `.mdbook-src/`，校验每个目标位于公开范围；不会将仓库根目录或整个工作区当作 mdBook 源目录。新增文档须加入章节清单。书稿生成、Mermaid 资产和 HTML 输出都由忽略规则排除，不提交重复产物。

<a id="local-materials"></a>

## 本地测试材料与历史讨论

根目录 `experiments/` 保存测试脚本、夹具、原始模型回复、运行日志及环境记录，可能含历史服务地址和本机路径；`GPT.md` 保存大型历史讨论。这两类材料仅在本地保留，不加入 Git 或公开站点。本次整理已脱敏历史 Markdown 中的个人绝对路径和测试服务地址；涉及冻结哈希的原件以本地非公开副本保留，并在脱敏文档注明对应关系，不改写原始成绩或冒充哈希仍相同。`docs/experiments/` 是整理后的报告，继续公开；原始材料的排除不改变报告中的失败、条件和证据边界。

公开页面中指向上述本地材料的链接会转换为“本地材料，不发布”说明；原正文保留本地追溯路径，生成网站不创建不存在的下载链接。相邻 go-mini 源码链接在书稿中转换为其官方仓库入口；这些入口指向当前上游，固定提交及读取范围仍以[库记录](go-mini-integration.md#source-snapshots)为准。

本机凭据文件、IDE 状态及生成目录同样不提交。忽略规则不影响已经在 Git 索引中的文件，因此发布检查还核对索引，拒绝仍被跟踪的本地测试目录、历史讨论和凭据文件。只从索引移除不删除本地文件；若未来已经形成含敏感内容的提交，需要另外处理提交历史，不能仅依赖忽略规则。

<a id="local-build"></a>

## 本地构建

本工作流固定使用 **mdBook 0.5.4** 与 **mdbook-mermaid 0.17.1**。本地可使用相同版本的官方二进制，或安装：

```sh
cargo install mdbook --version 0.5.4 --locked
cargo install mdbook-mermaid --version 0.17.1 --locked
```

在仓库根目录执行：

```sh
python3 scripts/docs.py build
```

该命令检查公开源文件、准备书稿、安装插件随附的 Mermaid 前端资源、运行 mdBook 并检查输出。生成网站位于 `book/`。需要预览时，先构建，再运行 `mdbook serve --open`；编辑原文后重新执行构建命令，同步生成书稿。

其他入口：`python3 scripts/docs.py check` 检查源文件和索引；`prepare` 只生成书稿；`verify` 检查已有 HTML 输出。它们只处理文档，不运行设计中的实验、模型请求或产品程序。原 Mermaid 围栏直接转成图表，资源随网站发布，不依赖浏览器临时访问第三方图表 CDN。

<a id="github-pages"></a>

## GitHub 工作流

工作流位于 `.github/workflows/mdbook.yml`。相关文件发生 push、PR 变化或手动触发时执行检查与构建；仅默认分支上的非 PR 运行上传并部署 Pages。构建读取源码，部署作业单独取得 Pages 写入与身份令牌权限；不会将模型服务凭据传给文档构建。

首次在目标 GitHub 仓库使用时，将 **Settings → Pages → Build and deployment → Source** 设为 **GitHub Actions**，并允许 `github-pages` 环境从默认分支部署。工作流读取 Pages 的站点路径供构建使用，部署地址显示在环境和工作流输出中；仓库名称和域名无需写死。

工作流从官方 release 下载固定版本工具，并校验对应 SHA-256。升级时同时更新版本、下载摘要和这里的说明，再检查构建、站内链接及 Mermaid；第三方工具版本不是 TinyAGI 产品版本。

依据于 2026-09-21 核对：[mdBook 的 CI 说明](https://rust-lang.github.io/mdBook/continuous-integration.html)、[mdbook-mermaid 配置](https://github.com/badboy/mdbook-mermaid#configure-your-mdbook-to-use-mdbook-mermaid)、[GitHub Pages 自定义工作流](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)。本仓库的章节筛选与发布检查是自身构建规则。

<a id="checks"></a>

## 发布检查与适用边界

源文件检查覆盖公开章节、目录及协作说明中的已知凭据形态、认证串、带认证的 URL、个人绝对路径和测试服务地址；命中只输出文件、行号与规则名，不打印匹配值。检查同时拒绝折叠块和可能读取清单外文件的 include 指令。

构建后继续检查 HTML、打印页、搜索索引及脚本中的同类敏感模式，核对站内链接、锚点和 Mermaid 资源，拒绝意外出现的原始 Markdown、测试脚本、运行日志或数据库文件。自动模式检查不能识别一切未知秘密或语义上的隐私；新增环境记录和外部材料仍须审阅。构建通过也不代表设计能力经过实测，GitHub 部署完成状态以实际 Actions 结果为准。
