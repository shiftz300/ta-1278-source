# TA-1278 source archive

本地研究资料与恢复备份。应用仓库位于相邻的 `ta-1278/`，其构建不依赖此目录。本仓库保存研究资料；私人采集、验证输出、恢复备份与临时文件仍仅在本地保留。

| 目录 | 内容 |
|---|---|
| `research/` | 迁出的固件结构报告、资源解析、反汇编、实机对照图及研究工具 |
| `private/acquisition/` | 早期采集工作区，包含物理 NAND、NV、私人数据及工具；仅本地保存 |
| `private/sessions/` | 原始实机诊断会话和截图，可能含私人数据 |
| `validation/replica/` | 桌面复刻的历次截图、比对与验证结果 |
| `validation/runtime/` | 运行时测试材料 |
| `backups/` | 分离前完整源码快照、未提交修改及 Git 历史 bundle |
| `temporary/` | 原有临时实验与可重建输出，暂未删除 |
| `manifests/` | 早期清单与本次整理的路径映射、SHA-256 |

## 从哪里看

- [研究入口](research/nokia-ta1278-research/README.md)
- [设备报告](research/nokia-ta1278-research/device-report.md)
- [结论与边界](research/nokia-ta1278-research/findings.md)
- [研究工具及迁移说明](research/README.md)
- [分离前恢复快照](backups/separation-20261027-130617/README.md)

研究内部相对路径保持原样，避免破坏证据链。旧报告中的绝对路径代表当时环境，可通过 `manifests/organization.json` 查找现在的位置；未修改原始记录以伪装成新采集。原有清单同样保留原值。

## 发布边界

`.gitignore` 默认排除私人数据、恢复备份、临时文件和验证目录。研究目录也不是自动批准的公开清单；提交时沿用原研究项目的发布边界及权利说明，按需挑选文件。不要将整个目录连同 Git 历史备份一起公开。

## 校验

`research/migration.json` 记录从应用迁出的每个文件；`manifests/organization.json` 记录本次目录整理前后位置与校验值。迁移先验证副本再移出原路径；本次目录重排逐文件校验通过，没有删除原有成果。

## 本次应用分离验证

[校验报告](validation/separation-20261027/report.json)：默认测试 202 项、无窗口测试 139 项通过；45 张 CPU 页面图除主屏时钟外一致；Clippy、资源校验及签名打包通过。该验证不等于新增实机或原生窗口验收。运行资源与 T9 保留在应用中，不依赖此归档。
