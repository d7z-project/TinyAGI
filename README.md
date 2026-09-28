# TinyAGI

研究一个长期存在、能够自行组织认知与行动并持续演化的统一主体：感知环境，形成和调整关注，组织心智与异构能力，行动并积累经历。对话、受托任务和主动学习都是它可以开展的活动。

**当前处于设计阶段，尚未发布产品。** 文档描述目标架构与设计依据；已实现的库能力、已有实验结果和待实现机制分别标明。

设计围绕五项能力展开：

- **持续认知与自主活动**：认知可以直接归属于主体或心智，环境变化和自身关注都可成为起点；按需要形成活动和任务。[运行主线](design/DESIGN.md#subject-loop)连接感知、行动和经历，长工作与主体生命周期分开。
- **按需获取内容与能力**：[资料、记忆、程序、模型和运行对象分别管理](design/DESIGN.md#domain-views)，按接收者提供受限视图；[外部检索提供者](design/DESIGN.md#retrieval)可按用途发现、选择、组合和评价，向量服务与 Attemory 同级接入。明确选读才将内容交给认知，执行、维护与交付使用各自契约。
- **形成并维护个体**：通过[完整提示词初始化与迁移说明](design/DESIGN.md#initialization-migration)创建、更新人物，允许个体差异；[客户端预制能力库](design/DESIGN.md#prebuilt-capabilities)供主体按需选用。
- **扩展能力与学习**：复用、组合或构建工具，在沙箱中评估后按适用范围采用。专门的主动学习属于实验性扩展，投入有上限且可关闭；正常感知、联想、自主日常活动和经历积累仍然保留。
- **管理与人工控制**：Web 工作台覆盖主体状态、模型服务、试验主体和行为配置；[机密独立管理](design/docs/management-workspace.md#secret-management)，默认使用引用，受信适配器及 RPC 实现可按用途取得原值，防止向不可信 API 或其他非预期对象泄漏。

[计算节约](design/DESIGN.md#resource-efficiency)贯穿输入和能力执行：利用提供者前缀复用、有效结果、增量准备及有界运行复用，保持所需信息、独立判断和响应要求；实际质量、时延和净费用分别评价。

工程方案采用单机核心，业务状态保存在 SQLite，文档、媒体和大型产物保存在本地文件中；通过 go-mini MRPC 接入 Go、Rust 和 Node.js（npm）能力。具体部署及依赖见工程参考，逻辑总图只描述职责与交互。

按以下顺序阅读：

1. [总体设计](design/DESIGN.md)：目标 → 逻辑架构 → 核心概念 → 完整流程 → 机制与取舍。
2. [文档索引](design/docs/README.md)：六份专题的职责、阅读路线和术语入口。
3. [工程参考](design/docs/engineering-reference.md)：部署、技术栈、存储、依赖及选择理由。
4. [设计决策与适用边界](design/docs/research-plan.md)：已确认要求、已定方案、建议及用途配置。
5. [实施方案与阶段验收](design/TODO.md)：交付顺序、首批范围、关键契约及验收条件。

查证选择依据时使用[实验与资料索引](design/docs/whole-system-evidence.md)；核对跨专题约束时使用[一致性决策](design/docs/research-plan.md#architecture-consistency)。历史实验保留原条件、结果和失败，不作为当前待办。设计按主题维护，更新规则见[文档规范](design/docs/documentation-guide.md)。

文档网站使用支持 Mermaid 的 mdBook；本地执行 `python3 design/scripts/docs.py build`，生成内容位于 `design/book/`。GitHub Pages 工作流、工具版本及公开范围见[文档发布说明](design/docs/documentation-publishing.md)。实验报告的数据可用性另有说明。
