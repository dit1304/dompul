from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def cek_kuota(msisdn):
    """Fungsi untuk mengambil data kuota dari API"""
    url = f"https://apigw.kmsp-store.com/sidompul/v3/cek_kuota?msisdn={msisdn}&isJSON=true"
    headers = {
        "Authorization": "Basic c2lkb21wdWxhcGk6YXBpZ3drbXNw",  # Basic Auth
        "X-API-Key": "4352ff7d-f4e6-48c6-89dd-21c811621b1c",  # API Key
        "X-App-Version": "3.0.0",
        "User-Agent": "Mozilla/5.0"
    }
    
    response = requests.get(url, headers=headers)
    return response.json()

@app.route('/cek_kuota', methods=['GET'])
def api_cek_kuota():
    msisdn = request.args.get('msisdn')
    if not msisdn:
        return jsonify({"error": "msisdn parameter is required"}), 400
    data = cek_kuota(msisdn)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

