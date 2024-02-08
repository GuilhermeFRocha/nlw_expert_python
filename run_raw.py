from flask import Flask, request, jsonify
from barcode import Code128
from barcode.writer import ImageWriter

app = Flask(__name__)

@app.route('/create_tag' , methods=["POST"])
def create_tag():
  body = request.json
  product_code = body.get('product_code')

  tag = Code128(product_code, writer=ImageWriter())
  path__from__tag = f'{tag}'
  tag.save(path__from__tag)
  return jsonify({"tag_path": path__from__tag})

if __name__ == '__main__':
        app.run(host='0.0.0.0', port = 3000)
