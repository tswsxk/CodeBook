# coding: utf-8
# 2019/9/18 @ tongshiwei

import re
from docx import Document

VARIABLE = re.compile(r"(?<=\$)([\w\d_]+)")


def invitation(name, country, email, address, target):
    doc = Document("template.docx")
    for paragraph in doc.paragraphs:
        if '$' in paragraph.text:
            text = paragraph.text
            match = VARIABLE.search(text)
            if match:
                paragraph.text = text[:match.start()-1]
                paragraph.text += eval(text[match.start():match.end()].lower())
                paragraph.text += text[match.end():]
    doc.save(target)


if __name__ == '__main__':
    invitation(
        "Shiwei Tong",
        "China",
        "tongsw@mail.ustc.edu.cn",
        "404",
        "tongsw.docx"
    )
    invitation(
        "Yu Yin",
        "China",
        "yxonic@gmail.com",
        "212",
        "yxonic.docx"
    )
