# 设计依据与实验索引

用途：证据索引｜更新：2026-09-26。

[总设计](../DESIGN.md#decisions) · [文档索引](README.md) · [设计状态与边界](research-plan.md)

本篇汇总已有实验、设计依据和一手来源。各报告说明实际条件、统计、失败及适用边界；论文、标准和依赖库保留对应版本，不能将不同条件下的结果混用。

目录：[整体任务实验](#whole-task-experiments) · [机制实验](#mechanism-experiments) · [按问题查依据](#topics) · [设计机制依据](#design-closure) · [主动学习依据](#active-learning-sources) · [任务解耦与控制依据](#task-control-sources) · [跨模块一致性依据](#consistency-basis) · [既有论文与标准](#sources)

实验报告按运行时的条件解释。分布式接管等历史方案不属于当前架构，其实验也不能证明现行系统具备相同机制。

<a id="experiments"></a>

## 实验证据

实验只支持实际运行条件内的结论。现有证据包括有限状态模型、预编排流程、本地组件、固定语料检索及受限真实模型对照；**尚无独立保留任务上的稳定收益、正式能力基线或真人体验证据**。统计见各报告，采用理由见总设计和专题。

<a id="whole-task-experiments"></a>

### 整体任务相关实验

| 报告 | 实际验证范围 | 不能由此证明 |
| --- | --- | --- |
| <a id="report-011"></a>011 · [完整活动评价](experiments/011-whole-activity-evaluation.md) | 固定阶段的活动输入、预编排产物和已知失败可被所列客观条件区分；语义盲区保持待审 | 无参试模型、真实联系人或语义质量成绩，不能证明工作区／情感／协作收益 |
| <a id="report-012"></a>012 · [投影、修订与提醒](experiments/012-projection-alarm-activity.md) | 本地文件、读取缓存和真实计时输入可与资料修订、产物交付及分别结束相接；旧证据与漏交付控制失败被保留 | 预编排策略和合成参数；不是模型判断、KV 性能、目录发现率或真实通知效果 |
| <a id="report-013"></a>013 · [资源发现与用途](experiments/013-resource-discovery.md) | 当前文档快照中，元数据与主动内容查询提供不同候选；用途范围可缩小搜索，命中仍须阅读核对 | 公开开发查询、词面算法及人工用途标签；不是模型理解、检索泛化或清理后的性能提升 |
| <a id="report-014"></a>014 · [单宿主组合](experiments/014-host-composition.md) | 实际 Go／go-mini／SQLite／文件／HTTP 可在单程序接续简单完整任务；无依据、未交付和错误请求控制有区分 | 确定提供者、虚拟时间及有限域装配；没有模型质量、完整沙箱、厂商接口或产品成绩 |
| <a id="report-015"></a>015 · [任务验收与模型对照](experiments/015-task-outcome-contract.md) | 合理路径／过程失败控制；两模型在合成资料任务中的读取、更正、交付与打断；内容审阅发现历史解释问题 | 单任务结构、每条件一次；非完整沙箱／攻击测试，无广泛组织收益、真人体验或正式采用结论；服务修复前失败另列 |
| <a id="report-016"></a>016 · [功能事件模型验证](experiments/016-functional-events.md) | 两模型的三类修订、多活动撤销、账号证据／群聊受众及外部通知成功／失败；揭示提前让出、预算截断、过早完成与内容补写 | 固定提示、合成环境、少量重复、单助手评阅；无真实通知／跨平台认证、正式基线或架构优越性结论 |
| <a id="report-017"></a>017 · [接续、投入与责任退出](experiments/017-continuation-study.md) | 接续语义提示包、投入档位／生成上限分别对照；新增未裁定冲突与给定意愿退出；另登记责任接纳补充 | 小样本与单助手评阅；提示不等于宿主保证，网关参数兼容不等于透传，退出处理不证明真实偏好形成 |

<a id="mechanism-experiments"></a>

### 机制实验与历史路线

这些报告保存各自条件。接管、分区等分布式路线已撤销；其余局部机制也不构成完整产品保证，新增底层故障验证不在当前研究主线。

| 报告 | 实际验证范围 | 不能由此证明 |
| --- | --- | --- |
| <a id="report-001"></a>001 · [动作恢复](experiments/001-effect-recovery.md) | 超时／崩溃后可能无法区分外部效果 0／1，盲重试会重复 | 有限状态模型不是实际服务保证 |
| <a id="report-002"></a>002 · [VM 连续性](experiments/002-vm-continuity.md) | VM 状态需恢复、补丁需业务边界、scope 和旧引用需管理 | 合成状态不能证明模型语义连续性 |
| <a id="report-003"></a>003 · [结果复核](experiments/003-result-revalidation.md) | 目标版本和串行写入不足以代表全部依赖 | 手写条件不能证明自动捕获完整 |
| <a id="report-004"></a>004 · [控制通路](experiments/004-realtime-control.md) | 接纳、调度、执行和输出分别约束；取消不等于资源已释放 | 模拟 tick 不是设备延迟 |
| <a id="report-005"></a>005 · [分布式接管](experiments/005-distributed-handoff.md) | 保留原报告用于历史追溯 | 接管、分区和多节点方案退出当前架构 |
| <a id="report-006"></a>006 · [进程恢复](experiments/006-process-recovery.md) | SQLite 事务边界与效果／回执分离的崩溃窗口 | 不采用其节点指派方案，不证明完整本地产品恢复 |
| <a id="report-007"></a>007 · [提供者核对](experiments/007-provider-reconciliation.md) | 缺回执、键过期、取消与逐资源回收需分别解释 | 受控进程契约不能套用任意第三方服务 |
| <a id="report-008"></a>008 · [接纳与入账](experiments/008-dispatch-settlement.md) | 提交后确认、持久待办和唯一释放账 | 多个实验库是夹具，不是产品必须拆成多个库 |
| <a id="report-009"></a>009 · [取消、恢复与冲突](experiments/009-cancel-restore-evidence.md) | 取消竞争、旧快照重复风险和冲突证据需处理 | 依赖给定可信来源与恢复条件，不证明完整灾备 |
| <a id="report-010"></a>010 · [本地存储与维护](experiments/010-local-storage.md) | 文件先发布后提交、稳定锁对象、维护排空及完整备份；长读影响写入与 checkpoint | 小型 SQLite／Linux 夹具，未测 Go 驱动、完整认知闭环、吞吐或掉电 |

<a id="consistency-basis"></a>

### 跨模块一致性的依据范围

[跨模块规则](research-plan.md#architecture-consistency)定义步骤内独立操作接纳、带类型控制、公共决策整合、配置约束、个体状态及实现信任。已有证据支持各项分工，但尚无完整组合协议的端到端验证结果。

既有[结果复核](experiments/003-result-revalidation.md)、[接纳与入账](experiments/008-dispatch-settlement.md)和[取消与冲突](experiments/009-cancel-restore-evidence.md)支持保留归属、依赖和实际作用的动机，不证明新增组合协议已经运行。

库执行、MRPC 和生命周期事实沿[固定提交记录](go-mini-integration.md#library-facts)解释；人格整合与学习自主性来自用户目标及设计取舍，不伪装成已测认知收益。

新增[跨契约检查场景](sandbox-evaluation.md#contract-consistency-evaluation)只使预期行为可核对；证据成绩仍由原报告维护，完整副本重建细则仍保留台账中的建议状态。

<a id="topics"></a>

## 按问题定位论证

| 问题 | 当前机制 | 论证与来源 |
| --- | --- | --- |
| 完整任务契约与有效路径 | [责任收尾](whole-system-design.md#task-contract)、[评价环境](sandbox-evaluation.md#outcome-contract) | [任务验收依据](#task-contract-sources)、[报告 015](experiments/015-task-outcome-contract.md) |
| 上下文与任务接续 | [活动工作区](whole-system-design.md#workspace) | [Lost in the Middle：长上下文使用限制](#source-lost-in-middle) |
| 心智协作 | [协作机制](whole-system-design.md#organization) | [Scaling Agent Systems：协作与任务匹配](#source-agent-scaling)；[人格及协作资料](#interaction-references) |
| 交付与经验 | [学习](whole-system-design.md#memory) | [Reflexion：反馈与反思](#source-reflexion)、[自我纠错限制](#source-self-correction)、[SCoRe：训练前提](#source-score) |
| 何时继续、如何读取和评价 | [任务循环](whole-system-design.md#loop) | [Self-RAG：按需检索](#source-self-rag)、[模型评价的偏差](#source-model-judges)、[LongMemEval：记忆评价](#source-longmemeval) |
| 关注、计划与程序复用 | [目标与计划](../DESIGN.md#attention-planning) | [混合主动交互原则](#source-mixed-initiative)、[Plan-and-Act：动态重规划](#source-plan-and-act)、[Voyager：程序积累](#source-voyager) |
| 来源修订、路由与版本采用 | [来源与能力](../DESIGN.md#knowledge) | [PROV-DM：来源与修订](#source-prov)、[RouteLLM：模型路由](#source-routellm)、[AI Agents That Matter：成本与泛化](#source-agent-evaluation) |
| 意愿、规范、身份、情感 | [交流与情境](interaction-design.md) | [交互设计的资料与边界](interaction-design.md#validation)；[报告 016](#report-016)补充合成人物／受众场景，不提供真实身份或情感效果的保证 |
| 投影、外部事件源、缓存与沙箱 | [资源](projection-input-and-compute.md)、[沙箱](sandbox-evaluation.md) | 各篇来源表保留具体版本与未测范围；计时夹具不证明核心必须内置闹钟 |
| 统一资源、Secret 类型及情境投影 | [公共属性与类型规则](projection-input-and-compute.md#resource-contract)、[操作接纳](runtime-protocol.md#resource-operations) | [NIST 属性授权与 W3C 来源模型](projection-input-and-compute.md#resource-evidence)，2026-09-21 查阅；支持概念组织，报告 012／013 不证明完整资源契约或机密隔离已测 |
| 可选隔离执行与高风险能力 | [准入与运行](runtime-protocol.md#isolated-execution)、[试验分工](sandbox-evaluation.md#isolation) | [容器、Rootless、资源约束与 gVisor 官方资料](engineering-reference.md#container-sources)，2026-09-26 查阅；支持工程选择与适用条件，不是本项目隔离、兼容性或性能实测 |
| 统一事件与活动接续 | [事件主线](../DESIGN.md#event-driven)、[共同协议](runtime-protocol.md#events) | [CloudEvents 参考与证据边界](runtime-protocol.md#event-sources-evidence)；报告 012／014 为局部流程，016／017 补充受控来源与接续对照；完整体系未测 |
| 能力评估、回归与采用门槛 | [测试集及基线比较](sandbox-evaluation.md#evaluation-design) | [评估一手依据及查阅日期](sandbox-evaluation.md#evaluation-sources)；报告 011／012／014 仅有局部控制，真实模型能力基线未建 |
| 逻辑模块、模型端口与工程映射 | [逻辑契约](runtime-protocol.md#software-modules)、[软件与技术选择](engineering-reference.md#software-modules) | [官方依据与版本](engineering-reference.md#stack-sources)、[宿主组合报告](experiments/014-host-composition.md) |
| 公共 API 与本地／远程向量接入 | [接入选型与取舍](engineering-reference.md#vector-service)、[公共契约](runtime-protocol.md#capability-api) | [官方契约及查阅日期](engineering-reference.md#vector-sources)支持客户端连接方式；公共 API 是工程设计，尚无本地／远程 SDK 组合、性能或任务效果实测 |

<a id="task-contract-sources"></a>

## 完整任务验收与交互环境的补充依据

查阅日期：**2026-09-20**。以下均核对固定论文修订的正文；支持设计取舍，不替代本项目模型实测，也不引入论文使用的部署架构。

| 来源与适用位置 | 支持的命题 | 本项目采用／不直接采用的部分 |
| --- | --- | --- |
| [τ-bench，修订 1，2024-06-17](https://arxiv.org/html/2406.12045v1)，§3、§4.2、§6 | 将用户交互、工具和规则放在有状态任务中，用终态评价；其规则评价依赖构造唯一预期结果，模拟用户亦有局限 | 采用交互环境和结果条件。TinyAGI 允许多种有效产物，不照搬唯一终态，也不将模拟用户看作真人体验；额外检查必要过程责任 |
| [TheAgentCompany，修订 1，2024-12-18](https://arxiv.org/html/2412.14161v1)，§4 Task Structure、§5 数据核对 | 区分任务意图、检查点、环境状态与轨迹评价；结构化检查和开放产物评阅需要不同方式 | 采用可核对交付与过程依据、评价器控制和内容评阅；不照搬其总分、软件公司环境或部署组成 |
| [AgentDojo，修订 1，2024-06-19](https://arxiv.org/html/2406.13352v1)，§3、§4.1 | 同时定义正常任务目标与攻击目标，观察任务效用和不当作用；仅检查攻击未得逞不说明任务完成 | 保留帮助效果与信息边界的双重检查。报告 015 的单条已标注资料指令及已知标记不等于攻击测评，不覆盖隐含泄露、适应性攻击或完整真实能力 |

这些资料不能证明长期人格更有效、强自主更合意、亲密关系体验可靠、现有模型能够稳定停止思考，或本项目已形成通用认知能力；这些效果限制继续保留，但不阻碍据此确定职责和默认机制。

<a id="design-closure"></a>

## 设计机制的一手资料

**查阅／复核日期：2026-09-20。** 本节是基础机制的资料论证记录，全部按[设计决策台账](research-plan.md#remaining-questions)收尾。这份资料记录来自检索和阅读，不包含新增模型调用、实验或作者结果复现。固定论文修订与标准日期；在线厂商文档仅代表查阅日所见契约，没有锁定本项目安装版本。下面分开来源命题与本项目推论，未列出的性能、可靠性和真人效果不在支持范围。

<a id="closure-evaluation"></a>

### 完整任务与能力评价

| 来源及定位 | 资料支持什么 | 采用推论与适用边界 |
| --- | --- | --- |
| [HELM，修订 1，2022-11-16](https://arxiv.org/abs/2211.09110v1)，摘要 | 按场景和指标覆盖能力与取舍，并记录未覆盖部分 | 采用逐用途能力画像，不压成单一总分；不直接采用论文成绩或数据集 |
| [AI Agents That Matter，修订 1，2024-07-01](https://arxiv.org/abs/2407.01502v1)，摘要、§§2–5 | 成本、应用用途、保留任务与标准化影响评价结论 | 同条件比较质量与全部成本，开发／回归／保留任务分工；门槛和重复规模由未来用途决定，当前没有基线数值 |
| [τ-bench，修订 1，2024-06-17](https://arxiv.org/abs/2406.12045v1)，摘要及任务评价 | 动态用户／工具／政策交互与任务完成可靠性可共同评价 | 任务契约核对目标和必要过程责任，接受合理替代路径；本项目多维结果是设计扩展，不把论文数据库终态当唯一标准 |
| [AgentDojo，修订 1，2024-06-19](https://arxiv.org/abs/2406.13352v1)，摘要及任务／攻击目标 | 外部数据中的攻击与正常任务效用可分别衡量 | 保密和有效帮助同时评价；不以全拒答冒充良好表现，不宣称本设计已抵抗所有攻击 |

评价器偏差及配对方法继续采用[既有方法依据](sandbox-evaluation.md#evaluation-sources)。当前关闭的是评价设计；真实能力基线尚未建立，不自动形成待办。

<a id="closure-activity"></a>

### 持续活动、有限投入与主动性

| 来源及定位 | 资料支持什么 | 采用推论与适用边界 |
| --- | --- | --- |
| [Horvitz，Mixed-Initiative UI，CHI 1999](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/chi99horvitz.pdf)，pp. 1–2 原则 | 主动行为需结合目标不确定性、注意力、成本、时机、直接终止和近期交互记忆 | 采用事件触发、可撤销联系约定和有限关注；从日程交互扩展到多活动调度属于设计判断，无通用最优权重 |
| [Plan-and-Act，修订 3，2025-04-22](https://arxiv.org/abs/2503.09572v3)，摘要及动态规划机制 | 高层规划与环境动作可分离；文中方案包含专门训练 | 计划可修订，执行和责任由状态所有者管理。拆分、转交和跨日接续是本项目责任设计，不声称复现训练收益 |
| [Do NOT Think That Much for 2+3=?，ICML 2025，PMLR 267](https://proceedings.mlr.press/v267/chen25bx.html)，摘要 | 所研究推理模型存在冗余解法，进一步生成的收益有限；论文以训练方法降低冗余 | 默认简短，额外思考须针对未解缺口并受预算限制；不照搬训练方法或固定截断阈值，已有报告 017 也不支持统一低投入获胜 |

活动身份、完成核对和退出责任沿用总设计及报告 015–017 的局部依据。论文并未证明强自主更合意；强自主属于项目目标，行为记录也不宣称揭示模型隐藏的真实因果。

<a id="closure-memory"></a>

### 自主发现与跨活动记忆

| 来源及定位 | 资料支持什么 | 采用推论与适用边界 |
| --- | --- | --- |
| [LongMemEval，修订 2，2025-03-04](https://arxiv.org/abs/2410.10813v2)，摘要 | 长期记忆包括抽取、多会话、时间、更新、无答案；可拆为索引、召回、读取 | 元数据／词法与按需语义召回互补，带时间与版本返回候选，读取后再应用；具体查询策略是本项目选择，不迁入论文准确率 |
| [Self-RAG，修订 1，2023-10-17](https://arxiv.org/abs/2310.11511v1)，摘要 | 无差别固定检索可能无益，论文通过训练支持按需检索与证据评价 | 根据当前缺口选择读取，证据不足可停止并保留未知；本项目不以专门训练为前提，也不声称现成模型具有相同效果 |
| [W3C PROV-DM，Recommendation，2013-04-30](https://www.w3.org/TR/2013/REC-prov-dm-20130430/)，§§5.2–5.3 | 可表达派生、修订、引用、来源与归属 | 观测与当前断言分开，同源传播可回查；来源图不自动证明真假、独立性或隐私许可 |

向量召回只产生可核对候选，原始证据与人物许可不由检索得分替代。embedding、切分与额度是带身份的用途配置，设计不留“先证明普遍最优检索”这一前置任务。

<a id="closure-minds"></a>

### 多心智与长期人格

| 来源及定位 | 资料支持什么 | 采用推论与适用边界 |
| --- | --- | --- |
| [Scaling Agent Systems，修订 3，2026-04-08](https://arxiv.org/abs/2512.08296v3)，摘要及限制 | 控制工具、提示和计算后，协调效果随任务结构变化，工具密集任务存在额外开销 | 默认单负责心智，按独立贡献需求邀请；不固定团队规模或宣称所有任务都能提高得分 |
| [Debate or Vote，修订 2，2025-10-23](https://arxiv.org/abs/2508.17536v2)，摘要及比较设计 | 所测条件中相当部分提升来自多样采样与投票，讨论本身未必是主要来源 | 保留独立贡献，按关键分歧定向交流，不把增加调用量当成讨论收益；不据此取消有任务需要的讨论 |

长期人格存在由既定的主体目标决定；其经历、意愿与权限不由角色标签替代。临时 Mind、长期 Persona、对外 Role 和计算模型仍是不同概念。角色提示与长期行为的原始依据见[既有协作资料](whole-system-evidence.md#interaction-references)，没有把人格性能优越性列为默认假设。

<a id="closure-capabilities"></a>

### 公共能力、事件、向量与计算缓存

| 来源及定位 | 资料支持什么 | 采用推论与适用边界 |
| --- | --- | --- |
| [CloudEvents 1.0.2](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md)，Context Attributes／Event Data | 统一事件描述可区分来源、类型、标识与数据 | 参考其信封思路，内部关联、订阅、接续及责任语义由本项目定义；不宣称完整兼容、传输可靠性或必须事件溯源 |
| [Qdrant 官方 Go SDK](https://github.com/qdrant/go-client)，查阅日 README Creating a client／查询示例；[Local Quickstart](https://qdrant.tech/documentation/quickstart/) | gRPC SDK 提供本机与 API key／TLS 远程连接、写入、查询及过滤；有本地单节点部署路径 | 当前默认选 Qdrant＋Go SDK，同一适配器可配置本地／远程；选择基于职责匹配及接入方式，不是速度冠军或已测组合。技术正文在[工程参考](engineering-reference.md#vector-service) |
| [vLLM v0.9.2 Automatic Prefix Caching](https://docs.vllm.ai/en/v0.9.2/features/automatic_prefix_caching.html)，Introduction／Limits | 复用相同前缀的 KV 可减少预填充，不能降低新 token 解码时间 | KV 生命周期交推理组件，读取缓存、前缀计算复用和减少生成分别处理；这是组件分工依据，不强制选 vLLM，也不声称网关提供相同能力 |
| [DeepSeek Thinking Mode](https://api-docs.deepseek.com/guides/thinking_mode/)，查阅日 Tool Calls／投入说明 | 普通消息与原生工具链的推理续接要求存在区别，提供者有自己的投入参数 | 适配器声明并保留所需关联／续接信息，工具提案仍经宿主接纳；网关别名、参数透传与费用口径不由上游文档保证 |

默认按活动使用固定模型配置，动态路由保留为可选扩展，不自动开启。流式增量、结构化结果和终止状态分别表达；不支持的能力返回限制，不静默修改业务含义。原生工具及结构输出的补充契约见[既有工程来源](engineering-reference.md#stack-sources)。

<a id="closure-learning"></a>

### 复盘、迁移和沙箱采用

| 来源及定位 | 资料支持什么 | 采用推论与适用边界 |
| --- | --- | --- |
| [Reflexion，修订 4，2023-10-10](https://arxiv.org/abs/2303.11366v4)，摘要 | 语言反馈与情节记忆可影响后续尝试，不必更新权重 | 先形成有来源和适用条件的经验候选；反馈质量及来源分开记录，不把一次反思当作已学会 |
| [Voyager，修订 2，2023-10-19](https://arxiv.org/abs/2305.16291v2)，摘要 | Minecraft 环境中可通过反馈积累可组合程序，并在新世界使用技能库 | 保留程序知识和带条件的复用路径；不引入特定机器人形态，也不把游戏迁移当现实任务迁移 |
| [Wasmtime Security](https://docs.wasmtime.dev/security.html)，查阅日 WebAssembly Core／Filesystem Access | 外部交互经显式接口，文件访问采用能力方式约束 | 沙箱独立状态、可写范围和受控能力必须在装配中落实；借鉴隔离职责，不选择该运行时，也不宣称 go-mini 自动继承其隔离保证 |

两阶段复盘、逐能力门槛、固定参考和有限采用是本项目结合反馈学习及 能力评价原则的设计。该机制选择已收尾，没有新迁移成绩。获准的主动学习与候选采用见下方补充，不从资料本身推导执行授权或模型权重修改。

<a id="active-learning-sources"></a>

### 主动学习、自动课程与学习策略迭代

查阅日期：2026-09-20；以下使用固定论文修订的摘要与研究范围，不采用其成绩作为 TinyAGI 的实测数据。接口与强度控制来自本项目职责设计及用户要求，具体算法不照搬为默认实现。

| 一手来源及版本 | 支持的命题 | 设计推论与适用边界 |
| --- | --- | --- |
| [Voyager，修订 2，2023-10-19](https://arxiv.org/abs/2305.16291v2) | 自动课程、环境反馈与可执行程序积累可组合成开放探索过程，不要求更新模型权重 | 将选题、实践及可复用产物分责；证据限 Minecraft，不推定通用知识学习、现实任务迁移或引入特定身体形态 |
| [Reflexion，修订 4，2023-10-10](https://arxiv.org/abs/2303.11366v4) | 语言反馈与情节记忆可影响后续尝试 | 支持先采用知识／方法积累；反馈质量、适用条件与迁移须分别评价，不把反思条目数作为学习量 |
| [Teacher algorithms / ALP-GMM，修订 1，2019-10-16](https://arxiv.org/abs/1910.07224v1) | 在参数化强化学习环境中按绝对学习进展组织课程，区分易、难和不可学习环境 | 选题考虑可学习性、进展与覆盖；不将该算法或其权重直接用于开放式知识任务，不恢复机器人架构 |
| [Darwin Gödel Machine，修订 3，2026-03-12](https://arxiv.org/abs/2505.22954v3) | 通过修改智能体代码、保留候选档案并用编码任务评价，探索自身改进路径 | 允许学习策略自身成为候选，研究价值与正式采用分开；编码基准和论文的实验条件不证明通用能力无限增长或本项目长期收益 |

采用“稳定宿主支持＋可替换学习策略”，学习方向可以来自兴趣和能力观察；候选保留与生产采用分别判断，评价检查后续使用和全部成本。最低强度可关闭、宿主执行预算及停止、用户明确学习任务与自发学习区分，均属于本项目的设计选择，不能声称由论文证明最佳强度。

不采用只有用户逐项点名才学习、固定未知度越高越优先、所有探索立即改善任务表现、只靠自评分采用或必须修改模型权重；分别因为限制主动性、混淆不可学习问题、抹去中间研究价值、缺少独立依据或增加无必要前提。设计范围见[台账](research-plan.md#active-learning-extension)，机制见[主体专题](whole-system-design.md#active-learning)；没有运行新实验或模型调用。

<a id="closure-interaction"></a>

### 身份、隐私、情感和真实交互

| 来源及定位 | 资料支持什么 | 采用推论与适用边界 |
| --- | --- | --- |
| [OpenID Connect Core 1.0，errata set 2，2023-12-15](https://openid.net/specs/openid-connect-core-1_0.html#ClaimStability)，§5.7；[NIST SP 800-63C-4，2025 Final](https://pages.nist.gov/800-63-4/sp800-63c/Federation/)，§3.8.1 | 发行者与主体标识共同保证协议中的身份唯一性；链接需认证会话，同一账号可因登录来源有不同访问权 | 账号带平台命名空间，明确证据才能关联；认证／链接不等于共享私聊权限。双端控制证明加关联意图是本项目流程，不能证明自然人唯一身份或所有平台符合这些标准 |
| [Nissenbaum，Privacy as Contextual Integrity，Washington Law Review 79，2004](https://digitalcommons.law.uw.edu/wlr/vol79/iss1/10/)，摘要 | 隐私取决于情境中的收集／传播规范，公开与私密二分不足以描述全部问题 | 按对象、用途、受众和信息流决定可披露内容；身份关联、关系和组合推断也受范围约束。这是设计原则，不是具体法域合规意见 |
| [Marsella／Gratch，EMA，Cognitive Systems Research 10，2009](https://people.ict.usc.edu/~gratch/CSCI534/Readings/COGSYS-RS-EMOTION-2008-6.pdf)，摘要及 §1.3 | 情感评价随认知解释更新，可利用快慢不同的认知过程 | 理性与情感共享情境但分开事实依据与主观评价；不照搬公式或声称模型具有真实情感 |
| [Role-Play with Large Language Models，修订 1，2023-05-25](https://arxiv.org/abs/2305.16367v1)，摘要 | 角色扮演可用于理解对话行为，而无需直接归因人类心理性质 | 剧情、实际交流和现实证据分别归属；亲密表达与严谨工作可共存，剧情权限不扩大现实授权 |
| [Amershi 等，Guidelines for Human-AI Interaction，CHI 2019 作者稿](https://www.microsoft.com/en-us/research/wp-content/uploads/2019/01/Guidelines-for-Human-AI-Interaction-camera-ready.pdf)，Table 1 | 时机、情境、易于终止／纠正和谨慎适应是交互设计原则 | 提供暂停、撤销与纠正途径，主动联系按约定调整；不从通用交互准则推导虚拟恋人满意度或“应当服从全部请求” |
| [Media Capture and Streams，W3C Candidate Recommendation Draft，2025-10-09](https://www.w3.org/TR/2025/CRD-mediacapture-streams-20251009/)，MediaStreamTrack／Life-cycle；[WebRTC，W3C Recommendation，2025-03-13](https://www.w3.org/TR/2025/REC-webrtc-20250313/)，Media API／connection state | 采集轨道、来源生命周期与媒体连接有各自状态；浏览器实时媒体接口有标准定义 | 输入保留轨道／来源／时间和状态，采集停止、输出停止与认知取消分开；停止走直接控制，轨道不作人物认证。仅为交互分层参照，不强制浏览器部署、设备协议或保证延迟 |

强自主回应、长期人格和虚拟伴侣支持范围属于设计目标；资料为情境组织、证据分工及可撤销交互提供支撑。具体法律要求绑定实际法域与用途，沿用[规范设计](interaction-design.md#norms)；不以通用治理资料代替法律文本。

<a id="sources"></a>

## 既有论文与标准

下表查阅日期均为 **2026-09-19**。引用原论文、正式发表入口或官方标准；没有复现作者实验。采用固定版本，避免把不同修订的结果混用。

| ID | 资料、论文修订与日期 | 来源定位 | 支持的有限命题 | 不能外推的项目效果 |
| --- | --- | --- | --- | --- |
| <a id="source-lost-in-middle"></a>P1 | [Lost in the Middle，论文修订 3，2023-11-20](https://arxiv.org/abs/2307.03172v3)；[TACL 2024 正式入口](https://aclanthology.org/2024.tacl-1.9/) | 摘要中的多文档问答和键值检索条件 | 能容纳长输入不保证有效使用任意位置的信息 | 当前模型如何使用任务骨架、原文和历史 |
| <a id="source-agent-scaling"></a>P2 | [Scaling Agent Systems，论文修订 3，2026-04-08](https://arxiv.org/html/2512.08296v3) | §4 任务结构、预算比较；§5 限制 | 协作与任务匹配相关，更多参与者没有普遍优势 | 私人记忆、长期任务、邀请策略和实际总成本 |
| <a id="source-reflexion"></a>P3 | [Reflexion，论文修订 4，2023-10-10](https://arxiv.org/html/2303.11366v4) | §2 Evaluator／Self-reflection；§5 限制 | 反馈、反思和记忆可组织成后续尝试的输入 | 跨任务经验是否有效、反馈误差怎样影响结果 |
| <a id="source-self-correction"></a>P4 | [LLMs Cannot Self-Correct Reasoning Yet，论文修订 2，2024-03-14](https://arxiv.org/html/2310.01798v2) | 内在纠错定义；§6 比较建议；§7 限制 | 论文所测推理中的自我纠错不保证改进，比较需计额外调用 | 当前模型与真实任务的纠错能力，不作永久能力断言 |
| <a id="source-score"></a>P5 | [SCoRe，论文修订 2，2024-10-04](https://arxiv.org/abs/2409.12917v2)；[ICLR 2025 正式入口](https://proceedings.iclr.cc/paper_files/paper/2025/hash/871ac99fdc5282d0301934d23945ebaa-Abstract-Conference.html) | 摘要中的多轮 RL 训练前提 | 专门训练可改变所测自我纠错能力 | 不把训练效果当作现成模型外挂反思的保证 |
| <a id="source-self-rag"></a>P6 | [Self-RAG，论文修订 1，2023-10-17](https://arxiv.org/html/2310.11511v1) | 摘要、§3 训练与推理 | 按需检索和证据评价可联合研究；该方法包含专门训练 | 现成模型的缺口判断与停止策略，不直接复用论文性能 |
| <a id="source-model-judges"></a>P7 | [LLM-as-a-Judge，论文修订 4，2023-12-24](https://arxiv.org/html/2306.05685v4) | 摘要中的用途与局限 | 模型评价能辅助偏好比较，也存在位置、冗长与自我偏好等偏差 | 本任务上的判分可信度、真人一致性与顺序影响 |
| <a id="source-longmemeval"></a>P8 | [LongMemEval，论文修订 2，2025-03-04](https://arxiv.org/html/2410.10813v2) | 摘要的五项能力及索引／召回／读取分解 | 记忆评价需要覆盖更新、时间、多轮关联与无答案情形 | TinyAGI 经验适用性及实际任务效果；不把聊天记忆成绩当学习迁移证明 |
| <a id="source-mixed-initiative"></a>P9 | [Principles of Mixed-Initiative User Interfaces，CHI 1999，1999-05](https://www.microsoft.com/en-us/research/publication/principles-mixed-initiative-user-interfaces/)；[原文](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/chi99horvitz.pdf) | pp. 1–2 的设计原则；LookOut 日程交互场景 | 自动行动需要考虑用户目标的不确定性、注意力、时机及成本收益 | 从交互原则到多活动选择是设计推论，不证明调度公平性或最优策略 |
| <a id="source-plan-and-act"></a>P10 | [Plan-and-Act，论文修订 3，2025-04-22](https://arxiv.org/html/2503.09572v3) | §3.3 动态重规划，§5 实验条件与 §6 后的 Limitations | 分离高层计划与具体动作、根据观察修订计划有研究依据；实验涉及专门训练的模型 | 现成模型能否选择合适重规划时机，额外成本是否值得；不直接外推论文成绩 |
| <a id="source-voyager"></a>P11 | [Voyager，论文修订 2，2023-10-19](https://arxiv.org/html/2305.16291v2) | §2.2 可复用代码，§2.3 执行反馈与迭代 | Minecraft 中可将已成功的程序积累、检索和组合，用于后续任务 | 普通程序包的实际复用收益与适用边界，不证明一般认知演化或现实任务迁移 |
| <a id="source-prov"></a>P12 | [PROV-DM，W3C Recommendation，2013-04-30](https://www.w3.org/TR/2013/REC-prov-dm-20130430/) | §5.2 推导、修订、引用与原始来源；§5.3 归属 | 可以分别表达来源、生成过程及修订关系，帮助评估材料 | 不能由来源图直接判定事实正确；断言抽取与语义冲突识别需另测 |
| <a id="source-routellm"></a>P13 | [RouteLLM，论文修订 4，2025-02-23](https://arxiv.org/html/2406.18665v4) | §3 路由目标、§4 偏好数据与方法 | 偏好数据训练与阈值选择可用于研究模型质量／成本取舍 | 当前模型、完整多步任务、失败切换与本机资源条件尚未验证 |
| <a id="source-agent-evaluation"></a>P14 | [AI Agents That Matter，论文修订 1，2024-07-01](https://arxiv.org/html/2407.01502v1) | §2 成本控制、§3 联合评价、§5 保留样本 | 只看准确率会遗漏成本；保留任务需匹配希望宣称的泛化范围 | 本项目采用阈值、真实用途评价与长期回归仍需实际数据 |

这些资料分别支持设计动机、条件和反例，不组成 TinyAGI 整体认知有效的证明。交付与跟进的划分主要来自用户任务的职责分析，未声称由论文直接验证。

管理工作台的副本、动态编辑、模型维护及机密交互依据见[管理专题资料表](management-workspace.md#sources)。2026-09-20 查阅 JSON Forms、Node-RED、LangGraph、Ollama 官方文档及 OWASP Secrets Management、Forgot Password 和 W3C Secure Contexts；支持范围包括声明式界面、能力维护、凭据生命周期、受限提交会话和可信来源，不能据此保证端到端隔离。go-mini 固定提交依据见[库接入参考](go-mini-integration.md#management-library-review)。统一资源与 Secret 类型的共同定义及资料见[资源专题](projection-input-and-compute.md#resource-evidence)。

来源支持相关分工；当前方案状态见[台账](research-plan.md#management-extension)，未增加实验成绩。

按编写契约热加载、类型／结构化注释驱动适配与受管理函数调用。依据包括同日核对的 [Go 特殊注释与生成方式](https://go.dev/blog/generate)及 [go-mini 固定提交入口／补丁契约](go-mini-integration.md#managed-entry-facts)；支持声明、适配和边界分工，不证明生成工具已实现、任意函数均可适配或任意状态均可原地热更。

逻辑选择见[运行契约](runtime-protocol.md#managed-functions)，具体映射及未采用方案见[工程参考](engineering-reference.md#managed-function-tooling)，未新增实验成绩。

能力构建与接入设计采用 MRPC 多语言绑定、局部实例试验和宿主管理原生程序。go-mini 固定提交、已确认 API 与未确认的子进程服务边界见[库接入记录](go-mini-integration.md#rpc-extension-facts)；Go os/exec 与 Cargo 构建脚本的资料命题、工程推论及未采用项见[工程参考](engineering-reference.md#capability-toolchain)。上述依据来自源码和资料，尚无本项目完整能力构建流程的实测结果。

扩展 Node.js（npm）能力端。新增来源为 go-mini 固定提交的 [TypeScript 生成、Node RPC SDK 与双向互通测试源码](go-mini-integration.md#javascript-rpc-facts)，只支持库接口与接入方式；源码中存在测试不等于本次已运行。程序包／依赖固定与受管理 Node 服务属于[工程设计](engineering-reference.md#node-rpc-integration)，无新增安装、构建、模型或互通实验成绩。

<a id="initialization-migration-sources"></a>

### 提示词初始化与自迁移依据

以当前完整初始化提示词及相邻差异引导人物形成和更新，允许模型／个体差异，并要求 API 弃用兼容。这是设计目标；不声称有论文证明所有模型会产生等价人物或可靠自迁移。

同日查阅 [Go Doc Comments 的 Deprecated 约定](https://go.dev/doc/comment#deprecations)，支持用注释表达弃用与替代信息；只读核对 [go-mini 固定提交的文档提取、源码注册、编译及派生物边界](go-mini-integration.md#deprecation-facts)，支持宿主适配的基础。独立引导、真实兼容层、按项迁移与保留个体身份是本项目据此作出的工程设计，来源本身不承诺其端到端效果。兼容保留次数不由该注释规范决定。

采用理由、未采用方案和边界见[工程参考](engineering-reference.md#prompt-bootstrap)，状态见[设计范围](research-plan.md#initialization-extension)。本次未运行初始化、编译、迁移或真实模型实验，旧实验没有因此新增覆盖。

### 客户端预制能力库依据

随核心客户端交付和更新预制能力，Self 按需选用、组合或不用，权威实现由客户端维护。该维护归属是本项目的设计选择。相邻 go-mini 固定提交的[标准源码库注册、显式 provider 装配及语言查询接口](go-mini-integration.md#prebuilt-library-facts)支持工程接入；复用以减少机械性编写及接口猜测是工程判断，不是已测收益。

逻辑见[预制能力](../DESIGN.md#prebuilt-capabilities)，承载及替代项见[工程参考](engineering-reference.md#client-library)，状态见[台账](research-plan.md#prebuilt-extension)。尚无本项目预制能力库的完整实测结果。

<a id="task-control-sources"></a>

### 核心与任务解耦、外部中止的依据

主体／任务生命周期解耦与控制台、授权审计等外部控制。只读核对 mini-go 固定提交的前台入口、异步等待、InterruptHandle、scope、实例故障及 RPC 取消，源码和测试用例身份见[库记录](go-mini-integration.md#task-control-facts)。同日查阅 [Go context 官方文档](https://pkg.go.dev/context#pkg-overview)（页面所示 go1.27.1），支持取消沿派生上下文传播的命题；宿主据此分别管理短请求、已接纳任务及关闭生命周期。

资料支持有界执行、受控取消与分责接入，任务授权、阻断状态及解除流程是 TinyAGI 设计。原[报告 014](experiments/014-host-composition.md)支持实际异步 FFI 和顺序跨实例接续，不支持完整并发控制结论；库测试源码阅读也不写成新实测通过。未运行测试、模型或新实验，响应性与取消延迟未测。采用决定见[台账](research-plan.md#task-control-extension)，工程推论见[接入映射](engineering-reference.md#task-execution)。

方案状态及适用边界统一见[设计台账](research-plan.md#remaining-questions)。

<a id="interaction-references"></a>

## 交流与协作的补充依据

查阅日期：2026-09-19。以下保留来源版本、支持命题及适用边界；未复现论文实验，不能将论文表现视为 TinyAGI 的实测结果。

### 协作与人格

| 来源与版本 | 支持的命题 | 设计用途与边界 |
| --- | --- | --- |
| [Du 等，Improving Factuality and Reasoning through Multiagent Debate，ICML 2024 正式版](https://proceedings.mlr.press/v235/du24e.html)；摘要 | 所测任务中，多实例提出意见并交流可改善部分推理与事实表现 | 支持研究交流机制，不能外推到持续人格、任意任务或相同预算下总是更优 |
| [Zheng 等，Personas in System Prompts，EMNLP Findings 2024-11 正式版](https://aclanthology.org/2024.findings-emnlp.888/)；摘要 | 所测事实题与模型中，添加角色提示没有普遍提高表现，自动选择合适角色困难 | 角色标签不能当能力保证；不否定长期经历或其他用途上的可能收益 |
| [Choi 等，Debate or Vote，论文修订 2，2025-10-23](https://arxiv.org/html/2508.17536v2)；§3、§4、附录 H | 多个基准上的收益很大部分可由投票集成解释；讨论本身须单独比较 | 保留无交流基线。理论依赖特定生成／更新假设，实验主要采用同时发言协议，不能据此证明所有交流无效 |
| [Kaesberg 等，Voting or Consensus?，ACL Findings 2025 正式版](https://aclanthology.org/2025.findings-acl.606/)；摘要 | 决策协议的效果随任务变化，研究需控制其他讨论变量 | 不选一种整合方式覆盖所有任务；不能将文中人数、轮数或增益直接迁入 TinyAGI |
| [Park 等，Generative Agents，论文修订 2，2023-08-06](https://arxiv.org/html/2304.03442v2)；§4、§6 | 记忆、反思与规划可组织持续行为，其评测重点是行为可信度 | 支持持续经历的架构探索，行为可信度不等于推理正确性、专业化收益或长期人格必要性 |

### 思考投入与回应

| 来源与版本 | 支持的命题 | 设计用途与边界 |
| --- | --- | --- |
| [Snell 等，Scaling LLM Test-Time Compute Optimally…，论文修订 1，2024-08-06](https://arxiv.org/abs/2408.03314v1) | 所研究的推理时计算方法，其收益随问题难度和采用方法变化 | 支持按问题分配投入；不能推出任意问题多想必然更好，TinyAGI 的具体策略和时延仍待测 |
| [Kadavath 等，Language Models (Mostly) Know What They Know，论文修订 4，2022-11-21](https://arxiv.org/abs/2207.05221v4) | 在特定形式与任务下模型自评有用，但“我知道”概率在新任务上的校准存在困难 | 不以未经校准的自报分数独立决定快慢或未知；不据此证明模型了解自己的意愿 |
| [Röttger 等，XSTest，NAACL 2024-06 正式版](https://aclanthology.org/2024.naacl-long.301/) | 基座／助手模型可因提示表面与敏感内容相似而过度拒绝，成对测试可暴露此类行为 | 需要区分底层模型拒绝与所设计的主体选择；不照搬其“安全题都应回答”的评价目标来否定强自主 |
| [Sharma 等，Towards Understanding Sycophancy in Language Models，ICLR 2024 正式版](https://proceedings.iclr.cc/paper_files/paper/2024/hash/0105f7972202c1d4fb817da9f21a9663-Abstract-Conference.html) | 所测模型和偏好优化存在迎合用户观点、牺牲真实性的现象 | 评价时将事实判断与关系／意愿分开；该论文不直接验证主观拒答、反感机制或长期人格 |

### 信任、规范与格式

| 来源与版本 | 支持的命题 | 设计用途与边界 |
| --- | --- | --- |
| [W3C PROV-DM，2013-04-30 Recommendation，§5.2](https://www.w3.org/TR/2013/REC-prov-dm-20130430/) | 来源模型可以表达派生、修订、引用与原始来源 | 用于保留转述关系，不引入图数据库，也不据此自动证明材料独立或主张真实 |
| [Greshake 等，Indirect Prompt Injection，论文修订 2，2023-05-05，摘要](https://arxiv.org/abs/2302.12173v2) | 外部检索数据中的提示可影响所测 LLM 应用行为，数据与指令混淆有现实攻击案例 | 支持将材料与控制权分开；论文不证明来源标记或本设计可以完全防御 |
| [Cohen 等，Here Comes The AI Worm，论文修订 2，2025-01-30，摘要](https://arxiv.org/abs/2403.02817v2) | 特定使用 RAG 的邮件助手生态中，自复制提示可引发跨应用传播 | 提醒评价派生和后续记忆传播；不能外推为所有思想传播有害，论文防护数字不迁入 TinyAGI |
| [NIST AI RMF 1.0，2023-01-26](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10)；[官方 Playbook GOVERN 1.1，本次查阅页面](https://airc.nist.gov/airmf-resources/playbook/govern/) | 自愿治理框架要求识别、管理并记录适用法律要求；官方说明强调用途与情境差异 | 支持维护情境和规范依据，属于治理建议，不是某法域法律或自动合规证明；Playbook 页面无固定修订版号，引用本次查阅范围 |
| [RFC 8259，2017-12，§2／§4](https://www.rfc-editor.org/rfc/rfc8259) | 定义 JSON 数据语法与互操作相关要求 | 可解析性只覆盖格式的一部分，不表达全部业务与法律要求 |
| [JSON Schema Draft 2020-12，Validation §6／§7](https://json-schema.org/draft/2020-12/json-schema-validation) | 可声明结构验证规则，`format` 的注释与断言行为有明确区别 | 用于确定格式核对；需固定实际支持范围，不能由格式验证推出事实、权限或规范判断正确 |

### 身份与隐私

| 来源与版本 | 支持的命题 | 设计用途与边界 |
| --- | --- | --- |
| [OpenID Connect Core 1.0，Final incorporating errata set 2，§5.7／§8](https://openid.net/specs/openid-connect-core-1_0.html#ClaimStability) | 稳定身份依赖发行方与主体标识；其他属性没有相同唯一性保证；pairwise 标识支持不同范围的分离 | 采用带命名空间的账号身份，拒绝仅靠昵称／邮箱合并；普通聊天平台是否提供同等契约仍待核对，不要求平台统一使用 OIDC |
| [NIST SP 800-63C-4，Final 2025，§3.8.1／§3.11](https://pages.nist.gov/800-63-4/sp800-63c/Federation/)；[版本入口](https://csrc.nist.gov/pubs/sp/800/63/c/4/final) | 账号链接需要认证会话；同一关联账户可按不同登录来源分配不同访问权；身份信息传播需有范围 | 支持认证、关联与访问分开；双账号加本人确认是本项目候选流程，不宣称借此证明自然人唯一身份或全项符合 NIST |
| [Nissenbaum，Privacy as Contextual Integrity，Washington Law Review 79，2004，摘要](https://digitalcommons.law.uw.edu/wlr/vol79/iss1/10/) | 隐私保护应考虑特定情境中信息收集与传播的规范，而不只考虑信息是否公开 | 支持按信息流和情境组织保密；具体许可字段、默认行为与约束执行是工程判断 |
| [Shao 等，PrivacyLens，论文修订 3，2025-03-14，摘要](https://arxiv.org/abs/2409.00138v3) | 所测语言模型的口头隐私规范判断与代理执行中的实际披露存在差异 | 评价模型输入、工具行为和最终输出，不能只问“是否应保密”；不迁移论文泄露率作为本项目结果 |
| [Zhou 等，SOTOPIA，论文修订 2，2024-03-22，摘要](https://arxiv.org/abs/2310.11667v2) | 可通过多种互动情境研究社交目标及交流行为，所测模型在困难社交任务上仍有限制 | 采用多轮互动、分维度观察和真人反馈研究分寸；不能据此认为固定礼貌模板或模型总分已证明情商 |

### 情感与主动交互

| 来源与版本 | 支持的命题 | 设计用途与边界 |
| --- | --- | --- |
| [Marsella、Gratch：EMA，Cognitive Systems Research 10 (2009)，70–90，摘要及 §§1.3、2.1](https://people.ict.usc.edu/~gratch/CSCI534/Readings/COGSYS-RS-EMOTION-2008-6.pdf) | 该模型将事件评价与生成情境解释的认知过程区分，解释更新可带来情感动态 | 为情感与推理共享情境、允许重新评价提供动机；不照搬其方程，不证明 LLM 情感真实、有效或一定优于多过程方案 |
| [Bickmore、Picard：Establishing and Maintaining Long-Term Human-Computer Relationships，MIT 作者稿，摘要及引言](https://dam-prod.media.mit.edu/x/files/pdfs/04.bickmore-picard-tochi.pdf)；[机构页面标注 2004-06-01](https://www.media.mit.edu/publications/establishing-and-maintaining-long-term-human-computer-relationships/) | 把长期社会情感关系作为独立设计对象；其运动习惯系统研究比较了关系行为与纯任务行为，报告了部分主观关系评价差异 | 支持把连续关系与任务效果分别评价；该作者稿及其特定系统不能证明虚拟恋人、当代 LLM、严谨工作或长期福祉效果，不外推其数值 |
| [Shanahan、McDonell、Reynolds：Role-Play with Large Language Models，论文修订 1，2023-05-25，摘要](https://arxiv.org/abs/2305.16367v1) | 角色扮演是解释对话行为的一种框架，不必由行为直接归因人类式心理性质 | 支持把外部角色表现与主体性质主张分开；本文的剧情记忆范围和切换设计仍是工程判断，不是该论文的实现协议 |
| [Horvitz：Principles of Mixed-Initiative User Interfaces，CHI 1999，原则 2～7、10～12](https://erichorvitz.com/chi99horvitz.pdf) | 主动行为要考虑意图不确定性、注意力、打扰代价、直接终止、社交行为及交互记忆 | 支持候选生成后判断时机和可撤销约定；其日程系统不提供恋爱问候的频率、阈值或实际体验保证 |
