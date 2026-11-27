# 第二版金融书籍 OCR 文字包

共1183本，压缩1379.89 MB，解压5.03 GB。
包含正式results的Markdown/JSON、manifest、原质量报告、完整书名索引和队列快照；不含原PDF、页面图片、隔离和历史候选。
有缺页或缺输入记录的书0本，详见包内index.json；识别结果不等于质量验收通过。

在本目录运行 `python3 unpack.py`，自动校验、合并、解压到reading/。
解压后查看 `reading/index.json` 查书名，正文在 `reading/V2/books/V2-BOOK-xxxxxx/results/page-xxxx.md`。
旧158本包、501本包均保留，本包不更改任何源机器任务状态。
