# Summary

- [TinyAGI](README.md)
- [文档索引](docs/README.md)

# 总体设计

- [TinyAGI 逻辑总设计](DESIGN.md)

# 逻辑专题

- [主体运行、认知协作与学习](docs/whole-system-design.md)
- [交流、人物与情境](docs/interaction-design.md)
- [资源契约、输入与计算](docs/projection-input-and-compute.md)
- [逻辑模块、能力契约与运行协议](docs/runtime-protocol.md)
- [沙箱、能力评估、回归测试与复盘](docs/sandbox-evaluation.md)
- [管理工作台与人工干预](docs/management-workspace.md)

# 工程参考

- [工程选型与部署参考](docs/engineering-reference.md)
- [go-mini 库行为与接入参考](docs/go-mini-integration.md)

# 决策、证据与维护

- [设计决策与适用边界](docs/research-plan.md)
- [设计依据与实验索引](docs/whole-system-evidence.md)
- [文档维护与证据规范](docs/documentation-guide.md)
- [文档构建、公开范围与 GitHub Pages](docs/documentation-publishing.md)

# 历史实验报告

- [报告 001 · 动作恢复的受限状态枚举](docs/experiments/001-effect-recovery.md)
- [报告 002 · 实际 go-mini 的运行边界实验](docs/experiments/002-vm-continuity.md)
- [报告 003 · 依赖校验与慢速结果复核](docs/experiments/003-result-revalidation.md)
- [报告 004 · 控制通路、取消与资源占用](docs/experiments/004-realtime-control.md)
- [报告 005 · 分布式接管、执行端重启与旧结果](docs/experiments/005-distributed-handoff.md)
- [报告 006 · 真实进程与持久化边界](docs/experiments/006-process-recovery.md)
- [报告 007 · 提供者核对、取消与回收](docs/experiments/007-provider-reconciliation.md)
- [报告 008 · 接纳、启动与核对入账](docs/experiments/008-dispatch-settlement.md)
- [报告 009 · 取消竞争、备份恢复与冲突证据](docs/experiments/009-cancel-restore-evidence.md)
- [报告 010 · SQLite、本地文件与维护边界](docs/experiments/010-local-storage.md)
- [报告 011 · 完整活动评价环境与客观评价](docs/experiments/011-whole-activity-evaluation.md)
- [报告 012 · 投影、资料修订与闹钟输入贯穿完整活动](docs/experiments/012-projection-alarm-activity.md)
- [报告 013 · 资源投影之后的资料发现与依据用途](docs/experiments/013-resource-discovery.md)
- [报告 014 · 单宿主整体组件组合](docs/experiments/014-host-composition.md)
- [报告 015 · 完整任务验收契约与真实模型开发对照](docs/experiments/015-task-outcome-contract.md)
- [报告 016 · 真实模型功能事件验证](docs/experiments/016-functional-events.md)
- [报告 017 · 任务接续、有限投入与责任退出](docs/experiments/017-continuation-study.md)
