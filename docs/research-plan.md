# 设计决策与适用边界

用途：设计决策台账｜更新：2026-09-21。

[总设计](../DESIGN.md#validation) · [文档索引](README.md) · [资料依据](whole-system-evidence.md#design-closure)

本篇集中说明设计约束、采用方案、待定细节和用途配置。资料支持的机制选择与实际验证范围分别记录。

| 阅读主题 | 章节入口 |
| --- | --- |
| 总体状态 | [当前范围](#research-status) · [状态定义](#closure-status) · [完整任务](#whole-system) · [基础设计](#remaining-questions) · [用途配置](#deferred) |
| 扩展方案 | [管理工作台](#management-extension) · [能力扩展](#capability-extension) · [Node.js 补充](#node-rpc-extension) · [主动学习](#active-learning-extension) |
| 个体与控制 | [初始化与迁移](#initialization-extension) · [预制能力库](#prebuilt-extension) · [任务控制](#task-control-extension) · [架构一致性](#architecture-consistency) |
| 维护 | [后续维护](#next-steps) |

<a id="research-status"></a>

## 当前范围

当前处于设计阶段：以既有实验和一手资料明确机制，不运行新增实验或模型调用，不推进产品实现。逻辑设计、工程映射和历史证据分别维护；未来测试或实施按用户明确要求确定范围。

<a id="closure-status"></a>

## 状态及其含义

| 状态 | 适用对象 | 含义 |
| --- | --- | --- |
| 设计约束 | 统一主体、强自主、统一事件、投影、完整管理、可信机密输入等系统要求 | 必须在架构与专题保持一致；不表示已实现 |
| 已定设计 | 基础机制，以及既定的编写契约、调用边界热加载、能力构建与多语言接入、主动学习扩展及强度控制、提示词初始化与个体自迁移、客户端预制能力库、核心／任务解耦及外部控制、跨契约规则 | 已有资料或局部证据支持，可作为继续设计及未来实现的依据 |
| 设计建议 | 管理工作台中尚未单独确认的副本重建细则 | 已提出方案，具体继承与重建规则尚未最终确定 |
| 用途配置 | 模型、设备、预算、联系窗口和评价门槛等 | 随具体用途确定，不是未关闭架构问题 |
| 历史证据 | 报告、脚本、输入、失败与原始数据 | 仅支持其固定条件，不是当前任务队列 |

基础架构已有明确方案。实际能力、性能和真人体验尚无完整测量，属于证据边界；副本重建等具体细节仍保留建议状态。

<a id="whole-system"></a>

## 完整任务的处理流程

事件进入后核对来源、受众与活动；主体决定承担范围、关注和投入；按缺口检索投影并主动读取；调用能力取得有来源的结果；状态所有者核对交付、责任及后续约定；将实际反馈形成带适用范围的经验。临时聊天、工作、陪伴、后台活动和外部通知共享该闭环。

评价设计覆盖有效结果、来源依据、必要过程责任及全部成本。开发、已知回归和独立保留任务分开；结构／环境事实检查、内容评阅及实际体验分开。参照组不自动成为采用基线，模型裁判不独立决定采用。方法正文见[沙箱评估](sandbox-evaluation.md#evaluation-design)。

<a id="remaining-questions"></a>

## 决策台账

下表各项均为**已定设计**。资料和局部实验支持所列机制与取舍；将它们组合为完整系统属于本项目的设计判断。自主意愿、长期人格等价值取向属于项目目标，与可测量的能力效果分别记录。

| 原问题 | 最终采用方案与理由 | 未采用／暂缓方案及原因 | 资料与正文 |
| --- | --- | --- | --- |
| 完整任务与能力评价 | 以任务契约和有效结果集合验收；分能力画像，同时计质量、责任与成本；开发／回归／保留任务分开；同条件配对、重复、独立内容复核和预先声明的用途门槛构成基线方法。这样能区分完成、恢复和过程失败 | 不用唯一参考路径、一次通过或单一自评分决定能力；论文分数不能填成本项目初始基线；不编造统一样本量或百分比门槛 | [资料](whole-system-evidence.md#closure-evaluation)；[评估规格](sandbox-evaluation.md#evaluation-design) |
| 回应与持续活动 | 统一事件、关注表及活动工作区；每次继续须有具体缺口、下一动作和预算；完成、等待、未知和退出分别表达。拆分保留父责任与子产物映射，转交经接纳才生效，重新接纳核对现状；跨日从持久状态接续。默认简短，复杂工作按缺口投入，主体可因兴趣／好恶调整意愿但须交代原责任 | 不靠无限推理或模型自报完成；不以内置闹钟驱动主体；不固定“低投入总是好”或全局最优调度公式。强自主属于设计目标，不宣称论文已证明合意性 | [活动依据](whole-system-evidence.md#closure-activity)、[情境依据](whole-system-evidence.md#closure-interaction)；[运行](whole-system-design.md)、[交流](interaction-design.md) |
| 记忆与世界认知 | 索引、召回、读取分开；名称／精确条件先用元数据及词法，语义缺口按需补向量召回，合并候选时保留出处并去重；范围不足有预算地扩展，仍不足保留未知。跨活动记忆带时间、版本、用途、归属和许可；同源转述不算独立证据，纠正可回查 | 不选向量库作唯一事实库，不默认全量注入或全量索引；不按相似度自动合并人物或采信主张，不以重复转述增加可信度；不预设通用最优切分或融合权重 | [记忆依据](whole-system-evidence.md#closure-memory)；[记忆](whole-system-design.md#memory)、[资源](projection-input-and-compute.md#projection)、[检索工程](engineering-reference.md#vector-service) |
| 心智协作 | 一个主负责心智起步，有明确调查／核对／相关经历需求才邀请；独立贡献后围绕分歧交流，按证据整合。长期人格保留身份、私有经历与意愿，临时角色承担可变职责；总预算约束全部参与者 | 不默认全员讨论、固定专家人数、强制一致或以角色名授予专业性；不把采样增加的收益归因讨论，也不要求长期人格先证明提高任务得分才能存在。人数／轮次按任务上限配置 | [协作依据](whole-system-evidence.md#closure-minds)；[组织机制](whole-system-design.md#organization) |
| 能力与模型 | 公共 API 表达请求、结果、来源、范围和能力差异；外部通知源由能力创建／接入。模型工具提案经宿主接纳，流式片段与终止分开，失败／截断／拒绝不混同。固定默认模型配置，KV 由推理组件管理；向量检索通过公共能力契约接入，产品及部署选择集中于工程参考 | 不自建 KV 计算或默认动态模型路由，不因缓存命中省略事实／权限复核；不把 SDK、同名模型别名或 HTTP 成功当兼容保证。不恢复集群、K8s 或对象存储 | [能力依据](whole-system-evidence.md#closure-capabilities)；[公共端口](runtime-protocol.md#capability-api)、[工程选择](engineering-reference.md) |
| 经验与演化 | 两阶段复盘区分当时可得依据与后来结果；先形成带来源、适用条件、反例和失效条件的 Reference；使用时核对当前情境。程序／策略候选进入独立状态和受控能力的沙箱，扩大采用按预先声明的分能力门槛；保留固定参考与采用历史以识别累计退化 | 不把反思文本或来源任务成功当作迁移，不因反馈自动更新权重／采用代码；获准自主迭代按下方主动学习范围处理，不把模拟人物与状态整体合入现实。缺少采用依据时保持候选身份和原行为，不宣称已学会 | [学习依据](whole-system-evidence.md#closure-learning)；[记忆与采用](whole-system-design.md#memory)、[沙箱](sandbox-evaluation.md) |
| 人物、情感与多模态 | 账号身份带平台命名空间，关联以明确可核对证据和本人意图为准；关联、认证、读取与披露分别控制。情感评价共享任务情境，现实／实际交流／剧情分别归属；主动联系遵守可撤销约定。多模态保留来源、时间、轨道和状态，轨道不等于人物；停止控制优先于认知，身份／受众未知时缩小披露并维持可提供的公共帮助 | 不靠昵称／声纹相似强行跨平台认人，不以亲密降低工作事实标准；不固定爱意分数或问候频次，不因无人回复加频；不把传输标准当说话人识别或端到端实时性证明 | [交互依据](whole-system-evidence.md#closure-interaction)；[人物情境](interaction-design.md)、[输出与控制](runtime-protocol.md#streams) |

<a id="deferred"></a>

## 留给具体用途的配置

这些配置在具体用途接入时确定，不作为待补研究：

| 配置对象 | 由谁在何时确定 | 设计已规定的约束 |
| --- | --- | --- |
| 模型、SDK、服务与设备版本 | 实际接入时由工程配置固定 | 声明能力、处理范围、费用口径与终止语义；不以同名／同结构推定等价 |
| embedding、切分、检索额度 | 按语料与所用 embedding 契约设置 | 索引绑定资源版本和生成配置；覆盖未知可见，跨配置不混查 |
| 主动学习强度与策略 | 有权管理者配置强度及额度，策略在范围内选择议题；具体初始档位随用途确定 | 最低关闭不自发学习；启用有界，副本不能提高额度；自发学习与用户明确任务分开，关闭与在途收束可见 |
| 思考预算、参与人数、轮次与实时目标 | 按活动用途、可用资源和用户要求设置 | 有总上限，全部分支计费；不虚构统一最优数值，无具体进展则停止 |
| 联系渠道、窗口和频率 | 由双方关系／任务约定形成，可修改和撤销 | 不默认跨平台发送，不以无回复提高频率 |
| 能力门槛、样本和基线 | 建立能力基线时，在查看候选成绩前确定 | 质量／成本及关键失败分维度，保留未知和失败，不复用公开调参样本冒充保留任务 |
| 法域与业务规范 | 具体用途接入时绑定适用规范与来源 | 按情境判断适用性；论文或格式通过不构成法律合规证明 |

容量、备份、驱动和故障矩阵继续不作为当前设计前置条件；旧局部证据仅支持原范围。

<a id="management-extension"></a>

## 管理工作台的要求与建议

| 范围 | 状态与唯一正文 |
| --- | --- |
| 完整管理、模型／服务维护 | 已纳入设计；[管理职责与范围](management-workspace.md#coverage) |
| 普通用户的机密归属、专用指令、可信提交及过滤转换 | 设计要求；[机密机制](management-workspace.md#secret-projection)，具体命令名及字段为示意 |
| 可运行 AGI 副本 | 设计要求；基准重建、创建后暂停、分支操作及有限采用为[设计建议](sandbox-evaluation.md#replica) |
| 动态表单、蓝图及代码编辑 | 类型推导、结构化注释和自动生成适配已纳入设计；[编辑映射](management-workspace.md#dynamic-editing)，具体语法与组件未冻结 |
| 提交立即生效 | 按编写契约准备候选、调用边界切换、等待或撤销计算后接续、失败保留旧内容已纳入设计；[生效契约](management-workspace.md#apply) |
| 受管理函数与热加载 | 采用：宿主管长期状态、稳定函数标识、有界调用、类型与注释描述、生成入口及沙箱测试；[编写与调用契约](runtime-protocol.md#managed-functions)、[工程映射](engineering-reference.md#managed-function-tooling) |

资料与未采用方案见[管理依据](management-workspace.md#sources)。既定的热加载方案降低手工适配及任意栈恢复的设计负担；收益是工程判断，未量化性能或开发成本。副本细则仍独立保留建议状态。

<a id="capability-extension"></a>

## 能力构建与接入的设计范围

能力扩展采用以下流程和责任分工，支持 Go、Rust 和 Node.js（npm）实现：

| 范围 | 采用方案与唯一正文 | 未采用方向与理由 |
| --- | --- | --- |
| 完整能力闭环 | 先复用和组合，有缺口才构建；形成可追溯产物、分层试验、按适用范围采用及结果复盘；[总设计](../DESIGN.md#capability-development) | 不默认每个问题都生成工具或把构建成功等同任务能力；目标是开放扩展，非无限资源保证 |
| MRPC 与 Go／Rust／Node.js（npm） | 复用多语言生成、本地／跨进程绑定、资源和替换；外部能力实现由核心宿主管理；[工程选择](engineering-reference.md#capability-toolchain) | 不全函数 RPC 化，不重复建设序列化协议，不将原生动态库装载作为默认，不恢复 TinyAGI 集群 |
| 接口与动态管理 | 跨语言接口有唯一声明来源，内部函数仍用类型与元数据；实现、表单和实际调用绑定一致；[运行契约](runtime-protocol.md#capability-lifecycle)、[管理入口](management-workspace.md#capability-management) | 不并行手写多语言类型与表单，不把路由登记更新当成已有客户端已切换 |
| 试验与运行对象 | 局部程序、能力组合、主体副本分层；构建全过程受控；子工作共享父活动预算；[沙箱](sandbox-evaluation.md#test-scopes) | 不默认全量复制主体，不把子 VM 或独立进程当作完整隔离，不复制生产资源句柄 |
| 库事实与宿主补充 | 固定提交的 RPC、嵌入 API 与检索边界见[接入记录](go-mini-integration.md#rpc-extension-facts) | 未确认库已有通用子进程或脚本子 VM 管理服务；宿主封装是待实现设计，不记录为已完成接入 |

一手资料足以支持以上机制分工，未新增构建成功率、性能或任务收益实测。具体工具链版本、平台隔离适配和投入额度随用途配置，不列作当前未关闭架构项。此前副本重建细则的建议状态保留，这次分层确认不扩大为对所有副本细节的确认。

<a id="node-rpc-extension"></a>

### Node.js 与 npm 能力端补充

2026-09-21 用户明确扩展能力端至 Go／Rust／Node.js（npm），本项为已定设计。沿既有 MRPC 单一接口来源生成 TypeScript／JavaScript 调用与服务适配，复用 npm 生态；程序包、锁定依赖、运行环境及 SDK 资源共同关联固定实现。依赖准备、试验、信任、任务中止、替换与 Secret 继续走原契约，不新建主体或独立管理后端。

选择理由是使用现有 JavaScript SDK／包及库已有 RPC 支持；不要求把 npm 能力改写为 Go／Rust，也不强制所有能力转为 Node。当前 Node SDK 的 WebSocket 接入与 Go／Rust 的可选原生传输分别装配，不假定全部传输对等。库依据见[固定快照](go-mini-integration.md#javascript-rpc-facts)，工程方式见[Node 接入](engineering-reference.md#node-rpc-integration)；尚无本项目 Node 接入实测结果。

<a id="active-learning-extension"></a>

## 主动学习与自我迭代的设计范围

主动学习扩展及其强度控制已纳入设计，最低强度为关闭。具体学习策略和长期收益仍具有实验性。

| 范围 | 采用决定与唯一正文 |
| --- | --- |
| 主动发起与持续经营 | 兴趣、成长方向、未来用途、能力盲区和环境变化均可提出学习议题；复用目标、活动和资源；[主体学习](whole-system-design.md#active-learning) |
| 实践与自我迭代 | 阅读、练习、构建、整理与迁移分工；可在分支改进学习策略本身，研究价值与正式采用分开；[总体机制](../DESIGN.md#active-learning)、[学习评价](sandbox-evaluation.md#learning-evaluation) |
| 学习强度与关闭 | 宿主强制执行有界投入，最低关闭；不自主发起／继续学习及自动采用待用候选，在途按停止规则收束；普通任务、正常记忆和已有能力使用保持；[运行契约](runtime-protocol.md#learning-intensity) |
| 用户明确学习任务 | 按独立任务及预算接纳，不隐式打开主动学习，也不借任务名继续后台学习；来源由宿主绑定；同上契约 |
| 管理与接入 | 页面维护强度、有效额度、议程和采用结果；复用 go-mini／MRPC 与既有宿主；[工作台](management-workspace.md#learning-management)、[工程映射](engineering-reference.md#active-learning-integration)、[库接入](go-mini-integration.md#active-learning-adapter) |

资料支持课程、反馈记忆及代码迭代的分工，不证明本项目长期成长收益、最佳强度或任意任务自我提升。具体预设名称、数值、初始强度、探索比例、课程算法及可选训练框架按用途配置，不列作当前架构未关闭项。学习不能修改正在使用的评价规则或扩大权限。资料与替代项见[学习依据](whole-system-evidence.md#active-learning-sources)。

<a id="initialization-extension"></a>

## 提示词初始化与个体自迁移的设计范围

初始化采用完整提示词，迁移采用差异与语义说明；共同运行契约与个体实现分别维护。

| 范围 | 采用决定与唯一正文 |
| --- | --- |
| 初始化与个体差异 | 当前完整提示词引导产生最小人物与个体程序，接受模型及人格差异，必要运行契约一致；[人物形成](whole-system-design.md#self-initialization) |
| 个体迁移 | 相邻文本 diff 配套语义说明，按实际代码和迁移项自行适配；保留主体身份、历史和配置，跨修订有覆盖关系；[运行协议](runtime-protocol.md#bootstrap-migration) |
| 引导与维护 | 宿主入口独立于生成程序，首次生成和失败修复均有预算、诊断与候选采用；固定管理不依赖认知启动；[工作台](management-workspace.md#initialization-management) |
| 弃用及兼容 | 注释提示加真实旧接口实现，保留若干稳定 API 契约修订；语言及客户端变化另核对，缓存不作启动保证；[工程参考](engineering-reference.md#prompt-bootstrap)、[库事实](go-mini-integration.md#deprecation-facts) |
| 关闭主动学习 | 获准的必要兼容维护独立接纳，不提高学习强度或权限，不扩展为自主能力探索；[引导契约](runtime-protocol.md#bootstrap-migration) |
| 评价 | 检查共同契约、连续性及受影响功能，不要求所有个体同码同答；未来检查场景已定义，尚未执行；[沙箱](sandbox-evaluation.md#initialization-evaluation) |

未采用统一人格程序覆盖、向所有个体套用同一源码补丁、更新即重建人物、仅标弃用而不保留行为或永久携带全部旧运行时。理由及资料见[工程取舍](engineering-reference.md#prompt-bootstrap)与[证据记录](whole-system-evidence.md#initialization-migration-sources)。具体提示词正文、首次模型／预算、兼容保留数量和正式接口标识在未来发布或接入时固定，属于用途及支持策略，当前不伪造数值或新增待执行实验。生成可用率、长期人格连续性和跨客户端兼容效果未实测。

<a id="prebuilt-extension"></a>

## 客户端预制能力库的设计范围

预制库随核心客户端交付与更新，权威定义和实现对 Self 只读。Self 可选择使用、组合、独立包装或不使用。维护权、调用权限和实际作用分别定义，运行约束仍由宿主执行；适用范围包括初始化、正常认知、维护及管理。

逻辑及选择理由见[总设计](../DESIGN.md#prebuilt-capabilities)，详细职责见[运行契约](runtime-protocol.md#prebuilt-library)，客户端与库装配见[工程参考](engineering-reference.md#client-library)。

[管理入口](management-workspace.md#prebuilt-management)区分预制定义、使用配置及个体包装；[沙箱评价](sandbox-evaluation.md#prebuilt-evaluation)覆盖实际依赖和共同契约。新增能力供个体选用，已依赖实现的更新按兼容政策及实际迁移处理，未采用强制统一人格或自动改写个体程序的方式。

固定提交的[库依据](go-mini-integration.md#prebuilt-library-facts)支持源码装配、文档与语言工具接入；维护归属属于设计约束，初始化收益属于工程判断。具体函数清单、模块前缀和参数在实际接入时确定，不新增待执行实验；当前没有产品实现或新增效果实测。

<a id="task-control-extension"></a>

## 核心／任务解耦与外部控制的设计范围

主体、业务任务、认知执行和外部操作具有独立生命周期。任务超时或失败不结束 Self，也不长期占用认知入口；长工作独立管理，结果通过事件接续。控制台、获授权用户及安全审计模块可通过宿主直接打断执行、阻断推进或中止任务，不等待认知批准。

| 设计范围 | 正文及边界 |
| --- | --- |
| 持续主体与独立任务 | [总设计](../DESIGN.md#core-task-control)、[主体场景](whole-system-design.md#task-independence)、[生命周期](runtime-protocol.md#core-task-lifecycle)；资源和预算仍受共同约束，不承诺无条件即时模型回应 |
| 控制与收尾 | [运行契约](runtime-protocol.md#task-control)；控制资格和实际停止分开，子工作、新派发及迟到结果纳入范围，无关工作保持 |
| 审计及解除 | 授权决定与建议分开，限定可信来源和范围；多原因解除及重新接纳不能绕过有效阻断；审计算法和全面检查流程未预设 |
| 管理和评价 | [工作台](management-workspace.md#task-control-management)、[评价场景](sandbox-evaluation.md#task-control-evaluation)；已定义未来验收，不新增待执行实验 |
| 真实库接入 | [固定提交源码及测试阅读](go-mini-integration.md#task-control-facts)、[工程装配](engineering-reference.md#task-execution)；任务控制映射由宿主补充，资料核对不等于运行验证 |

原报告 014 的异步 FFI 与顺序跨实例接续不覆盖慢任务期间处理新输入、审计中止及故障隔离的完整场景。当前状态为设计已定、接入与实测未完成。具体容量、期限及审计规则按用途或后续明确需求确定。

<a id="architecture-consistency"></a>

## 跨模块的一致性规则

下表统一跨模块的职责与时序规则。这些是依据既有资料和库行为形成的设计选择，不构成新增实验结果；完整副本重建细则仍属于设计建议。

| 范围 | 最终采用方案及理由 | 排除的解释与唯一正文 |
| --- | --- | --- |
| 控制对象与传播 | Episode 是持续活动，Task 是活动内可选任务安排，Operation 是已接纳工作；当前尝试另有执行身份。控制携带类型与传播范围，认知中断和任务停止各有归属 | 不使用含义不明的“任务 ID”，不因认知被取消而自动终止独立操作；[生命周期与控制](runtime-protocol.md#core-task-lifecycle) |
| 步骤与操作接纳 | 步骤内通过独立入口接纳请求，保留稳定请求键与回执；最终提案引用已有操作并接纳剩余意图。支持先读工具结果再作判断，也保留失败前已发生的成本和效果 | 不重复派发，不用最终提交失败抹去独立工作；[时序](runtime-protocol.md#step-operation-admission) |
| 统一主体的公共决定 | 私有 Mind 状态、受委托活动决定与 Self 公共提案分开；指定既有心智承担整合，按证据与责任裁定，未决保留原公共状态 | 不设永久最高人格、不以写入先后或多数票取代公共决定；[公共整合](whole-system-design.md#public-decisions) |
| 配置与当前约束 | 代码及普通行为配置随执行固定；覆盖按声明范围解析，授权、Secret、额度、学习关闭和控制按当前值核对 | 不采用无条件最后写入胜出，不让旧配置冻结有效控制；[配置解析](runtime-protocol.md#configuration-resolution) |
| 个体持久状态 | 个体自由定义主观逻辑，宿主管归属、结构、修订、可见与写入范围及转换；程序和数据结构一致采用 | 不强制统一人格数据，也不把自定义内容变成第二份公共真值；[状态契约](runtime-protocol.md#individual-state) |
| 能力采用与实现信任 | 功能采用、实现来源／产物信任、用途授权分别成立；受信维护者或既定发布策略授予资格，执行环境满足声明约束才接纳 | 不从测试通过、相同接口或模型自评推导机密访问权；[实现准入](runtime-protocol.md#implementation-trust) |
| 学习与任务构建 | 关闭主动学习保留必要任务内工具构建；长期安装、泛化和改变主体默认策略另有采用范围。启用探索时可主动提出策略候选 | 不按“是否写代码”分类，不强制先反复失败才产生程序候选；[学习强度](runtime-protocol.md#learning-intensity) |
| 作用与停止反馈 | Effect 跟踪预期或可能作用，不等同已发生；禁止原业务交付不禁止按受众发送控制回执和必要退出说明 | 不伪造已停止或已成功，不借控制通知恢复任务；[效果](runtime-protocol.md#effects)、[控制](runtime-protocol.md#task-control) |
| 文档层次与证据 | 总图先给一级职责，再提供完整关系图；当前逻辑、工程承载、库固定快照、受限模型证据及历史材料各归其位置 | 不把当前源码链接当不可变快照，不把未测写成没有任何模型证据；[维护规范](documentation-guide.md)、[快照入口](go-mini-integration.md#source-snapshots) |
| 沙箱范围与建议状态 | 通用局部试验按需装配；完整副本请求按既有建议继承完整授权范围。工作台按所选试验模式展示继承范围和缺失状态 | 不以最小任务切片冒称完整副本，重建细则仍待确定；[副本建议](sandbox-evaluation.md#replica) |

对应检查场景集中于[跨契约评价规格](sandbox-evaluation.md#contract-consistency-evaluation)。这些规则尚无完整组合实验结果。

<a id="next-steps"></a>

## 后续维护

新需求、相反证据或实际任务中的失败可能触发设计调整。调整时明确受影响的目标、机制与适用范围；实现、实验和文档维护分别说明各自结果。

当前按[维护规范](documentation-guide.md#workflow)保留资料日期、版本、命题与推论，检查总图、职责、场景和链接的一致性。如果以后另行开展实验，预登记、冻结、失败保留和证据分类规则继续适用；不能改写旧输入和成绩。
