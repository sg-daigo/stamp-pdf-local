# stamp-pdf-local

ローカルの PDF ファイルに印影画像（はんこ）を合成するスクリプトです。

## 概要

`main.py` を実行すると、指定した PDF の任意のページへ PNG 画像の印影を合成し、新しい PDF として出力します。

## 必要環境

- Python 3.13 以上
- [uv](https://github.com/astral-sh/uv)（パッケージ管理）

## セットアップ

```bash
uv sync
```

## 使い方

`main.py` の実行エリアにあるパラメータを編集してから実行します。

```python
INPUT_FILE  = "original.pdf"  # 元のPDFパス
OUTPUT_FILE = "stamped.pdf"   # 出力先PDFパス
STAMP_IMAGE = "hanko.png"     # 印影画像のパス（背景透過PNGを推奨）

X_POS       = 500   # 左端からの距離（ポイント）
Y_POS       = 680   # 下端からの距離（ポイント）
WIDTH       = 50    # 印影の幅（ポイント）
HEIGHT      = 50    # 印影の高さ（ポイント）
TARGET_PAGE = 0     # スタンプを押すページ（0始まり）
```

```bash
uv run main.py
```

## 座標系について

ReportLab の座標系は **左下が原点 (0, 0)** です。A4 サイズのページは横 595 × 縦 842 ポイントです（1 インチ = 72 ポイント）。

## 依存ライブラリ

| ライブラリ | 用途 |
|---|---|
| [pypdf](https://pypdf.readthedocs.io/) | PDF の読み込み・書き込み・ページ合成 |
| [reportlab](https://www.reportlab.com/) | 印影を配置した一時 PDF ページの生成 |
