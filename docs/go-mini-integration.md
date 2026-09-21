# go-mini 库行为与接入参考

用途：执行库与接入参考（工程资料）｜更新：2026-09-21。

[文档索引](README.md) · [工程映射](engineering-reference.md#vm-deployment) · [总体设计](../DESIGN.md#vm-deployment) · [设计状态](research-plan.md#research-status)

基础库核对日期为 2026-09-19。[宿主组合实验](experiments/014-host-composition.md)实际运行提交 `2f58a21748b92bae83ee37cca570ceb9bf387692` 的导出快照，覆盖编译、独立实例、异步 FFI 和跨实例业务接续；未重新验证下表全部热更新行为。

第 1 节按各自固定提交记录库行为与适用边界，其余章节维护宿主接入设计。运行分段、步骤约束和部署流程按当前[设计决策与边界](research-plan.md#remaining-questions)解释，不自动安排验证。库接口存在不等于系统设计已成立。

早期基础核对使用 go-mini 提交 `7c195d9`（2026-09-18，`feat: add revision diagnostics and improve runtime fairness`）。结论来自文档、实现和测试源码阅读；记录的是该提交快照，不同提交的行为须分别核对。

TinyAGI 的独立研究模块使用同一提交执行了[生命周期与补丁实验](experiments/002-vm-continuity.md)，没有运行或修改 go-mini 自身的回归测试。接口阅读证据与实测结果分别保留。

上游资料：[架构](https://github.com/d7z-team/go-mini/blob/main/ARCHITECTURE.md)、[使用指南](https://github.com/d7z-team/go-mini/blob/main/USAGE.md)、[RPC 指南](https://github.com/d7z-team/go-mini/blob/main/RPC.md)。这些概览链接跟随上游主分支；下方事实表中的源码链接使用对应固定提交。

本篇目录：[快照读取](#source-snapshots) · [1. 已确认的基础](#library-facts)／[管理补充核对](#management-library-review)／[命名入口依据](#managed-entry-facts)／[RPC 与嵌入补充](#rpc-extension-facts)／[JavaScript RPC](#javascript-rpc-facts)／[弃用与源码事实](#deprecation-facts)／[任务执行与控制依据](#task-control-facts)／[预制库依据](#prebuilt-library-facts)／[初始化适配](#bootstrap-adapter)／[主动学习接入](#active-learning-adapter) · [2. 三层分工](#responsibilities) · [3. 认知循环与运行分段](#runtime-segments) · [4. 业务安全边界与补丁提交](#patch) · [5. 部署标识与崩溃恢复](#deployment) · [6. 回收与关闭](#cleanup) · [7. 影子验证的边界](#shadow-validation)。

<a id="source-snapshots"></a>

## 源码版本与证据范围

下方事实表按提交标识引用源码。复查时使用对应提交，不能以主分支当前内容代替历史证据。源码中存在测试用例，只能证明该用例已经定义；实际运行结果另见实验报告。

<a id="library-facts"></a>

## 1. 已确认的基础

本表适用前述早期固定提交 `7c195d9`；后续补充分别标明自己的提交，不能从相邻段落推定已经重新核对全部条目。

| 已有机制 | 核对位置 | TinyAGI 的用法及限制 |
| --- | --- | --- |
| 完整 Program 比较 | `runtime/patch_inspect.go`：`ComparePrograms` | 查看结构、声明、能力和符号变化；结构兼容不等于行为正确 |
| 准备与提交补丁 | `runtime/hot_reload.go`：`PreparePatch`、`ApplyPatch` | 宿主先确定业务边界，再使用 VM 安全点提交 |
| 已准备补丁的检查 | `PatchPlan.Inspect` | 读取基准 generation；必须在 plan 关闭或提交之前读取 |
| 版本存活摘要 | `runtime/revision_inspect.go`：`RevisionRetention` | 已发布版本与待提交候选分开，诊断旧代码为何存活 |
| 有界版本引用扫描 | 同上：`RevisionRoots` | 显式限制节点、深度和根数量；`Complete=false` 不能解释为已扫描全部 |
| 新命名调用使用当前版本 | `runtime/scheduler_run.go`、热更新指南 | 可变认知逻辑通过命名函数调用进入；旧闭包和 defer 不自动升级 |
| 按版本定位代码 | `runtime/debug_inspect.go`、`tooling/dap/source.go` | 记录 generation、ProgramHash、SymbolsHash，避免将旧帧归因给新源码 |
| 执行与 scope 分离 | `USAGE.md` 的运行实例章节 | 入口返回不等于后台任务结束；等待取消不等于资源已释放 |
| 分片推进与统计 | `Execution.PollSteps`、`ScopeStats`、`Instance.RuntimeStats` | 有界推进、采样与宿主预算；不等同墙钟 CPU 限速 |
| 时钟与随机输入注入 | `InstanceOptions.Clock`、`Entropy` | 在测试实例中控制部分外部输入 |
| 长期编译会话 | `compiler/service/session.go` 的 `Session.Build` | 构建捕获指定源码版本；不另假设存在名为 BuildSession 的 facade |
| MRPC 绑定与清理 | `RPC.md` | 早期记录包含绑定与清理；当前接入扩大为本地绑定与跨进程能力，逐项契约及更新快照见下方 RPC 补充，不将网络作为所有宿主模块的通信前提 |

版本摘要中的 `Pins` 是显式引用计数，`GlobalRoot` 来自最近的根扫描；它们不是旧版本物理占用字节数，也不是全部闭包数量。引用扫描返回独立诊断数据，不强制释放版本。

尚未在此次核对范围内确认稳定的通用 VM 调度记录/重放、完整 Runtime Observer 或专用事后故障报告 API。当前实验可使用已确认的执行统计、调试信息、宿主调用边界与业务日志，不以这些额外接口为前置条件。

<a id="management-library-review"></a>

### 管理、副本与动态编辑的补充核对

于 2026-09-20 只读核对go-mini 提交 `a0d1558571159cb017d12e4a0a4c1cbf795f8b9a` 的 [USAGE](https://github.com/d7z-team/go-mini/blob/a0d1558571159cb017d12e4a0a4c1cbf795f8b9a/USAGE.md)；以下不覆盖原报告的库版本或实测范围：

| 库文档明确的行为 | 设计影响 |
| --- | --- |
| 长期运行：业务进度由宿主持久化，执行镜像和值快照不是完整 VM 恢复点 | AGI 副本从持久业务状态与固定程序重建，不能宣称已支持任意运行栈克隆 |
| 热更新：旧帧、defer 和闭包保持旧 revision，新命名调用使用当前 revision | 补丁提交本身不能保证正在执行的认知全部切换；立即生效须由宿主管理受影响步骤及旧响应 |
| 热更新保持 globals 与状态契约，不兼容时创建新实例并由应用迁移 | 动态代码提交可准备替代实例，无法兼容则明确失败，不能偷偷清空人格或活动状态 |

<a id="managed-entry-facts"></a>

### 命名入口与编写契约的接入依据

核对日期：2026-09-20；go-mini 提交 `a0d1558571159cb017d12e4a0a4c1cbf795f8b9a`，仅阅读文档和源码，未运行测试。

| 已确认事实 | 本项目采用方式与边界 |
| --- | --- |
| [USAGE 入口生命周期](https://github.com/d7z-team/go-mini/blob/a0d1558571159cb017d12e4a0a4c1cbf795f8b9a/USAGE.md)、[Instance 调用实现](https://github.com/d7z-team/go-mini/blob/a0d1558571159cb017d12e4a0a4c1cbf795f8b9a/runtime/instance_call.go)：Call／Start 在当前 revision 的显式入口表查找名称；未登记时报错 | 从受管理函数声明生成 EntryPoint 或稳定分派入口，不能直接宣称可调用任意内部符号 |
| [编译会话](https://github.com/d7z-team/go-mini/blob/a0d1558571159cb017d12e4a0a4c1cbf795f8b9a/compiler/service/session.go)接受 EntryPoints；[调用集成测试源码](https://github.com/d7z-team/go-mini/blob/a0d1558571159cb017d12e4a0a4c1cbf795f8b9a/integrations/calls_test.go)展示函数到命名入口的显式映射 | 支持生成适配方向；测试源码阅读不等于这轮运行测试或验证任意类型映射 |
| 当前同一实例已有 active execution 时拒绝再启动入口；FFI 回调不能同步重入同一 Instance | 管理调用沿宿主调度，测试可在独立沙箱实例进行，不从函数登记推导任意并发调用 |
| 旧帧、defer、闭包保留旧 revision；补丁保持 globals、导出及命名类型／函数状态契约 | 长期状态由宿主管理，跨调用保存函数标识，边界切换；不兼容契约仍需新实例与明确转换 |

类型与注释驱动的生成器属于 TinyAGI 设计，尚未确认或实现通用 `agi:` 注解能力。固定分派入口不消除库的内部兼容要求。逻辑契约见[受管理函数](runtime-protocol.md#managed-functions)，语法示意见[工程参考](engineering-reference.md#managed-function-tooling)。

<a id="rpc-extension-facts"></a>

### RPC、多语言服务与局部 VM 的补充核对

核对日期：2026-09-20；go-mini 提交 `a0d1558571159cb017d12e4a0a4c1cbf795f8b9a`。只读核对 [RPC.md](https://github.com/d7z-team/go-mini/blob/a0d1558571159cb017d12e4a0a4c1cbf795f8b9a/RPC.md)、[USAGE.md](https://github.com/d7z-team/go-mini/blob/a0d1558571159cb017d12e4a0a4c1cbf795f8b9a/USAGE.md)、[ARCHITECTURE.md](https://github.com/d7z-team/go-mini/blob/a0d1558571159cb017d12e4a0a4c1cbf795f8b9a/ARCHITECTURE.md)，并检索标准宿主及 Rust runtime 源码；未运行生成器、编译器、RPC 服务或测试，未改写早期实验版本与成绩。

| 已确认的库事实／检索边界 | 本项目接入方式与限制 |
| --- | --- |
| `.mrpc` 生成 Go、Mini-Go、Rust 类型及客户端／服务端适配；跨界类型遵循 MRPC 类型规则 | 跨语言接口统一来源；TinyAGI 的管理元数据与表单生成补充在接口之上，不重复手写序列化 |
| 生成 Provider 可本地绑定，Mini-Go 可经 Host／FFI 调用；编译器和核心 runtime 不依赖 RPC／MRPC | MRPC 作为能力接入层，普通内部调用保持直接调用，不要求改造核心 VM |
| Mini-Go 生成 Serve 入口可发布服务，宿主须装配 PublishProvider；连接发起方不限定业务调用方向 | 原生服务、脚本服务及宿主可按受控接口相互调用，发布和反向调用均需宿主授权 |
| Router 支持标签／亲和选择；绑定后固定 Provider，重新选择需创建新客户端 | 仅动态能力使用 Router；声明标签不是权限，切换登记不等于旧客户端已切换 |
| Gateway 支持 ws、wss、ws+unix；启动时没有业务服务，需要显式发布，Endpoint 可作 Binder | 本地原生能力经受控 Unix socket／回环配置连接；不另设业务 stdio 协议或独立中间件要求 |
| 生成调用提供上下文／错误处理及资源交付封装；直接 RouteSet.Call 仍有 Accept／Discard 责任 | 复用生成客户端，不额外维护冲突的调用资源协议；业务 Operation 与授权仍由 TinyAGI 管理 |
| resource 归创建服务实例及连接；路由变化不迁移资源；大载荷分片仍有边界，持续流用 Read／Write 等资源方法 | 临时句柄不当持久事实或可克隆副本；资源投影与按需读取仍由业务契约控制 |
| Program 热更新保留 FFI 会话，不替换 Go handler 或重新发布 Provider | 脚本补丁和原生实现替换分开处理 |
| PrepareReplace／Replace 更新 publication；新绑定选新 Provider，旧绑定及资源继续；Drain 只阻止新绑定 | 生效须结合受影响执行边界与客户端重绑；等待旧 publication 实际关闭再释放 backend |
| Rust crate 在 playground/runtime-rust；rpc feature 提供服务、Router、Endpoint、Host，rpc-gateway 增加传输；生成需 rustfmt | 原生 Rust 可直接实现生成 handler，不要求嵌入 VM；依赖和工具链在真正接入时固定，不宣称已完成产品组合验证 |
| Engine 有 Check／Compile／Test，Compile 返回可共享 Program；Program.Instantiate 创建实例，Call／Start 执行命名入口 | 宿主封装小型试验服务，复用程序并隔离可变状态；不是脚本已经内置完整“子 VM 管理”业务 API |
| 同一活跃 Instance 的重入限制、scope 清理与逻辑限额见命名入口及使用指南 | 子试验使用独立 Instance；父活动预算覆盖全部分支，逻辑限额不代表原生进程资源隔离 |
| 对 stdlib、Go runtime 及 Rust runtime 源码的本次检索未确认通用操作系统子进程管理服务 | 使用宿主标准库封装进程管理的设计；VM 内部任务不能当作系统子进程，检索结果不是对所有未来库能力的否定 |

接入顺序：定义能力接口和管理元数据 → 使用 MRPC 生成绑定 → 实现 Go／Rust／Node.js 或 Mini-Go 服务 → 经受控工具链／实例形成产物与试验结果 → 按采用规则准备运行 → 在调用边界切换实际绑定 → 观察结果并回收所属资源。该顺序是当前 TinyAGI 设计，未实际执行；Node.js 的新增库支持按下面的独立快照解释，不改写上表旧提交的设计范围。

具体工程选择、原生进程管理、构建环境及官方工具链依据见[能力工具链](engineering-reference.md#capability-toolchain)；逻辑生命周期见[运行协议](runtime-protocol.md#capability-lifecycle)，小型实例与主体副本的用途分层见[沙箱](sandbox-evaluation.md#test-scopes)。

<a id="javascript-rpc-facts"></a>

### JavaScript／TypeScript 与 Node.js RPC 补充核对

核对日期：2026-09-21；go-mini 固定提交 `295eb19d74305bd39c3ddf0fa88e01c52fdc446b`。以下为文档、包声明、实现及测试源码阅读；未安装 npm 包、生成绑定、编译或运行互通测试。源码版本的解释见[证据范围](#source-snapshots)。

| 来源与已设计范围 | TinyAGI 接入与边界 |
| --- | --- |
| [RPC 指南](https://github.com/d7z-team/go-mini/blob/295eb19d74305bd39c3ddf0fa88e01c52fdc446b/RPC.md)：TypeScript／JavaScript API；`.mrpc` 可用 `-ts-out` 生成 TypeScript ESM，支持客户端与 Provider，`-ts-runtime` 指定 SDK 导入 | 延伸同一接口来源，JavaScript 从生成绑定构建；不手写平行协议，不将 TS 类型检查当作业务授权 |
| [SDK 说明](https://github.com/d7z-team/go-mini/blob/295eb19d74305bd39c3ddf0fa88e01c52fdc446b/playground/runtime-rust/runtime-wasm/README.md)及[包声明](https://github.com/d7z-team/go-mini/blob/295eb19d74305bd39c3ddf0fa88e01c52fdc446b/playground/runtime-rust/runtime-wasm/package.json)：包名 `@d7z-team/mini-go`，当前声明版本 `0.1.0`、Node `>=22.18.0`；`/rpc` 与 `/rpc-worker` 有 Node／浏览器条件导出 | 采用 `@d7z-team/mini-go/rpc`；版本是此次库声明，不是 TinyAGI 产品版本，也不证明 npm 公共仓库发布状态。具体部署固定所取得分发物 |
| [Node RPC 入口](https://github.com/d7z-team/go-mini/blob/295eb19d74305bd39c3ddf0fa88e01c52fdc446b/playground/runtime-rust/runtime-wasm/sdk/node-rpc.ts)、[Worker](https://github.com/d7z-team/go-mini/blob/295eb19d74305bd39c3ddf0fa88e01c52fdc446b/playground/runtime-rust/runtime-wasm/sdk/node-rpc-worker.ts)、[网络适配](https://github.com/d7z-team/go-mini/blob/295eb19d74305bd39c3ddf0fa88e01c52fdc446b/playground/runtime-rust/runtime-wasm/sdk/rpc-network.ts)：Worker 加载 WASM RPC Endpoint，经 WebSocket 建立连接 | Node 能直接调用／发布服务，不需 Mini-Go Program；仍须分发 SDK 的 Worker／WASM 资源。未由此确认 Node RPC 支持 Unix socket，也不把 Worker 当完整沙箱 |
| RPC 指南及[RPC 类型](https://github.com/d7z-team/go-mini/blob/295eb19d74305bd39c3ddf0fa88e01c52fdc446b/playground/runtime-rust/runtime-wasm/sdk/rpc-types.ts)、[连接实现](https://github.com/d7z-team/go-mini/blob/295eb19d74305bd39c3ddf0fa88e01c52fdc446b/playground/runtime-rust/runtime-wasm/sdk/rpc-runtime.ts)：显式 timeoutMs／AbortSignal，close 与 terminate 分开；断线结束待处理工作，资源失效后重新连接并绑定 | 宿主提供期限并保留操作事实；取消等待或终止 Worker 不证明处理函数／外部动作已停止，不自动重试不明动作 |
| RPC 指南：64 位整数为 bigint，字节为 Uint8Array 或 null，optional 为 undefined，map 为 Map；资源保留原 binding 归属 | 使用生成类型及资源客户端，不以普通 JSON 序列化代替 wire 契约；字段到表单或模型可见表示的转换仍由宿主适配 |
| [Node 测试源码](https://github.com/d7z-team/go-mini/blob/295eb19d74305bd39c3ddf0fa88e01c52fdc446b/playground/runtime-rust/runtime-wasm/tests/node.test.js)含生成 TypeScript RPC 与 Go 双向互通用例 | 表明库已有对应测试场景；证据为测试源码阅读，不代表本项目已运行该用例或完成 Node 接入 |

该快照支持将能力端扩充为 Go／Rust／Node.js（npm），同时保留 Mini-Go 脚本编排及已有宿主接入。工程装配、依赖产物和生命周期见[Node 接入](engineering-reference.md#node-rpc-integration)；宿主管理 Node 服务仍属待实现设计，旧实验成绩不外推到新增路径。

<a id="deprecation-facts"></a>

### 弃用信息、源码分发与初始化接入依据

2026-09-21 只读核对go-mini 提交 `a0d1558571159cb017d12e4a0a4c1cbf795f8b9a`；未运行生成、编译、实例或测试。本记录补充下列事实，不重写早期库快照与实验结论。

| 已确认事实 | 来源与适用边界 |
| --- | --- |
| 文档提取识别以 `Deprecated:` 开始的段落 | [comments.go](https://github.com/d7z-team/go-mini/blob/a0d1558571159cb017d12e4a0a4c1cbf795f8b9a/compiler/doc/comments.go) 的 `deprecatedText`；[model.go](https://github.com/d7z-team/go-mini/blob/a0d1558571159cb017d12e4a0a4c1cbf795f8b9a/compiler/doc/model.go) 的 `Symbol.Deprecated`；[extract.go](https://github.com/d7z-team/go-mini/blob/a0d1558571159cb017d12e4a0a4c1cbf795f8b9a/compiler/doc/extract.go) 将弃用信息写入符号文档。可复用来显示迁移提示，不等于编译器已拒绝弃用调用或自动生成兼容实现 |
| 宿主可注册模块源码 | [USAGE.md](https://github.com/d7z-team/go-mini/blob/a0d1558571159cb017d12e4a0a4c1cbf795f8b9a/USAGE.md) 的 `NewStandardLibrary`、`NewModuleLibrary`、`NewLibrarySet` 与 `Config.Libraries`；逻辑导入前缀和提供的 FS 决定依赖装配，使用期间源码 FS 须保持不变 |
| 检查、编译、实例与命名调用可分开组织 | 同一指南及[已有读取记录](#rpc-extension-facts)；能支持宿主引导器编译候选、创建独立实例，不表示已有 TinyAGI 人物生成／迁移流程 |
| 源码、资源和 `.mrpc` 声明是分发边界 | [ARCHITECTURE.md](https://github.com/d7z-team/go-mini/blob/a0d1558571159cb017d12e4a0a4c1cbf795f8b9a/ARCHITECTURE.md) 的“编译、链接与派生物”；执行镜像、生成绑定、缓存等属于当前工具链派生物，不能将旧缓存当作跨客户端可启动保证 |
| 程序比较与补丁适用范围有限 | [基础读取记录](#library-facts)的 ComparePrograms／PreparePatch 处理程序结构与运行补丁；不能单独证明宿主接口语义、业务数据或整个客户端升级兼容 |

本次源码与文档阅读未确认现成的“按 API 修订保留旧实现、自动迁移人格程序、完整调用点弃用告警”服务。上述是 TinyAGI 待实现的宿主设计，不能把文档字段或单个编译 API 记作完整能力已具备。

<a id="prebuilt-library-facts"></a>

### 预制源码库、宿主装配与工具接入依据

2026-09-21 只读核对提交 `a0d1558571159cb017d12e4a0a4c1cbf795f8b9a`，未运行编译或测试。[USAGE.md](https://github.com/d7z-team/go-mini/blob/a0d1558571159cb017d12e4a0a4c1cbf795f8b9a/USAGE.md)说明 Engine 自动提供标准库源码，额外模块通过 NewStandardLibrary／NewModuleLibrary／NewLibrarySet 注册；宿主提供源码集合，compiler 按 import 选择依赖，使用期间库 FS 保持不变。系统能力仍需显式装配 provider。这支持“预制源码与运行能力分别提供”的工程分工。

同一指南说明 Go 应用可使用 compiler/language 查询语言信息，compiler/service.Session 管理分析和构建；[symbols.go](https://github.com/d7z-team/go-mini/blob/a0d1558571159cb017d12e4a0a4c1cbf795f8b9a/compiler/language/symbols.go)提供 DocumentSymbols／WorkspaceSymbols。[既有记录](#deprecation-facts)另确认文档提取、Check 及派生物边界。可据此设计源码结构、文档和诊断适配，不将工具存在解释为 TinyAGI 已实现完整能力库或初始化保证。

TinyAGI 的预制命名空间保护、客户端发布身份、个体包装区分、工具权限和投影过滤由宿主补充。语言标准库、TinyAGI 预制能力及 Self 个体程序各有维护来源；预制操作复用 MRPC／Host 及原状态所有者，客户端升级维护权威实现，个体可选用并按兼容规则迁移。详细[工程映射](engineering-reference.md#client-library)与[逻辑契约](runtime-protocol.md#prebuilt-library)分别维护。

<a id="bootstrap-adapter"></a>

### 提示词引导器与 Self 迁移的宿主适配

Go 宿主先登记稳定人物身份、有效程序及引导进度，再用既有模型与工具端口形成候选。完整提示词和迁移说明是可追溯资源；读取仍有目的和范围，机密不进入提示词。未有可运行 `.mgo` 或其启动失败时，有限工具循环由宿主推动，认知实例成功采用后恢复正常主体运行，不另外设置常驻竞争人格。

编译适配按固定源码及库集合调用 Check／Compile，将受控 Host／Provider 装配到独立 Instance；试验、预算、结果及采用归原所有者。客户端更换工具链后重新检查实际源码，旧程序只能在实际兼容条件满足时继续使用。对 TinyAGI 自有接口保留旧源码包装或对应 handler，Deprecated 元数据仅描述状态；接口语义、支持窗口与迁移完成记录由宿主维护。

必要兼容维护以用户更新请求或既有授权策略为来源，即使主动学习关闭也可按单独范围和预算处理；不能用迁移任务代替被禁止的自发学习。详细映射见[工程参考](engineering-reference.md#prompt-bootstrap)，完整语义见[运行协议](runtime-protocol.md#bootstrap-migration)。

<a id="task-control-facts"></a>

### 任务执行、前台入口与控制的固定提交核对

2026-09-21 只读核对提交 `a0d1558571159cb017d12e4a0a4c1cbf795f8b9a` 的文档、实现及测试源码，未运行库测试、产品程序或新实验。以下测试名表示已阅读的用例，不表示测试已实际运行。

| 库事实 | 来源及宿主适用边界 |
| --- | --- |
| Start 遇到活跃前台 Execution／foreground 会拒绝新入口 | [instance_call.go](https://github.com/d7z-team/go-mini/blob/a0d1558571159cb017d12e4a0a4c1cbf795f8b9a/runtime/instance_call.go) 的 start；Pending 不等于前台已释放，不能依赖异步 FFI 自动接纳另一前台调用 |
| PollSteps 有本次推进额度，Ready 可唤醒；累计限制保持 | [execution.go](https://github.com/d7z-team/go-mini/blob/a0d1558571159cb017d12e4a0a4c1cbf795f8b9a/runtime/execution.go)、[execution_poll_steps_test.go](https://github.com/d7z-team/go-mini/blob/a0d1558571159cb017d12e4a0a4c1cbf795f8b9a/runtime/execution_poll_steps_test.go)；让出 worker 与结束业务执行分别处理，步数非墙钟保证 |
| Wait 的 context 取消请求取消执行；WaitScope 只限制等待 | [execution.go](https://github.com/d7z-team/go-mini/blob/a0d1558571159cb017d12e4a0a4c1cbf795f8b9a/runtime/execution.go) 的 waitValues、[execution_scope.go](https://github.com/d7z-team/go-mini/blob/a0d1558571159cb017d12e4a0a4c1cbf795f8b9a/runtime/execution_scope.go)；ScopeDone 等待该调用的 task、timer 及 FFI 收束，不代表远端业务效果消失 |
| InterruptHandle 绑定 Execution，Interrupt 调用 requestCancel | [execution.go](https://github.com/d7z-team/go-mini/blob/a0d1558571159cb017d12e4a0a4c1cbf795f8b9a/runtime/execution.go)；Cancel 取得 VM owner 处理控制，Interrupt 仅提交请求；[scheduler_lifecycle_test.go](https://github.com/d7z-team/go-mini/blob/a0d1558571159cb017d12e4a0a4c1cbf795f8b9a/runtime/scheduler_lifecycle_test.go) 的 TestInterruptHandleOnlyCancelsItsExecution 检查旧句柄不取消新执行 |
| scope 取消与实例故障边界不同 | 同一测试文件的 TestCancelOneBackgroundScopeKeepsOtherScope、TestLibraryBackgroundPanicFaultsInstance；[vm_error_limits_test.go](https://github.com/d7z-team/go-mini/blob/a0d1558571159cb017d12e4a0a4c1cbf795f8b9a/runtime/vm_error_limits_test.go) 的 TestVMEnforcesStepLimitInsideLoopAndKeepsLibraryOpen。library scope 步数限制可局部结束，未恢复后台 panic 可使实例失败，scope 不是全部故障的隔离边界 |
| 普通入口与 main 的生命周期不同 | [USAGE.md](https://github.com/d7z-team/go-mini/blob/a0d1558571159cb017d12e4a0a4c1cbf795f8b9a/USAGE.md) 的入口表；main 返回会结束实例其余任务，普通入口返回与 scope 完成分开 |
| FFI 回调须快速且不可同步重入同实例，RPC 长任务需配合取消 | [USAGE.md](https://github.com/d7z-team/go-mini/blob/a0d1558571159cb017d12e4a0a4c1cbf795f8b9a/USAGE.md)、[ARCHITECTURE.md](https://github.com/d7z-team/go-mini/blob/a0d1558571159cb017d12e4a0a4c1cbf795f8b9a/ARCHITECTURE.md)、[RPC.md](https://github.com/d7z-team/go-mini/blob/a0d1558571159cb017d12e4a0a4c1cbf795f8b9a/RPC.md)；阻塞工作在提供者有界执行器中运行，宿主仍承担实际资源清理与停止核对 |

任务标识到执行／子工作映射、控制来源授权、继续推进资格、阻断解除及迟到结果处理属于 TinyAGI 宿主设计。库接口不直接提供业务任务控制面，也不证明主体持续响应已经端到端验证。接入见[工程参考](engineering-reference.md#task-execution)，逻辑见[任务控制](runtime-protocol.md#task-control)。

<a id="responsibilities"></a>

## 2. 三层分工

| 层 | 责任 |
| --- | --- |
| 通用 VM | 执行、调度、scope、FFI、限额、版本与热更新 |
| TinyAGI Go 宿主 | 认知步骤、状态提交、操作、权限、事件、部署、影子验证与复盘 |
| go-mini 认知程序 | 上下文组织、下一步意图、能力选择、心智协作和认知策略 |

认知与能力的当前边界：go-mini 选择资源及读取范围，只取得投影和所请求的内容；模型推理及 KV 计算由外部计算组件完成。跨业务边界的请求、结果、状态修订与接续沿[统一事件协议](runtime-protocol.md#events)表达，宿主绑定来源和执行域，回调不直接重入 VM。认知可经能力创建或接入外部事件源，闹钟仅为通知源示例；核心与 VM 不内置其业务计时。适配器可在宿主进程中，外部通知对象由相应提供者维护；内部步骤完成也可推动有目的的接续。这些是 TinyAGI 的设计边界，不是声称 go-mini 已提供这些业务能力。

`StepID`、`MindID`、`DecisionID` 等属于宿主协议，不要求 VM 知道这些概念。接口通过 MRPC 生成绑定；稳定宿主能力本地注入 FFI，动态原生能力由宿主管理子进程并配置跨进程绑定，不需要为了所有本机函数建立网络服务。

生产认知实例只装配受控的 TinyAGI 宿主接口，不注入可绕过动作登记的通用文件、Shell、网络 provider 或任意远程路由 fallback。实际执行能力由 Go 操作模块按范围委托给受控提供者；凭据由宿主保管并按用途交受信适配器或原生服务使用，原值不回传认知；协议内填写目标地址不能自动获得新的访问范围。

go-mini 的 Go module path 为 `github.com/d7z-team/mini-go`，与仓库名称不同。实验通过固定源码提交确定依赖版本，复现实验或准备接入时应使用报告注明的版本。

<a id="active-learning-adapter"></a>

### 主动学习策略与宿主接入

主动学习模块按受管理编写契约提供选题、实践、结果解释和策略候选入口，使用已记录的命名调用、独立实例、MRPC 与补丁机制。库只承担执行、调用和资源生命周期；学习活动来源、强度及自动采用资格由 TinyAGI 宿主判定，不将它们记录为 go-mini 已有 API。库事实继续采用上方固定提交读取记录，上述接入方式尚无新增库实验结果。

学习强度最低为关闭。宿主在创建／接续学习执行、接纳下属工作及自动采用之前核对当前强度；不能仅让脚本在入口自行判断，也不能从同一 Program 新建 Instance 获得新额度。关闭时取消或收束所属工作，等待和回收行为遵循库原契约，不把 Cancel 返回或入口结束当成所有后台资源已经关闭。

普通业务实例、已采用程序和共享 Host／Provider 的生命周期独立，关闭学习不应将它们一并销毁。用户明确要求的学习由宿主按独立任务范围接纳，扩展及子 VM 不能通过自报任务来源绕过零强度。学习策略自身修订沿候选比较和边界切换，当前评价条件、运行强度及历史证据不随候选代码被替换。完整映射见[工程参考](engineering-reference.md#active-learning-integration)，语义见[强度契约](runtime-protocol.md#learning-intensity)。

<a id="runtime-segments"></a>

## 3. 认知循环与运行分段

核心认知循环继续写在 go-mini 内，宿主负责推进 VM 和交付上下文。下列是业务伪代码，`Next`、`AcceptOperation`、`Commit` 尚不是已存在的 TinyAGI API：

```text
RunSegment:
    循环:
        ctx, available = Host.Next()
        如果不再接纳本分段: 返回
        continuation = Step(ctx)
            按需 Host.AcceptOperation(ctx.step_token, request_key, request)
            短调用可在局部预算内取得结果；长工作只保留操作引用并返回
            已接纳操作及实际读取依据由宿主记录
        receipt = Host.Commit(ctx.step_token, continuation)
        处理提交结果，再获取下一上下文
```

步骤内操作接纳与最终状态提交分别沿[运行契约](runtime-protocol.md#step-operation-admission)处理；Commit 关联已有操作并接纳尚未提交的意图，不重复派发。最终步骤被撤销不抹去独立操作；是否继续或停止由带目标范围的当前控制决定。

分段采用 library 入口承载一次运行段。`Step` 及其调用图包含可变认知逻辑，外层循环只调度上下文和提交。按编写契约采用有可结束边界的调用，跨调用进度由宿主保存；长驻旧根循环不作为默认，尚无分段成本或认知连续性收益实测。长期任务的事实状态仍独立于 VM scope。

宿主在步骤边界结束分段，等待入口及该分段所属局部 scope 收束，再重入 library 入口；长任务由宿主 Operation 独立管理，不在此等待整项任务结束。连续性取决于所保留的状态是否完整，不能由重入动作本身保证。需要回收 globals 或彻底释放旧实例资源时，可以研究关闭实例后从持久状态新建的方案。

实测在合成整数状态下，同实例重入保留 global，新实例需要显式恢复；这不等于语义认知状态已经验证。全局闭包可在 scope 结束后继续保留旧版本，因此分段不能自动替代引用与回调管理。默认引用扫描也可能截断，须保留 Complete 和扫描预算信息。

这一设计针对两个已确认的运行约束，但其代价尚未测量：

1. 永久外层调用帧可能长期引用最早版本。命名调用能进入新代码，但不会释放旧根帧。
2. scope 的累计步数不会因 `PollSteps` 或热更新重置。长期循环默认可能耗尽累计配额。

分段按可结束的业务工作范围组织，具体资源上限随用途配置，不是固定的思考次数。无输入时由宿主就绪通知或可处理输入的有界事件循环等待，不忙轮询，也不把外部长任务等待留在唯一前台入口。每个步骤的超时或指令上限由宿主监控；越界时取消相应执行、撤销步骤令牌并从已确认工作区接续该心智，不假定 VM 已提供按业务 Step 自动重置的配额。

配额对照确认新 scope 获得独立预算，热更新不重置旧 scope 计数。宿主还需维护跨分段的活动预算，并单独考虑标准库初始化成本；真实模型／工具的计量仍待接入，不能把反复重入视为活动预算刷新。宿主组合实验已在两段新实例之间保留累计夹具调用数，未测试预算耗尽或真实 token／费用。

既有实验曾比较不同后台状态约束，证据按原范围保留。当前设计要求的编写契约要求跨调用工作通过宿主 Operation／事件接续，局部闭包和内部任务不越过调用生命周期；该选择来自当前规范，不作为旧实验已经证明的最优方案。

<a id="patch"></a>

## 4. 业务安全边界与补丁提交

本节流程针对认知 Program；原生 Provider 的替换、旧客户端重绑及资源归属采用[RPC 补充契约](#rpc-extension-facts)与[工程映射](engineering-reference.md#capability-toolchain)，不能套用 ApplyPatch 替换原生 handler。

同一心智一次只接纳一个部署操作。准备候选程序和影子验证可以在独立实例中进行，不占用生产认知步骤。

主体自主采用前，候选须在拟采用用途下满足[能力与回归门槛](sandbox-evaluation.md#regression-gates)，报告关联程序、宿主、模型、提示、材料及评价配置。编译、`ComparePrograms` 和补丁兼容检查只回答结构问题，不代替完整任务比较；证据不足时保留候选，沿用现有配置。通过测试形成自主采用依据；人工管理提交按既定的[生效契约](management-workspace.md#apply)完成结构、授权与切换核对，不把完整实验作为每次提交的强制前置。

对应调用边界契约的库接入流程：

1. 保存源码、类型与注释描述、配置、生成适配及 Program 身份，检查编写规范；自主采用时另关联相应用途的验证报告。
2. 使用 `ComparePrograms` 查看差异，检查实际授权需求；能力声明变少不能直接证明风险降低。
3. 停止目标心智接纳新步骤，等待当前步骤提交或撤销；确认没有步骤内 VM 子任务或不受宿主管理的调用。
4. 持久化部署意图与目标产物，调用 `PreparePatch`，保存 `Inspect` 报告后调用 `ApplyPatch`。
5. 记录成功的实例、generation 和代码身份，完成生效状态及调用／页面描述的一致切换，再开放新调用并报告提交成功。

在边界上可以存在尚未完成的宿主 Operation，因为它们不依赖旧 VM 栈；请求和完成事件必须有稳定的协议版本，候选认知代码需能处理这些结果。

`busy` 或 `stale_plan` 会关闭原 plan，必须重新准备。未提交的 plan 由创建者关闭。结构不兼容时仅在业务状态与在途结果能够明确转换时准备替代实例，否则提交失败并保留旧内容；不让 VM 自动迁移主体历史。

仅记录步骤起始 generation 不能证明步骤内未跨版本调用，因此生产部署必须遵守上述业务边界，不能仅凭 VM 允许随时 patch 就在认知步骤中途切换。

<a id="deployment"></a>

## 5. 部署标识与崩溃恢复

需要区分：

- `ArtifactID`：源码、配置与工具链输入的产物身份，并关联 ProgramHash 和 SymbolsHash。
- `DeploymentSeq`：本地 SQLite 中持久保存的部署序号，关联目标 Mind；重新部署旧源码也分配新序号。
- `RunID + InstanceID + Generation`：本次宿主运行中的 VM 执行身份，generation 只在该实例内向前推进。

不能把 VM generation 当作跨进程重启的全局序号。新实例可以从初始 generation 开始；历史追踪使用以上完整关联。

核心 go-mini 认知运行嵌入单个 TinyAGI 宿主进程，多个心智按需使用实例；可选原生能力子进程由同一宿主管理，不另持有主体状态。进程重启从本地 SQLite 状态和代码文件重建 VM，不保存调用栈或资源句柄；未完外部操作仍需核对，新代码必须兼容其结果协议。

数据库提交与 VM 内存切换没有共同事务。宿主先登记部署意图，切换成功并登记完成前保持业务入口关闭：

- VM 切换失败：保留当前业务部署，记录失败原因后再开放。
- VM 切换成功但完成记录暂时失败：继续关闭入口，保留 owner 并重试登记，不执行未记录版本的业务步骤。
- 进程在中间崩溃：旧 VM 已消失，新进程按数据库最后完成的部署新建实例；未完成部署标为中断，再决定是否重新验证和发布。

回到历史代码是新的部署，不撤销已提交状态、已发送操作或现实动作。历史代码还需兼容当前宿主数据和结果协议；不兼容时迁移或拒绝该部署。

<a id="cleanup"></a>

## 6. 回收与关闭

本节关闭流程针对明确选中的实例；单项任务控制先按[任务归属](engineering-reference.md#task-execution)找到目标执行，不关闭无关核心、实例或共享服务。停止目标的新步骤和补丁，通知脚本在边界返回或按控制请求取消，推进并等待入口，再等待所属 scope，最后由实例所有者调用 `Shutdown`。不依赖取消时一定执行 guest defer。

关闭等待超时仅代表本次等待结束，owner 仍承担继续清理责任。Instance 关闭自己的 FFI Session，共享 Host、RPC 连接和后台服务由对应创建者在实例清理后关闭。

Operation 的持久记录不随 VM 关闭消失，但当前进程里的执行仍需按其重连、取消或结果核对协议处理。不能因为换了 VM 就声称远端动作已停止。

<a id="shadow-validation"></a>

## 7. 影子验证的边界

影子验证属于[统一沙箱](sandbox-evaluation.md)的用途；任务、程序、Reference 及复盘也可使用沙箱。旧库核对日期与实验版本保持原样，2026-09-20 的沙箱接口补充见[独立来源记录](sandbox-evaluation.md#sources)。

当前候选在新的 Instance 中重放指定业务事件，并提供替代的事件源、时钟、随机源、模型结果和能力结果。替代能力禁止实际外部写入，不能只靠脚本自觉遵守。独立实例还需配套分域的活动／记忆、文件区、订阅与回调；不共享生产 FFI 会话或能力句柄，不提供生产 fallback。允许的真实模型计算仍受外发范围和总预算约束；新实例本身不是完整沙箱证明。

同一代码与完整固定输入可用于受控场景的回归；代码变更产生不同能力请求时，必须由替代服务响应，或明确报告该分支缺少夹具。不能按“第 N 次调用”盲目返回旧录制的第 N 个结果。

重新调用真实模型属于重新评估，替换行为后模拟未来属于反事实实验；两者都不承诺与历史相同。没有调度决策与全部非确定输入的记录，不把业务事件重放称为 VM 级确定性重放。
