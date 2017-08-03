from routes import *
from read_xls import excel_table_byindex as etb
import os
import flask
from flask import make_response

main = Blueprint('uploads', __name__)

Model = User


def file_name(filename):
    count = len(os.listdir(os.path.dirname(os.path.realpath(__file__))[:-6] + 'static/img/')) + 1
    name = str(count) + '.' + filename.split('.')[-1]
    print(name)
    return name


@main.route('/add', methods=['POST'])
@login_required
def add():
    # 通过 request.files 访问通过表单上传的文件
    # uploaded 是表单上传时候的文件名（name="uploaded")
    f = request.files.get('uploaded')
    print('request', request)
    print('upload, ', request.files, type(request.files))
    print('f', f)
    if f:
        filename = f.filename
        ext = filename.split('.')[-1].lower()
        valid_filetypes = ('png', 'jpg', 'jpeg', 'gif', 'apng', 'xls')
        if ext in valid_filetypes:
            filename = file_name(filename)
            print('filename, ', filename)
            path = os.path.dirname(os.path.realpath(__file__))[:-6] + 'static/img/' + filename
            print(path)
            print(os.getcwd())
            f.save(path)
            # 保存文件路径
            u = current_user()
            u.person_file = path
            u.save()
            # return redirect(url_for('user.profile'))
            # return render_template('user/person_profile.html')
            return redirect(url_for('user.person_profile'))

        else:
            return '<h1>文件类型或大小不对</h1>'
    else:
        return '<h1>没有上传</h1>'


@main.route('/<filename>')
def read(filename):
    # 这个函数直接返回文件的响应
    return flask.send_from_directory(os.path.dirname(os.path.realpath(__file__))[:-6] + 'static/img/', filename)


@main.route('/read_file')
def read_file():
    u = current_user()
    l = etb(u.person_file)
    print('l', l)
    # # k = list(etb(u.person_file)[0].keys())
    # d = {
    #     str(u.id): l
    # }
    import json
    d = json.dumps(l)
    return make_response(d)
