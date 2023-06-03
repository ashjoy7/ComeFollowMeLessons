from flask import Flask, request, jsonify

app = Flask(__name__)
comments = []

@app.route('/comments', methods=['POST'])
def add_comment():
    comment = request.json['comment']
    comments.append(comment)
    return jsonify({'message': 'Comment added successfully'})

@app.route('/comments', methods=['GET'])
def get_comments():
    return jsonify(comments)

if __name__ == '__main__':
    app.run()
