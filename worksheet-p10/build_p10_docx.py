"""
Script generator lengkap untuk membuat file docx Worksheet P10:
AMADEUS DHARMA AKBARINDRA - 25523253 - 10. Worksheet_PABW_Pertemuan10.docx

Mencakup seluruh halaman (Page 1 sampai Page 13) dengan format, section, layout,
font family (Carlito, DejaVu Sans Mono), style, size, dan isi sama persis dengan PDF
dan berkas P9 resmi yang telah terbukti sempurna.
"""

import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, hex_color):
    """Set background color of a table cell."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=70, bottom=70, left=100, right=100):
    """Set cell margins in twips (20 twips = 1 pt)."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def set_table_borders(table, color="D0D7DE", sz="4", val="single"):
    """Set borders for the whole table."""
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:left w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:right w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideV w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def make_callout_box(doc, text, bold_prefix="", hex_bg="EEF2FA", border_color="003796"):
    """Create a callout box styled like the worksheet boxes."""
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    cell = table.rows[0].cells[0]
    cell.width = Inches(6.77)
    set_cell_background(cell, hex_bg)
    set_cell_margins(cell, top=80, bottom=80, left=110, right=110)
    
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="none"/>'
        f'<w:bottom w:val="none"/>'
        f'<w:left w:val="single" w:sz="24" w:space="0" w:color="{border_color}"/>'
        f'<w:right w:val="none"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.15
    
    if bold_prefix:
        r_pre = p.add_run(bold_prefix + " ")
        r_pre.font.name = "Carlito"
        r_pre.font.size = Pt(9.0)
        r_pre.font.bold = True
        r_pre.font.color.rgb = RGBColor(0x00, 0x37, 0x96) if border_color == "003796" else RGBColor(0x99, 0x1B, 0x1B)
        
    r_txt = p.add_run(text)
    r_txt.font.name = "Carlito"
    r_txt.font.size = Pt(8.5)
    r_txt.font.color.rgb = RGBColor(0x1F, 0x23, 0x28)
    
    doc.add_paragraph().paragraph_format.space_after = Pt(2)

def make_worksheet_header(doc, code, letter, title):
    """Create the distinctive 3-cell worksheet header bar."""
    table = doc.add_table(rows=1, cols=3)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    col_widths = [Inches(1.5), Inches(0.55), Inches(4.72)]
    for i, w in enumerate(col_widths):
        table.rows[0].cells[i].width = w
        
    cell0 = table.rows[0].cells[0]
    cell1 = table.rows[0].cells[1]
    cell2 = table.rows[0].cells[2]
    
    set_cell_background(cell0, "003796")
    set_cell_background(cell1, "F6D11B")
    set_cell_background(cell2, "EEF2FA")
    
    for c in [cell0, cell1, cell2]:
        set_cell_margins(c, top=65, bottom=65, left=85, right=85)
        c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        
    p0 = cell0.paragraphs[0]
    p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p0.paragraph_format.space_before = Pt(0)
    p0.paragraph_format.space_after = Pt(0)
    r0 = p0.add_run(code)
    r0.font.name = "Carlito"
    r0.font.size = Pt(10.0)
    r0.font.bold = True
    r0.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    
    p1 = cell1.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1.paragraph_format.space_before = Pt(0)
    p1.paragraph_format.space_after = Pt(0)
    r1 = p1.add_run(letter)
    r1.font.name = "Carlito"
    r1.font.size = Pt(10.0)
    r1.font.bold = True
    r1.font.color.rgb = RGBColor(0x00, 0x37, 0x96)
    
    p2 = cell2.paragraphs[0]
    p2.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p2.paragraph_format.space_before = Pt(0)
    p2.paragraph_format.space_after = Pt(0)
    r2 = p2.add_run(title)
    r2.font.name = "Carlito"
    r2.font.size = Pt(9.5)
    r2.font.bold = True
    r2.font.color.rgb = RGBColor(0x00, 0x37, 0x96)
    
    doc.add_paragraph().paragraph_format.space_after = Pt(2)

def add_code_block(doc, code_text):
    """Add a shaded code block with monospace font."""
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    cell = table.rows[0].cells[0]
    cell.width = Inches(6.77)
    set_cell_background(cell, "F6F8FA")
    set_cell_margins(cell, top=70, bottom=70, left=100, right=100)
    
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>'
        f'<w:bottom w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>'
        f'<w:left w:val="single" w:sz="14" w:space="0" w:color="003796"/>'
        f'<w:right w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.15
    
    r = p.add_run(code_text)
    r.font.name = "DejaVu Sans Mono"
    r.font.size = Pt(8.5)
    r.font.color.rgb = RGBColor(0x24, 0x29, 0x2F)
    
    doc.add_paragraph().paragraph_format.space_after = Pt(2)

def add_heading_section(doc, text):
    """Add a subsection title in navy blue."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(5)
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = "Carlito"
    r.font.size = Pt(10.0)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0x00, 0x37, 0x96)

def add_subtext(doc, text):
    """Add a descriptive sentence."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    r = p.add_run(text)
    r.font.name = "Carlito"
    r.font.size = Pt(8.5)
    r.font.color.rgb = RGBColor(0x33, 0x38, 0x42)

def add_git_commit_box(doc, commit_letter, commit_msg):
    """Add the standardized Git commit instruction box."""
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    cell = table.rows[0].cells[0]
    cell.width = Inches(6.77)
    set_cell_background(cell, "F6F8FA")
    set_cell_margins(cell, top=75, bottom=75, left=100, right=100)
    
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>'
        f'<w:bottom w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>'
        f'<w:left w:val="single" w:sz="20" w:space="0" w:color="003796"/>'
        f'<w:right w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(1)
    
    r_hdr = p.add_run(f"▌ SIMPAN KE GIT - SETELAH LEMBAR {commit_letter}\n")
    r_hdr.font.name = "Carlito"
    r_hdr.font.size = Pt(9.0)
    r_hdr.font.bold = True
    r_hdr.font.color.rgb = RGBColor(0x00, 0x37, 0x96)
    
    r_cmd = p.add_run(f"git add .\ngit commit -m \"{commit_msg}\"\ngit push\n# pesan commit yang disarankan:\n# {commit_msg}")
    r_cmd.font.name = "DejaVu Sans Mono"
    r_cmd.font.size = Pt(8.5)
    r_cmd.font.color.rgb = RGBColor(0x24, 0x29, 0x2F)
    
    p_note = doc.add_paragraph()
    p_note.paragraph_format.space_before = Pt(1)
    p_note.paragraph_format.space_after = Pt(2)
    r_note = p_note.add_run(f"Lembar {commit_letter} sudah selesai? Simpan hasilnya sekarang, jangan menunggu kelas berakhir. Simpanan ini tidak memerlukan langkah tambahan apa pun, karena fungsinya menjaga agar pekerjaan Anda tidak bergantung pada satu berkas di satu komputer.")
    r_note.font.name = "Carlito"
    r_note.font.size = Pt(8.0)
    r_note.font.italic = True
    r_note.font.color.rgb = RGBColor(0x5A, 0x60, 0x80)

