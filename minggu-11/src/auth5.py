@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))