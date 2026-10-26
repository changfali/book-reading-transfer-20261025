# 书库跨机器阅读

## 新增：全部未整本读完的书（2026-10-26）

[501本文字迁移包与使用说明](remaining-text-20261026/README.md)：仅排除192本有明确整本已读记录的书，其余全部纳入，包括部分L2、已分配、正在读和旧外发包中的书。

- 下载合计 **356.35 MiB（373.66 MB）**，9卷，每卷不超过40 MiB。
- 解压后约 **1.62 GiB**；首次使用建议预留 **4 GB**，包括Git文件、合并压缩包和解压内容。
- 不含原书PDF和图片。OCR/原生文字、已有候选、成果与来源/断点随包保存；BOOK-0390缺可用文字，已明确登记。
- 不改变原电脑认领或阅读进程。另一台机器独立保存成果，返回时按原文区间去重合并。

```bash
git clone https://github.com/changfali/book-reading-transfer-20261025.git
cd book-reading-transfer-20261025
python3 remaining-text-20261026/unpack.py
```

已拉取过仓库的机器先执行 `git pull`，再运行上述解包脚本。脚本自动核对SHA-256并解压，不覆盖已有的 `reading/` 目录。
将 `remaining-text-20261026/reading/开始阅读.txt` 发给阅读对话，说明实际解压根目录。不要再同时解压旧包重复读同一批书。

## 保留的旧包：原未分配158本

本仓库为公开仓库，包含158本书的可用OCR、原生整理文本、规则和已有阅读成果。`reading-text.zip`约65 MiB。

## Linux使用

无需登录GitHub即可拉取：

```bash
git clone https://github.com/changfali/book-reading-transfer-20261025.git
cd book-reading-transfer-20261025
python3 -m zipfile -e reading-text.zip reading
```

将 `reading/开始阅读.txt` 的内容复制给服务器上的阅读对话，并告诉它本包的解压根目录是当前仓库下的 `reading/`。依照 `reading/manifest.json` 及每本书的 `task.json` 续读，已保存成果不重读。

这份轻量版不含原书PDF和图像，图表依赖必须保留待核，不能猜测或声称已完成图文核验。8本已有受保护旧L2，优先复用；BOOK-0390未有可用OCR／整理文本，保留输入问题并继续其他可读书。完整原书包仍保留在原电脑。

本包沿用已有外部机器任务认领，不重新分配书籍；本机正常读者会跳过这些认领。仓库不含API密钥、模型权重、虚拟环境或整库数据库。

新成果保存在 `reading/outputs/`，断点保存在 `reading/checkpoints/`。返回这些目录及 `reading/manifest.json`，由原项目合并；不要覆盖原电脑的任务数据库。
