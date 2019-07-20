from flask import render_template, Blueprint, jsonify, request

main = Blueprint('main', __name__)

@main.route("/", methods=['GET'])
def return_index():
    return render_template('index.html')

@main.route("/xuchen")
def return_xuchen():
    return 'xuchen'

@main.route("/upload/image", methods=['POST'])
def upload_image():
    files = request.files['image']
    print(files)
    return jsonify({"message": "Success!"})