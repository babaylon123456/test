from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# 模拟数据库存储兑换码和对应信息
redemption_data = {
    "ABC123": "test111",
    "DEF456": "test222",
    # 添加更多数据...
}

@app.route('/redemption', methods=['GET'])
def get_redemption_info():
    code = request.args.get('code')
    if code in redemption_data:
        info = redemption_data[code]
        return jsonify({'info': info})
    else:
        return jsonify({'error': 'Invalid redemption code'}), 404

if __name__ == '__main__':
    app.run(debug=False)

