import random

from flask import Flask, request, jsonify
import jwt
import os

app = Flask(__name__)

APP_HOST = os.getenv('APP_HOST', '0.0.0.0')
APP_PORT = os.getenv('APP_PORT', '8000')


flags_iso_2 = ["AF", "AX", "AL", "DZ", "AS", "AD", "AO", "AI", "AQ", "AG", "AR", "AM", "AW", "AU", "AT", "AZ", "BS",
               "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BV", "BR", "IO", "BN", "BG", "BF",
               "KH", "CM", "CA", "CV", "KY", "CF", "TD", "CL", "CN", "CX", "CC", "CO", "KM", "CG", "CD", "CK", "CR",
               "HR", "CU", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "GQ", "ER", "EE", "ET", "FK", "FO",
               "FI", "FR", "GF", "PF", "TF", "GA", "GM", "GE", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT",
               "GN", "GW", "GY", "HT", "HM", "VA", "HN", "HK", "HU", "IS", "IN", "ID", "IR", "IQ", "IE", "IM", "IL",
               "JM", "JP", "JE", "JO", "KZ", "KE", "KI", "KR", "KP", "KW", "KG", "LA", "LV", "LB", "LS", "LR", "LY",
               "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM",
               "MC", "MN", "ME", "MS", "MA", "MZ", "MM", "NA", "NR", "NP", "NL", "AN", "NC", "NZ", "NI", "NE", "NG",
               "NF", "MP", "NO", "OM", "PK", "PW", "PS", "PA", "PG", "PY", "PE", "PH", "PN", "PL", "PT", "PR", "QA",
               "RO", "RU", "RW", "BL", "SH", "KN", "LC", "MF", "PM", "VC", "WS", "SM", "ST", "SA", "SN", "RS", "SC",
               "SG", "SK", "SI", "SB", "SO", "ZA", "GS", "ES", "LK", "SD", "SR", "SJ", "SZ", "SE", "CH", "SY", "TW",
               "TZ", "TH", "TL", "TG", "TK", "TO", "TT", "TN", "TR", "TM", "TC", "TV", "UG", "UA", "AE", "GB", "US",
               "UY", "UZ", "VU", "VE", "VN", "VG", "VI", "WF", "EH", "YE", "ZM", "ZW",
               ]

with open('flag.txt') as fp:
    FLAG = fp.read()


def create_token(user='guest'):
    return jwt.encode({'user': user}, app.config['SECRET_KEY'], "HS256")


def decode_token(token_):
    return jwt.decode(token_, app.config['SECRET_KEY'], algorithms=["HS256"])


@app.route('/flag', methods=['GET'])
def flag():
    token_ = request.args.get('token')
    if not token_:
        return jsonify({'message': 'You need to provide a token'})

    data = decode_token(token_)
    user = data.get('user')
    if user == 'admin':
        return jsonify({'message': FLAG})

    return jsonify({'message': f'https://countryflagsapi.com/png/{random.choice(flags_iso_2)}'})


@app.route('/token', methods=['GET'])
def token():
    return jsonify({'token': create_token()})


if __name__ == '__main__':
    app.secret_key = str(os.urandom)
    app.run(host=APP_HOST, port=APP_PORT, debug=False)
