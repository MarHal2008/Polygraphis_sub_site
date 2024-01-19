from flask import Flask, render_template, request

app = Flask(__name__)

subs = {
    'HE': 'AL',
    'LL': 'DR',
    'OW': 'PO',
    'OR': 'MI',
    'LD': 'OD',
    'HI': 'JU',
    'IN': 'VW',
    'TO': 'ZX',
    'BE': 'YT',
    'OF': 'QP',
    'AN': 'RS',
    'RE': 'FG',
    'ON': 'HJ',
    'AT': 'KL',
    'EN': 'ZM',
    'ND': 'BN',
    'GO': 'CV',
    'ME': 'DW',
    'IS': 'EX',
    'BY': 'TY',
    'IT': 'UI',
    'SO': 'VJ',
    'WE': 'WK',
    'AR': 'XL',
    'CO': 'YM',
    'NO': 'ZN',
    'AS': 'OP',
    'TA': 'QR',
    'TE': 'ST',
    'IO': 'UV',
    'DE': 'WX',
    'VE': 'YZ',
    'RI': 'AB',
    'RO': 'CD',
    'NU': 'EF',
    'MA': 'GH',
    'FO': 'IJ',
    'ES': 'KL',
    'UN': 'MN',
    'DO': 'OP',
    'UR': 'QR',
    'PR': 'TS',
    'BO': 'UV',
    'TR': 'WX',
    'SU': 'YZ',
    'CL': 'AB',
    'BL': 'CD',
    'WI': 'EF',
    'SH': 'GH',
    'PI': 'IJ',
    'ST': 'KL',
    'CH': 'MN',
    'TH': 'OP',
    'SP': 'QR',
    'SL': 'TS',
    'SC': 'UV',
    'PL': 'WX',
    'KI': 'YZ',
    'SI': 'AB',
    'TI': 'CD',
    'BI': 'EF',
    'DI': 'GH',
    'FI': 'IJ',
    'LI': 'KL',
    'MI': 'MN',
    'NI': 'OP',
    'QU': 'ST',
    'RU': 'TS',
    'DU': 'UV',
    'TU': 'WX',
    'CU': 'YZ',
    'BU': 'CD',
    'FU': 'EF',
    'GU': 'GH',
    'HU': 'IJ',
    'JU': 'KL',
    'KU': 'MN',
    'LU': 'OP',
    'MU': 'QR',
    'PU': 'TS',
    'UU': 'AB',
    'VU': 'CD',
    'WU': 'EF',
    'XU': 'GH',
    'YU': 'IJ',
    'ZU': 'KL',
    'AU': 'MN',
    'EU': 'OP',
    'OU': 'QR',
    'IU': 'ST'
} # the substitutions


def sub_encryption(text, subs):
    result = ''
    for i in range(0, len(text) - 1, 2):
        if text[i:i + 2] in subs:
            result += subs[text[i:i + 2]]
        else:
            result += text[i:i + 2]
    if len(text) % 2 == 0 and text[-2:] in subs:
        result += subs[text[-2:]]
    elif len(text) % 2 == 0:
        result += text[-2:]
    return result


def sub_decryption(text, subs):
    inverse_subs = {v: k for k, v in subs.items()}
    result = ''
    for i in range(0, len(text), 2):
        if text[i:i + 2] in inverse_subs:
            result += inverse_subs[text[i:i + 2]]
        elif text[i] in inverse_subs:
            result += inverse_subs[text[i]]
        else:
            result += text[i]
    if len(text) % 2 != 0 and text[-1] in inverse_subs:
        result += inverse_subs[text[-1]]
    elif len(text) % 2 != 0:
        result += text[-1]
    return result


@app.route("/encrypt")
def encrypt():
    return "Type in the word to encrypt" + render_template('PSenc-form.html')


@app.route('/encrypt', methods=['POST'])
def encrypt_post():
    text = request.form['word_to_enc']
    enc_text = text.upper()
    encrypted = sub_encryption(enc_text, subs)
    return encrypted


@app.route("/decrypt")
def decrypt():
    return "Type in the word to decrypt" + render_template('PSdec-form.html')


@app.route('/decrypt', methods=['POST'])
def decrypt_post():
    text = request.form['word_to_dec']
    dec_text = text.upper()
    decrypted = sub_decryption(dec_text, subs)
    return decrypted


if __name__ == "__main__":
    app.run("localhost", 8081)
