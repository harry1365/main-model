import os
from flask import Flask, render_template, request, redirect, url_for, session, jsonify, send_file
import io

app = Flask(__name__)
app.secret_key = os.environ.get('SESSION_SECRET', 'chimera-dev-secret-key')

ADMIN_USER = 'admin'
ADMIN_PASS = 'chimera123'

users = [
    {'id': 1, 'name': 'Agent Shadow', 'device_id': 'DEV-7X92-ALPHA', 'status': 'Pending', 'risk_level': 'Low'},
    {'id': 2, 'name': 'Ghost Runner', 'device_id': 'DEV-3K41-BRAVO', 'status': 'Pending', 'risk_level': 'Medium'},
    {'id': 3, 'name': 'Cipher Wolf', 'device_id': 'DEV-9M88-DELTA', 'status': 'Active', 'risk_level': 'Low'},
    {'id': 4, 'name': 'Phoenix Eye', 'device_id': 'DEV-2F15-ECHO', 'status': 'Denied', 'risk_level': 'High'},
    {'id': 5, 'name': 'Raven Strike', 'device_id': 'DEV-6L73-FOXTROT', 'status': 'Pending', 'risk_level': 'Medium'},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    officer_id = request.form.get('officer_id')
    password = request.form.get('password')
    
    if officer_id == ADMIN_USER and password == ADMIN_PASS:
        session['logged_in'] = True
        session['user'] = officer_id
        return redirect(url_for('admin'))
    else:
        return render_template('index.html', error='Invalid credentials. Access denied.')

@app.route('/admin')
def admin():
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    return render_template('dashboard.html', users=users)

@app.route('/api/approve/<int:user_id>', methods=['POST'])
def approve_user(user_id):
    if not session.get('logged_in'):
        return jsonify({'success': False, 'message': 'Unauthorized'}), 401
    for user in users:
        if user['id'] == user_id:
            user['status'] = 'Active'
            return jsonify({'success': True, 'message': f"User {user['name']} approved", 'status': 'Active'})
    return jsonify({'success': False, 'message': 'User not found'}), 404

@app.route('/api/deny/<int:user_id>', methods=['POST'])
def deny_user(user_id):
    if not session.get('logged_in'):
        return jsonify({'success': False, 'message': 'Unauthorized'}), 401
    for user in users:
        if user['id'] == user_id:
            user['status'] = 'Denied'
            return jsonify({'success': True, 'message': f"User {user['name']} denied", 'status': 'Denied'})
    return jsonify({'success': False, 'message': 'User not found'}), 404

@app.route('/download/chimera')
def download_chimera():
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    placeholder_content = b'CHIMERA_SECURE_PACKAGE_v1.0\nThis is a placeholder APK file for demonstration purposes.\nIn production, this would be the actual application binary.'
    return send_file(
        io.BytesIO(placeholder_content),
        mimetype='application/vnd.android.package-archive',
        as_attachment=True,
        download_name='Chimera_v1.0.apk'
    )

@app.route('/portal')
def portal():
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    return render_template('portal.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