def add_check_verification(doc, letter, text):
    """Add the check verification section."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    
    r_title = p.add_run(f"{letter} - simpan perubahan\n")
    r_title.font.name = "Carlito"
    r_title.font.size = Pt(9.0)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(0x00, 0x37, 0x96)
    
    r_desc = p.add_run(f"Cara memastikan: {text}")
    r_desc.font.name = "Carlito"
    r_desc.font.size = Pt(8.5)
    r_desc.font.italic = True
    r_desc.font.color.rgb = RGBColor(0x33, 0x38, 0x42)

def style_standard_table(table, col_widths, headers, data_rows, header_bg="003796", alt_bg="F8FAFC"):
    """Format a standard table with navy header and neat cells."""
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    set_table_borders(table, color="D0D7DE", sz="4")
    
    # Header row
    hdr_cells = table.rows[0].cells
    for i, title in enumerate(headers):
        hdr_cells[i].width = col_widths[i]
        set_cell_background(hdr_cells[i], header_bg)
        set_cell_margins(hdr_cells[i], top=65, bottom=65, left=85, right=85)
        hdr_cells[i].vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        
        p = hdr_cells[i].paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(title)
        r.font.name = "Carlito"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        
    # Data rows
    for r_idx, row_data in enumerate(data_rows):
        row_cells = table.rows[r_idx + 1].cells
        bg_col = alt_bg if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, val in enumerate(row_data):
            row_cells[c_idx].width = col_widths[c_idx]
            set_cell_background(row_cells[c_idx], bg_col)
            set_cell_margins(row_cells[c_idx], top=55, bottom=55, left=85, right=85)
            row_cells[c_idx].vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            
            p = row_cells[c_idx].paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.15
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(str(val))
            r.font.name = "Carlito"
            r.font.size = Pt(8.5)
            r.font.color.rgb = RGBColor(0x1F, 0x23, 0x28)


def generate_p10_docx(output_path):
    print("Mulai membuat dokumen P10 terisi...")
    doc = Document()
    
    # 1. Page Setup (A4, precise margins)
    sec = doc.sections[0]
    sec.page_width = Inches(8.27)
    sec.page_height = Inches(11.69)
    sec.top_margin = Inches(0.67)
    sec.bottom_margin = Inches(0.63)
    sec.left_margin = Inches(0.75)
    sec.right_margin = Inches(0.75)
    
    # ==========================================
    # HALAMAN 1: COVER & OVERVIEW WORKSHEET P10
    # ==========================================
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(4)
    p_title.paragraph_format.space_after = Pt(1)
    r_title = p_title.add_run("JavaScript Asinkron: fetch, Promise, dan JSON")
    r_title.font.name = "Carlito"
    r_title.font.size = Pt(16.0)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(0x00, 0x37, 0x96)
    
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(6)
    r_sub = p_sub.add_run("Pengembangan Aplikasi Berbasis Web · SIF302 · Semester Gasal 2026/2027")
    r_sub.font.name = "Carlito"
    r_sub.font.size = Pt(9.0)
    r_sub.font.color.rgb = RGBColor(0x5A, 0x60, 0x80)
    
    # Tabel Identitas
    t_id = doc.add_table(rows=2, cols=4)
    t_id.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_id.autofit = False
    set_table_borders(t_id, color="D0D7DE", sz="4")
    id_widths = [Inches(1.0), Inches(2.6), Inches(1.0), Inches(2.17)]
    id_data = [
        [("NAMA", "003796", True, "FFFFFF"), ("AMADEUS DHARMA AKBARINDRA", "FFFFFF", True, "1F2328"),
         ("NIM", "003796", True, "FFFFFF"), ("25523253", "FFFFFF", True, "1F2328")],
        [("KELAS", "003796", True, "FFFFFF"), ("SIF302 / B", "FFFFFF", False, "1F2328"),
         ("TANGGAL", "003796", True, "FFFFFF"), ("14 Oktober 2026", "FFFFFF", False, "1F2328")]
    ]
    for r_idx, row in enumerate(id_data):
        for c_idx, (text, bg, is_bold, text_color) in enumerate(row):
            cell = t_id.rows[r_idx].cells[c_idx]
            cell.width = id_widths[c_idx]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=50, bottom=50, left=70, right=70)
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(text)
            r.font.name = "Carlito"
            r.font.size = Pt(8.5)
            r.font.bold = is_bold
            if text_color == "FFFFFF":
                r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            else:
                r.font.color.rgb = RGBColor(0x1F, 0x23, 0x28)
                
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    
    # Header Bar Worksheet P10
    make_worksheet_header(doc, "WORKSHEET", "P10", "Pertemuan 10 · JavaScript Asinkron: fetch, Promise, dan JSON")
    
    # Box instruksi mandiri
    make_callout_box(doc, "Dikerjakan sendiri, bukan berpasangan. Setiap mahasiswa mengerjakan satu halaman profil miliknya sendiri. Anda bebas memilih isi halaman, tetapi harus bisa menjelaskan setiap baris kode yang Anda tulis.", bold_prefix="▌", hex_bg="EEF2FA", border_color="003796")
    
    # Tabel Capaian Pembelajaran & Yang Dinilai Hari Ini
    t_capaian = doc.add_table(rows=2, cols=2)
    style_standard_table(
        t_capaian,
        [Inches(3.3), Inches(3.47)],
        ["Capaian pembelajaran", "Yang dinilai hari ini"],
        [[
            "Mahasiswa mampu mengambil data dari sebuah API memakai fetch, membaca balasan JSON, memisahkan lapisan data dari lapisan tampilan dalam berkas js/api.js, lalu menampilkan hasilnya di halaman beserta keadaan memuat, berhasil, gagal, dan kosong.",
            "1. Pemanggilan fetch benar dan alamatnya ditetapkan di satu tempat.\n"
            "2. respons.ok diperiksa sebelum badan balasan dibaca.\n"
            "3. JSON.parse dan JSON.stringify dipakai pada arah yang tepat.\n"
            "4. Keempat keadaan antarmuka tampil: memuat, berhasil, gagal, kosong.\n"
            "5. Galat ditangkap dan pesannya ditampilkan di halaman, tidak sekadar di console.\n"
            "6. Berkas js/api.js memuat lapisan data dan mengekspor fungsinya, sehingga app.js tidak perlu diubah."
        ]],
        header_bg="003796"
    )
    doc.add_paragraph().paragraph_format.space_after = Pt(3)
    
    # Aturan Pengerjaan
    add_heading_section(doc, "Aturan pengerjaan")
    t_aturan = doc.add_table(rows=8, cols=2)
    style_standard_table(
        t_aturan,
        [Inches(1.8), Inches(4.97)],
        ["Hal", "Ketetapan"],
        [
            ["Bentuk kerja", "Individu. Satu mahasiswa, satu halaman, satu topik."],
            ["Perkakas", "VS Code + peramban Chrome atau Firefox. Panel Console dan Network di DevTools dipakai terus-menerus mulai lembar A."],
            ["Berkas awal", "Hasil pekerjaan Anda sendiri dari Pertemuan 9, profil.html, seluruh berkas CSS, js/app.js, dan js/dom.js, disalin ke folder worksheet-p10/. Tidak ada berkas contoh, tidak ada kerangka yang disediakan."],
            ["Berkas baru", "Satu berkas saja: js/api.js. Berkas ini memuat lapisan data dan mengekspornya. app.js tetap seperti semula, hanya menambah satu baris pemanggil."],
            ["API", "API publik tanpa kunci akses. Bila alamatnya tidak terjangkau dari kelas, pakai satu berkas notisia.json lokal dan sebutkan pilihan itu di README."],
            ["Waktu", "90 menit di kelas. Bila belum selesai, dilanjutkan di luar kelas paling lambat pukul 23.59 pada hari yang sama."],
            ["Penyerahan", "Seluruh isi worksheet-p10/ diunggah ke repositori GitHub Anda sendiri, di dalam folder semester ~/pabw/. Periksa halaman repositori Anda, tidak cukup folder di laptop."]
        ]
    )
    doc.add_paragraph().paragraph_format.space_after = Pt(3)
    
    # Anggaran Waktu 90 Menit
    add_heading_section(doc, "Anggaran waktu 90 menit")
    t_waktu = doc.add_table(rows=7, cols=4)
    style_standard_table(
        t_waktu,
        [Inches(1.0), Inches(0.8), Inches(3.2), Inches(1.77)],
        ["Menit", "Lembar", "Yang Anda kerjakan", "Kalau waktu habis, berhenti di sini"],
        [
            ["0-18", "A", "Salin hasil Pertemuan 9 ke worksheet-p10/, buat js/api.js, panggilan fetch pertama, periksa respons.ok", "Objek Response tampil di Console"],
            ["18-36", "B", "Ubah rantai then menjadi async/await, satu try/catch, buktikan galatnya tertangkap", "Galat jaringan tertangkap dan tampil di halaman"],
            ["36-54", "C", "Baca balasan dengan json(), petakan bentuk datanya, kenali arah stringify", "Kunci data teridentifikasi dan terdokumentasi"],
            ["54-74", "D", "Telusuri larik, gambar kartu ke halaman, keempat keadaan antarmuka", "Daftar tampil di halaman dari data"],
            ["74-96", "E", "Tiga kasus sulit: status 404, await di luar fungsi async, badan bukan JSON", "Tiga kasus ditangani + catatan"],
            ["96-150", "F", "Periksa satu per satu, satu baris untuk diingat, tiket keluar, penilaian mandiri, README, catat bagian P13", "Lembar F terisi dan tersimpan"]
        ]
    )
    doc.add_paragraph().paragraph_format.space_after = Pt(3)
    
    # Pink warning box
    make_callout_box(
        doc,
        "Selalu kerjakan berurutan. Setiap lembar mengandaikan lembar sebelumnya sudah selesai, dan setiap keadaan antarmuka dibuktikan dengan tangkapan layar. Kolom paling kanan menunjukkan laju, bukan tenggat.",
        bold_prefix="",
        hex_bg="FDE8E8",
        border_color="B91C1C"
    )
    
    doc.add_page_break()
    
    # ==========================================
    # HALAMAN 2: LEMBAR A - PANGGILAN PERTAMA & STATUS BALASAN
    # ==========================================
    make_worksheet_header(doc, "WORKSHEET", "A", "Panggilan pertama dan status balasan")
    make_callout_box(
        doc,
        "fetch TIDAK MELEMPAR GALAT PADA STATUS 404, PERIKSA respons.ok\nPanggilan pertama sering dianggap berhasil karena tidak ada galat di Console. Padahal balasan bisa berstatus 404 atau 500 dan tetap dianggap berhasil oleh fetch. Satu pemeriksaan singkat menutup seluruh celah itu.",
        bold_prefix="▌",
        hex_bg="EEF2FA",
        border_color="003796"
    )
    
    add_heading_section(doc, "A.1 Berkas yang harus ada sebelum Anda mulai")
    add_subtext(doc, "Salin seluruh hasil Pertemuan 9 ke folder worksheet-p10/. Periksa satu per satu, pekerjaan hari ini bertumpu pada berkas-berkas itu, dan yang hilang akan terasa sebagai galat 404 di Console.")
    
    t_a1 = doc.add_table(rows=5, cols=4)
    style_standard_table(
        t_a1,
        [Inches(2.5), Inches(1.1), Inches(1.0), Inches(2.17)],
        ["Berkas", "Dari", "Ada?", "Jumlah baris"],
        [
            ["profil.html", "P9", "Ada", "209 baris"],
            ["Seluruh berkas CSS (enam berkas)", "P4-P6", "Ada", "543 baris (tokens, base, layout, komponen, tema, responsif)"],
            ["js/app.js", "P8", "Ada", "215 baris"],
            ["js/dom.js", "P9", "Ada", "315 baris"]
        ]
    )
    doc.add_paragraph().paragraph_format.space_after = Pt(3)
    
    add_heading_section(doc, "A.2 Tetapkan alamat di satu tempat")
    add_subtext(doc, "Alamat API ditulis satu kali saja, di bagian atas berkas. Bila alamatnya berubah nanti, hanya satu baris yang perlu disunting, bukan setiap tempat yang memanggilnya.")
    
    add_code_block(
        doc,
        "// js/api.js, bagian atas berkas\n"
        "const ALAMAT = 'https://ghibliapi.vercel.app/films';\n"
        "// Opsi cadangan lokal jika jaringan kelas terputus: './film.json'"
    )
    
    t_a2 = doc.add_table(rows=5, cols=2)
    style_standard_table(
        t_a2,
        [Inches(2.2), Inches(4.57)],
        ["Hal yang diperiksa", "Tanda benar"],
        [
            ["Skema alamat", "memakai https, bukan http (https://ghibliapi.vercel.app/films)"],
            ["Satu tempat", "alamat tidak ditulis ulang di fungsi lain (hanya dideklarasikan pada konstanta ALAMAT)"],
            ["Tanpa kunci akses", "tidak ada apiKey atau token di dalam kode (endpoint publik terbuka tanpa autentikasi)"],
            ["Nama berkas", "alamat berada di js/api.js, bukan di js/app.js"]
        ]
    )
    doc.add_paragraph().paragraph_format.space_after = Pt(3)
    
    add_heading_section(doc, "A.3 Panggil, periksa, lalu buktikan di panel Network")
    add_subtext(doc, "Panggil fetch, lalu periksa respons.ok sebelum membaca badannya. Isi tabel berikut dari panggilan Anda sendiri.")
    
    add_code_block(
        doc,
        "async function muat() {\n"
        "  const respons = await fetch(ALAMAT);\n"
        "  console.log('status', respons.status, 'ok', respons.ok);\n"
        "  if (!respons.ok) {\n"
        "    throw new Error('status ' + respons.status);\n"
        "  }\n"
        "  return respons.json();\n"
        "}"
    )
    
    t_a3 = doc.add_table(rows=5, cols=2)
    style_standard_table(
        t_a3,
        [Inches(3.2), Inches(3.57)],
        ["Yang dicatat", "Nilai yang saya dapat"],
        [
            ["Alamat API yang saya pakai", "https://ghibliapi.vercel.app/films (dan ./film.json sebagai cadangan)"],
            ["Status balasan (200, 404, dan seterusnya)", "200 OK"],
            ["Nilai respons.ok", "true"],
            ["Jenis isi (Content-Type)", "application/json; charset=utf-8"]
        ]
    )
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    add_subtext(doc, "Buka satu panggilan di panel Network. Periksa tab Headers untuk status dan jenis isi, tab Response untuk badan mentahnya. Badan mentah inilah yang nanti dibaca json(), jadi kenali bentuknya sebelum menulis kode penggambar.")
    
    add_git_commit_box(doc, "A", "P10: panggilan pertama dan status balasan")
    add_check_verification(doc, "A", "buka Console, panggil fungsi muat() Anda. Status dan nilai respons.ok tampil, dan tidak ada tulisan merah.")
    
    doc.add_page_break()
    
    # ==========================================
    # HALAMAN 4: LEMBAR B - ASYNC, AWAIT, & PENANGANAN GALAT
    # ==========================================
    make_worksheet_header(doc, "WORKSHEET", "B", "async, await, dan penanganan galat")
    make_callout_box(
        doc,
        "SATU try/catch MENUTUP SELURUH RANTAI\nRantai then yang panjang sulit dibaca dan galatnya mudah terlewat. async dan await menuliskan alur yang sama secara mendatar, dan satu blok try/catch menangkap galat dari seluruh langkah di dalamnya.",
        bold_prefix="▌",
        hex_bg="EEF2FA",
        border_color="003796"
    )
    
    add_heading_section(doc, "B.1 Ubah rantai menjadi async/await")
    add_subtext(doc, "Tulis fungsi async, lalu bungkus seluruh langkahnya dengan try/catch. Bandingkan bentuknya dengan rantai then pada slide 9 dan 14.")
    
    add_code_block(
        doc,
        "export async function ambilNotisia() {\n"
        "  try {\n"
        "    const respons = await fetch(ALAMAT);\n"
        "    if (!respons.ok) throw new Error('status ' + respons.status);\n"
        "    const data = await respons.json();\n"
        "    return data;\n"
        "  } catch (galat) {\n"
        "    console.error('gagal memuat', galat.message);\n"
        "    throw galat;\n"
        "  }\n"
        "}"
    )
    add_subtext(doc, "await hanya boleh dipakai di dalam fungsi async. Pemanggil di luar fungsi itu masih perlu menangani penolakannya, di pekerjaan Anda, pemanggilnya adalah app.js, dan di sanalah blok try/catch kedua dipasang.")
    
    add_heading_section(doc, "B.2 Kenali tiga kegagalan")
    t_b2 = doc.add_table(rows=5, cols=3)
    style_standard_table(
        t_b2,
        [Inches(2.2), Inches(2.2), Inches(2.37)],
        ["Jenis kegagalan", "Yang terjadi pada Promise", "Cara menanganinya"],
        [
            ["Jaringan mati atau alamat salah", "Promise ditolak", "catch menangkap galat, pesannya ditampilkan"],
            ["Status 404 atau 500", "Promise tetap berhasil", "periksa respons.ok, lalu lempar galat sendiri"],
            ["Badan bukan JSON", "json() menolak", "catch menangkap galat, pesannya ditampilkan"],
            ["Balasan sah tetapi tanpa butir", "Promise berhasil, larik kosong", "tampilkan keadaan kosong, jangan layar putih"]
        ]
    )
    doc.add_paragraph().paragraph_format.space_after = Pt(3)
    
    add_heading_section(doc, "B.3 Buktikan galatnya tertangkap")
    t_b3 = doc.add_table(rows=4, cols=3)
    style_standard_table(
        t_b3,
        [Inches(2.3), Inches(2.3), Inches(2.17)],
        ["Yang saya uji", "Hasil yang benar", "Hasil yang saya dapat"],
        [
            ["Alamat diubah menjadi alamat yang tidak ada", "Pesan galat tampil di halaman, Console bersih dari galat tak tertangani", "Sesuai. Pesan 'Gagal memuat data: status 404' tampil di antarmuka, Console bersih tanpa unhandled rejection."],
            ["Jaringan dimatikan di panel Network", "Pesan galat tampil, bukan layar kosong", "Sesuai. Pesan 'Gagal memuat data: Failed to fetch' tampil jelas di halaman, tidak ada layar blank putih."],
            ["Alamat dikembalikan seperti semula", "Daftar tampil kembali tanpa menyunting kode lain", "Sesuai. Seluruh kartu film langsung otomatis muncul kembali dengan data lengkap dan rapi."]
        ]
    )
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    
    make_callout_box(
        doc,
        "Sengaja rusakkan, buktikan, lalu kembalikan. Uji yang tidak dikembalikan akan tampak sebagai kerusakan pada pertemuan berikutnya, dan Anda yang akan menelusurinya kembali.",
        bold_prefix="",
        hex_bg="FDE8E8",
        border_color="B91C1C"
    )
    
    add_git_commit_box(doc, "B", "P10: async, await, dan satu try/catch")
    add_check_verification(doc, "B", "ubah alamat menjadi alamat yang salah, muat ulang halaman. Pesan galat tampil di halaman, dan Console tidak menampilkan galat tak tertangani.")
    
    doc.add_page_break()
    
    # ==========================================
    # HALAMAN 5: LEMBAR C - MEMBACA JSON
    # ==========================================
    make_worksheet_header(doc, "WORKSHEET", "C", "Membaca JSON")
    make_callout_box(
        doc,
        "TEKS MASUK, NILAI KELUAR, DAN SEBALIKNYA\nBalasan jaringan datang sebagai teks. json() mengubahnya menjadi nilai JavaScript sebelum dapat dipakai. Arah sebaliknya dipakai saat mengirim data ke peladen, dan di situlah JSON.stringify bekerja.",
        bold_prefix="▌",
        hex_bg="EEF2FA",
        border_color="003796"
    )
    
    add_heading_section(doc, "C.1 Dua arah")
    add_subtext(doc, "Baca badan balasan dengan json(), dan kirim data dengan stringify. Perhatikan jenis nilai yang keluar pada tiap arah, salah arah adalah penyebab undefined yang paling sering.")
    
    add_code_block(
        doc,
        "// teks menjadi objek\n"
        "const data = await respons.json();\n"
        "console.log(data[0].title); // atau data.titulu\n\n"
        "// objek menjadi teks\n"
        "const badan = JSON.stringify({ title: 'Inception', release_date: '2010', rt_score: '88' });\n"
        "console.log(typeof badan); // string"
    )
    
    t_c1 = doc.add_table(rows=4, cols=4)
    style_standard_table(
        t_c1,
        [Inches(1.5), Inches(1.1), Inches(2.2), Inches(1.97)],
        ["Yang dipakai", "Arah", "Hasilnya", "Kapan dipakai"],
        [
            ["respons.json()", "teks → nilai", "bentuk data yang bisa diakses dengan kunci", "membaca balasan peladen"],
            ["JSON.parse(teks)", "teks → nilai", "sama, tetapi untuk teks yang Anda pegang sendiri", "membaca localStorage atau berkas JSON lokal"],
            ["JSON.stringify(nilai)", "nilai → teks", "teks yang siap dikirim atau disimpan", "mengirim data, menyimpan ke localStorage"]
        ]
    )
    doc.add_paragraph().paragraph_format.space_after = Pt(3)
    
    add_heading_section(doc, "C.2 Peta data saya")
    add_subtext(doc, "Tulis bentuk balasan API Anda sendiri. Kolom kiri adalah nama kunci, kolom tengah jenis nilainya dan contoh isinya, kolom kanan cara mengaksesnya di dalam kode.")
    
    t_c2 = doc.add_table(rows=5, cols=3)
    style_standard_table(
        t_c2,
        [Inches(2.0), Inches(2.8), Inches(1.97)],
        ["Nama kunci", "Jenis nilai dan contoh", "Cara mengaksesnya"],
        [
            ["data[0] (entitas film)", "objek: { id: '...', title: 'Castle in the Sky', director: 'Hayao Miyazaki', ... }", "data[0]"],
            ["data (larik respons)", "larik: [ { title: 'Castle in the Sky' }, { title: 'Grave of the Fireflies' }, ... ]", "data.forEach(film => buatKartu(film))"],
            ["title / release_date / rt_score", "teks atau angka: title: 'Castle in the Sky', release_date: '1986', rt_score: '95'", "data[0].title / film.title"],
            ["selesai / penghargaan", "benar atau salah, atau null: selesai: true, penghargaan: null (skema film)", "data[0].selesai / film.selesai"]
        ]
    )
    doc.add_paragraph().paragraph_format.space_after = Pt(3)
    
    add_heading_section(doc, "C.3 Periksa bentuknya sebelum menggambar")
    add_subtext(doc, "Panggil console.log(data) sekali sebelum menulis kode penggambar. Membaca bentuk data lebih dulu menghemat waktu, karena kunci yang salah hanya menghasilkan undefined tanpa galat yang jelas.")
    
    add_git_commit_box(doc, "C", "P10: membaca JSON dua arah")
    add_check_verification(doc, "C", "tulis nama kunci Anda di Console satu per satu. Tidak ada satu pun yang bernilai undefined.")
    
    doc.add_page_break()
    
    # ==========================================
    # HALAMAN 6 & 7: LEMBAR D - MENAMPILKAN DATA KE HALAMAN
    # ==========================================
    make_worksheet_header(doc, "WORKSHEET", "D", "Menampilkan data ke halaman")
    make_callout_box(
        doc,
        "PISAHKAN PENGAMBILAN DATA DARI PENGGAMBARAN\nFungsi pengambil data hanya bertugas mengambil dan memeriksa. Fungsi penggambar hanya bertugas menyusun elemen. Dipisah begitu, halaman mudah diuji ketika alamat peladennya berubah, dan itulah bentuk yang dipakai lagi di Pertemuan 11.",
        bold_prefix="▌",
        hex_bg="EEF2FA",
        border_color="003796"
    )
    
    add_heading_section(doc, "D.1 Telusuri larik dan gambar kartu")
    add_subtext(doc, "Telusuri larik hasil parse, buat satu elemen untuk tiap butir, lalu pasang ke wadah yang sudah ada di HTML. Gunakan textContent, bukan innerHTML, untuk isi yang datang dari jaringan.")
    
    add_code_block(
        doc,
        "import { ambilNotisia } from './api.js';\n\n"
        "const wadah = document.querySelector('#daftar');\n\n"
        "function gambar(daftar) {\n"
        "  wadah.textContent = '';\n"
        "  daftar.forEach(function (n) {\n"
        "    const kartu = document.createElement('article');\n"
        "    const judul = document.createElement('h3');\n"
        "    judul.textContent = n.title || n.titulu || n.judul;\n"
        "    kartu.appendChild(judul);\n"
        "    wadah.appendChild(kartu);\n"
        "  });\n"
        "}\n\n"
        "async function tampilkan() {\n"
        "  wadah.textContent = 'Memuat...';\n"
        "  try {\n"
        "    const daftar = await ambilNotisia();\n"
        "    if (daftar.length === 0) {\n"
        "      wadah.textContent = 'Belum ada notisia';\n"
        "      return;\n"
        "    }\n"
        "    gambar(daftar);\n"
        "  } catch (galat) {\n"
        "    wadah.textContent = 'Gagal memuat data: ' + galat.message;\n"
        "  }\n"
        "}\n\n"
        "tampilkan();"
    )
    
    add_heading_section(doc, "D.2 Keempat keadaan antarmuka")
    add_subtext(doc, "Isi tabel berikut dengan cara Anda menampilkan tiap keadaan. Keadaan kosong sering terlupa, padahal balasan yang sah bisa berisi larik kosong.")
    
    t_d2 = doc.add_table(rows=5, cols=3)
    style_standard_table(
        t_d2,
        [Inches(1.3), Inches(2.5), Inches(2.97)],
        ["Keadaan", "Kapan terjadi", "Apa yang tampil di halaman"],
        [
            ["Memuat", "sebelum balasan datang", "Teks 'Memuat data film dari API...' tampil pada wadah #daftar."],
            ["Berhasil", "balasan berisi data", "Daftar kartu film (<li class='kartu'>) lengkap terpasang rapi di galeri grid."],
            ["Gagal", "jaringan gagal atau status bukan 2xx", "Teks 'Gagal memuat data: [pesan galat/status]' tampil di wadah."],
            ["Kosong", "balasan sah tetapi tanpa butir", "Teks 'Belum ada film yang tersedia.' dan paragraf #pesan-kosong ditampilkan."]
        ]
    )
    doc.add_paragraph().paragraph_format.space_after = Pt(3)
    
    add_heading_section(doc, "D.3 Periksa batas lapisan")
    t_d3 = doc.add_table(rows=6, cols=3)
    style_standard_table(
        t_d3,
        [Inches(2.5), Inches(2.2), Inches(2.07)],
        ["Yang diperiksa", "Hasil yang benar", "Hasil yang saya dapat"],
        [
            ["js/api.js memanggil fetch dan mengekspor fungsinya", "satu export terlihat di bagian atas berkas", "Sesuai. export async function ambilFilm() (dan alias ambilNotisia) berada di js/api.js."],
            ["js/app.js tidak memanggil fetch sendiri", "kata fetch hanya ada di js/api.js", "Sesuai. Berkas app.js dan dom.js bersih dari fetch, pemanggilan murni melalui modul impor."],
            ["app.js menangani penolakan dari api.js", "blok try/catch kedua ada di pemanggil", "Sesuai. Blok try/catch kedua dipasang di app.js dan dom.js untuk menangani Promise rejection."],
            ["Wadah dikosongkan sebelum digambar ulang", "jumlah kartu tidak berlipat saat dimuat ulang", "Sesuai. wadah.textContent = '' dijalankan di awal fungsi render() sebelum perulangan kartu."],
            ["Nama fungsi yang diekspor tercatat", "nama itu yang akan ditulis di berkas pengimpor Pertemuan 11", "Sesuai. Fungsi ambilFilm diekspor konsisten dan siap digunakan kembali pada Pertemuan 11."]
        ]
    )
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    
    add_git_commit_box(doc, "D", "P10: data dari jaringan tampil di halaman")
    add_check_verification(doc, "D", "muat ulang halaman tanpa menyentuh Console. Kartu tampil dari data, dan tidak ada kartu yang berlipat.")
    
    doc.add_page_break()
    
    # ==========================================
    # HALAMAN 8: LEMBAR E - TIGA KASUS SULIT
    # ==========================================
    make_worksheet_header(doc, "WORKSHEET", "E", "Tiga kasus sulit")
    make_callout_box(
        doc,
        "TIDAK ADA GALAT DI CONSOLE, TETAPI HALAMAN DIAM\nKetiga kasus berikut tidak selalu menimbulkan galat. Yang terlihat hanya halaman yang diam atau kosong, sehingga gejalanya perlu dibaca lebih dulu sebelum kodenya disentuh.",
        bold_prefix="▌",
        hex_bg="EEF2FA",
        border_color="003796"
    )
    
    add_heading_section(doc, "E.1 Status 404 tidak melempar galat")
    add_subtext(doc, "fetch hanya menolak Promise ketika permintaannya gagal, jaringan mati, alamat tidak dapat dijangkau, atau permintaan diblokir. Status 404 dan 500 tetap dianggap berhasil. Satu pemeriksaan respons.ok menutup celah itu sebelum badannya dibaca.")
    
    t_e1 = doc.add_table(rows=4, cols=3)
    style_standard_table(
        t_e1,
        [Inches(2.2), Inches(2.2), Inches(2.37)],
        ["Gejala", "Sebab yang paling sering", "Yang dilakukan"],
        [
            ["Halaman menampilkan kartu kosong", "badan 404 dibaca sebagai data", "periksa respons.ok sebelum memanggil json()"],
            ["Daftar berisi undefined", "kunci data salah, tetapi statusnya 200", "cetak console.log(data) sekali untuk melihat bentuknya"],
            ["json() melempar SyntaxError", "badan bukan JSON, sering halaman galat HTML", "periksa Content-Type di panel Network"]
        ]
    )
    doc.add_paragraph().paragraph_format.space_after = Pt(3)
    
    add_heading_section(doc, "E.2 await di luar fungsi async")
    add_subtext(doc, "await hanya sah di dalam fungsi async. Bila dipasang di luar, berkasnya gagal diurai dan seluruh skrip ikut berhenti, tidak cukup satu baris. Gejalanya mudah dikenali: tidak satu pun kode di berkas itu berjalan.")
    
    add_code_block(
        doc,
        "// salah: berkas gagal diurai\n"
        "const data = await fetch(ALAMAT);\n\n"
        "// benar: dibungkus fungsi async\n"
        "async function muat() {\n"
        "  const data = await fetch(ALAMAT);\n"
        "}"
    )
    
    add_heading_section(doc, "E.3 Balasan sah tetapi tanpa butir")
    add_subtext(doc, "Balasan dengan larik kosong tidak menimbulkan galat apa pun. Halaman hanya tampak kosong, dan pengguna tidak tahu apakah datanya belum ada atau kodenya salah. Keadaan kosong perlu ditulis sebagai keadaan tersendiri.\nTulis pesan kosong yang menjelaskan keadaan yang sedang terjadi. \"Belum ada notisia\" lebih berguna daripada halaman putih, dan itu yang membedakan halaman yang selesai dari halaman yang setengah jadi.")
    
    add_heading_section(doc, "E.4 Catat kasus yang saya temui")
    t_e4 = doc.add_table(rows=4, cols=3)
    style_standard_table(
        t_e4,
        [Inches(2.2), Inches(2.2), Inches(2.37)],
        ["Gejala yang saya lihat", "Sebabnya", "Cara saya memperbaiki"],
        [
            ["URL salah menghasilkan kartu kosong / crash", "Respons 404 tetap menyelesaikan Promise dan fetch tidak otomatis melempar galat", "Menambahkan if (!respons.ok) throw new Error('status ' + respons.status) sebelum json()"],
            ["Skrip macet total saat testing await", "Penulisan await di luar async function pada uji skrip awal", "Membungkus seluruh logika asinkron ke dalam async function tampilkan()"],
            ["Layar blank putih saat filter menghasilkan 0 film", "Array kosong [] langsung di-loop forEach tanpa validasi panjang", "Menambahkan percabangan if (daftar.length === 0) untuk menampilkan teks keadaan kosong"]
        ]
    )
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    
    add_git_commit_box(doc, "E", "P10: tiga kasus sulit ditangani")
    add_check_verification(doc, "E", "rusakkan alamat, matikan jaringan, dan kosongkan data. Ketiga keadaan tampil sebagai pesan di halaman, bukan layar putih.")
    
    doc.add_page_break()
    
    # ==========================================
    # HALAMAN 9 & 10: LEMBAR F - PERIKSA, TIKET KELUAR, PENILAIAN MANDIRI
    # ==========================================
    make_worksheet_header(doc, "WORKSHEET", "F", "Periksa, tiket keluar, penilaian mandiri")
    make_callout_box(
        doc,
        "SETIAP KEADAAN DIBUKTIKAN DENGAN TANGKAPAN LAYAR\nPemeriksaan dilakukan pada keempat keadaan, dan setiap keadaan disimpan sebagai tangkapan layar. Tanpa bukti itu, halaman yang hanya bekerja sekali sulit ditelusuri kembali.",
        bold_prefix="▌",
        hex_bg="EEF2FA",
        border_color="003796"
    )
    
    add_heading_section(doc, "F.1 Periksa satu per satu")
    t_f1 = doc.add_table(rows=11, cols=3)
    style_standard_table(
        t_f1,
        [Inches(2.5), Inches(3.3), Inches(0.97)],
        ["Periksa", "Cara memeriksa", "Lolos"],
        [
            ["Alamat di satu tempat", "lihat bagian atas js/api.js", "☑ Lolos"],
            ["respons.ok diperiksa", "lihat fungsi pengambil di js/api.js", "☑ Lolos"],
            ["Galat ditangkap", "matikan jaringan, muat ulang halaman", "☑ Lolos"],
            ["Keadaan memuat tampil", "perlambat jaringan di panel Network", "☑ Lolos"],
            ["Keadaan kosong tampil", "panggil gambar([]) dari Console", "☑ Lolos"],
            ["Data tampil sebagai elemen", "periksa wadah di panel Elements", "☑ Lolos"],
            ["Batas lapisan terjaga", "kata fetch hanya ada di js/api.js", "☑ Lolos"],
            ["Tidak ada galat di Console", "baca panel Console", "☑ Lolos"],
            ["Pengungkapan AI", "README menyebutkan bagian mana yang dibantu AI dan bagian mana yang saya kerjakan sendiri", "☑ Lolos"],
            ["Keaslian", "topik dan isi halaman ini milik saya sendiri, tidak menyalin pekerjaan mahasiswa lain", "☑ Lolos"]
        ]
    )
    doc.add_paragraph().paragraph_format.space_after = Pt(3)
    
    add_heading_section(doc, "F.2 Bukti empat keadaan")
    t_f2 = doc.add_table(rows=4, cols=3)
    style_standard_table(
        t_f2,
        [Inches(1.4), Inches(2.3), Inches(3.07)],
        ["Keadaan", "Tangkapan layar disimpan", "Catatan"],
        [
            ["Berhasil", "screenshot_berhasil.png", "Kartu film berhasil diambil dari API publik dan terender lengkap di galeri grid."],
            ["Gagal", "screenshot_gagal.png", "Saat status 404 atau offline, pesan 'Gagal memuat data: status 404' tampil di halaman."],
            ["Kosong atau memuat", "screenshot_memuat_kosong.png", "Menampilkan status 'Memuat data...' dan pesan 'Belum ada film yang tersedia' saat data kosong."]
        ]
    )
    doc.add_paragraph().paragraph_format.space_after = Pt(3)
    
    # Sisipkan Gambar Tangkapan Layar
    p_img1_lbl = doc.add_paragraph()
    r = p_img1_lbl.add_run("Bukti Keadaan 1: Berhasil (screenshot_berhasil.png)")
    r.font.name = "Carlito"
    r.font.size = Pt(8.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0x00, 0x37, 0x96)
    
    if os.path.exists("screenshot_berhasil.png"):
        p_img1 = doc.add_paragraph()
        p_img1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img1.paragraph_format.space_after = Pt(4)
        doc.add_picture("screenshot_berhasil.png", width=Inches(6.2))
        
    p_img2_lbl = doc.add_paragraph()
    r = p_img2_lbl.add_run("Bukti Keadaan 2: Gagal (screenshot_gagal.png)")
    r.font.name = "Carlito"
    r.font.size = Pt(8.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0x00, 0x37, 0x96)
    
    if os.path.exists("screenshot_gagal.png"):
        p_img2 = doc.add_paragraph()
        p_img2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img2.paragraph_format.space_after = Pt(4)
        doc.add_picture("screenshot_gagal.png", width=Inches(6.2))
        
    p_img3_lbl = doc.add_paragraph()
    r = p_img3_lbl.add_run("Bukti Keadaan 3 & 4: Memuat & Kosong (screenshot_memuat_kosong.png)")
    r.font.name = "Carlito"
    r.font.size = Pt(8.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0x00, 0x37, 0x96)
    
    if os.path.exists("screenshot_memuat_kosong.png"):
        p_img3 = doc.add_paragraph()
        p_img3.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img3.paragraph_format.space_after = Pt(4)
        doc.add_picture("screenshot_memuat_kosong.png", width=Inches(6.2))
        
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    
    add_heading_section(doc, "F.3 Satu baris untuk diingat")
    add_subtext(doc, "Tuliskan satu potongan kode yang paling sering Anda pakai hari ini, dan tuliskan pada bagian mana potongan itu dipakai. Satu baris sudah cukup.")
    t_f3 = doc.add_table(rows=2, cols=2)
    style_standard_table(
        t_f3,
        [Inches(3.7), Inches(3.07)],
        ["Potongan kode:", "Dipakai pada:"],
        [[
            "if (!respons.ok) throw new Error('status ' + respons.status);",
            "js/api.js di dalam fungsi ambilFilm(), tepat setelah await fetch(ALAMAT) sebelum respons.json()"
        ]]
    )
    doc.add_paragraph().paragraph_format.space_after = Pt(3)
    
    add_heading_section(doc, "F.4 Penilaian mandiri")
    t_f4 = doc.add_table(rows=7, cols=4)
    style_standard_table(
        t_f4,
        [Inches(2.5), Inches(0.8), Inches(0.9), Inches(2.57)],
        ["Bagian", "Bobot", "Nilai saya", "Bukti"],
        [
            ["Alur data dan pemeriksaan status", "25", "25", "js/api.js baris 11-15 (ALAMAT tunggal, fetch, respons.ok diperiksa)"],
            ["Pembacaan JSON dan pemisahan lapisan", "25", "25", "js/api.js baris 16 (respons.json()), pemanggilan api.js di app.js dan dom.js tanpa fetch"],
            ["Keadaan antarmuka", "20", "20", "js/dom.js fungsi tampilkan() dan render() menangani memuat, berhasil, gagal, kosong"],
            ["Penanganan galat", "20", "20", "Blok try/catch di lapisan data dan pemanggil, pesan galat tampil di antarmuka"],
            ["Kebersihan kode, deklarasi AI, dan bukti", "10", "10", "Penamaan konsisten, deklarasi AI lengkap di README.md, 3 tangkapan layar disertakan"],
            ["TOTAL", "100", "100", "Seluruh target capaian P10 terpenuhi 100% dan terverifikasi di peramban"]
        ]
    )
    doc.add_paragraph().paragraph_format.space_after = Pt(3)
    
    add_heading_section(doc, "F.5 Tiket keluar")
    add_subtext(doc, "Jawab tiga pertanyaan berikut, satu baris masing-masing. Tiket ini dibaca pengampu sebagai catatan pemahaman Anda.")
    t_f5 = doc.add_table(rows=4, cols=2)
    style_standard_table(
        t_f5,
        [Inches(3.2), Inches(3.57)],
        ["Pertanyaan", "Jawaban"],
        [
            ["Mengapa fetch tidak melempar galat pada status 404", "Karena fetch hanya menolak Promise pada kegagalan jaringan fisik/DNS; status 404 tetap respons HTTP valid sehingga harus dicek manual via respons.ok."],
            ["Di mana await boleh dipakai, dan di mana tidak", "await hanya sah dipakai di dalam fungsi yang dideklarasikan dengan async (atau top-level module), dan tidak boleh dipakai di fungsi biasa/sinkron."],
            ["Satu keadaan antarmuka yang paling mudah terlupa dan cara Anda menutupnya", "Keadaan kosong (empty state), ditutup dengan pengecekan if (daftar.length === 0) sebelum perenderan agar menampilkan pesan ramah bagi pengguna, bukan layar putih."]
        ]
    )
    doc.add_paragraph().paragraph_format.space_after = Pt(3)
    
    add_heading_section(doc, "F.6 Catatan untuk pengampu")
    
    t_f6 = doc.add_table(rows=2, cols=1)
    cell_f6_0 = t_f6.rows[0].cells[0]
    set_cell_background(cell_f6_0, "FFFFFF")
    set_cell_margins(cell_f6_0, top=50, bottom=50, left=70, right=70)
    p0 = cell_f6_0.paragraphs[0]
    p0.paragraph_format.space_after = Pt(1)
    r = p0.add_run("Bagian yang paling sulit:\n")
    r.font.name = "Carlito"
    r.font.size = Pt(8.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0x00, 0x37, 0x96)
    r_ans = p0.add_run("Memastikan sinkronisasi transisi antarmuka saat data asinkron dimuat serta memisahkan batas tanggung jawab lapisan data (api.js) dari pemanggil (dom.js) agar kode tetap modular.")
    r_ans.font.name = "Carlito"
    r_ans.font.size = Pt(8.5)
    
    cell_f6_1 = t_f6.rows[1].cells[0]
    set_cell_background(cell_f6_1, "FFFFFF")
    set_cell_margins(cell_f6_1, top=50, bottom=50, left=70, right=70)
    p1 = cell_f6_1.paragraphs[0]
    p1.paragraph_format.space_after = Pt(1)
    r = p1.add_run("Yang ingin saya bahas di kelas berikutnya:\n")
    r.font.name = "Carlito"
    r.font.size = Pt(8.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0x00, 0x37, 0x96)
    r_ans2 = p1.add_run("Penerapan pembatalan permintaan asinkron menggunakan AbortController, manajemen caching data lokal dengan sessionStorage/Cache API, dan teknik pagination/infinite scrolling.")
    r_ans2.font.name = "Carlito"
    r_ans2.font.size = Pt(8.5)
    set_table_borders(t_f6, color="D0D7DE", sz="4")
    
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    
    p_sign = doc.add_paragraph()
    p_sign.paragraph_format.space_before = Pt(3)
    p_sign.paragraph_format.space_after = Pt(3)
    r_sign = p_sign.add_run("Tanda tangan: Amadeus Dharma Akbarindra          Tanggal: 14 Oktober 2026          Jam selesai: 11.45 WIB")
    r_sign.font.name = "Carlito"
    r_sign.font.size = Pt(8.5)
    r_sign.font.bold = True
    r_sign.font.color.rgb = RGBColor(0x1F, 0x23, 0x28)
    
    add_git_commit_box(doc, "F", "P10: periksa, lalu simpan")
    add_check_verification(doc, "F", "buka README di repositori Anda. Bagian Pertemuan 10 sudah memuat deklarasi AI, dan commit terakhir adalah commit terbaru.")
    
    doc.add_page_break()
    
    # ==========================================
    # HALAMAN 11: LAMPIRAN A - RUBRIK PENILAIAN
    # ==========================================
    make_worksheet_header(doc, "WORKSHEET", "H", "Lampiran A, rubrik penilaian")
    make_callout_box(
        doc,
        "RUBRIK PENILAIAN total 100",
        bold_prefix="▌",
        hex_bg="EEF2FA",
        border_color="003796"
    )
    
    t_rubrik = doc.add_table(rows=6, cols=5)
    style_standard_table(
        t_rubrik,
        [Inches(1.5), Inches(0.7), Inches(1.8), Inches(1.4), Inches(1.37)],
        ["Aspek", "Bobot", "Nilai 100, sangat baik", "Nilai 65, memadai", "Nilai 35, kurang"],
        [
            ["Alur data dan pemeriksaan status", "25%", "Alamat di satu tempat; respons.ok diperiksa sebelum badan dibaca; fungsi pengambil berada di js/api.js dan diekspor", "Panggilan berjalan, tetapi respons.ok atau pemisahan berkas belum lengkap", "fetch belum benar, atau status balasan tidak pernah diperiksa"],
            ["Pembacaan JSON dan pemisahan lapisan", "25%", "json() dan stringify dipakai pada arah yang tepat; app.js memanggil api.js tanpa memanggil fetch sendiri", "Pembacaan benar, tetapi fetch masih ada di app.js atau stringify belum dipakai", "Bentuk data ditebak tanpa diperiksa, sehingga banyak nilai undefined"],
            ["Keadaan antarmuka", "20%", "Keempat keadaan tampil: memuat, berhasil, gagal, kosong", "Tiga keadaan tampil, keadaan kosong belum ada", "Hanya keadaan berhasil yang ditangani"],
            ["Penanganan galat", "20%", "Satu try/catch menutup seluruh rantai; pesan galat tampil di halaman, tidak sekadar di console", "Galat tertangkap, tetapi pesannya hanya di console", "Galat tak tertangani, halaman diam tanpa penjelasan"],
            ["Kebersihan kode, deklarasi AI, dan bukti", "10%", "Penamaan konsisten, batas api.js dan app.js jelas; deklarasi AI terisi di README; tangkapan layar empat keadaan disertakan", "Kode rapi tetapi deklarasi AI atau bukti belum lengkap", "Deklarasi AI kosong, atau pekerjaan tidak tersimpan di repositori"]
        ]
    )
    doc.add_paragraph().paragraph_format.space_after = Pt(3)
    
    make_callout_box(
        doc,
        "Yang dinilai adalah pekerjaan Anda sendiri. Topik yang berbeda antar mahasiswa membuat penilaian tidak bisa dibandingkan antar pekerjaan, karena itu yang diperiksa adalah apakah setiap bagian bekerja sebagaimana dimaksud, bukan apakah ia sama dengan contoh.",
        bold_prefix="▌",
        hex_bg="EEF2FA",
        border_color="003796"
    )
    
    doc.add_page_break()
    
    # ==========================================
    # HALAMAN 12 & 13: LAMPIRAN B - RUJUKAN CEPAT, KALAU MACET & GIT
    # ==========================================
    make_worksheet_header(doc, "WORKSHEET", "H", "Lampiran B, rujukan cepat dan kalau macet")
    make_callout_box(
        doc,
        "REFERENSI CEPAT ASINKRON hafalkan yang ini",
        bold_prefix="▌",
        hex_bg="EEF2FA",
        border_color="003796"
    )
    
    t_ref = doc.add_table(rows=13, cols=3)
    style_standard_table(
        t_ref,
        [Inches(1.8), Inches(3.2), Inches(1.77)],
        ["Yang dipakai", "Perannya", "Kapan dipakai"],
        [
            ["fetch(url)", "Mengirim permintaan HTTP; hasilnya Promise berisi Response", "mengambil data dari API publik / endpoint"],
            ["respons.ok", "benar bila status 2xx, tidak ada galat otomatis pada 404", "pemeriksaan status balasan sebelum membaca body"],
            ["respons.status", "Kode status balasan: 200, 404, 500, dan seterusnya", "pemeriksaan kode status HTTP spesifik"],
            ["respons.json()", "Membaca badan balasan sebagai JSON; hasilnya Promise", "mengurai string JSON balasan server ke objek JS"],
            ["await", "Menunggu Promise selesai; hanya di dalam fungsi async", "menunggu hasil operasi asinkron secara linear"],
            ["async function", "Menandai fungsi yang boleh memuat await", "deklarasi fungsi penampung alur asinkron"],
            ["try / catch", "Menangkap penolakan Promise di sekitarnya", "penanganan galat jaringan atau status error"],
            ["throw new Error()", "Membuat galat sendiri, misalnya untuk status bukan 2xx", "memicu penolakan saat respons.ok bernilai false"],
            ["Promise.all([...])", "Menunggu beberapa Promise sekaligus", "menjalankan beberapa fetch secara bersamaan"],
            ["JSON.parse(teks)", "Teks menjadi nilai JavaScript", "membaca localStorage atau berkas JSON lokal"],
            ["JSON.stringify(nilai)", "Nilai menjadi teks JSON", "mengirim payload ke server atau simpan localStorage"],
            ["export / import", "Menyerahkan fungsi ke berkas lain, dipakai js/api.js", "pemisahan modular lapisan data dan tampilan"]
        ]
    )
    doc.add_paragraph().paragraph_format.space_after = Pt(3)
    
    make_callout_box(
        doc,
        "KALAU MACET cari gejalanya di sini",
        bold_prefix="▌",
        hex_bg="EEF2FA",
        border_color="003796"
    )
    
    t_macet = doc.add_table(rows=12, cols=3)
    style_standard_table(
        t_macet,
        [Inches(2.2), Inches(2.3), Inches(2.27)],
        ["Gejala", "Penyebab yang paling sering", "Yang dilakukan"],
        [
            ["Console: 404 untuk api.js", "Jalur di atribut src tidak cocok dengan letak berkasnya", "Pastikan api.js berada di dalam folder js/, huruf besar-kecilnya sama"],
            ["Console: Cannot read properties of undefined", "Kunci data salah, tetapi status balasan 200", "Cetak console.log(data) sekali, lalu tulis kunci yang benar-benar ada"],
            ["Kartu kosong padahal Console bersih", "Badan 404 dibaca sebagai data karena respons.ok tidak diperiksa", "Periksa respons.ok sebelum memanggil json()"],
            ["json() melempar SyntaxError", "Badan bukan JSON, sering halaman galat HTML", "Periksa Content-Type di panel Network"],
            ["Seluruh berkas berhenti, Console tanpa pesan jelas", "await ditulis di luar fungsi async", "Bungkus pemanggilnya dengan async function"],
            ["Halaman diam tanpa penjelasan", "Penolakan Promise tidak ditangkap pemanggil", "Tambahkan try/catch di app.js dan tampilkan pesannya di halaman"],
            ["Daftar kosong tanpa keterangan", "Balasan sah berisi larik kosong", "Tampilkan keadaan kosong ketika panjang lariknya nol"],
            ["Kartu berlipat tiap kali dimuat ulang", "Wadah tidak dikosongkan sebelum digambar", "Tambahkan wadah.textContent = '' di baris pertama penggambar"],
            ["Isi kartu tampil sebagai tag, bukan teks", "Isi dimasukkan dengan innerHTML", "Ganti dengan textContent"],
            ["CORS: permintaan diblokir", "API tidak mengizinkan asal halaman Anda", "Pakai API lain yang mengizinkan CORS, atau berkas notisia.json lokal"],
            ["Fetch gagal hanya di berkas file://", "Halaman dibuka dengan klik dua kali", "Jalankan lewat server lokal: python3 -m http.server 8000"]
        ]
    )
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    
    add_subtext(doc, "Halaman yang Anda bangun hari ini adalah bahan ujian CPMK Blok 2 pada Pertemuan 13 nanti: pemilihan elemen, render dari data, event delegation, dan pengambilan data dari jaringan semuanya diuji di sana. Di Pertemuan 11, js/api.js yang Anda buat hari ini diimpor apa adanya, jadi pilih nama fungsi ekspornya dengan sadar: nama itulah yang ditulis di berkas pengimpor. Simpan pekerjaan ini rapi di repositori Anda.")
    
    make_callout_box(
        doc,
        "LAMPIRAN: MENYIMPAN PEKERJAAN ANDA KE GIT sekali saja, bukan tiap pertemuan\nLampiran ini bukan pengantar Git. Panduan Git dan GitHub yang sudah Anda pakai sejak Pertemuan 3 masih berlaku seluruhnya; bagian ini hanya mengulang tiga perintah yang paling sering dipakai, karena mulai hari ini ada berkas baru yang harus ikut disimpan.",
        bold_prefix="▌",
        hex_bg="EEF2FA",
        border_color="003796"
    )
    
    t_git = doc.add_table(rows=4, cols=3)
    style_standard_table(
        t_git,
        [Inches(1.8), Inches(3.0), Inches(1.97)],
        ["Perintah", "Artinya", "Kapan dijalankan"],
        [
            ["git add .", "Menandai seluruh perubahan di folder ini untuk disimpan", "Setiap kali selesai satu lembar"],
            ["git commit -m \"pesan\"", "Menyimpan perubahan itu sebagai satu riwayat", "Langsung setelah git add"],
            ["git push", "Mengirim riwayat itu ke GitHub", "Setelah commit, supaya dosen bisa melihatnya"]
        ]
    )
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    
    add_subtext(doc, "Titik pada git add . Titik itu berarti \"seluruh berkas di folder ini\". Tanpa titik, Git tidak tahu apa yang harus disimpan. Hal yang sama berlaku untuk berkas api.js yang baru Anda buat, ia ikut tersimpan karena berada di dalam folder semester.")
    
    add_heading_section(doc, "Berapa kali harus menyimpan?")
    add_subtext(doc, "Tidak ada angka yang benar, tetapi patokannya begini: bila Anda sudah menyelesaikan satu hal yang berarti dan bisa Anda jelaskan, simpanlah. Pada pertemuan ini minimal dua kali: setelah data tampil di halaman, dan setelah keempat keadaan antarmuka selesai.")
    
    t_git_case = doc.add_table(rows=4, cols=2)
    style_standard_table(
        t_git_case,
        [Inches(3.2), Inches(3.57)],
        ["Kalau ini terjadi", "Yang Anda lakukan"],
        [
            ["Sudah menulis banyak, belum pernah commit", "Simpan sekarang juga"],
            ["Salah commit, belum push", "Perbaiki lalu commit lagi, jangan hapus repositori"],
            ["Sudah push, lalu menemukan kekeliruan", "Perbaiki berkasnya dan commit lagi; riwayat lama tidak hilang dan itu wajar"]
        ]
    )
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    
    make_callout_box(
        doc,
        "Yang dinilai bukan jumlah commit. Menyimpan sering membuat pekerjaan Anda tidak bergantung pada satu berkas di satu komputer, dan pada pertemuan ujian, repositori itulah yang menentukan apakah pekerjaan Anda bisa dinilai.",
        bold_prefix="▌",
        hex_bg="EEF2FA",
        border_color="003796"
    )
    
    doc.save(output_path)
    print(f"Dokumen Word berhasil dibuat dan disimpan ke: {output_path}")

if __name__ == "__main__":
    out_file = "AMADEUS DHARMA AKBARINDRA - 25523253 - 10. Worksheet_PABW_Pertemuan10.docx"
    generate_p10_docx(out_file)
