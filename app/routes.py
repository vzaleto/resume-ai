from flask import Blueprint, request, jsonify

main = Blueprint('main', __name__)

@main.route('/api/generate-resume', methods=['POST'])
def generate_resume():
    data = request.json
    prompt = data.get('prompt', '')

    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    result = generate_resume(prompt)
    return jsonify({'result', result})