from flask import Flask, request, jsonify, render_template, redirect, send_from_directory, send_file
from flask_cors import CORS
from collections import Counter
import subprocess, os, webbrowser


app = Flask(__name__)
app.static_folder = 'static'
CORS(app)
def run_cpp_code():
    cpp_file = '/home/imeon/Project_Olympiad/Debugging/zapuskator.cpp'
    cpp_file_o = '/home/imeon/Project_Olympiad/Debugging/zapuskator'
    # try:
    #     os.remove('/home/imeon/Project_Olympiad/Debugging/' + 'tempCodeRunnerFile')
    #     os.remove('/home/imeon/Project_Olympiad/Debugging/' + 'tempCodeRunnerFile.cpp')
    #     os.remove(cpp_file_o)
    # except:
    #     pass
    compilation_result = subprocess.run(["g++", cpp_file, "-o", cpp_file_o], capture_output=True, text=True)

    if compilation_result.returncode == 0:
        execution_result = subprocess.run([cpp_file_o], capture_output=True, text=True)
        ans  = execution_result.stdout

        return ans
    else:
        return "Ошибка при выполнении запроса"
@app.route('/login', methods = ['POST'])
def login_user():
    ip_address = request.remote_addr


    login = request.form.get('login')
    password = request.form.get('password')
    file_path_l = '/home/imeon/Project_Olympiad/login_list/login_list.txt'
    login2 = ''
    with open(file_path_l, 'r') as ss:
        login2 = ss.read()
    ok = 1
    sf = ip_address + '%' + login + '%' + password
    if sf in login2:
        x = login2.index(sf) + len(sf)
        if login2[x] != '%':
            ok = 0
    if ok and sf in login2 and password != '' and login != '':
        file_path_online = '/home/imeon/Project_Olympiad/online_users/online.txt'
        with open(file_path_online, 'a') as ss:
            ss.write("\n" + ip_address + "%" + login + '%')
        return jsonify({"result":"Вы успешно вошли в свой аккаунт!"})
    elif not ok or (ip_address + "%" + login in login2 and ip_address + "%" + login + "%" + password not in login2) or password == '':
        return jsonify({"result":"Неправильный Парол"})
    else:

        return jsonify({"result":"Такой логин не существует("})

@app.route('/register', methods=['POST'])
def register_user():
    username = request.form.get('username')
    login = request.form.get('login')
    ip_address = request.remote_addr

    password = request.form.get('password')
    file_path_l = '/home/imeon/Project_Olympiad/login_list/login_list.txt'
    login2 = ''
    with open(file_path_l, 'r') as ss:
        login2 = ss.read()
    if login in login2 or login == '':
        return jsonify({"result":"Такой логин уже существует!"})

    with open(file_path_l, 'a') as ss:
        ss.write('\n' + ip_address + "%" + login + '%' + password + '%' + username)

    return jsonify({"result":"Вы успешно создали Аккаунт!"})

@app.route('/upload', methods=['POST'])
def upload_file():
    ip_address = request.remote_addr
    if 'file' not in request.files:
        return jsonify({'result': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'result': 'No selected file'})

    try:
        content = file.read().decode('utf-8')
        file_path_c = '/home/imeon/Project_Olympiad/Debugging/smart.cpp'
        with open(file_path_c, 'w') as output_file:
            output_file.write(content)
        login = ''
        with open('/home/imeon/Project_Olympiad/online_users/online.txt', 'r') as file:
            f = file.readline()
            while ip_address not in f:
                f = file.readline()
            p1 = f
        ind = p1.index('%')
        ind1 = p1.index('%', ind + 1)
        login = p1[ind + 1:ind1]
        p = run_cpp_code()
        new_text = "\nA%" + p + "\n"
        with open('/home/imeon/Project_Olympiad/logins_submit/' + login + '.txt', 'a') as file:
                file.write(new_text)
        return jsonify({'result': 'О да ты смог отправить код серверу'})

    except Exception as e:
        return jsonify({'result': 'Error', 'error_message': str(e)})

