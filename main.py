from packages.setup import setup

setup()


import numpy as np
import math
from cipher.caesar import Caesar
from cipher.reverse import Reverse
from cipher.subsition import Subsition
from cipher.transposition import Transposition
from cipher.affine import Affine
from cipher.hill import Hill
from cipher.vigenere import Vigenere
from cipher.rot13 import Rot13
from cipher.b64 import Base64
from cipher.xor import Xor
from cipher.multiply import Multiply
from cipher.des import Des
from cipher.elgamal import Elgamalx
from cipher.rsa import RSAX

caesar = Caesar()
reverse = Reverse()
subsition = Subsition()
transposition = Transposition()
affine = Affine()
hill = Hill()
vignere = Vigenere()
rot13 = Rot13()
base64 = Base64()
xor = Xor()
multiply = Multiply()
des = Des()
elgamal = Elgamalx()
rsa = RSAX()


import PySimpleGUI as sg

sg.theme("DarkBlue12")
FONT = "Roboto"
FONT_SIZE = 15
BUTTON_WIDTH = 18
BUTTON_HEIGHT = 1

menu_layout = [
    [
        sg.Push(),
        sg.Text(
            "Hệ Mã Cổ Điển",
            font=(FONT, FONT_SIZE + 5),
            size=(BUTTON_WIDTH + 5, BUTTON_HEIGHT),
            justification="center",
        ),
        sg.Push(),
    ],
    [
        sg.Push(),
        sg.Button(
            "Mã Đảo Ngược", font=(FONT, FONT_SIZE), size=(BUTTON_WIDTH, BUTTON_HEIGHT)
        ),
        sg.Button(
            "Mã Caesar", font=(FONT, FONT_SIZE), size=(BUTTON_WIDTH, BUTTON_HEIGHT)
        ),
        sg.Button(
            "Mã Đổi Chỗ", font=(FONT, FONT_SIZE), size=(BUTTON_WIDTH, BUTTON_HEIGHT)
        ),
        sg.Button(
            "Mã Thay Thế Đơn",
            font=(FONT, FONT_SIZE),
            size=(BUTTON_WIDTH, BUTTON_HEIGHT),
        ),
        sg.Button(
            "Mã Affine", font=(FONT, FONT_SIZE), size=(BUTTON_WIDTH, BUTTON_HEIGHT)
        ),
        sg.Button(
            "Mã Vigenere", font=(FONT, FONT_SIZE), size=(BUTTON_WIDTH, BUTTON_HEIGHT)
        ),
        sg.Push(),
    ],
    [sg.VPush()],
    [
        sg.Push(),
        sg.Button(
            "Mã Hill", font=(FONT, FONT_SIZE), size=(BUTTON_WIDTH, BUTTON_HEIGHT)
        ),
        sg.Button(
            "Mã ROT13", font=(FONT, FONT_SIZE), size=(BUTTON_WIDTH, BUTTON_HEIGHT)
        ),
        sg.Button(
            "Mã Base64", font=(FONT, FONT_SIZE), size=(BUTTON_WIDTH, BUTTON_HEIGHT)
        ),
        sg.Button("Mã XOR", font=(FONT, FONT_SIZE), size=(BUTTON_WIDTH, BUTTON_HEIGHT)),
        sg.Button(
            "Mã Nhân", font=(FONT, FONT_SIZE), size=(BUTTON_WIDTH, BUTTON_HEIGHT)
        ),
        sg.Push(),
    ],
    [
        sg.Push(),
        sg.Text(
            "Hệ Mã Khối",
            font=(FONT, FONT_SIZE + 5),
            size=(BUTTON_WIDTH + 5, BUTTON_HEIGHT),
            justification="center",
        ),
        sg.Push(),
    ],
    [
        sg.Push(),
        sg.Button("Mã DES", font=(FONT, FONT_SIZE), size=(BUTTON_WIDTH, BUTTON_HEIGHT)),
        sg.Push(),
    ],
    [
        sg.Push(),
        sg.Text(
            "Hệ Mã Công Khai",
            font=(FONT, FONT_SIZE + 5),
            size=(BUTTON_WIDTH + 5, BUTTON_HEIGHT),
            justification="center",
        ),
        sg.Push(),
    ],
    [
        sg.Push(),
        sg.Button("Mã RSA", font=(FONT, FONT_SIZE), size=(BUTTON_WIDTH, BUTTON_HEIGHT)),
        sg.Button(
            "Mã Elgamal", font=(FONT, FONT_SIZE), size=(BUTTON_WIDTH, BUTTON_HEIGHT)
        ),
        sg.Push(),
    ],
    [
        sg.Push(),
        sg.Text(
            "Lưu Ý: Hãy rê chuột vào đối tượng có dấu * để xem thêm thông tin!",
            font=(FONT, FONT_SIZE),
            size=(BUTTON_WIDTH + 40, BUTTON_HEIGHT),
            justification="center",
            text_color="yellow",
        ),
        sg.Push(),
    ],
]

