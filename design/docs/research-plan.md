# 设计决策与适用边界

用途：设计决策台账。

[总设计](../DESIGN.md#validation) · [文档索引](README.md) · [资料依据](whole-system-evidence.md#design-closure)

本篇集中说明设计约束、采用方案、待定细节和用途配置。资料支持的机制选择与实际验证范围分别记录。

| 阅读主题 | 章节入口 |
| --- | --- |
| 总体状态 | [当前范围](#research-status) · [状态定义](#closure-status) · [主体运行](#whole-system) · [基础设计](#remaining-questions) · [用途配置](#deferred) |
| 领域与扩展 | [领域对象与视图](#domain-boundaries) · [外部检索提供者](#retrieval-design) · [计算节约](#efficiency-design) · [独立机密](#secret-management) · [管理工作台](#management-extension) · [能力扩展](#capability-extension) · [Node.js 补充](#node-rpc-extension) · [主动学习](#active-learning-extension) |
| 个体与控制 | [初始化与迁移](#initialization-extension) · [预制能力库](#prebuilt-extension) · [隔离执行](#isolated-execution-extension) · [任务控制](#task-control-extension) · [架构一致性](#architecture-consistency) |
| 维护 | [执行库验证](#library-validation) · [后续维护](#next-steps) |

<a id="research-status"></a>

## 当前范围

当前处于设计阶段，以既有实验和一手资料明确机制，不推进产品实现或新增模型调用。执行库更新可单独开展固定提交的回归与接入核对；当前范围见[库更新验证](#library-validation)。逻辑设计、工程映射和实测证据分别维护，库测试不构成产品实现。

实施顺序、首批交付范围及阶段验收集中维护于[实施方案](../TODO.md)，规划中的交付和检查条件不计为已经实现或验证。

<a id="library-validation"></a>

### 执行库更新验证

go-mini 以固定提交 `fbb16ee99748e84b523bbd677bd477258c358956` 作为新的核对基线。采用上游测试检查执行与取消、热更新、编译缓存、MRPC 生成及 Go／Rust／Node 接入；逐项结果和环境边界唯一见[报告 018](experiments/018-go-mini-library-validation.md)，当前接口解释见[库参考](go-mini-integration.md#current-verification)。

保留单宿主、有限认知入口、业务任务独立管理和外部能力接入的设计。库内部并行、SDK 队列、采样统计与编译器会话各按实际职责使用，不把它们扩展为完整任务调度器、主体克隆或机密服务。后续依赖更新按[固定流程](go-mini-integration.md#update-verification)检查差异及受影响范围，旧报告不被新成绩覆盖；完整主体、实际模型效果和跨平台发行仍不在该库验证范围。

<a id="closure-status"></a>

## 状态及其含义

| 状态 | 适用对象 | 含义 |
| --- | --- | --- |
| 设计约束 | 持续主体、自主认知、强自主意愿、统一事件、按需内容、完整管理与机密可信使用等系统要求 | 必须在架构与专题保持一致；不表示已实现 |
| 已定设计 | 主体直接认知、按需活动、领域分责、同级检索、编写与热加载、能力扩展、学习与初始化、任务解耦、授权委托、接纳前交互、记忆维护、上下文有效性、有限纠正及按问题装配的主体级试验 | 结合资料与既有局部证据形成的机制选择；可作为后续设计及实现依据，不表示效果已经验证 |
| 用途配置 | 模型、设备、预算、联系窗口和评价门槛等 | 随具体用途确定，不是未关闭架构问题 |
| 历史证据 | 报告、脚本、输入、失败与原始数据 | 仅支持其固定条件，不是当前任务队列 |

基础架构与试验主体的装配规则已有明确方案，完整状态导入是受用途及兼容条件限制的可选方式。实际能力、性能和真人体验尚无完整测量，属于证据边界；接口签名、具体表示和额度留给用途及工程配置，不将其视为未关闭的逻辑问题。

<a id="whole-system"></a>

## 主体持续运行与活动组织

主体从环境线索、当前处境、兴趣与未决问题出发，组织心智和异构能力，行动或调整关注，并积累经历。Step 和能力调用可直接归属 Self／Mind；交流、Episode 和 Task 按需要关联。认知程序决定方法与主观意义，宿主落实状态、执行、额度及停止；完整任务的接纳与交付用于具体承担的工作。

正常认知、自主日常活动和经历积累不受主动学习关闭影响；专门研究、练习、能力实验与认知程序迭代受学习强度限制。机密默认保持引用，受信组件按实际用途取得原值，重点防止不可信 API 及非预期接收方获得秘密。

评价覆盖无新对话时的主体活动、注意选择、异构能力、经历影响和中断接续，并保留完整任务的责任与成本评价。原实验只支持各自任务或组件条件，未证明完整自主运行效果。[主体机制](whole-system-design.md#overview)、[直接认知契约](runtime-protocol.md#cognitive-scope)、[评价范围](sandbox-evaluation.md#subject-evaluation)

<a id="remaining-questions"></a>

## 决策台账

下表各项均为**已定设计**。资料和局部实验支持所列机制与取舍；将它们组合为完整系统属于本项目的设计判断。自主意愿、长期人格等价值取向属于项目目标，与可测量的能力效果分别记录。

| 原问题 | 最终采用方案与理由 | 未采用／暂缓方案及原因 | 资料与正文 |
| --- | --- | --- | --- |
| 主体认知与活动关系 | Self／Mind 可直接开展认知，Goal 保存持续意图，Episode 按需组织活动，Task 保存执行安排；保持主体在无对话、无任务时的连续性 | 不把请求接纳或固定任务树设为思考前提，不让宿主审批主观意义 | [主体运行](whole-system-design.md#loop)、[运行归属](runtime-protocol.md#cognitive-scope) |
| 完整任务与能力评价 | 以任务契约和有效结果集合验收；分能力画像，同时计质量、责任与成本；开发／回归／保留任务分开；同条件配对、重复、独立内容复核和预先声明的用途门槛构成基线方法。这样能区分完成、恢复和过程失败 | 不用唯一参考路径、一次通过或单一自评分决定能力；论文分数不能填成本项目初始基线；不编造统一样本量或百分比门槛 | [资料](whole-system-evidence.md#closure-evaluation)；[评估规格](sandbox-evaluation.md#evaluation-design) |
| 回应与持续活动 | 统一事件、关注表及活动工作区；认知可从内在关注或环境变化直接接续，具体活动保留下一步和投入范围；完成、等待、未知和退出分别表达。拆分保留父责任与子产物映射，转交经接纳才生效，重新接纳核对现状；跨日从持久状态接续。默认简短，复杂工作按缺口投入，主体可因兴趣／好恶调整意愿但须交代原责任 | 不靠无限推理或模型自报完成；不以内置闹钟驱动主体；不固定“低投入总是好”或全局最优调度公式。强自主属于设计目标，不宣称论文已证明合意性 | [活动依据](whole-system-evidence.md#closure-activity)、[情境依据](whole-system-evidence.md#closure-interaction)；[运行](whole-system-design.md)、[交流](interaction-design.md) |
| 记忆与世界认知 | 领域真值、外部检索和内容读取分开；按缺口选择合格提供者，来源保留时间、修订、归属和用途。同源转述或重复命中不增加独立证据，纠正可回查，覆盖不足保留未知 | 不选检索服务作唯一事实库，不默认全量注入或提交全部服务；不按相关性自动认人或采信主张，不预设通用最优查询策略 | [记忆依据](whole-system-evidence.md#closure-memory)；[记忆](whole-system-design.md#memory)、[视图](materials-and-context.md#projection)、[检索分工](#retrieval-design) |
| 心智协作 | 一个主负责心智起步，有明确调查／核对／相关经历需求才邀请；独立贡献后围绕分歧交流，按证据整合。长期人格保留身份、私有经历与意愿，临时角色承担可变职责；总预算约束全部参与者 | 不默认全员讨论、固定专家人数、强制一致或以角色名授予专业性；不把采样增加的收益归因讨论，也不要求长期人格先证明提高任务得分才能存在。人数／轮次按所属认知或活动额度配置 | [协作依据](whole-system-evidence.md#closure-minds)；[组织机制](whole-system-design.md#organization) |
| 能力与模型 | 公共 API 表达请求、结果、来源、范围和能力差异；外部通知源由能力创建／接入。模型工具提案经宿主接纳，流式片段与终止分开，失败／截断／拒绝不混同。认知按用途选择已装配的模型、感知、算法和工具，提供者经接口执行实际计算 | 自动路由优化可后续扩展，不以 SDK、同名模型别名或 HTTP 成功推定兼容；不省略事实与权限核对。不恢复集群、K8s 或对象存储 | [能力依据](whole-system-evidence.md#closure-capabilities)；[公共端口](runtime-protocol.md#capability-api)、[工程选择](engineering-reference.md) |
| 计算节约与性能保持 | 利用提供者前缀复用、稳定装配、有效结果、相同只读工作合并、增量准备及有界运行复用，减少重复工作并保留主体行为 | 不用旧答案代替独立判断，不为命中扩大上下文、冻结状态或自动降级模型；供应商机制不证明网关透传或完整收益 | [逻辑规则](materials-and-context.md#cache)、[运行](runtime-protocol.md#execution-reuse)、[一手依据](engineering-reference.md#efficiency-sources) |
| 计算方式与可选组件 | 按缺口组合规则、经验、专用计算、轻量判断与生成式推理，减少不必要工作；外部开源实现沿已有能力体系按需接入 | 不设固定快慢主体或必经判断层；具体实现保留候选身份，不指定默认组件，资料不构成本项目收益实测 | [有限思考](materials-and-context.md#effort)；[候选与资料](engineering-reference.md#optional-cognition-components) |
| 经验与演化 | 两阶段复盘区分当时可得依据与后来结果；先形成带来源、适用条件、反例和失效条件的 Reference；使用时核对当前情境。程序／策略候选进入独立状态和受控能力的沙箱，扩大采用按预先声明的分能力门槛；保留固定参考与采用历史以识别累计退化 | 不把反思文本或来源任务成功当作迁移，不因反馈自动更新权重／采用代码；获准自主迭代按下方主动学习范围处理，不把模拟人物与状态整体合入现实。缺少采用依据时保持候选身份和原行为，不宣称已学会 | [学习依据](whole-system-evidence.md#closure-learning)；[记忆与采用](whole-system-design.md#memory)、[沙箱](sandbox-evaluation.md) |
| 人物、情感与多模态 | 账号身份带平台命名空间，关联以明确可核对证据和本人意图为准；关联、认证、读取与披露分别控制。情感评价结合主体处境与交流情境，现实／实际交流／剧情分别归属；主动联系遵守可撤销约定。多模态保留来源、时间、轨道和状态，轨道不等于人物；停止控制优先于认知，身份／受众未知时缩小披露并维持可提供的公共帮助 | 不靠昵称／声纹相似强行跨平台认人，不以亲密降低工作事实标准；不固定爱意分数或问候频次，不因无人回复加频；不把传输标准当说话人识别或端到端实时性证明 | [交互依据](whole-system-evidence.md#closure-interaction)；[人物情境](interaction-design.md)、[输出与控制](runtime-protocol.md#streams) |

<a id="deferred"></a>

## 留给具体用途的配置

这些配置在具体用途接入时确定，不作为待补研究：

| 配置对象 | 由谁在何时确定 | 设计已规定的约束 |
| --- | --- | --- |
| 模型、SDK、服务与设备版本 | 实际接入时由工程配置固定 | 声明能力、处理范围、费用口径与终止语义；不以同名／同结构推定等价 |
| 复用策略、容量与费用口径 | 接入实际提供者时声明支持方式，按用途设置保存、回收、并发与允许等待范围 | 所需信息、独立判断、期限和权限不因命中而改变；实际费用、估算与未知分开，不固化统一期限或折扣 |
| 检索绑定、策略、材料准备与额度 | 按领域用途、实际提供者契约及语料设置 | 提供者同级，材料关联对象类型和修订，覆盖未知可见；特有参数留在对应适配，不强制全部实现支持 |
| 主动学习强度与策略 | 有权管理者配置强度及额度，策略在范围内选择议题；具体初始档位随用途确定 | 最低关闭不自发学习；启用有界，试验主体不能提高额度；自发学习与用户明确任务分开，关闭与在途收束可见 |
| 思考预算、参与人数、轮次与实时目标 | 按活动用途、可用资源和用户要求设置 | 有总上限，全部分支计费；不虚构统一最优数值，无具体进展则停止 |
| 联系渠道、窗口和频率 | 由双方关系／任务约定形成，可修改和撤销 | 不默认跨平台发送，不以无回复提高频率 |
| 能力门槛、样本和基线 | 建立能力基线时，在查看候选成绩前确定 | 质量／成本及关键失败分维度，保留未知和失败，不复用公开调参样本冒充保留任务 |
| 法域与业务规范 | 具体用途接入时绑定适用规范与来源 | 按情境判断适用性；论文或格式通过不构成法律合规证明 |

容量、备份、驱动和故障矩阵继续不作为当前设计前置条件；旧局部证据仅支持原范围。

<a id="retrieval-design"></a>

## 领域检索与同级外部提供者

检索作为正式外部能力类别、领域入口与提供者分层、各实现同级接入为已定设计。提供者可发现、指定调用、配置、维护及评价，实际安装和启用可选；具体组件与接口见[向量服务及 Attemory 接入](engineering-reference.md#retrieval-providers)。

| 决定 | 理由及适用边界 |
| --- | --- |
| 领域定义查询含义，公共接入负责调用组织 | 记忆、资料、程序定位和能力发现可复用接入，同时保留对象类型、状态所有权和处理范围 |
| 提供者同级，默认配置按用途确定 | 不固定某实现为必经通路或后备，也不要求每次调用全部服务；具体计算和服务内部状态由外部组件维护 |
| 支持指定、单次、并行、分步及替代查询 | 调用记录保留提供者贡献，所有分支共用原认知或活动预算；得分不直接比较，同源重复不增加独立证据 |
| 材料准备与来源映射独立管理 | 外部空间不等同于人物或会话；明确范围内可以批量准备及持续同步，登记对象不自动提交全文 |
| 管理与评价覆盖完整接入 | 查询、材料提交与维护权限分开；配置提交、准备完成及实际可查分别报告，单提供者与组合策略同条件评价 |

采用现成 API／SDK 减少专用引擎开发，代价是接口差异、材料同步和外部服务维护。拒绝用统一向量字段约束全部实现，也不把所有领域查询改成通用资源管理。逻辑在[总设计](../DESIGN.md#retrieval)与[运行契约](runtime-protocol.md#retrieval)，操作在[工作台](management-workspace.md#retrieval-management)，评价在[沙箱](sandbox-evaluation.md#retrieval-evaluation)。

依据为[官方接口资料](engineering-reference.md#retrieval-sources)及[向量服务契约](engineering-reference.md#vector-sources)。报告 013／014 的局部查询与组合不覆盖这些外部服务，资料不证明本项目检索质量、组合收益或端到端性能；实际接入版本、策略及预算归用途配置，不新增验证前置任务。

<a id="efficiency-design"></a>

## 计算节约与复用的设计范围

分层复用与增量处理为已定设计。认知决定材料及计算用途，各处理能力复用符合条件的输入处理、结果和准备工作，宿主共用预算、控制及观测；不建立统一资源实体或独立缓存服务。方案以保持所需信息、计算目的、响应要求和正常主体行为为前提。

| 采用项 | 选择理由与适用边界 |
| --- | --- |
| 稳定输入与提供者前缀复用 | 减少相同输入的重复处理，当前输出仍重新生成；装配不统一人格、不任意重排语义，实际命中及费用按服务反馈 |
| 有效结果及相同只读工作合并 | 避免重复读取、解析和确定计算；保留各请求归属、权限及取消，实际执行成本只计一次，独立采样不合并 |
| 增量准备与有界运行复用 | 复用未变材料、依赖和合格运行准备；无法确认影响范围时重算，必要状态独立保存，后台批量不损害实时要求 |
| 完整性能与费用观察 | 同时观察质量、行为、响应、控制、费用及占用；首次准备、重复使用和失效重建分别报告，未知不视为零成本 |

不采用按相似问题默认复用答案、为命中保留无关材料、默认空请求保温、无界常驻，以及以节约名义暗中降级模型或降低学习强度。改变信息、采样或认知组织的方案仍按行为候选评价，不能直接取得透明优化资格。

一手资料支持采用机制，现有实验不构成完整节约基线；网关参数、实际折扣和端到端净收益仍受具体接入与负载限制。容量、期限、收费口径及用途门槛属于配置，不自动新增实验待办。[逻辑](../DESIGN.md#resource-efficiency)、[资料与取舍](engineering-reference.md#efficiency-sources)、[管理](management-workspace.md#efficiency-management)、[评价](sandbox-evaluation.md#efficiency-evaluation)

<a id="domain-boundaries"></a>

## 领域对象与受限视图的设计范围

资料、记忆、程序、配置、模型、运行对象、事件源、索引、缓存和机密按各自业务契约管理为已定设计。投影保留为面向当前接收者的受限视图，不采用统一资源实体、公共属性必填表或万能读写接口。详细定义见[对象与所有权](materials-and-context.md#domain-objects)。

| 决策 | 理由与唯一正文 |
| --- | --- |
| 按状态所有者及实际操作划分 | 文档读取、记忆修订、程序采用、模型加载和缓存清理含义不同；[领域边界](materials-and-context.md#domain-objects) |
| 资料、判断和程序分别维护 | 原文不随断言修订而覆盖，Reference 专指可复用知识／方法，文件承载不改变对象归属；[资料契约](materials-and-context.md#materials-contract)、[记忆](whole-system-design.md#memory) |
| 交付内容与业务记录关联 | 正文由文档或程序产物维护，活动保存要求，交付与评价保存各自结果，不复制正文真值；[管理详情](management-workspace.md#domain-management) |
| 共用机制保持有限 | 共享带类型引用、可信调用上下文、来源关联、查询及页面工具；具体操作由各领域接纳；[运行协议](runtime-protocol.md#domain-operations) |
| 视图、读取和执行使用分开 | 对象登记、程序加载、模型运行及管理员查看不自动向认知展开内容；[认知输入](materials-and-context.md#context-reading) |
| 来源派生与运行使用分开 | 摘要、向量和构建产物保留来源，使用模型或凭据不使全部结果成为权重或机密派生；[关系规则](materials-and-context.md#provenance) |
| 按领域装配沙箱 | 分别声明只读基准、可写状态和试验操作，不克隆生产会话或授权；[装配规则](sandbox-evaluation.md#isolation) |

代价是维护各领域接口及关联；不按文件格式拆分职责，不为每个对象新建服务、数据库或审批，不把投影重新包装成通用对象管理器。具体签名及存储结构留给工程接入，逻辑拆分保持原单机承载选择。

[Microsoft 领域分析、NIST 属性授权与 W3C 来源模型](materials-and-context.md#domain-evidence)支持职责划分及共用机制，适用版本及支持命题由专题保存。报告 012／013 仅支持原读取和发现条件，不证明全部领域接入或完整隔离已测；不新增待执行实验。

<a id="secret-management"></a>

## 独立机密管理的设计范围

Secret 独立保管、可信提交、授权使用及必要记录为已定设计。目标是让凭据完成预期用途，并避免泄漏到不可信远程 API 或其他非预期对象；普通认知默认使用引用，实际接收方按组件、用途与目标确定。

| 决策 | 理由与唯一正文 |
| --- | --- |
| 独立身份、归属及授权 | 普通资料读取不解析原值，用户可维护自己的凭据；[对象与权限](management-workspace.md#secret-concepts) |
| 代理使用与原值交付并存 | 受信适配器和 RPC SDK 可正常使用凭据，既有授权内无需逐次确认；[专用契约](runtime-protocol.md#secret-contract) |
| 按实际接收边界配置 | 本地不自动可信，远程认证目标可以合格；确需原值的计算组件走专用输入，模型／工具标签不替代信任判断；[处理流程](management-workspace.md#secret-pipeline) |
| 普通上下文、日志与导出保持引用 | 防止无关模型、遥测或其他接口接收秘密；测试用途单独配置；[评价规格](sandbox-evaluation.md#secret-evaluation) |
| 必要使用记录与当前效力 | 保留授权、领取及结果，撤销限制后续访问，已交付值的上游效力另行处理；[记录与撤销](management-workspace.md#secret-audit) |
| 加密与外发控制分责 | 保管和传输采用工程保护，实际接收方及请求目标另行约束；[工程映射](engineering-reference.md#maintenance-secrets) |

不采用禁止全部执行方取得原值、按技术类型一律禁止或放行、每次使用重新审批，以及用密文存储替代出站边界检查。独立模块不要求新增服务或数据库；原值交付依赖实际接收方可信性，未运行新的机密实验。来源及支持范围见[资料](management-workspace.md#secret-sources)与[库接入事实](go-mini-integration.md#secret-rpc-facts)。

<a id="management-extension"></a>

## 管理工作台的设计范围

| 范围 | 状态与唯一正文 |
| --- | --- |
| 完整管理、模型／服务维护 | 已纳入设计；[管理职责与范围](management-workspace.md#coverage) |
| 独立机密、用户归属、可信提交、授权分配及访问审计 | 已定设计；[机密机制](management-workspace.md#secret-management)，命令名及字段为示意，状态见[机密设计范围](#secret-management) |
| 可运行试验主体 | 已定设计；按问题选择实际程序、所需初态及环境，默认暂停，只激活指定工作，按覆盖评价并有限采用；[试验契约](sandbox-evaluation.md#trial-subject) |
| 完整状态导入 | 可选能力；用于有明确范围的迁移或长期行为评价，限定支持的状态格式、程序及环境，不要求任意扩展的通用克隆；[初态与导入](sandbox-evaluation.md#trial-initial-state) |
| 动态表单、蓝图及代码编辑 | 类型推导、结构化注释和自动生成适配已纳入设计；[编辑映射](management-workspace.md#dynamic-editing)，具体语法与组件未冻结 |
| 提交立即生效 | 按编写契约准备候选、调用边界切换、等待或撤销计算后接续、失败保留旧内容已纳入设计；[生效契约](management-workspace.md#apply) |
| 受管理函数与热加载 | 采用：宿主管长期状态、稳定函数标识、有界调用、类型与注释描述、生成入口及沙箱测试；[编写与调用契约](runtime-protocol.md#managed-functions)、[工程映射](engineering-reference.md#managed-function-tooling) |

资料与未采用方案见[管理依据](management-workspace.md#sources)。既定的热加载方案降低手工适配及任意栈恢复的设计负担；收益是工程判断，未量化性能或开发成本。

<a id="capability-extension"></a>

## 能力构建与接入的设计范围

能力扩展采用以下流程和责任分工，支持 Go、Rust 和 Node.js（npm）实现：

| 范围 | 采用方案与唯一正文 | 未采用方向与理由 |
| --- | --- | --- |
| 完整能力闭环 | 先复用和组合，有缺口才构建；形成可追溯产物、分层试验、按适用范围采用及结果复盘；[总设计](../DESIGN.md#capability-development) | 不默认每个问题都生成工具或把构建成功等同任务能力；目标是开放扩展，非无限资源保证 |
| MRPC 与 Go／Rust／Node.js（npm） | 复用多语言生成、本地／跨进程绑定、资源和替换；外部能力实现由核心宿主管理；[工程选择](engineering-reference.md#capability-toolchain) | 不全函数 RPC 化，不重复建设序列化协议，不将原生动态库装载作为默认，不恢复 TinyAGI 集群 |
| 接口与动态管理 | 跨语言接口有唯一声明来源，内部函数仍用类型与元数据；实现、表单和实际调用绑定一致；[运行契约](runtime-protocol.md#capability-lifecycle)、[管理入口](management-workspace.md#capability-management) | 不并行手写多语言类型与表单，不把路由登记更新当成已有客户端已切换 |
| 试验与运行对象 | 局部程序、能力组合、主体级试验分层；构建全过程受控；子工作共享父活动预算；[沙箱](sandbox-evaluation.md#test-scopes) | 不默认全量复制主体，不把子 VM 或独立进程当作完整隔离，不复制生产资源句柄 |
| 库事实与宿主补充 | 固定提交的 RPC、嵌入 API 与检索边界见[接入记录](go-mini-integration.md#rpc-extension-facts) | 未确认库已有通用子进程或脚本子 VM 管理服务；宿主封装是待实现设计，不记录为已完成接入 |

一手资料支持以上机制分工，尚无完整构建成功率、性能或任务收益实测。具体工具链版本、平台隔离适配和投入额度随用途配置。

<a id="node-rpc-extension"></a>

### Node.js 与 npm 能力端补充

能力端支持 Go／Rust／Node.js（npm），本项为已定设计。沿既有 MRPC 单一接口来源生成 TypeScript／JavaScript 调用与服务适配，复用 npm 生态；程序包、锁定依赖、运行环境及 SDK 分发文件共同关联固定实现。依赖准备、试验、信任、任务中止、替换与 Secret 继续走原契约，不新建主体或独立管理后端。

选择理由是使用现有 JavaScript SDK／包及库已有 RPC 支持；不要求把 npm 能力改写为 Go／Rust，也不强制所有能力转为 Node。当前 Node SDK 的 WebSocket 接入与 Go／Rust 的可选原生传输分别装配，不假定全部传输对等。库依据见[固定快照](go-mini-integration.md#javascript-rpc-facts)，当前实测范围见[报告 018](experiments/018-go-mini-library-validation.md)；[Node 工程接入](engineering-reference.md#node-rpc-integration)中的完整服务管理与能力采用仍属设计。

<a id="active-learning-extension"></a>

## 主动学习与自我迭代的设计范围

主动学习扩展及其强度控制已纳入设计，最低强度为关闭。具体学习策略和长期收益仍具有实验性。

| 范围 | 采用决定与唯一正文 |
| --- | --- |
| 主动发起与持续经营 | 兴趣、成长方向、未来用途、能力盲区和环境变化均可提出学习议题；复用目标、活动、资料、记忆及程序候选；[主体学习](whole-system-design.md#active-learning) |
| 实践与自我迭代 | 阅读、练习、构建、整理与迁移分工；可在分支改进学习策略本身，研究价值与正式采用分开；[总体机制](../DESIGN.md#active-learning)、[学习评价](sandbox-evaluation.md#learning-evaluation) |
| 学习强度与关闭 | 宿主强制执行有界投入，最低关闭；不自主发起／继续学习及自动采用待用候选，在途按停止规则收束；正常认知、自主日常活动、经历积累和已有能力使用保持；[运行契约](runtime-protocol.md#learning-intensity) |
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

<a id="isolated-execution-extension"></a>

## 可选隔离执行的设计范围

隔离执行是默认提供契约、按需装配环境的预制能力。高风险能力按实际实现、用途和请求匹配强制限制；环境缺失时主体及其他合格能力继续可用，受影响操作不能自动回落普通路径。该机制已定，尚未实现或运行本项目隔离验证。

| 设计范围 | 采用方案及适用边界 |
| --- | --- |
| 准入与生命周期 | [总设计](../DESIGN.md#isolated-execution)、[运行契约](runtime-protocol.md#isolated-execution)；覆盖准备、构建、试验和正式运行，绑定原操作及预算，不按本地／远程或接口名称豁免 |
| 信息、机密与权限 | 资料、程序、环境及机密分别沿所属领域契约与受限视图处理；外部发送和 Secret 使用另行授权，隔离不授予实现信任或原值访问 |
| 可选依赖及替代路径 | 需要隔离时缺失即拒绝该执行，可换合格能力或缩小范围；增强要求不能降为较弱环境 |
| 承载选择 | [工程参考](engineering-reference.md#container-execution)采用可选容器提供者，Linux 优先 Rootless Docker，预留 gVisor 增强隔离；具体运行时版本、配置及计算资源额度按实际用途确定 |
| 管理与评价 | [工作台](management-workspace.md#execution-environments)显示所需与有效条件及实际停止；[评价规格](sandbox-evaluation.md#isolated-execution-evaluation)区分环境检查、隔离效果与认知质量，未新增实验成绩 |
| 资料及边界 | [官方资料](engineering-reference.md#container-sources)支持机制和环境前提；不证明完整隔离、远端控制、平台兼容或性能 |

不采用强制所有能力容器化、每次请求重建环境、向候选开放引擎管理权或以容器存在证明绝对安全。具体兼容性和性能属于接入条件，不自动形成当前待执行任务。

<a id="task-control-extension"></a>

## 核心／任务解耦与外部控制的设计范围

主体、业务任务、认知执行和外部操作具有独立生命周期。任务超时或失败不结束 Self，也不长期占用认知入口；长工作独立管理，结果通过事件接续。控制台、获授权用户及安全审计模块可通过宿主直接打断执行、阻断推进或中止任务，不等待认知批准。

| 设计范围 | 正文及边界 |
| --- | --- |
| 持续主体与独立任务 | [总设计](../DESIGN.md#core-task-control)、[主体场景](whole-system-design.md#task-independence)、[生命周期](runtime-protocol.md#core-task-lifecycle)；资源和预算仍受共同约束，不承诺无条件即时模型回应 |
| 控制与收尾 | [运行契约](runtime-protocol.md#task-control)；止动请求、正式接纳和实际停止分别确认，子工作、新派发及迟到结果纳入范围，无关工作保持 |
| 审计及解除 | 授权决定与建议分开，限定可信来源和范围；多原因解除及重新接纳不能绕过有效阻断；审计算法和全面检查流程未预设 |
| 管理和评价 | [工作台](management-workspace.md#task-control-management)、[评价场景](sandbox-evaluation.md#task-control-evaluation)；已定义未来验收，不新增待执行实验 |
| 真实库接入 | [固定提交源码及测试阅读](go-mini-integration.md#task-control-facts)、[工程装配](engineering-reference.md#task-execution)；任务控制映射由宿主补充，资料核对不等于运行验证 |

原报告 014 的异步 FFI 与顺序跨实例接续不覆盖慢任务期间处理新输入、审计中止及故障隔离的完整场景。当前状态为设计已定、接入与实测未完成。具体容量、期限及审计规则按用途或后续明确需求确定。

<a id="architecture-consistency"></a>

## 跨模块的一致性规则

下表统一主体认知、活动组织与运行基础之间的职责；交互接纳、执行控制、机密使用和试验是相应场景的支撑机制。这些是结合既有职责、资料和库行为形成的设计选择，不构成新增实验结果。

| 范围 | 最终采用方案及理由 | 排除的解释与唯一正文 |
| --- | --- | --- |
| 主体认知与正常经历 | 运行直接绑定 Self／Mind、能力范围和预算，可选关联交流与活动；学习关闭保留普通认知、日常活动和经历积累 | 不制造虚构任务取得执行资格，不把全部自发行为归为学习；[归属](runtime-protocol.md#cognitive-scope)、[学习边界](runtime-protocol.md#learning-intensity) |
| 领域对象与具体操作 | 各领域维护身份、状态、操作和生命周期，投影为受限视图；引用、查询和页面工具不接管真值 | 不采用统一资源模型，不混用资料、记忆、程序、模型和缓存；[领域定义](materials-and-context.md#domain-objects)、[操作](runtime-protocol.md#domain-operations) |
| 独立机密与执行接收方 | SecretGrant 分别授予代理使用、原值读取等操作；按实际接收方、用途和目标交付，普通认知默认使用引用 | 不按 RPC 协议本身授予权限，不将原值夹带到普通模型输入或无关服务，不把撤销当作已收回明文；[专用契约](runtime-protocol.md#secret-contract) |
| 执行分类与可选隔离 | 核心提供仅经宿主能力访问外界的基础受限执行；直接接触系统环境的扩展及高风险实现另须合格环境，按实际可达能力分类 | 不把生成认知程序一概变成可选环境依赖，也不借程序名称豁免要求；[执行分类](runtime-protocol.md#execution-classes) |
| 接纳前交互 | 交流职责保存请求、澄清和处理结果，有限投入关联原会话及输入事件；明确接纳后建立活动并承接投入 | 不将收消息视为业务承诺，不制造无归属调用或以接纳刷新预算；[交互](whole-system-design.md#request-intake)、[运行归属](runtime-protocol.md#interaction-scope) |
| 授权来源与委托 | 共同上下文保留发起者、执行者、权利来源及接收方，领域逐项接纳；子委托限于允许范围，当前父依据继续约束访问 | 不合并全部参与者权限，不让自主活动沿用无关用户委托，不另建通用权限实体；[授权契约](runtime-protocol.md#capability-authority) |
| 记忆形成与维护 | 必要过程记录与选择性长期记忆分开，临时内容不自动升级；归档、更正、淡出检索与删除分别处理 | 不默认每消息总结，不用检索命中替代当前判断，不借必要维护绕过学习关闭；[记忆生命周期](whole-system-design.md#memory-lifecycle) |
| 计算节约与共享执行 | 输入处理、结果复用和独立生成分别声明；复用在当前范围内执行，共享成本一次登记，冷／热条件与完整收益分别评价 | 不用命中率替代质量，不合并独立判断、不冻结有效更新；[输入](runtime-protocol.md#model-reuse)、[运行与结算](runtime-protocol.md#execution-reuse) |
| 上下文有效性 | 根据处理许可与披露变化分别核对已读输入、摘要、会话及待交付产物；不能可靠排除受限历史时重新装配 | 不只检查新读取，不将停止本地复用当外部删除，不无条件清空仍获准内容；[上下文契约](materials-and-context.md#context-validity) |
| 已交付结论纠正 | 原活动所有者按已知使用关系组织有限处置，区别后来变化、当时错误和新增未知；有当前授权及预算才继续工作或发送 | 不永久监测全部历史，不恢复被撤销联系，不以改正文冒充通知；[纠正契约](whole-system-design.md#delivery-correction) |
| 控制对象与传播 | Self／Mind 可直接控制，主体暂停与输出停止分别表达；Episode 是持续活动，Task 是活动内可选任务安排，Operation 是已接纳工作；当前尝试另有执行身份。控制携带类型与传播范围，认知中断和任务停止各有归属 | 不使用含义不明的“任务 ID”，不因认知被取消而自动终止独立操作；[生命周期与控制](runtime-protocol.md#core-task-lifecycle) |
| 步骤与操作接纳 | 步骤内通过独立入口接纳请求，保留稳定请求键与回执；最终提案引用已有操作并接纳剩余意图。支持先读工具结果再作判断，也保留失败前已发生的成本和效果 | 不重复派发，不用最终提交失败抹去独立工作；[时序](runtime-protocol.md#step-operation-admission) |
| 统一主体的公共决定 | 私有 Mind 状态、受委托活动决定与 Self 公共提案分开；指定既有心智承担整合，按证据与责任裁定，未决保留原公共状态 | 不设永久最高人格、不以写入先后或多数票取代公共决定；[公共整合](whole-system-design.md#public-decisions) |
| 配置与当前约束 | 代码及普通行为配置随执行固定；覆盖按声明范围解析，授权、Secret、额度、学习关闭和控制按当前值核对 | 不采用无条件最后写入胜出，不让旧配置冻结有效控制；[配置解析](runtime-protocol.md#configuration-resolution) |
| 个体持久状态 | 个体自由定义主观逻辑，宿主管归属、结构、修订、可见与写入范围及转换；程序和数据结构一致采用 | 不强制统一人格数据，也不把自定义内容变成第二份公共真值；[状态契约](runtime-protocol.md#individual-state) |
| 能力采用与实现信任 | 功能采用、实现来源／产物信任、用途授权分别成立；受信维护者或既定发布策略授予资格，执行环境满足声明约束才接纳 | 不从测试通过、相同接口或模型自评推导机密访问权；[实现准入](runtime-protocol.md#implementation-trust) |
| 学习与任务构建 | 关闭主动学习保留正常主体认知、经历积累及普通活动需要的工具构建；长期安装、泛化和改变主体默认策略另有采用范围。启用探索时可主动提出策略候选 | 不按“是否写代码”分类，不强制先反复失败才产生程序候选；[学习强度](runtime-protocol.md#learning-intensity) |
| 作用与停止反馈 | Effect 跟踪预期或可能作用，不等同已发生；止动请求、正式控制接纳和实际停止分开；禁止原业务交付不禁止按受众发送控制回执和必要退出说明 | 不从发送或局部停止推断任务中止已接纳，不借控制通知恢复任务；[效果](runtime-protocol.md#effects)、[控制](runtime-protocol.md#task-control) |
| 文档层次与证据 | 总图先给一级职责，再提供完整关系图；当前逻辑、工程承载、库固定快照、受限模型证据及历史材料各归其位置 | 不把当前源码链接当不可变快照，不把未测写成没有任何模型证据；[维护规范](documentation-guide.md)、[快照入口](go-mini-integration.md#source-snapshots) |
| 主体级试验与状态导入 | 按问题装配所需初态及环境，复用正式认知与运行契约，默认只激活指定工作；完整状态导入为条件明确的可选方式 | 不将通用完整克隆作为测试前提，不自动接手全部生产工作，不以覆盖缺失冒充能力失败；[试验契约](sandbox-evaluation.md#trial-subject) |

对应检查场景集中于[跨契约评价规格](sandbox-evaluation.md#contract-consistency-evaluation)。这些规则尚无完整组合实验结果。

授权与来源依据 [NIST SP 800-162、RFC 8693 与 W3C PROV-DM](materials-and-context.md#domain-evidence)，执行分层复用既有[库装配记录](go-mini-integration.md#library-facts)和[环境资料](engineering-reference.md#container-sources)。这些资料支持属性判断、委托身份、来源关联及能力约束；交流预算、记忆选择与有限纠正是本项目据此形成的具体规则，不宣称由标准直接证明端到端正确或认知收益。

主体级试验依据及未采用方案见[试验装配资料](sandbox-evaluation.md#trial-sources)。采用真实运行逻辑与按问题装配的初态，保留完整任务评价，同时限制无关历史和外部依赖的重建负担；不采用默认完整克隆、任意现场恢复或自动继承全部生产工作。该维护成本与有效性判断属于设计推论，没有新增对照成绩。

<a id="next-steps"></a>

## 后续维护

新需求、相反证据或实际任务中的失败可能触发设计调整。调整时明确受影响的目标、机制与适用范围；实现、实验和文档维护分别说明各自结果。

当前按[维护规范](documentation-guide.md#workflow)保留资料来源、版本、命题与推论，检查总图、职责、场景和链接的一致性。如果以后另行开展实验，预登记、冻结、失败保留和证据分类规则继续适用；不能改写旧输入和成绩。
