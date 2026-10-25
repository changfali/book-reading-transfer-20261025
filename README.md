# 书库跨机器阅读

本仓库为私有仓库，包含158本书的可用OCR、原生整理文本、规则和已有阅读成果。`reading-text.zip`约65 MiB。

## Linux使用

使用有权访问本私有仓库的GitHub账号或凭据：

```bash
git clone https://github.com/changfali/book-reading-transfer-20261025.git
cd book-reading-transfer-20261025
python3 -m zipfile -e reading-text.zip reading
```

将 `reading/开始阅读.txt` 的内容复制给服务器上的阅读对话，并告诉它本包的解压根目录是当前仓库下的 `reading/`。依照 `reading/manifest.json` 及每本书的 `task.json` 续读，已保存成果不重读。

这份轻量版不含原书PDF和图像，图表依赖必须保留待核，不能猜测或声称已完成图文核验。8本已有受保护旧L2，优先复用；BOOK-0390未有可用OCR／整理文本，保留输入问题并继续其他可读书。完整原书包仍保留在原电脑。

本包沿用已有外部机器任务认领，不重新分配书籍；本机正常读者会跳过这些认领。仓库不含API密钥、模型权重、虚拟环境或整库数据库。

新成果保存在 `reading/outputs/`，断点保存在 `reading/checkpoints/`。返回这些目录及 `reading/manifest.json`，由原项目合并；不要覆盖原电脑的任务数据库。