buttons_layout = [
    [
        sg.Push(),
        sg.Button(
            "Mã Hóa", font=(FONT, FONT_SIZE - 2), size=(BUTTON_WIDTH, BUTTON_HEIGHT)
        ),
        sg.Button(
            "Giải Mã", font=(FONT, FONT_SIZE - 2), size=(BUTTON_WIDTH, BUTTON_HEIGHT)
        ),
        sg.Button(
            "Quay lại", font=(FONT, FONT_SIZE - 2), size=(BUTTON_WIDTH, BUTTON_HEIGHT)
        ),
        sg.Push(),
    ]
]

input_layout = [
    [
        sg.Push(),
        sg.Text(
            "",
            font=(FONT, FONT_SIZE + 5),
            size=(BUTTON_WIDTH + 5, BUTTON_HEIGHT),
            justification="center",
            key="TITLE",
        ),
        sg.Push(),
    ],
    [
        sg.Text(
            "Đầu Vào: ",
            font=(FONT, FONT_SIZE),
            size=(BUTTON_WIDTH, BUTTON_HEIGHT),
        ),
        sg.InputText(
            font=(FONT, FONT_SIZE - 2), size=(BUTTON_WIDTH + 40, BUTTON_HEIGHT)
        ),
    ],
]

output_layout = [
    [
        sg.Text(
            "Kết Quả: ",
            font=(FONT, FONT_SIZE),
            size=(BUTTON_WIDTH, BUTTON_HEIGHT),
        ),
        sg.InputText(
            readonly=True,
            font=(FONT, FONT_SIZE - 2),
            text_color="black",
            key="RESULT",
            size=(BUTTON_WIDTH + 40, BUTTON_HEIGHT),
        ),
    ],
    [
        sg.Push(),
        sg.Text(
            "",
            font=(FONT, FONT_SIZE - 2),
            size=(BUTTON_WIDTH + 40, BUTTON_HEIGHT),
            justification="center",
            key="ERROR",
            text_color="orange",
        ),
        sg.Push(),
    ],
]

caesar_layout = [
    [
        sg.Text(
            "Khóa (Số Nguyên):* ",
            font=(FONT, FONT_SIZE),
            size=(BUTTON_WIDTH, BUTTON_HEIGHT),
            tooltip="Khóa là một số nguyên dương hoặc âm.\nVD: 3, 5, -3\nNếu giải mã đầu vào mà không nhập khóa, chương trình sẽ tự cố gắng giải mã nó.",
        ),
        sg.InputText(
            font=(FONT, FONT_SIZE - 2),
            size=(BUTTON_WIDTH + 40, BUTTON_HEIGHT),
            key="CAESAR_KEY",
        ),
    ]
]

transposition_layout = [
    [
        sg.Text(
            "Khóa (Chuỗi kí tự):* ",
            font=(FONT, FONT_SIZE),
            size=(BUTTON_WIDTH, BUTTON_HEIGHT),
            tooltip="Khóa là một chuỗi kí tự số hoặc ký tự trong bảng chữ cái (ngẫu nhiên hoặc là một từ khóa).\nVD: ciphzer, abcde, 13254.",
        ),
        sg.InputText(
            font=(FONT, FONT_SIZE - 2),
            size=(BUTTON_WIDTH + 40, BUTTON_HEIGHT),
            key="TRANSPOSITION_KEY",
        ),
    ]
]

subsition_layout = [
    [
        sg.Text(
            "Khóa (Bảng Chữ):* ",
            font=(FONT, FONT_SIZE),
            size=(BUTTON_WIDTH, BUTTON_HEIGHT),
            tooltip="Khóa là một bảng chữ cái thay thế đơn.\nNếu để trống và sử dụng mã hóa, hệ thống sẽ tự tạo ngẫu nhiên khóa.",
        ),
        sg.InputText(
            font=(FONT, FONT_SIZE - 2),
            size=(BUTTON_WIDTH + 40, BUTTON_HEIGHT),
            key="SUBSITION_KEY",
        ),
    ]
]

affine_layout = [
    [
        sg.Text(
            "Khóa a (Số Nguyên):* ",
            font=(FONT, FONT_SIZE),
            size=(BUTTON_WIDTH, BUTTON_HEIGHT),
            tooltip="Khóa a là một số nguyên dương.\na phải là số nguyên tố cùng nhau với 26.\nVD: 5, 7, 11",
        ),
        sg.InputText(
            font=(FONT, FONT_SIZE - 2),
            size=(BUTTON_WIDTH + 40, BUTTON_HEIGHT),
            key="AFFINE_KEY_A",
        ),
    ],
    [
        sg.Text(
            "Khóa b (Số Nguyên):* ",
            font=(FONT, FONT_SIZE),
            size=(BUTTON_WIDTH, BUTTON_HEIGHT),
            tooltip="Khóa b là một số nguyên dương.\nVD: 4, 10, 2",
        ),
        sg.InputText(
            font=(FONT, FONT_SIZE - 2),
            size=(BUTTON_WIDTH + 40, BUTTON_HEIGHT),
            key="AFFINE_KEY_B",
        ),
    ],
]