@app.route('/get_login')
def get_login():
    login2 = ''
    ip_address = request.remote_addr
    login = ''
    with open('/home/imeon/Project_Olympiad/online_users/online.txt', 'r') as file:
        login2 = file.read().strip()
    if ip_address in login2:
        ind = login2.index(ip_address)
        ind1 = login2.index('%', ind + 1)
        ind2 = login2.index('%', ind1 + 1)
        login = login2[ind1 + 1:ind2]
    return {"login":login}

@app.route('/logout')
def logout():
    ip_address = request.remote_addr
    f = ''
    p = []
    with open('/home/imeon/Project_Olympiad/online_users/online.txt', 'r') as file:
        f = file.readline()
        while f != '':
            if ip_address not in f:p += [f]
            f = file.readline()
    with open('/home/imeon/Project_Olympiad/online_users/online.txt', 'w') as file:
        file.write('')
    with open('/home/imeon/Project_Olympiad/online_users/online.txt', 'a') as file:
        for i in p:
            file.write('\n' + i)
    return 'File cleared successfully', 200
@app.route('/get_packages', methods=['GET'])
def get_packages():
    login = ''
    ip_address = request.remote_addr

    with open('/home/imeon/Project_Olympiad/online_users/online.txt', 'r') as file:
        f = file.readline()
        while ip_address not in f:
            f = file.readline()
        p1 = f
    ind = p1.index('%')
    ind1 = p1.index('%', ind + 1)
    login = p1[ind + 1:ind1]
    packages_data = []
    login += '.txt'
    with open('/home/imeon/Project_Olympiad/logins_submit/' + login, 'a+') as ss:
        ss.seek(0)
        x = ss.readline()
        for i in range(1000):
            if x != '' and x != '\n':
                ix = x.index('%')
                packages_data.append({'name':x[:ix], 'verdict':x[ix + 1:]})
            x = ss.readline()
    packages_data.reverse()
    return jsonify(packages_data)
@app.route('/get_task_description1')
def get_task_description1():
    file_path = '/home/imeon/Project_Olympiad/Tasks/Task1_description.txt'

    with open(file_path, 'r') as file:
        task_description = file.read()
    return jsonify({'taskDescription': task_description})

@app.route('/<path:image_name>')
def get_image(image_name):
    return send_from_directory('/home/imeon/Project_Olympiad/', image_name)
@app.route('/get_news')
def get_newss():
    ip_address = request.remote_addr

    file_path = '/home/imeon/Project_Olympiad/text_news/text_news.txt'
    with open(file_path, 'r',  encoding='utf-8') as ss:
        login2 = ss.readlines()
    return jsonify(*login2)
@app.route('/get_info_user')
def get_info_userr():
    ip_address = request.remote_addr

    login = ''
    with open('/home/imeon/Project_Olympiad/login_list/login_list.txt', 'r') as file:
        f = file.readline()
        while ip_address not in f:
            f = file.readline()
        p1 = f
    ind = p1.index('%')
    ind1 = p1.index('%', ind + 1)
    ind2 = p1.index('%', ind1 + 1)
    login = p1[ind + 1:ind1]
    name = p1[ind2 + 1:]
    cnt = 0
    v = Counter()
    with open('/home/imeon/Project_Olympiad/logins_submit/' + login + '.txt', 'r') as ss:
        ss.seek(0)
        x = ss.readline()
        for i in range(1000):
            if x != '' and x != '\n':
                ix = x.index('%')
                #packages_data.append({'name':x[:ix], 'verdict':x[ix + 1:]})

                if v[x[:ix]] == 0 and x[ix + 1:] == 'Ok\n':
                    cnt += 1
                    v[x[:ix]] = 1
            x = ss.readline()
    return {'name':name, "login":login, 'count':cnt}

@app.route('/change_name', methods=['POST'])
def change_name():
    data = request.json
    new_username = data.get('newUserName')
    ip_address = request.remote_addr
 
    return jsonify({"message": "Имя пользователя успешно изменено."})

# Маршрут для изменения пароля пользователя
@app.route('/change_password', methods=['POST'])
def change_password():
    data = request.json
    new_password = data.get('newPassword')

    # Ваша логика обновления пароля пользователя в базе данных или хранилище
    # Здесь примерно будет выглядеть как-то так:
    # users[username]['password'] = new_password

    return jsonify({"message": "Пароль пользователя успешно изменен."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
