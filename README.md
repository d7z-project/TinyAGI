# TinyAGI

研究一个长期存在的统一主体：在数字环境与通用设备中感知和行动，按需组织心智与能力，从实际结果中形成记忆和改进。

**当前处于设计阶段，没有产品发布版本。** 统一事件连接观察、认知、能力调用及结果；资源默认投影、按需读取；完整管理工作台覆盖主体业务、模型服务、沙箱副本及用户机密。能力可按需构建、试验和采用，工程上复用 go-mini MRPC 接入 Go／Rust／Node.js（npm）能力，并由宿主管理局部 VM 和能力子进程。主动学习与自我迭代作为实验性扩展纳入设计，学习强度有上限，最低可关闭、不主动学习。设计按主题持续修订，不用 v1／v2 区分产品阶段。

人物通过[完整提示词初始化与差异说明自迁移](DESIGN.md#initialization-migration)，允许不同模型形成不同个体；宿主提供独立引导／维护入口及 API 弃用兼容窗口，帮助原人物持续更新。客户端同时携带[预制能力库](DESIGN.md#prebuilt-capabilities)，由客户端维护权威实现，Self 可选择调用、组合或不用，保留个体认知自由。

[核心与任务解耦](DESIGN.md#core-task-control)：长任务独立受管理，超时和中止回到所属活动；控制台及获授权审计可直接控制任务，Self 继续处理其他输入。认知中断、任务停止和操作取消按各自范围处理；步骤内已接纳工作不因最终状态提交失败而消失。跨专题的公共决策、配置生效、个体状态和实现信任边界集中见[一致性决策](docs/research-plan.md#architecture-consistency)。

按以下顺序阅读：

1. [总体设计](DESIGN.md)：目标 → 逻辑架构 → 核心概念 → 完整流程 → 机制与取舍。
2. [文档索引](docs/README.md)：六份专题的职责、阅读路线和术语入口。
3. [工程参考](docs/engineering-reference.md)：部署、技术栈、存储、依赖及选择理由。
4. [设计决策与适用边界](docs/research-plan.md)：已确认要求、已定方案、建议及用途配置。

查证选择依据时使用[实验与资料索引](docs/whole-system-evidence.md)；历史材料中的写稿号、实验修订号和外部依赖版本不代表 TinyAGI 产品版本。历史实验保留原条件与失败，不能作为当前待办。更新规则见[文档规范](docs/documentation-guide.md)。

文档网站使用支持 Mermaid 的 mdBook；本地执行 `python3 scripts/docs.py build`，生成内容位于 `book/`。GitHub Pages 工作流、工具版本及公开范围见[文档发布说明](docs/documentation-publishing.md)。原始测试目录与历史讨论仅在本地保留，不进入公开书稿。