vigenere_layout = [
    [
        sg.Text(
            "Khóa (Chuỗi Ký Tự):* ",
            font=(FONT, FONT_SIZE),
            size=(BUTTON_WIDTH, BUTTON_HEIGHT),
            tooltip="Khóa là một chuỗi kí tự trong bảng chữ cái (ngẫu nhiên hoặc là một từ khóa).\nVD: cipher, abcde.",
        ),
        sg.InputText(
            font=(FONT, FONT_SIZE - 2),
            size=(BUTTON_WIDTH + 40, BUTTON_HEIGHT),
            key="VIGENERE_KEY",
        ),
    ]
]

hill_layout = [
    [
        sg.Text(
            "Ma Trận:* ",
            font=(FONT, FONT_SIZE),
            size=(BUTTON_WIDTH + 19, BUTTON_HEIGHT),
            tooltip="Khóa là một ma trận kích thước 2x2.\nSố trong ma trận phải nguyên tố cùng nhau với 26.\nVD: [[3 3],[2 5]]",
        ),
        sg.InputText(
            font=(FONT, FONT_SIZE - 2),
            size=(BUTTON_WIDTH, BUTTON_HEIGHT),
            key="HILL_00_KEY",
        ),
        sg.InputText(
            font=(FONT, FONT_SIZE - 2),
            size=(BUTTON_WIDTH, BUTTON_HEIGHT),
            key="HILL_01_KEY",
        ),
    ],
    [
        sg.Text(
            font=(FONT, FONT_SIZE),
            size=(BUTTON_WIDTH + 19, BUTTON_HEIGHT),
        ),
        sg.InputText(
            font=(FONT, FONT_SIZE - 2),
            size=(BUTTON_WIDTH, BUTTON_HEIGHT),
            key="HILL_10_KEY",
        ),
        sg.InputText(
            font=(FONT, FONT_SIZE - 2),
            size=(BUTTON_WIDTH, BUTTON_HEIGHT),
            key="HILL_11_KEY",
        ),
    ],
]

xor_layout = [
    [
        sg.Text(
            "Khóa (Chuỗi Ký Tự):* ",
            font=(FONT, FONT_SIZE),
            size=(BUTTON_WIDTH, BUTTON_HEIGHT),
            tooltip="Khóa là một chuỗi kí tự trong bảng chữ cái (ngẫu nhiên hoặc là một từ khóa).\nVD: cipher, abcde.",
        ),
        sg.InputText(
            font=(FONT, FONT_SIZE - 2),
            size=(BUTTON_WIDTH + 40, BUTTON_HEIGHT),
            key="XOR_KEY",
        ),
    ]
]

des_layout = [
    [
        sg.Text(
            "Khóa (Chuỗi Ký Tự):* ",
            font=(FONT, FONT_SIZE),
            size=(BUTTON_WIDTH, BUTTON_HEIGHT),
            tooltip="Khóa là một chuỗi 8 kí tự trong bảng chữ cái hoặc các kí tự số (ngẫu nhiên hoặc là một từ khóa).\nVD: abcdefgh, immortal, 12345678.",
        ),
        sg.InputText(
            font=(FONT, FONT_SIZE - 2),
            size=(BUTTON_WIDTH + 40, BUTTON_HEIGHT),
            key="DES_KEY",
        ),
    ]
]

multiply_layout = [
    [
        sg.Text(
            "Khóa (Số Nguyên):* ",
            font=(FONT, FONT_SIZE),
            size=(BUTTON_WIDTH, BUTTON_HEIGHT),
            tooltip="Khóa a là một số nguyên dương.\na phải là số nguyên tố cùng nhau với 26.\nVD: 5, 7, 11",
        ),
        sg.InputText(
            font=(FONT, FONT_SIZE - 2),
            size=(BUTTON_WIDTH + 40, BUTTON_HEIGHT),
            key="MULTIPLY_KEY",
        ),
    ]
]

elgamal_layout = [
    [
        sg.Text(
            "Khóa Công Khai:* ",
            font=(FONT, FONT_SIZE),
            size=(BUTTON_WIDTH, BUTTON_HEIGHT),
            tooltip="Khóa công khai là một tập tin .txt lưu giá trị p, a, y.\n Được dùng để mã hóa văn bản.",
        ),
        sg.Input(font=(FONT, FONT_SIZE), size=(BUTTON_WIDTH + 14, BUTTON_HEIGHT)),
        sg.FileBrowse(
            key="ELGAMAL_PUBKEY",
            font=(FONT, FONT_SIZE),
            size=(BUTTON_WIDTH, BUTTON_HEIGHT),
        ),
    ],
    [
        sg.Text(
            "Khóa Bí Mật:* ",
            font=(FONT, FONT_SIZE),
            size=(BUTTON_WIDTH, BUTTON_HEIGHT),
            tooltip="Khóa công khai là một tập tin .txt lưu giá trị p, x.\n Được dùng để giải mã văn bản.",
        ),
        sg.Input(font=(FONT, FONT_SIZE), size=(BUTTON_WIDTH + 14, BUTTON_HEIGHT)),
        sg.FileBrowse(
            key="ELGAMAL_PRIKEY",
            font=(FONT, FONT_SIZE),
            size=(BUTTON_WIDTH, BUTTON_HEIGHT),
        ),
    ],
    [
        sg.Push(),
        sg.Button(
            "Tạo Khóa Elgamal",
            font=(FONT, FONT_SIZE - 2),
            size=(BUTTON_WIDTH, BUTTON_HEIGHT),
        ),
        sg.Push(),
    ],
]

