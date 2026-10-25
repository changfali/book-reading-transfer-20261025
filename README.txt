Git书库文本迁移

本目录可推送到私有Git仓库。reading-text.zip包含158本书的可用OCR、原生整理文本、已有成果和规则；不包含原书PDF与图像，不包含模型和密钥。原书完整版保持原样，未删除。

公司Linux服务器能访问所选Git平台时：
git clone <你的私有仓库HTTPS地址> book-reading
cd book-reading
python3 -m zipfile -e reading-text.zip reading

把 reading/开始阅读.txt 发给服务器上的AI，并告诉它解压根目录是当前仓库下的 reading/。按相对路径读任务，成果与断点持续保存；图表疑点保留待核。

本包仍使用原external-export认领，不重复分配任何书籍。未配置远程仓库、未上传任何文件。
