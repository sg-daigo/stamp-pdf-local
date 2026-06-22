import io
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import A4

# 1. 印影イメージを持つ一時的なPDF（ページ）を作成
def create_stamp_page(image_path, x, y, width, height) -> PdfReader:
    # ローカルの画像ファイルを読み込み
    with open(image_path, 'rb') as f:
        stamp_img = ImageReader(f)

        bio = io.BytesIO()
        c = canvas.Canvas(bio, pagesize=A4)

        # 印影を配置 (ReportLabの座標系は左下が原点(0,0)です)
        c.drawImage(stamp_img, x, y, width=width, height=height, mask='auto')
        c.save()

        bio.seek(0)
        return PdfReader(bio)

# 2. メインのPDFスタンプ付与処理
def stamp_pdf_local(input_pdf_path, output_pdf_path, image_path, x, y, width, height, target_page=0):
    # 入力PDFの読み込み
    input_pdf = PdfReader(input_pdf_path)
    writer = PdfWriter()
    
    # 指定されたページを取得
    original_page = input_pdf.pages[target_page]

    # 印影PDFを作成してマージ
    stamp_pdf = create_stamp_page(image_path, x, y, width, height)
    stamp_page = stamp_pdf.pages[0]
    original_page.merge_page(stamp_page)

    # 全ページを出力用ライターに追加
    for i, page in enumerate(input_pdf.pages):
        writer.add_page(original_page if i == target_page else page)

    # ローカルに保存
    with open(output_pdf_path, 'wb') as f:
        writer.write(f)
    print(f"Success: {output_pdf_path} を作成しました。")


# --- 実行エリア（ここを書き換えて実行してください） ---
if __name__ == "__main__":
    # 設定パラメータ
    INPUT_FILE = "original.pdf"    # 元のPDFパス
    OUTPUT_FILE = "stamped.pdf"   # 出力先PDFパス
    STAMP_IMAGE = "hanko.png"     # 印影画像のパス（背景透過のPNGを推奨）
    
    # 配置座標とサイズ（単位: ポイント / 1インチ＝72ポイント）
    # ※A4サイズは横595×縦842ポイントです
    X_POS = 500      # 左端からの距離
    Y_POS = 680      # 下端からの距離
    WIDTH = 50       # 印影の幅
    HEIGHT = 50      # 印影の高さ
    TARGET_PAGE = 0  # スタンプを押すページ（0始まり。最初のページは0）

    # 実行
    stamp_pdf_local(
        input_pdf_path=INPUT_FILE,
        output_pdf_path=OUTPUT_FILE,
        image_path=STAMP_IMAGE,
        x=X_POS,
        y=Y_POS,
        width=WIDTH,
        height=HEIGHT,
        target_page=TARGET_PAGE
    )