rsa_layout = [
    [
        sg.Text(
            "Khóa Công Khai:* ",
            font=(FONT, FONT_SIZE),
            size=(BUTTON_WIDTH, BUTTON_HEIGHT),
            tooltip="Khóa công khai là một tập tin .pem.\n Được dùng để mã hóa văn bản.",
        ),
        sg.Input(font=(FONT, FONT_SIZE), size=(BUTTON_WIDTH + 14, BUTTON_HEIGHT)),
        sg.FileBrowse(
            key="RSA_PUBKEY",
            font=(FONT, FONT_SIZE),
            size=(BUTTON_WIDTH, BUTTON_HEIGHT),
        ),
    ],
    [
        sg.Text(
            "Khóa Bí Mật:* ",
            font=(FONT, FONT_SIZE),
            size=(BUTTON_WIDTH, BUTTON_HEIGHT),
            tooltip="Khóa công khai là một tập tin .pem.\n Được dùng để giải mã văn bản.",
        ),
        sg.Input(font=(FONT, FONT_SIZE), size=(BUTTON_WIDTH + 14, BUTTON_HEIGHT)),
        sg.FileBrowse(
            key="RSA_PRIKEY",
            font=(FONT, FONT_SIZE),
            size=(BUTTON_WIDTH, BUTTON_HEIGHT),
        ),
    ],
    [
        sg.Push(),
        sg.Button(
            "Tạo Khóa RSA",
            font=(FONT, FONT_SIZE - 2),
            size=(BUTTON_WIDTH, BUTTON_HEIGHT),
        ),
        sg.Push(),
    ],
]


input_index = 0
layout = [
    [sg.VPush()],
    [
        sg.Column(menu_layout, key="MENU", visible=True, justification="center"),
        sg.Column(input_layout, key="INPUT", visible=False, justification="center"),
        sg.Column(caesar_layout, key="CAESAR", visible=False, justification="center"),
        sg.Column(
            transposition_layout,
            key="TRANSPOSITION",
            visible=False,
            justification="center",
        ),
        sg.Column(
            subsition_layout, key="SUBSITION", visible=False, justification="center"
        ),
        sg.Column(affine_layout, key="AFFINE", visible=False, justification="center"),
        sg.Column(
            vigenere_layout, key="VIGENERE", visible=False, justification="center"
        ),
        sg.Column(hill_layout, key="HILL", visible=False, justification="center"),
        sg.Column(output_layout, key="OUTPUT", visible=False, justification="center"),
        sg.Column(xor_layout, key="XOR", visible=False, justification="center"),
        sg.Column(
            multiply_layout, key="MULTIPLY", visible=False, justification="center"
        ),
        sg.Column(des_layout, key="DES", visible=False, justification="center"),
        sg.Column(elgamal_layout, key="ELGAMAL", visible=False, justification="center"),
        sg.Column(rsa_layout, key="RSA", visible=False, justification="center"),
        sg.Column(buttons_layout, key="BUTTONS", visible=False, justification="center"),
    ],
    [sg.VPush()],
]

