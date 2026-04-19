# -*- coding: utf-8 -*-
"""
Orchisky 主题应用工具 V2.0
"""
import os
import zipfile
import tempfile
import shutil

ORCHISKY_THEME_XML = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="Orchisky">
<a:themeElements>
<a:clrScheme name="Orchisky">
<a:dk1><a:srgbClr val="1A1A1A"/></a:dk1>
<a:lt1><a:srgbClr val="FFFFFF"/></a:lt1>
<a:dk2><a:srgbClr val="003D7A"/></a:dk2>
<a:lt2><a:srgbClr val="E8F0FA"/></a:lt2>
<a:accent1><a:srgbClr val="003D7A"/></a:accent1>
<a:accent2><a:srgbClr val="0056A8"/></a:accent2>
<a:accent3><a:srgbClr val="3A7FC1"/></a:accent3>
<a:accent4><a:srgbClr val="A8C8ED"/></a:accent4>
<a:accent5><a:srgbClr val="1A7A42"/></a:accent5>
<a:accent6><a:srgbClr val="B01C1C"/></a:accent6>
<a:hlink><a:srgbClr val="003D7A"/></a:hlink>
<a:folHlink><a:srgbClr val="0056A8"/></a:folHlink>
</a:clrScheme>
<a:fontScheme name="Orchisky">
<a:majorFont>
<a:latin typeface="宋体-简"/>
<a:ea typeface="完体-简"/>
<a:cs typeface="宋体-简"/>
<a:font script="Hans" typeface="宋体-简"/>
</a:majorFont>
<a:minorFont>
<a:latin typeface="Microsoft YaHei"/>
<a:ea typeface="Microsoft YaHei"/>
<a:cs typeface="Microsoft YaHei"/>
<a:font script="Hans" typeface="Microsoft YaHei"/>
</a:minorFont>
</a:fontScheme>
<a:fmtScheme name="Orchisky">
<a:fillStyleLst>
<a:solidFill><a:schemeClr val="phClr"/></a:solidFill>
<a:solidFill><a:schemeClr val="phClr"><a:tint val="60000"/></a:schemeClr></a:solidFill>
<a:solidFill><a:schemeClr val="phClr"><a:shade val="80000"/></a:schemeClr></a:solidFill>
</a:fillStyleLst>
<a:lnStyleLst>
<a:ln w="6350" cap="flat" cmpd="sng" algn="ctr"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill><a:prstDash val="solid"/><a:miter lim="800000"/></a:ln>
<a:ln w="12700" cap="flat" cmpd="sng" algn="ctr"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill><a:prstDash val="solid"/><a:miter lim="800000"/></a:ln>
<a:ln w="19050" cap="flat" cmpd="sng" algn="ctr"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill><a:prstDash val="solid"/><a:miter lim="800000"/></a:ln>
</a:lnStyleLst>
<a:effectStyleLst>
<a:effectStyle><a:effectLst/></a:effectStyle>
<a:effectStyle><a:effectLst/></a:effectStyle>
<a:effectStyle><a:effectLst/></a:effectStyle>
</a:effectStyleLst>
<a:bgFillStyleLst>
<a:solidFill><a:schemeClr val="phClr"/></a:solidFill>
<a:solidFill><a:schemeClr val="phClr"><a:tint val="95000"/></a:schemeClr></a:solidFill>
<a:solidFill><a:schemeClr val="phClr"><a:shade val="95000"/></a:schemeClr></a:solidFill>
</a:bgFillStyleLst>
</a:fmtScheme>
</a:themeElements>
<a:objectDefaults>
<a:spDef>
<a:spPr/><a:bodyPr/><a:lstStyle/>
<a:style>
<a:lnRef idx="0"><a:schemeClr val="accent1"/></a:lnRef>
<a:fillRef idx="1"><a:schemeClr val="accent1"/></a:fillRef>
<a:effectRef idx="0"><a:schemeClr val="accent1"/></a:effectRef>
<a:fontRef idx="minor"><a:schemeClr val="lt1"/></a:fontRef>
</a:style>
</a:spDef>
</a:objectDefaults>
<a:extraClrSchemeLst/>
</a:theme>'''


def _get_theme_xml():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    external_path = os.path.join(script_dir, 'theme1_orchisky.xml')
    if os.path.exists(external_path):
        with open(external_path, 'r', encoding='utf-8') as f:
            return f.read()
    return ORCHISKY_THEME_XML


def apply_orchisky_theme(prs):
    """'在 python-pptx Presentation 对象上应用主题（内存操作）"""
    theme_xml = _get_theme_xml().encode('utf-8')
    count = 0
    for part in prs.part.package.iter_parts():
        partname = str(part.partname).lower()
        if '/theme/theme' in partname and partname.endswith('.xml'):
            part._blob = theme_xml
            count += 1
    if count == 0:
        raise RuntimeError("未找到 theme1.xml，应用失败")
    return count


def apply_orchisky_theme_to_file(input_pptx, output_pptx=None):
    """在磁盘 pptx 文件上应用主题"""
    if output_pptx is None:
        output_pptx = input_pptx
    theme_xml = _get_theme_xml()
    work_dir = tempfile.mkdtemp()
    try:
        with zipfile.ZipFile(input_pptx, 'r') as z:
            z.extractall(work_dir)
        theme_dir = os.path.join(work_dir, 'ppt', 'theme')
        count = 0
        for fn in os.listdir(theme_dir):
            if fn.startswith('theme') and fn.endswith('.xml'):
                with open(os.path.join(theme_dir, fn), 'w', encoding='utf-8') as f:
                    f.write(theme_xml)
                count += 1
        if os.path.exists(output_pptx):
            os.remove(output_pptx)
        with zipfile.ZipFile(output_pptx, 'w', zipfile.ZIP_DEFLATED) as z:
            for root, _, files in os.walk(work_dir):
                for file in files:
                    full = os.path.join(root, file)
                    rel = os.path.relpath(full, work_dir)
                    z.write(full, rel)
        return count
    finally:
        shutil.rmtree(work_dir)


def fix_theme_fonts(prs, major_font='宋体-简', minor_font='Microsoft YaHei'):
    """向后兼容接口，内部调用 apply_orchisky_theme"""
    return apply_orchisky_theme(prs)
