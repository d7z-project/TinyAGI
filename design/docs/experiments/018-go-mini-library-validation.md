# 报告 018 · go-mini 库回归与跨语言接入

实验日期：2026-09-28（Asia/Shanghai）。证据：固定提交的上游库测试、真实编译及本机跨进程 RPC；无模型调用。

[库接入参考](../go-mini-integration.md#current-verification) · [工程映射](../engineering-reference.md#capability-toolchain) · [证据索引](../whole-system-evidence.md#report-018)

目录：[问题与条件](#conditions) · [结果](#results) · [关键契约](#contracts) · [复核命令](#commands) · [适用边界](#limits)

<a id="conditions"></a>

## 问题与固定条件

检查当前执行库是否继续支持 TinyAGI 所依赖的有限入口、独立实例、执行取消、热更新、编译缓存与多语言 RPC，并补充此前主要依据源码阅读的 Node 接入证据。以原有 Go、Rust 和 TypeScript 测试断言判断结果，不重新定义通过标准。

测试使用 [mini-go 提交 `fbb16ee99748e84b523bbd677bd477258c358956`](https://github.com/d7z-team/mini-go/tree/fbb16ee99748e84b523bbd677bd477258c358956) 的 `git archive` 导出。运行时本地已提交状态与上游 main 指向同一提交；导出目录独立构建，未修改上游工作区。各测试沿用该快照的源码、锁文件、接口和断言。

| 条件 | 实际取值与说明 |
| --- | --- |
| 系统 | Linux 6.18.52-1-lts，x86_64；不覆盖其他操作系统或架构 |
| Go | 上游 Makefile 指定的 Go 1.26.6；`GOTOOLCHAIN=local`、`GOWORK=off`，独立构建缓存 |
| Rust | rustc 1.98.1、Cargo 1.98.1，Arch Linux 工具链；使用 `Cargo.lock` 与 `--locked`，构建并发为 4 |
| Node／npm | Node v22.23.2、npm 12.0.2；`npm ci --ignore-scripts` 后显式执行 SDK 构建及类型检查 |
| WASM | wasm-bindgen 0.2.128，与锁文件匹配；没有预装目标标准库，使用上游 `MINIGO_BUILD_STD=1` 路径从源码构建 |
| Go 测试结果 | 全部使用 `-count=1`，不复用旧测试成绩；常规包并发为 4，race 包并发为 2 |
| Mini-Go 编译缓存 | 保留日常编译缓存；缓存契约用例使用上游定义的独立后端。构建缓存复用不计作新的性能测量 |
| RPC 环境 | 本机独立 Go／Rust peer 与 Node Worker，按用例建立回环连接；服务和输入均为上游测试夹具 |
| 源码与包身份 | Rust workspace 与 npm 源码包声明 `0.0.0-dev`；从源码构建，不代表下载或认证了公开发布包 |

源码归档 SHA-256：`62f6689e20ad7e3589a7fd90d7b0daef7c590a44153022c138c3502ba5e998f2`。初始预登记 SHA-256：`78ca6ce67893d2309b1dbd273bebf56e2974c2b74b99906550ba998be6b17213`。依据编译会话变更，在运行相关用例前补充检查范围，补充预登记 SHA-256：`ef4f985b99559c20971229c5b9bab6c7711e5696ed31cfafdcedd4202f53a0c1`。

<a id="results"></a>

## 运行结果

| 检查 | 实际范围 | 结果 |
| --- | --- | --- |
| Go 常规回归 | `ffi`、`runtime`、`rpc/...`、`compiler/cache`、`compiler/workspace`、`compiler/service`、`tooling/mrpc/...`、`integrations` | 14 个有测试包通过；另 1 个包没有测试文件。611 个顶层 Test、30 个 Fuzz 的种子入口通过；484 个子项通过，3 个顶层 Test 跳过 |
| Go race | `ffi`、`runtime`、`rpc/...`、`compiler/cache` | 6 个包通过，未报告数据竞争；523 个顶层 Test、28 个 Fuzz 的种子入口及 322 个子项通过，1 个 Test 跳过 |
| Rust RPC 与取消 | `rpc_*`、`cancellation`；启用 `rpc-gateway` 后另跑 Gateway | 54 项通过，0 失败、0 忽略；未启用 Gateway feature 时的同名二进制没有可运行用例，不计为通过项 |
| Rust 编译器与会话 | release 模式、`compiler,dap` feature，`compiler_entry` 与 `compiler_session` | 3 项通过，覆盖编译器入口、只保留已确认输入及语言分析复用 |
| Go／Rust 跨进程互通 | Endpoint 与 Gateway 两组，各覆盖 Go／Rust 服务端和客户端的 4 种组合 | 2 个顶层测试及 8 个组合通过，无跳过 |
| WASM 测试夹具 | `wasm_driver` 的异步初始化、清理、取消及镜像校验 | 2 项通过，生成 Node 使用的测试镜像 |
| Node 运行与 RPC | `node.test.js` | 8 项通过，无失败或跳过；包含 Worker 生命周期、队列取消、补丁及两种与 Go 双向互通方式 |
| Node 编译与语言工具 | Node 编译器镜像、语言服务、接纳期限、交付数据所有权及 Worker 丢失／候选失败恢复 | 主命令 4 项、补充恢复命令 1 项通过；浏览器对应项未选择，不计为已测 |
| SDK 类型与分发构建 | Rust WASM、TypeScript／Worker、编译器镜像及三组 TypeScript 类型检查 | 构建和类型检查均通过 |

Go 的子项包括子测试和已提供的 fuzz 种子执行，不能与顶层数量相加后解释为同样数量的独立功能，也没有运行持续随机 fuzz。常规与 race 中重复覆盖的场景分别记录，不算两份独立语义证据。

上述正式构建、类型检查与测试命令均退出 0，未修改上游断言，也未重试失败用例。运行后的归档比对未发现已跟踪源码内容改变。

### 跳过项与环境处理

- `TestAppendInitializesSpareSliceCapacityWithTypedZeros` 在常规与 race 中均因本次 append 未产生额外容量而按上游条件跳过；没有验证其备用容量分支。
- 常规 `integrations` 未提供 peer 可执行文件参数，因此跳过 `TestRPCPeerConformance` 和 `TestRPCGatewayConformance`。另在独立命令中显式绑定同快照构建的 peer，两项及全部 8 个组合通过。
- Node 语言工具按名称选择 Node 用例；浏览器、完整 npm 安装包检验和公开发布链不在所选范围。
- 前置探测遇到本机 SSH 配置不可用，改用 HTTPS 读取上游提交；工具版本探测曾因自动选择工具链尝试写入只读缓存，正式运行显式固定 Go 1.26.6 及独立工作区。正式测试未通过修改上游断言规避问题。

<a id="contracts"></a>

## 对接入设计有直接意义的结果

| 已运行的代表用例 | 支持的结论及边界 |
| --- | --- |
| `TestCancelReleasesRetainedRevisionAndKeepsInstanceOpen`、`TestInterruptHandleOnlyCancelsItsExecution` | 执行取消与实例关闭分开，旧执行的中断句柄不应取消新执行。业务任务与 Self 的生命周期分离仍由 TinyAGI 宿主负责 |
| `TestPatchKeepsActiveFrameAndDispatchesNamedCallsToCurrentRevision`、`TestRPCPendingCallAndResourceSurviveInstancePatch` | 旧帧保持所属 revision，新命名调用进入新代码；挂起 RPC 与资源不随脚本补丁自动重建。管理提交仍需实际绑定及执行边界协调 |
| `TestGuestProfileIsBoundedAndRevisionTagged` | 有界采样带代码版本与位置，可用于诊断。不是完整重放、进程内存或端到端成本统计 |
| `TestCompileCacheHitsRepeatedBuild`、依赖变更／优化／标签用例、`TestCompileCacheVerifyDetectsWrongHit`、`TestCompileContinuesWhenCacheBackendFails` | 可复用库自带编译缓存及失效检查；不需要另建平行编译缓存协议。没有测完整主体的净节约比例 |
| Go／Rust peer 与 Gateway 矩阵 | 实际覆盖对称调用、递归调用、资源使用、取消，以及发布／解析／保留旧绑定／撤销。不是任意网络条件或外部业务效果保证 |
| `Node generated TypeScript RPC interoperates with Go in both directions` | 生成 TypeScript 绑定与独立 Node RPC SDK 可实际调用、发布并处理资源，不要求加载认知 Program；SDK 仍依赖配套 Worker／WASM |
| Node 编译器与语言服务用例 | 可通过分发的编译器镜像处理源码、查询和增量分析，支持非 Go 工具端复用语言规则；不等于人物初始化、自迁移或管理蓝图已经实现 |

当前证据支持继续采用嵌入式执行库、有限入口、业务任务独立管理、现有编译缓存及 MRPC 多语言接入。无需因此改变单宿主架构、增加独立编译服务或将全部内部函数改为 RPC。

<a id="commands"></a>

## 主要复核命令

在上述固定快照及工具链下，Go 与 Rust 主要入口为：

```sh
make test \
  TEST_PACKAGES='./ffi ./runtime ./rpc/... ./compiler/cache ./compiler/workspace ./compiler/service ./tooling/mrpc/... ./integrations' \
  TEST_FLAGS='-count=1 -json -timeout=10m -p=4'

go test -race -count=1 -json -timeout=10m -p=2 \
  ./ffi ./runtime ./rpc/... ./compiler/cache

make runtime-rust-rpc-test

cargo test --locked --manifest-path playground/runtime-rust/Cargo.toml \
  --release -p mini-go --features compiler,dap \
  --test compiler_entry --test compiler_session
```

跨进程矩阵按上游 `make test-rpc-conformance` 的构建顺序准备 Go／Rust peer，再设置 `MINIGO_RPC_GO_PEER` 与 `MINIGO_RPC_RUST_PEER`，执行：

```sh
go test ./integrations -run '^TestRPC(Peer|Gateway)Conformance$' \
  -count=1 -json -timeout=3m
```

Node 路径先按锁文件准备 npm 开发依赖，显式构建 SDK 并执行 `npm run typecheck`；设置 `MINIGO_WASM_FIXTURES`，运行 Rust `wasm_driver` 生成镜像，再提供 `MINIGO_RPC_GO_PEER` 运行 `node --test --test-concurrency=1 tests/node.test.js`。编译与语言工具另选 `compiler.test.js`、`tools.test.js` 的 Node 项及 `tools_fault.test.js`。未直接运行包含全部浏览器和安装包场景的 `make runtime-wasm-test`。

具体生成和依赖要求以固定提交的 [Makefile](https://github.com/d7z-team/mini-go/blob/fbb16ee99748e84b523bbd677bd477258c358956/Makefile) 为准；后续提交若更改入口或产物布局，应先更新检查计划，不能机械沿用这些命令。

<a id="limits"></a>

## 适用边界与数据范围

这些结果来自上游已有测试与合成夹具，没有 TinyAGI 产品程序、真实模型、实际联系人或生产任务；也没有运行完整上游 CI、持续 fuzz、跨平台矩阵、容器隔离、真实机密服务或公网压力测试。对 RPC 身份和拦截器的源码核对不等于端到端防泄漏证明。

构建与测试日志中的耗时受缓存、并发准备和本机环境影响，不作为稳定延迟、吞吐或费用比较。当前复用机制有功能依据，实际性能和完整主体行为仍须在对应用途下单独评价。

公开报告提供固定来源、条件、命令、统计、跳过及结论边界。源码归档、预登记、锁文件摘要、完整日志和逐命令结果保留为研究证据，未随报告发布。原报告 002／014 的源码身份与成绩保持不变，新库结果不回填到历史实验。