window = sg.Window("CIPHER PROGRAM", layout, finalize=True, keep_on_top=True)
window.maximize()


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    # ---------------------------------------------------------------------------------------------------
    elif event == "Mã Đảo Ngược":
        window["MENU"].update(visible=False)
        window["INPUT"].update(visible=True)
        window["TITLE"].update("Mã Đảo Ngược")
        window["OUTPUT"].update(visible=True)
        window["BUTTONS"].update(visible=True)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "Quay lại":
                window["MENU"].update(visible=True)
                window["INPUT"].update(visible=False)
                window["OUTPUT"].update(visible=False)
                window["BUTTONS"].update(visible=False)
                window["RESULT"].update("")

                break
            elif event == "Mã Hóa":
                result = reverse.encrypt(values[input_index])

                window["RESULT"].update(f"{result}")
            elif event == "Giải Mã":
                result = reverse.decrypt(values[input_index])

                window["RESULT"].update(f"{result}")
    # ---------------------------------------------------------------------------------------------------
    elif event == "Mã Caesar":
        window["MENU"].update(visible=False)
        window["INPUT"].update(visible=True)
        window["TITLE"].update("Mã Caesar")
        window["CAESAR"].update(visible=True)
        window["OUTPUT"].update(visible=True)
        window["BUTTONS"].update(visible=True)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "Quay lại":
                window["MENU"].update(visible=True)
                window["INPUT"].update(visible=False)
                window["CAESAR"].update(visible=False)
                window["OUTPUT"].update(visible=False)
                window["BUTTONS"].update(visible=False)
                window["RESULT"].update("")
                window["ERROR"].update("")
                break
            elif event == "Mã Hóa":
                if values["CAESAR_KEY"].isnumeric():
                    result = caesar.encrypt(
                        values[input_index], int(values["CAESAR_KEY"])
                    )
                    window["ERROR"].update("")
                    window["RESULT"].update(f"{result}")
                else:
                    window["ERROR"].update("Lỗi: Khóa phải là một số nguyên!")
                    window["RESULT"].update("")

            elif event == "Giải Mã":
                if values["CAESAR_KEY"].isnumeric():
                    result = caesar.decrypt(
                        values[input_index], int(values["CAESAR_KEY"])
                    )
                    window["ERROR"].update("")
                    window["RESULT"].update(f"{result}")
                elif len(values["CAESAR_KEY"]) == 0:
                    k = caesar.break_caesar(values[input_index])[1]
                    window["CAESAR_KEY"].update(k)
                    result = caesar.decrypt(values[input_index], k)
                    window["RESULT"].update(f"{result}")
                else:
                    window["ERROR"].update("Lỗi: Khóa phải là một số nguyên!")
                    window["RESULT"].update("")
    # ---------------------------------------------------------------------------------------------------
    elif event == "Mã Đổi Chỗ":
        window["MENU"].update(visible=False)
        window["INPUT"].update(visible=True)
        window["TITLE"].update("Mã Đổi Chỗ")
        window["TRANSPOSITION"].update(visible=True)
        window["OUTPUT"].update(visible=True)
        window["BUTTONS"].update(visible=True)
        window["RESULT"].update("")
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "Quay lại":
                window["MENU"].update(visible=True)
                window["INPUT"].update(visible=False)
                window["TRANSPOSITION"].update(visible=False)
                window["OUTPUT"].update(visible=False)
                window["BUTTONS"].update(visible=False)
                window["RESULT"].update("")
                window["ERROR"].update("")
                break
            elif event == "Mã Hóa":
                if (
                    len(values[input_index]) != 0
                    and len(values["TRANSPOSITION_KEY"]) != 0
                ):
                    result = transposition.encrypt(
                        values[input_index], values["TRANSPOSITION_KEY"]
                    )
                    window["RESULT"].update(f"{result}")
                    window["ERROR"].update("")
                else:
                    window["ERROR"].update("Lỗi: Không có giá trị khóa!")
                    window["RESULT"].update("")
            elif event == "Giải Mã":
                if (
                    len(values[input_index]) != 0
                    and len(values["TRANSPOSITION_KEY"]) != 0
                ):
                    result = transposition.decrypt(
                        values[input_index], values["TRANSPOSITION_KEY"]
                    )
                    window["RESULT"].update(f"{result}")
                    window["ERROR"].update("")
                else:
                    window["ERROR"].update("Lỗi: Không có giá trị khóa!")
                    window["RESULT"].update("")
    # ---------------------------------------------------------------------------------------------------
    elif event == "Mã Thay Thế Đơn":
        window["MENU"].update(visible=False)
        window["INPUT"].update(visible=True)
        window["TITLE"].update("Mã Thay Thế Đơn")
        window["SUBSITION"].update(visible=True)
        window["OUTPUT"].update(visible=True)
        window["BUTTONS"].update(visible=True)
        window["RESULT"].update("")
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "Quay lại":
                window["MENU"].update(visible=True)
                window["INPUT"].update(visible=False)
                window["SUBSITION"].update(visible=False)
                window["OUTPUT"].update(visible=False)
                window["BUTTONS"].update(visible=False)
                window["RESULT"].update("")
                window["ERROR"].update("")
                break
            elif event == "Mã Hóa":
                if len(values["SUBSITION_KEY"]) != 26:
                    key = subsition.getRandomKey()
                    window["SUBSITION_KEY"].update(key)
                else:
                    key = values["SUBSITION_KEY"]
                result = subsition.encrypt(values[input_index], key)

                window["RESULT"].update(f"{result}")
            elif event == "Giải Mã":
                if len(values["SUBSITION_KEY"]) == 26:
                    result = subsition.decrypt(
                        values[input_index], values["SUBSITION_KEY"]
                    )
                    window["RESULT"].update(f"{result}")
                    window["ERROR"].update("")
                else:
                    window["ERROR"].update("Lỗi: Không có bảng chữ để giải mã!")
                    window["RESULT"].update("")

    # ---------------------------------------------------------------------------------------------------
    elif event == "Mã Affine":
        window["MENU"].update(visible=False)
        window["INPUT"].update(visible=True)
        window["TITLE"].update("Mã Affine")
        window["AFFINE"].update(visible=True)
        window["OUTPUT"].update(visible=True)
        window["BUTTONS"].update(visible=True)
        window["RESULT"].update("")
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "Quay lại":
                window["MENU"].update(visible=True)
                window["INPUT"].update(visible=False)
                window["AFFINE"].update(visible=False)
                window["OUTPUT"].update(visible=False)
                window["BUTTONS"].update(visible=False)
                window["RESULT"].update("")
                window["ERROR"].update("")
                break
            elif event == "Mã Hóa":
                if (
                    values["AFFINE_KEY_A"].isnumeric()
                    and values["AFFINE_KEY_B"].isnumeric()
                    and math.gcd(int(values["AFFINE_KEY_A"]), 26) == 1
                ):
                    a = int(values["AFFINE_KEY_A"])
                    b = int(values["AFFINE_KEY_B"])
                    affine.key = (a, b, affine.mode_inverse(int(a), 26))
                    result = affine.encrypt(values[input_index])
                    window["RESULT"].update(f"{result}")
                    window["ERROR"].update("")
                else:
                    window["ERROR"].update(
                        "Lỗi: a và b phải là số nguyên, a phải nguyên tố cùng nhau với 26!"
                    )
                    window["RESULT"].update("")
            elif event == "Giải Mã":
                if (
                    values["AFFINE_KEY_A"].isnumeric()
                    and values["AFFINE_KEY_B"].isnumeric()
                    and math.gcd(int(values["AFFINE_KEY_A"]), 26) == 1
                ):
                    a = int(values["AFFINE_KEY_A"])
                    b = int(values["AFFINE_KEY_B"])
                    affine.key = (a, b, affine.mode_inverse(int(a), 26))
                    result = affine.decrypt(values[input_index])
                    window["RESULT"].update(f"{result}")
                    window["ERROR"].update("")
                else:
                    window["ERROR"].update(
                        "Lỗi: a và b phải là số nguyên, a phải nguyên tố cùng nhau với 26!"
                    )
                    window["RESULT"].update("")
    # ---------------------------------------------------------------------------------------------------
    elif event == "Mã Vigenere":
        window["MENU"].update(visible=False)
        window["INPUT"].update(visible=True)
        window["TITLE"].update("Mã Vigenere")
        window["VIGENERE"].update(visible=True)
        window["OUTPUT"].update(visible=True)
        window["BUTTONS"].update(visible=True)
        window["RESULT"].update("")
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "Quay lại":
                window["MENU"].update(visible=True)
                window["INPUT"].update(visible=False)
                window["VIGENERE"].update(visible=False)
                window["OUTPUT"].update(visible=False)
                window["BUTTONS"].update(visible=False)
                window["RESULT"].update("")
                window["ERROR"].update("")
                break
            elif event == "Mã Hóa":
                if values["VIGENERE_KEY"].isalpha():
                    vignere.k = values["VIGENERE_KEY"]
                    result = vignere.encrypt(values[input_index])
                    window["RESULT"].update(f"{result}")
                    window["ERROR"].update("")
                else:
                    window["ERROR"].update(
                        "Lỗi: Khóa phải là chuỗi các kí tự trong bảng chữ cái!"
                    )
                    window["RESULT"].update("")
            elif event == "Giải Mã":
                if values["VIGENERE_KEY"].isalpha():
                    vignere.k = values["VIGENERE_KEY"]
                    result = vignere.decrypt(values[input_index])
                    window["RESULT"].update(f"{result}")
                    window["ERROR"].update("")
                else:
                    window["ERROR"].update(
                        "Lỗi: Khóa phải là chuỗi các kí tự trong bảng chữ cái!"
                    )
                    window["RESULT"].update("")
    # ---------------------------------------------------------------------------------------------------
    elif event == "Mã ROT13":
        window["MENU"].update(visible=False)
        window["INPUT"].update(visible=True)
        window["TITLE"].update("Mã ROT13")
        window["OUTPUT"].update(visible=True)
        window["BUTTONS"].update(visible=True)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "Quay lại":
                window["MENU"].update(visible=True)
                window["INPUT"].update(visible=False)
                window["OUTPUT"].update(visible=False)
                window["BUTTONS"].update(visible=False)

                window["RESULT"].update("")
                break
            elif event == "Mã Hóa":
                result = rot13.encrypt(values[input_index], 13)

                window["RESULT"].update(f"{result}")
            elif event == "Giải Mã":
                result = rot13.decrypt(values[input_index], 13)

                window["RESULT"].update(f"{result}")
    # ---------------------------------------------------------------------------------------------------
    elif event == "Mã Base64":
        window["MENU"].update(visible=False)
        window["INPUT"].update(visible=True)
        window["TITLE"].update("Mã Base64")
        window["OUTPUT"].update(visible=True)
        window["BUTTONS"].update(visible=True)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "Quay lại":
                window["MENU"].update(visible=True)
                window["INPUT"].update(visible=False)
                window["OUTPUT"].update(visible=False)
                window["BUTTONS"].update(visible=False)
                window["RESULT"].update("")
                break
            elif event == "Mã Hóa":
                result = base64.encrypt(values[input_index])

                window["RESULT"].update(f"{result}")
            elif event == "Giải Mã":
                result = base64.decrypt(values[input_index])

                window["RESULT"].update(f"{result}")
    # ---------------------------------------------------------------------------------------------------
    elif event == "Mã Hill":
        window["MENU"].update(visible=False)
        window["INPUT"].update(visible=True)
        window["TITLE"].update("Mã Hill")
        window["HILL"].update(visible=True)
        window["OUTPUT"].update(visible=True)
        window["BUTTONS"].update(visible=True)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "Quay lại":
                window["MENU"].update(visible=True)
                window["INPUT"].update(visible=False)
                window["HILL"].update(visible=False)
                window["OUTPUT"].update(visible=False)
                window["BUTTONS"].update(visible=False)
                window["RESULT"].update("")
                window["ERROR"].update("")
                break
            elif event == "Mã Hóa":
                if (
                    values["HILL_00_KEY"].isnumeric()
                    and values["HILL_01_KEY"].isnumeric()
                    and values["HILL_10_KEY"].isnumeric()
                    and values["HILL_11_KEY"].isnumeric()
                ):
                    result = hill.encrypt(
                        values[input_index],
                        np.array(
                            [
                                [
                                    int(values["HILL_00_KEY"]),
                                    int(values["HILL_01_KEY"]),
                                ],
                                [
                                    int(values["HILL_10_KEY"]),
                                    int(values["HILL_11_KEY"]),
                                ],
                            ]
                        ),
                    )
                    window["RESULT"].update(f"{result}")
                    window["ERROR"].update("")
                else:
                    window["ERROR"].update(
                        "Lỗi: Ma trận chỉ được các số là số nguyên tố cùng nhau với 26!"
                    )
                    window["RESULT"].update("")

            elif event == "Giải Mã":
                if (
                    values["HILL_00_KEY"].isnumeric()
                    and values["HILL_01_KEY"].isnumeric()
                    and values["HILL_10_KEY"].isnumeric()
                    and values["HILL_11_KEY"].isnumeric()
                ):
                    result = hill.decrypt(
                        values[input_index],
                        np.array(
                            [
                                [
                                    int(values["HILL_00_KEY"]),
                                    int(values["HILL_01_KEY"]),
                                ],
                                [
                                    int(values["HILL_10_KEY"]),
                                    int(values["HILL_11_KEY"]),
                                ],
                            ]
                        ),
                    )
                    window["RESULT"].update(f"{result}")
                    window["ERROR"].update("")
                else:
                    window["ERROR"].update(
                        "Lỗi: Ma trận chỉ được các số là số nguyên tố cùng nhau với 26!"
                    )
                    window["RESULT"].update("")
    # ---------------------------------------------------------------------------------------------------
    elif event == "Mã XOR":
        window["MENU"].update(visible=False)
        window["INPUT"].update(visible=True)
        window["TITLE"].update("Mã XOR")
        window["XOR"].update(visible=True)
        window["OUTPUT"].update(visible=True)
        window["BUTTONS"].update(visible=True)
        window["RESULT"].update("")
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "Quay lại":
                window["MENU"].update(visible=True)
                window["INPUT"].update(visible=False)
                window["XOR"].update(visible=False)
                window["OUTPUT"].update(visible=False)
                window["BUTTONS"].update(visible=False)
                window["RESULT"].update("")
                window["ERROR"].update("")
                break
            elif event == "Mã Hóa":
                if values["XOR_KEY"].isalpha():
                    xor.k = values["XOR_KEY"]
                    result = xor.encrypt(values[input_index])
                    window["RESULT"].update(f"{result}")
                    window["ERROR"].update("")
                else:
                    window["ERROR"].update(
                        "Lỗi: Khóa phải là chuỗi các kí tự trong bảng chữ cái!"
                    )
                    window["RESULT"].update("")
            elif event == "Giải Mã":
                if values["XOR_KEY"].isalpha():
                    xor.k = values["XOR_KEY"]
                    result = xor.decrypt(values[input_index])
                    window["RESULT"].update(f"{result}")
                    window["ERROR"].update("")
                else:
                    window["ERROR"].update(
                        "Lỗi: Khóa phải là chuỗi các kí tự trong bảng chữ cái!"
                    )
                    window["RESULT"].update("")
    # ---------------------------------------------------------------------------------------------------
    elif event == "Mã Nhân":
        window["MENU"].update(visible=False)
        window["INPUT"].update(visible=True)
        window["TITLE"].update("Mã Nhân")
        window["MULTIPLY"].update(visible=True)
        window["OUTPUT"].update(visible=True)
        window["BUTTONS"].update(visible=True)
        window["RESULT"].update("")
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "Quay lại":
                window["MENU"].update(visible=True)
                window["INPUT"].update(visible=False)
                window["MULTIPLY"].update(visible=False)
                window["OUTPUT"].update(visible=False)
                window["BUTTONS"].update(visible=False)
                window["RESULT"].update("")
                window["ERROR"].update("")

                break
            elif event == "Mã Hóa":
                if (
                    values["MULTIPLY_KEY"].isnumeric()
                    and math.gcd(int(values["MULTIPLY_KEY"]), 26) == 1
                ):
                    multiply.key = int(values["MULTIPLY_KEY"])
                    result = multiply.encrypt(values[input_index])
                    window["RESULT"].update(f"{result}")
                    window["ERROR"].update("")
                else:
                    window["ERROR"].update(
                        "Lỗi: Khóa phải là một số nguyên và phải là nguyên tố cùng nhau với 26!"
                    )
                    window["RESULT"].update("")
            elif event == "Giải Mã":
                if (
                    values["MULTIPLY_KEY"].isnumeric()
                    and math.gcd(int(values["MULTIPLY_KEY"]), 26) == 1
                ):
                    multiply.key = int(values["MULTIPLY_KEY"])
                    result = multiply.decrypt(values[input_index])
                    window["RESULT"].update(f"{result}")
                    window["ERROR"].update("")
                else:
                    window["ERROR"].update(
                        "Lỗi: Khóa phải là một số nguyên và phải là nguyên tố cùng nhau với 26!"
                    )
                    window["RESULT"].update("")
    # ---------------------------------------------------------------------------------------------------
    elif event == "Mã DES":
        window["MENU"].update(visible=False)
        window["INPUT"].update(visible=True)
        window["TITLE"].update("Mã DES")
        window["DES"].update(visible=True)
        window["OUTPUT"].update(visible=True)
        window["BUTTONS"].update(visible=True)
        window["RESULT"].update("")
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "Quay lại":
                window["MENU"].update(visible=True)
                window["INPUT"].update(visible=False)
                window["DES"].update(visible=False)
                window["OUTPUT"].update(visible=False)
                window["BUTTONS"].update(visible=False)
                window["RESULT"].update("")
                window["ERROR"].update("")
                break
            elif event == "Mã Hóa":
                if len(values["DES_KEY"]) == 8:
                    try:
                        result = des.encrypt(values[input_index], values["DES_KEY"])
                        window["RESULT"].update(f"{result}")
                    except:
                        pass
                    window["ERROR"].update("")
                else:
                    window["ERROR"].update(
                        "Lỗi: Khóa phải là một chuỗi 8 kí tự trong bảng chữ cái hoặc kí tự số!"
                    )
                    window["RESULT"].update("")

            elif event == "Giải Mã":
                if len(values["DES_KEY"]) == 8:
                    try:
                        result = des.decrypt(values[input_index], values["DES_KEY"])

                        window["RESULT"].update(f"{result}")
                    except:
                        pass
                    window["ERROR"].update("")
                else:
                    window["ERROR"].update(
                        "Lỗi: Khóa phải là một chuỗi 8 kí tự trong bảng chữ cái hoặc kí tự số!"
                    )
                    window["RESULT"].update("")
    # ---------------------------------------------------------------------------------------------------
    elif event == "Mã Elgamal":
        window["MENU"].update(visible=False)
        window["INPUT"].update(visible=True)
        window["TITLE"].update("Mã Elgamal")
        window["ELGAMAL"].update(visible=True)
        window["OUTPUT"].update(visible=True)
        window["BUTTONS"].update(visible=True)
        window["RESULT"].update("")
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "Quay lại":
                window["MENU"].update(visible=True)
                window["INPUT"].update(visible=False)
                window["ELGAMAL"].update(visible=False)
                window["OUTPUT"].update(visible=False)
                window["BUTTONS"].update(visible=False)
                window["RESULT"].update("")
                window["ERROR"].update("")
                break
            elif event == "Mã Hóa":
                result = elgamal.encrypt(values[input_index], values["ELGAMAL_PUBKEY"])
                if result == "":
                    window["ERROR"].update("Lỗi: Tập tin khóa công khai không phù hợp!")
                else:
                    window["ERROR"].update("")
                window["RESULT"].update(f"{result}")
            elif event == "Giải Mã":
                result = elgamal.decrypt(values[input_index], values["ELGAMAL_PRIKEY"])
                if result == "":
                    window["ERROR"].update("Lỗi: Tập tin khóa bí mật không phù hợp!")
                else:
                    window["ERROR"].update("")
                window["RESULT"].update(f"{result}")
            elif event == "Tạo Khóa Elgamal":
                elgamal.create_keys()
                window["ERROR"].update(
                    "Hai tập tin khóa đã được lưu trong đường dẫn ./keys/elgamal "
                )
    # --------------------------------------------------------------------------------------------
    elif event == "Mã RSA":
        window["MENU"].update(visible=False)
        window["INPUT"].update(visible=True)
        window["TITLE"].update("Mã RSA")
        window["RSA"].update(visible=True)
        window["OUTPUT"].update(visible=True)
        window["BUTTONS"].update(visible=True)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "Quay lại":
                window["MENU"].update(visible=True)
                window["INPUT"].update(visible=False)
                window["RSA"].update(visible=False)
                window["OUTPUT"].update(visible=False)
                window["BUTTONS"].update(visible=False)
                window["RESULT"].update("")
                window["ERROR"].update("")
                break
            elif event == "Mã Hóa":
                result = rsa.encrypt(values[input_index], values["RSA_PUBKEY"])
                if result == "":
                    window["ERROR"].update("Lỗi: Tập tin khóa công khai không phù hợp!")
                else:
                    window["ERROR"].update("")
                window["RESULT"].update(f"{result}")
            elif event == "Giải Mã":
                result = rsa.decrypt(values[input_index], values["RSA_PRIKEY"])
                if result == "":
                    window["ERROR"].update("Lỗi: Tập tin khóa bí mật không phù hợp!")
                else:
                    window["ERROR"].update("")
                window["RESULT"].update(f"{result}")
            elif event == "Tạo Khóa RSA":
                rsa.create_keys()
                window["ERROR"].update(
                    "Hai tập tin khóa đã được lưu trong đường dẫn ./keys/rsa "
                )
window.close()
