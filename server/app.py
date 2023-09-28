#!/usr/bin/env python3

from flask import Flask, request, jsonify, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with your actual secret key

@app.route('/articles/<int:id>', methods=['GET'])
def view_article(id):
    # Initialize 'page_views' in the session if it doesn't exist
    session['page_views'] = session.get('page_views', 0)

    # Increment the page_views for this user
    session['page_views'] += 1

    # Check if the user has exceeded the maximum page view limit (3 views)
    if session['page_views'] <= 3:
        # Replace this with actual article retrieval logic
        article_data = {
            'id': id,
            'title': 'Sample Article',
            'content': 'This is the content of the article.'
        }
        return jsonify(article_data)
    else:
        # User has exceeded the maximum page view limit
        response = {'message': 'Maximum pageview limit reached'}
        return jsonify(response), 401  # Unauthorized status code

@app.route('/clear', methods=['POST'])
def clear_session():
    session.clear()  # Clear the user's session
    return jsonify({'message': 'Session cleared'})

if __name__ == '__main__':
    app.run(debug=True)
