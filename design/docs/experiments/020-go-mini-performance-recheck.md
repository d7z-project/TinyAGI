# 报告 020 · go-mini 性能更新与工作台回归

实验日期：2026-09-28（Asia/Shanghai）。证据：固定源码、官方 npm 分发物、原有合成工作区、真实 Chromium／Angular／Go MRPC，以及受影响的 Go 库测试；无模型调用。

[库接入参考](../go-mini-integration.md#performance-update) · [原工作台实验](019-management-workspace-validation.md) · [工作台状态](../research-plan.md#management-extension)

目录：[结论](#conclusion) · [条件](#conditions) · [结果](#results) · [源码核对](#source-review) · [复核与边界](#audit) · [上游编译验证](#upstream-compiler-tests) · [扩额对照](#expanded-limits)

<a id="conclusion"></a>

## 结论

**更新后的前后端主链路通过；两个原界面工作区在所测预算下尚未完成浏览器语言服务打开。** 已观察的停止原因为步数、内存或期限限制，不据此判定编译语义错误。编译能力、运行预算和实际工作区的耗时分别评价；上游已有自举编译验证，其后端、输入及配置见[覆盖对照](#upstream-compiler-tests)。

宿主编译、浏览器执行、真实管理 RPC 的 14 项原回归全部通过。Go 缓存与执行控制的 37 个顶层目标测试通过，六组原生工作区打开／分析正常；Node 小型工作区与重复分析快照检查通过。

官方 npm 包默认设置下，原完整工作区与精简 FFI 工作区均在 `open` 阶段返回 `step_limit`，尚未进入 `prepare`、绘制及实际 RPC 的后续断言。该组保持发布物和默认额度不变；后续在独立副本进行[扩额对照](#expanded-limits)，分别记录新的限制。默认组既不证明增加额度足够，也不证明优化对执行速度无效。

<a id="conditions"></a>

## 固定条件与分发身份

| 项目 | 条件 |
| --- | --- |
| Go 源码快照 | [提交 `6a4047e`](https://github.com/d7z-team/mini-go/tree/6a4047e) 的独立归档，未修改；与性能提交 `fc9366cbc35f28b157f124825d2466f736bd4b55` 的差异仅在发布 workflow 和开发文档 |
| npm SDK | `@d7z-team/mini-go@0.0.19-git.gfc9366c`，官方 tarball，固定完整性；不使用旧目录中的 WASM 或编译器镜像 |
| 发布标签 | 本次 registry 返回 `git → 0.0.19-git.gfc9366c`，`latest → 0.0.13-git.gdbbdeda`；本次复测显式选择精确版本，标签状态不作为永久保证 |
| Go 工具链 | `go1.27.1-X:nodwarf5 linux/amd64`，`GOTOOLCHAIN=local`、`GOWORK=off`；与报告 019 的 Go 1.26.6 不同，不作原生耗时的受控加速对照 |
| 前端与驱动 | Node v22.23.2；复用原 Angular 22.2.0 AOT 页面、Playwright 1.62.1 和 Chromium 夹具；浏览器使用 `--no-sandbox`，不评价系统隔离 |
| 编译输入 | 原完整工作区、原 639 字节精简 FFI 界面，以及原六组诊断输入逐字复用 |
| 编译设置 | 发布包的 `createLanguageService()` 默认设置，单请求默认 30 秒；编译 VM 默认累计步数 100,000,000、逻辑堆 128 MiB、对象上限 500,000 |
| 实验顺序 | 重型构建与浏览器运行分开；两个工作区串行、各一次，分别建立浏览器和编译服务；不做全负载性能基准 |
| 业务状态 | 本机合成业务、测试身份和合成机密；宿主用新源码重建，保留原断言与两份契约各自匹配的绑定 |

输入旧版完整工作区使用原声明；14 项主链路使用后来增加 `Compile` 的声明，两者分别装配匹配的 Go 夹具，未混用契约。主链路仍通过宿主生成新镜像后交浏览器执行。

npm integrity：`sha512-JQVcSQG3baH9SsOOyQeXevkHtBVFxDMoGnKX3QqIV83JD1fhUthNkdyBm8ubH9RmwnVQzJN5IrKcFJkWzdQUog==`。

<a id="results"></a>

## 实际结果

| 检查 | 结果 | 支持范围 |
| --- | --- | --- |
| 原 Angular／MRPC 主链路 C01–C14 | 14 通过，0 失败 | 动态绘制、直接 Mini-Go RPC、TypeScript 状态查询、64 位值、身份／执行域、草稿与焦点、候选替换、任务独立、断线核对、机密分流、取消、文件控件和清理 |
| 小型浏览器语言工具 | C03 通过 | 编译并执行预期文本、只读依赖限制、错误诊断、取消后可继续使用；不是复杂工作区通过 |
| 完整工作区浏览器源码编译 | `open` 返回 `step_limit` | 服务创建开始至错误返回约 14.11 秒，包含创建开销；不是完成编译的时间 |
| 精简 FFI 界面浏览器源码编译 | `open` 返回 `step_limit` | 同口径约 20.96 秒；不是完成编译的时间 |
| Go 编译缓存／相关调度目标测试 | 20 个顶层测试通过 | 缓存限制身份、限制诊断、临时缓存所有权／容量、链接镜像与符号复用及阻塞上下文 |
| Go 取消、定时器和任务所有权目标测试 | 17 个顶层测试通过 | 控制取消、安全点、scope、等待交接、FFI 及定时器清理；不代表完整并发或 race 矩阵 |
| Node 官方小型工作负载 | `pure`、`typed-view` 均通过 | 打开、诊断和重复分析快照身份；打开约 343.8／646.7 ms，重复分析约 56.4／55.1 ms，均为单次观察 |

Go 日志合计包含 64 条顶层及子测试通过记录，属于 37 个顶层测试，不把子项重复算成独立实验。矩阵驱动退出 0 表示完成两项检查，其功能成绩仍是两项失败。

六组同输入原生 `workspace/open` 与 `workspace/analyze` 均无返回错误或工作区诊断；打开时间如下。它们是原生探针结果，不能代替浏览器成功或完整编译成绩。

| 输入 | 原生打开时间 |
| --- | --- |
| 纯函数 | 0.78 ms |
| 类型化视图，无 FFI | 0.79 ms |
| 最小 errors 引用 | 1,299.56 ms |
| 最小 ffi 引用 | 1,288.15 ms |
| 原精简界面 | 1,391.89 ms |
| 原完整界面 | 1,644.39 ms |

<a id="source-review"></a>

## 源码变化与接入影响

以下为 `fc9366c` 的源码核对，与上表实际执行分别解释。

| 更新 | 对 TinyAGI 的影响与边界 |
| --- | --- |
| [限制参数参与缓存身份](https://github.com/d7z-team/mini-go/blob/fc9366cbc35f28b157f124825d2466f736bd4b55/compiler/limits.go) | 归一化编译限制纳入缓存键，旧的宽松编译结果不能直接绕过新限制；目标测试已覆盖 |
| [临时缓存计量与准入](https://github.com/d7z-team/mini-go/blob/fc9366cbc35f28b157f124825d2466f736bd4b55/compiler/cache/transient.go) | 估算包含泛型语法树等载荷，过大项在克隆前受限；不把缓存设置等同于进程 RSS 硬上限 |
| [Rust 执行路径](https://github.com/d7z-team/mini-go/blob/fc9366cbc35f28b157f124825d2466f736bd4b55/playground/runtime-rust/src/instance/task_runner.rs)与[定时器](https://github.com/d7z-team/mini-go/blob/fc9366cbc35f28b157f124825d2466f736bd4b55/playground/runtime-rust/src/instance/timer.rs) | 减少任务私有执行路径上的引用计数和计时检查开销；不代表标准库分析的总指令量已降到默认额度内 |
| [Go 等待处理](https://github.com/d7z-team/mini-go/blob/fc9366cbc35f28b157f124825d2466f736bd4b55/runtime/scheduler_wait.go) | 统一空闲等待行为；此次相关控制回归通过，主体／任务的独立生命周期设计继续保留 |
| [SDK 语言服务](https://github.com/d7z-team/mini-go/blob/fc9366cbc35f28b157f124825d2466f736bd4b55/playground/runtime-rust/runtime-wasm/sdk/tools.ts) | 简化 dispose 的收束；公开 `CompilerOptions` 仍只包含 Worker／WASM 地址和取消信号，未开放普通调用者的编译步数／堆预算配置 |
| 编译身份已改变 | TinyAGI 继续固定源码、编译器、runtime 与产物身份，重新准备匹配镜像；不把旧缓存作为跨工具链兼容保证 |

上游新增的浏览器／Node 工作负载回归选择 `pure` 和 `typed-view`；这与本项目带 FFI／RPC 标准库依赖的两个失败工作区不是同一输入范围。源码中存在回归不能替代本项目消费者工作区通过。

当前继续使用“匹配镜像负责正常展示、宿主编译源码候选、浏览器语言工具按已测范围开放”。后续要关闭该问题，需让原两个工作区在明确支持的正式配置下完成打开、分析、生成镜像、执行和真实调用；不能只以更早返回限制错误或纯函数变快作验收。

<a id="audit"></a>

## 复核、准备失败与边界

独立证据包保存固定输入、源码归档、npm tarball、驱动、条件、构建日志、逐项结果、页面截图／trace 及汇总。首次受限环境禁止本机监听 socket，宿主未进入库工作负载；在允许本机测试服务的环境重跑，原准备失败单独保留。一次构建命令指向了项目根目录，已在任何执行前改为夹具模块重建；未将错误目录的构建作为主链路依据。

| 材料 | SHA-256 |
| --- | --- |
| Go 源码归档 | `09294a482e1677071f9f755e31814e99a6174da9fada83564395cd3775007068` |
| 官方 npm tarball | `da07c758273f7aad175246081a2ae35dc2438536d750ea811cb5601cda6ebfbc` |
| 138 项材料哈希清单 | `381a091261fbf51e6d601756d5a086f86f369a120a0a43046708c4659ccc80cb` |

报告 019 的 327 项基线、11 项补充、290 项预算对照和 109 项诊断材料全部逐项核对未变化。本次复测不修改原失败，不修改相邻库工作区。

本次复测未重跑 Rust 原生测试、全部库回归、完整跨语言 conformance、race 或 CPU 采样。已发布 WASM 后端通过所列浏览器和 Node 场景，不能据此声称 Rust 原生全部测试通过。未测任意源码、长期运行、完整主体、真实机密或生产安全；性能数据只描述固定用例，不给出通用加速倍率。

<a id="upstream-compiler-tests"></a>

## 上游编译器验证的覆盖对照

上游已定义编译器镜像、生成产物执行和原生／VM 差分验证。下表区分源码核对与本报告追加运行，不以存在测试代码推定该后端所有输入已经通过。

| 测试入口 | 实际覆盖与预算 | 证据范围 |
| --- | --- | --- |
| [Go `TestCompilerImageCompilesAndRunsSource`](https://github.com/d7z-team/mini-go/blob/fc9366cbc35f28b157f124825d2466f736bd4b55/compiler/bootstrap/compiler_service_test.go) | 构建编译器镜像，在 Go VM 中执行 `prepare`，再运行生成产物并检查结果；包含 build tags 与嵌入内容 | 源码核对，本次未重跑该测试 |
| [Go 自举配置](https://github.com/d7z-team/mini-go/blob/fc9366cbc35f28b157f124825d2466f736bd4b55/compiler/bootstrap/compiler_service_test_helpers_test.go)与[差分测试](https://github.com/d7z-team/mini-go/blob/fc9366cbc35f28b157f124825d2466f736bd4b55/compiler/bootstrap/compiler_differential_test.go) | 编译实例配置 20 亿步、8 GiB 分配计量上限及 4 Mi 集合元素上限；比较原生／VM 的诊断、镜像、符号和热缓存结果 | 上限不是实际消耗；Go 分配计量不能直接等同 Rust 逻辑堆、WASM 线性内存或进程 RSS |
| [Go `TestCompilerWorkloadsCheckAndAnalyze`](https://github.com/d7z-team/mini-go/blob/fc9366cbc35f28b157f124825d2466f736bd4b55/compiler/bootstrap/compilerentry/workloads_test.go) | 原生 Go 直接运行五组工作负载的 check、open 和重复 analyze，包含 `errors`、`ffi`、`ffi-view` | 在未修改的固定源码副本实际运行，五组全部通过；不是浏览器后端运行这五组 |
| [Rust 编译入口](https://github.com/d7z-team/mini-go/blob/fc9366cbc35f28b157f124825d2466f736bd4b55/playground/runtime-rust/tests/compiler_entry.rs)与[浏览器／Node 编译冒烟场景](https://github.com/d7z-team/mini-go/blob/fc9366cbc35f28b157f124825d2466f736bd4b55/playground/runtime-rust/runtime-wasm/tests/compiler_scenario.js) | 初始化编译器镜像并重复 check 空 `main`，配置 500 万步；不包含实际界面的标准库依赖闭包 | 源码核对；本报告的其他小型编译成绩分别列出，不冒充该套件全部重跑 |
| [Rust 会话测试](https://github.com/d7z-team/mini-go/blob/fc9366cbc35f28b157f124825d2466f736bd4b55/playground/runtime-rust/tests/compiler_session.rs)与[浏览器／Node tools 测试](https://github.com/d7z-team/mini-go/blob/fc9366cbc35f28b157f124825d2466f736bd4b55/playground/runtime-rust/runtime-wasm/tests/tools.test.js) | 共享 workload 回归明确筛选 `pure`、`typed-view`；其他小型夹具另覆盖查询、prepare、调试、取消和接续 | 不覆盖共享语料中的全部 FFI 依赖工作区 |

直接编译 `prepare` 与语言服务 `workspace/open` 是不同操作。前者生成产物，后者还建立可分析、查询和编辑的工作区；TinyAGI 不把全部语言工具流程设为每次界面运行的前提。镜像携带标准库源码不等于依赖已完成语义分析，参见[上游测量说明](https://github.com/d7z-team/mini-go/blob/fc9366cbc35f28b157f124825d2466f736bd4b55/DEVELOPMENT.md)。

公开 `MiniGo.create` 提供 `workload: "compiler"`、`maxSteps` 和 `maxHeapBytes`；该版本 WASM 通用入口限制堆配置不超过 256 MiB，且未开放对象数。`createLanguageService` 的公开 `CompilerOptions` 没有相同预算字段。因此不能把“语言服务缺少配置入口”写成“所有编译 API 都不能调预算”，也不能直接将 Go 自举测试的数值照搬为浏览器默认值。

<a id="expanded-limits"></a>

## 独立副本的扩额对照

保持原两个工作区、官方编译器镜像、编译算法及普通界面 VM 的限制不变。在固定源码副本补充语言服务到编译 VM 的预算参数传递，并允许请求期限超过原 30 秒上限；重新构建 WASM 与 TypeScript。这是实验适配，不是官方 npm 新增 API，也没有修改相邻库工作区。

按前一组的实际限制逐项扩大，所有提前终止仍保留未完成状态：

| 条件 | 完整工作区 | 精简 FFI 工作区 |
| --- | --- | --- |
| 10 亿步；30 秒；128 MiB／50 万对象 | `open` 触发期限，约 31.98 秒 | `open` 触发期限，约 30.73 秒 |
| 10 亿步；120 秒；128 MiB／50 万对象 | 解析依赖时触发堆或对象数限制，约 31.99 秒 | 解析依赖时触发堆或对象数限制，约 30.23 秒 |
| 10 亿步；120 秒；512 MiB／200 万对象 | `open` 触发期限，约 122.00 秒 | `open` 触发期限，约 122.00 秒 |

时间为各组 `open` 调用开始至错误返回，不含服务创建；取消和收束可使返回稍晚于期限。编译器逻辑堆／对象预算与浏览器实际内存占用不同，表中数值不是 RSS 测量。没有源码诊断或生成产物可供本组检查，不能将受控限额终止解释为语言语义失败，也不能记为完成编译。

本追加验证扩大了步数、期限和内存范围，尚未得到这两个工作区的完整浏览器语言服务成绩。没有继续运行预备的更高步数／更长期限条件，也未追加直接 `prepare` 路径的同输入对照；已验证的宿主编译和浏览器执行路径仍成立。

在 10 亿步、120 秒、512 MiB／200 万对象下，另于精简工作区打开约 200 ms 时发起取消，约 2.20 秒从请求开始返回 `AbortError`，主线程推进 220 次定时回调。随后同一语言服务对象用约 4.81 秒完成小型工作区打开、分析、编译和执行，返回预期文本；结束时 scope、task 和 FFI 计数均为零。该结果不证明取消即时完成，也不证明底层 Worker 或原工作区现场得以保留。

追加证据独立保存五文件预算适配、内存参数补充、未改动的编译器镜像、两份输入、SDK 构建、六项限额结果、上游五组 Go 工作负载及取消／恢复记录。原报告 020 的 138 项材料校验未变化；追加 229 项材料清单 SHA-256 为 `74aaab58214707c15811374230232a2de887017d2b775b684d119f4126ed8a06`。首次准备缺少派生资产目录，创建后复制原发布镜像并构建；该准备修正未运行编译负载，也未改变输入。
