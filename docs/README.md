# 文档索引

用途：阅读与术语索引｜更新：2026-09-21。

[项目入口](../README.md) · [完整总设计](../DESIGN.md) · [设计状态](research-plan.md)

默认阅读当前正文；历史材料只用于查证来源，不是另一套设计。所有状态与配置边界统一见[设计台账](research-plan.md#research-status)。

## 阅读路线

| 阅读目的 | 路线 |
| --- | --- |
| 建立整体认识 | [总设计](../DESIGN.md#reading-guide) → 目标／逻辑总图 → 核心概念 → 完整场景 → 机制与取舍 |
| 核对跨专题一致性 | [统一决策](research-plan.md#architecture-consistency) → [步骤与操作](runtime-protocol.md#step-operation-admission)／[公共决策](whole-system-design.md#public-decisions)／[配置与当前约束](runtime-protocol.md#configuration-resolution) |
| 理解资源、投影和 Secret | [总体契约](../DESIGN.md#resource-projections) → [公共属性与类型](projection-input-and-compute.md#resource-contract) → [操作接纳](runtime-protocol.md#resource-operations) → [资源管理](management-workspace.md#resource-management) |
| 理解任务解耦与外部中止 | [总体架构](../DESIGN.md#core-task-control) → [控制契约](runtime-protocol.md#task-control) → [控制台](management-workspace.md#task-control-management) → [mini-go 依据](go-mini-integration.md#task-control-facts) |
| 使用客户端预制能力 | [总体选择](../DESIGN.md#prebuilt-capabilities) → [维护与调用契约](runtime-protocol.md#prebuilt-library) → [工程接入](engineering-reference.md#client-library) |
| 创建与更新人物 | [总体流程](../DESIGN.md#initialization-migration) → [引导契约](runtime-protocol.md#bootstrap-migration) → [管理入口](management-workspace.md#initialization-management) → [工程接入](engineering-reference.md#prompt-bootstrap) |
| 深入某项机制 | 从总设计或下表进入对应专题；专题维护详细规则，其他文档只保留必要概览和链接 |
| 理解具体承载 | [工程参考](engineering-reference.md#physical-architecture) → 技术栈／存储／能力接入 → [库事实](go-mini-integration.md) |
| 核对选择与状态 | [设计台账](research-plan.md#closure-status) → 采用理由／备选／用途配置 → [证据索引](whole-system-evidence.md) |

## 六份逻辑设计专题

| 专题 | 唯一维护的详细机制 |
| --- | --- |
| [主体运行、认知协作与学习](whole-system-design.md) | 关注、工作区、连续性、任务责任、多人格组织与公共整合、经验形成、主动学习议程及策略迭代 |
| [交流、人物与情境](interaction-design.md) | 意愿与投入、信任／污染、规范／格式、身份／隐私、情感／角色及主动联系 |
| [资源契约、输入与计算](projection-input-and-compute.md) | 资源公共属性、类型规则、情境投影、表示与派生、读取及执行使用记录；外部事件源、有限思考与缓存／KV 分工 |
| [逻辑模块、能力契约与运行协议](runtime-protocol.md) | 状态归属、统一事件、能力构建与运行对象、学习强度及关闭、模型端口、步骤／操作接纳与生命周期、配置解析、个体状态与实现信任 |
| [沙箱、能力评估与回归](sandbox-evaluation.md) | 局部／组合／副本试验、构建环境、AGI 副本生命周期、隔离、复盘、测试材料、基线、评价及采用 |
| [管理工作台与人工干预](management-workspace.md) | 管理入口及身份、模型／服务及能力构建维护、用户机密与可信提交、动态表单／蓝图、提交与观察 |

跨专题边界：资源专题维护共同契约及 Secret 类型规则，运行协议维护操作接纳和实际调用，工作台维护归属、可信提交与页面交互；原状态所有者接纳修改，副本规则由沙箱维护。工程承载不写进逻辑图。

## 工程参考

| 参考 | 唯一维护范围 |
| --- | --- |
| [工程选型与部署](engineering-reference.md) | 物理部署、软件组合、技术栈、能力工具链／子进程、存储／文件、向量服务及选型依据 |
| [go-mini 库行为与接入](go-mini-integration.md) | 固定提交的读取记录、MRPC 多语言／资源／替换、实例／scope／补丁及宿主接入限制 |

<a id="experiments"></a>
## 决策与证据

| 查什么 | 位置 |
| --- | --- |
| 设计约束、已定设计、建议与配置 | [设计状态](research-plan.md#closure-status)、[基础设计](research-plan.md#remaining-questions)、[管理设计状态](research-plan.md#management-extension) |
| 已有实验、失败和原始数据 | [实验索引](whole-system-evidence.md#experiments)；各报告保持原条件 |
| 论文、标准和来源命题 | [按问题查依据](whole-system-evidence.md#topics)、[设计机制资料](whole-system-evidence.md#design-closure)、[论文与标准记录](whole-system-evidence.md#sources) |
| 文档怎样保持一致 | [维护规范](documentation-guide.md) |
| 构建网站、Mermaid、GitHub Pages 与公开范围 | [文档发布说明](documentation-publishing.md) |

设计按主题和日期维护。论文、协议和依赖版本用于定位来源，实验修订标识用于区分固定条件。

## 术语定位

先区分几个容易混用的词：

| 用语 | 本项目中的含义 |
| --- | --- |
| 接纳 | 确认承担请求或操作责任；不代表已经执行成功 |
| 采用 | 将候选方法、配置或程序用于明确的任务或范围；不自动扩大权限 |
| 交付 | 结果到达允许的接收点；保存文件或发出请求不等于交付成功 |
| 结束 | 当前活动不再推进；应分别说明完成、退出、取消或受阻等原因 |
| 已定设计 | 当前选择的方案；不等于已经实现或通过完整验证 |
| 实测结果 | 在已记录条件下实际运行得到的证据；适用范围以报告为准 |

### 主体、人物与交流

| 概念组 | 当前定义位置 |
| --- | --- |
| Self、Mind、Persona、Role、Person | [总概念](../DESIGN.md#domain)、[协作](whole-system-design.md#organization)、[人物](interaction-design.md#identity) |
| 私有 Mind 状态、活动委托、Self 公共整合 | [公共决定](whole-system-design.md#public-decisions)、[总体关系](../DESIGN.md#self-integration) |
| 完整初始化提示词、个体差异、Self 自迁移与引导修复 | [人物形成](whole-system-design.md#self-initialization)、[运行契约](runtime-protocol.md#bootstrap-migration)、[检查场景](sandbox-evaluation.md#initialization-evaluation)、[状态](research-plan.md#initialization-extension) |
| API 弃用、兼容窗口、提示词差异与客户端更新 | [工程映射](engineering-reference.md#prompt-bootstrap)、[库事实](go-mini-integration.md#deprecation-facts)、[管理入口](management-workspace.md#initialization-management) |
| 意愿、可答性、快慢投入、承担范围 | [回应](interaction-design.md#response)、[承诺](interaction-design.md#commitments) |
| 观测、命题、来源权威、污染 | [观测与信任](interaction-design.md#observation) |
| 规范、适用性、输出契约 | [规范](interaction-design.md#norms)、[格式](interaction-design.md#output) |
| 跨平台关联、参与者、受众、情境保密 | [关联](interaction-design.md#linking)、[隐私](interaction-design.md#privacy) |
| 情感评价、剧情、虚拟伴侣、主动联系 | [情感与角色](interaction-design.md#affect)、[问候与提醒](interaction-design.md#initiative) |

### 活动、执行与控制

| 概念组 | 当前定义位置 |
| --- | --- |
| Goal、Episode、关注表、工作区、计划 | [运行循环](whole-system-design.md#loop)、[工作区](whole-system-design.md#workspace) |
| Episode、Task、Operation、尝试与控制传播 | [身份和生命周期](runtime-protocol.md#core-task-lifecycle)、[控制语义](runtime-protocol.md#task-control) |
| Step、执行上下文、模型会话、Continuation | [连续性边界](whole-system-design.md#boundaries)、[运行步骤](runtime-protocol.md#step-context) |
| 任务契约、有效结果集合、责任收尾 | [主体任务](whole-system-design.md#task-contract)、[评价环境](sandbox-evaluation.md#outcome-contract)、[状态定义](research-plan.md#closure-status) |
| 证据未知、主体退出、原目标达成与活动结束 | [结果与责任的分工](../DESIGN.md#responsibility-outcomes)、[接纳与退出](interaction-design.md#commitments) |
| 步骤内独立接纳、请求键、最终提案与已接纳操作 | [接纳时序](runtime-protocol.md#step-operation-admission)、[工程提交](engineering-reference.md#commit) |
| 核心／任务解耦、认知中断、任务阻断／中止、外部审计控制 | [主体场景](whole-system-design.md#task-independence)、[生命周期](runtime-protocol.md#core-task-lifecycle)、[控制](runtime-protocol.md#task-control)、[工程](engineering-reference.md#task-execution)、[评价](sandbox-evaluation.md#task-control-evaluation)、[状态](research-plan.md#task-control-extension) |
| 统一事件、来源、订阅、请求／结果、内部接续 | [总事件主线](../DESIGN.md#event-driven)、[协议](runtime-protocol.md#events)、[外部通知源示例](projection-input-and-compute.md#event-sources) |
| Operation、Effect、Outcome、unknown | [操作与效果](runtime-protocol.md#operations)、[用途评价](../DESIGN.md#outcomes) |
| 依赖、执行条件、结果复核 | [复核](runtime-protocol.md#revalidation) |

### 资源、能力与配置

| 概念组 | 当前定义位置 |
| --- | --- |
| 资源、引用、描述、内容表示、投影、操作契约 | [共同定义](projection-input-and-compute.md#resource-contract)、[设计范围](research-plan.md#unified-resources) |
| 公共属性、类型规则、内容／描述修订、当前授权 | [属性与维护责任](projection-input-and-compute.md#resource-attributes)、[工程接入](engineering-reference.md#resource-integration) |
| 情境投影、选择性发现、读取／处理／使用／交付 | [投影](projection-input-and-compute.md#projection)、[操作](runtime-protocol.md#resource-operations)、[使用记录](projection-input-and-compute.md#resource-reading) |
| 内容派生、运行使用、来源和信息范围 | [派生规则](projection-input-and-compute.md#resource-derivation)、[资料](projection-input-and-compute.md#resource-evidence) |
| 读取／计算缓存、KV、有限思考 | [缓存](projection-input-and-compute.md#cache)、[投入](projection-input-and-compute.md#effort) |
| 逻辑模块、状态所有者、ModelRequest／Result | [职责](runtime-protocol.md#software-modules)、[模型端口](runtime-protocol.md#model-port) |
| 公共 API、事件接入／观察、ResourceSearch／VectorIndex | [公共契约](runtime-protocol.md#capability-api)、[检索责任](runtime-protocol.md#vector-service) |
| 能力构建、接口、产物、采用与运行对象 | [整体闭环](../DESIGN.md#capability-development)、[逻辑契约](runtime-protocol.md#capability-lifecycle)、[管理入口](management-workspace.md#capability-management)、[设计范围](research-plan.md#capability-extension) |
| 功能采用、实现信任、固定产物与环境准入 | [逻辑边界](runtime-protocol.md#implementation-trust)、[工程承载](engineering-reference.md#implementation-admission) |
| 客户端预制能力库、只读维护、可选使用与个体包装 | [逻辑契约](runtime-protocol.md#prebuilt-library)、[管理](management-workspace.md#prebuilt-management)、[评价](sandbox-evaluation.md#prebuilt-evaluation)、[库事实](go-mini-integration.md#prebuilt-library-facts)、[状态](research-plan.md#prebuilt-extension) |
| 热加载、编写契约、结构化注释与受管理函数 | [总设计](../DESIGN.md#hot-reload-contract)、[逻辑契约](runtime-protocol.md#managed-functions)、[表单与蓝图](management-workspace.md#dynamic-editing)、[函数测试](sandbox-evaluation.md#function-evaluation)、[工程生成工具](engineering-reference.md#managed-function-tooling) |
| 普通配置、作用域覆盖、当前权限与控制 | [解析与生效](runtime-protocol.md#configuration-resolution)、[管理视图](management-workspace.md#editing) |
| 个体自定义状态、结构修订与迁移 | [逻辑契约](runtime-protocol.md#individual-state)、[存储映射](engineering-reference.md#individual-state-storage) |
| 模型资产／推理服务维护、Secret 类型与使用绑定 | [资源类型](projection-input-and-compute.md#secret-resource)、[管理范围](management-workspace.md#technical-management)、[机密交互](management-workspace.md#secret-projection)、[运行契约](runtime-protocol.md#secret-contract)、[工程映射](engineering-reference.md#maintenance-secrets) |
| 用户机密归属、专用指令、一次性提交及过滤转换 | [归属与授权](management-workspace.md#secret-ownership)、[可信提交](management-workspace.md#secret-command)、[处理流程](management-workspace.md#secret-pipeline)、[用户场景](management-workspace.md#secret-scenario) |

### 学习、沙箱与评价

| 概念组 | 当前定义位置 |
| --- | --- |
| 主动学习、兴趣探索、学习议程与自我迭代 | [总设计](../DESIGN.md#active-learning)、[主体策略](whole-system-design.md#active-learning)、[评价](sandbox-evaluation.md#learning-evaluation)、[状态](research-plan.md#active-learning-extension) |
| 学习强度、关闭主动学习、明确学习任务与恢复 | [运行契约](runtime-protocol.md#learning-intensity)、[管理控件](management-workspace.md#learning-management)、[工程接入](engineering-reference.md#active-learning-integration)、[库装配](go-mini-integration.md#active-learning-adapter) |
| 经验、Reference、认知程序修订与候选采用 | [学习](whole-system-design.md#memory)、[候选](../DESIGN.md#branches) |
| Sandbox、重放、重新评估、反事实 | [沙箱职责](sandbox-evaluation.md#architecture)、[模式](sandbox-evaluation.md#modes) |
| 能力画像、用例／套件、开发／回归／保留任务 | [评估层次与覆盖](sandbox-evaluation.md#evaluation-design)、[测试材料](sandbox-evaluation.md#test-cases) |
| 基线、评价器、退化与采用门槛 | [可比条件](sandbox-evaluation.md#baselines)、[评价器](sandbox-evaluation.md#graders)、[判定与报告](sandbox-evaluation.md#regression-gates) |

### 工程与来源

| 概念组 | 当前定义位置 |
| --- | --- |
| 向量数据库、Go SDK、本地／远程与产品选型 | [接入参考](engineering-reference.md#vector-service)、[官方依据](engineering-reference.md#vector-sources) |
| MRPC、Go／Rust／Node.js（npm）、工具链、子 VM 与子进程 | [工程工具链](engineering-reference.md#capability-toolchain)、[库事实与接入](go-mini-integration.md#rpc-extension-facts)、[JavaScript RPC](go-mini-integration.md#javascript-rpc-facts)、[Node 工程接入](engineering-reference.md#node-rpc-integration)、[试验分层](sandbox-evaluation.md#test-scopes) |
| RunID、InstanceID、Generation、DeploymentSeq | [库身份映射](go-mini-integration.md#deployment)、[逻辑身份](runtime-protocol.md#identity) |
| 技术栈、软件依赖、SQLite、文件发布、锁与备份 | [工程参考](engineering-reference.md)、[存储机制](engineering-reference.md#persistence) |
| 固定源码提交与证据范围 | [读取方式](go-mini-integration.md#source-snapshots)、[基础库事实](go-mini-integration.md#library-facts) |

## 文档维护

设计规则、工程映射和实验结果分别维护，修改方法见[文档维护规范](documentation-guide.md)。网站构建、发布配置和安全检查见[文档发布说明](documentation-publishing.md)。
