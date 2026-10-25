Git书库文本迁移

当前仓库已公开，无需登录GitHub即可拉取。reading-text.zip包含158本书的可用OCR、原生整理文本、已有成果和规则；不包含原书PDF与图像，不包含模型和密钥。原书完整版保持原样，未删除。

公司Linux服务器能访问所选Git平台时：
git clone https://github.com/changfali/book-reading-transfer-20261025.git book-reading
cd book-reading
python3 -m zipfile -e reading-text.zip reading

把 reading/开始阅读.txt 发给服务器上的AI，并告诉它解压根目录是当前仓库下的 reading/。按相对路径读任务，成果与断点持续保存；图表疑点保留待核。

本包仍使用原external-export认领，不重复分配任何书籍。仓库地址：https://github.com/changfali/book-reading-transfer-20261025
