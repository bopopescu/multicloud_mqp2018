from flask import render_template, flash, redirect, url_for, request, Response, send_file
from . import app, db, bcrypt
from .forms import RegistrationForm, LoginForm, UpdateAccountForm, ResourceForm, WorkloadForm
from .models import User
from flask_login import login_user, current_user, logout_user, login_required
from .price import *
from libcloud.compute.providers import get_driver
from libcloud.compute.types import *
from libcloud.compute.base import NodeSize
from .deployment import deployment, get_node, wait_for_node
import time
import threading


class DeploymentThread(object):

    def __init__(self, node, os, name):

        self.os = os
        self.node = node
        self.name = name

        thread = threading.Thread(target=self.run, args=(node, os, name,))
        thread.daemon = True
        thread.start()

    def run(self):
        return deployment(self.node, self.os, self.name)


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form2 = RegistrationForm()
    form = LoginForm()
    if form2.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form2.password.data).decode('utf-8')
        user = User(username=form2.username.data, email=form2.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created for ' + str(form2.username.data) + '.', 'success')
        return redirect(url_for('login'))

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            print("Authenticated")
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login failed. Please check username and password.', 'danger')
    return render_template('home.html', title='Home', form=form, form2=form2)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created for ' + str(form.username.data) + '.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            print("Authenticated")
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login failed. Please check username and password.', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Account updated.', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    return render_template('account.html', title='Account', form=form)


@app.route('/workload', methods=['GET', 'POST'])
def workload_defined():
    # machine & deep learning
    # in memory
    # general purpose
    form = WorkloadForm()
    instance_provider = None

    if form.validate_on_submit():
        print("----VALID ON SUBMIT ----")
        print(request.form.get('type'))
        input = request.form.get('type')
        instance, top_three, valid_instances = find_instance_workload(input)
        types = []
        for i in top_three:
            types.append(detect_type(i))
        instance_provider = detect_type(instance)

        return render_template('options.html', title='Options', instance=instance,
                               top_three=top_three, instance_provider=instance_provider, types=types,
                               length=len(top_three))
    else:
        print("NOT VALID ON SUBMIT!!!!!!")

    if request.method == 'POST':
        """
        user_option = request.form.get('type')
        print("User option: " + user_option)
        if user_option == "ml":
            thread = DeploymentThread(instance, os, instance_name)
            node = thread.run()
        return render_template('deployment.html', title='Deploy', node=node.id, provider=provider,
                               ip_address=node.private_ips[0], name=node.name)
        """
        input = request.form.get('type')
        instance, top_three, valid_instances = find_instance_workload(input)
        types = []
        for i in top_three:
            types.append(detect_type(i))
        instance_provider = detect_type(instance)

        return render_template('options.html', title='Options', instance=instance,
                               top_three=top_three, instance_provider=instance_provider, types=types,
                               length=len(top_three))

    return render_template('workload.html', title='Workload-based', form=form)


@app.route('/custom', methods=['GET', 'POST'])
def custom():
# os
    # storage
    # memory
    # cpu

    instance2 = None
    instance_provider = None

    form = ResourceForm()
    if form.validate_on_submit():
        instance, top_three, valid_instances = find_instance(int(form.memory.data), int(form.storage.data))
        types = []
        os = form.os.data
        for i in top_three:
            types.append(detect_type(i))
        instance_provider = detect_type(instance)

        return render_template('options.html', title='Options', instance=instance,
                               top_three=top_three, instance_provider=instance_provider, types=types,
                               length=len(top_three), os=os, instance_name=form.name.data)

    if request.method == 'POST':
        user_option = request.form.get('options')
        print("User option: " + user_option)
        if user_option == "1":
            input = str(request.form.get('instance1'))
            instance_name = str(request.form.get('instance_name'))
            id, name, ram, disk, price, bandwidth, driver, extra = format_input(input)
            os = request.form.get('os1')
            provider = driver

            if driver == 'Amazon':
                driver = get_driver(Provider.EC2)
            else:
                driver = get_driver(Provider.GCE)

            if price == "None":
                instance = NodeSize(id=id, name=name, ram=int(ram), disk=int(disk), bandwidth=bandwidth, price=None, driver=driver, extra=None)
                print(instance)
            else:
                instance = NodeSize(id=id, name=name, ram=int(ram), disk=int(disk), bandwidth=bandwidth, price=float(price), driver=driver, extra=None)
                print(instance)

            thread = DeploymentThread(instance, os, instance_name)
            node = thread.run()
            print(node)

            return render_template('deployment.html', title='Deploy', node=node.id, provider=provider,
                                   ip_address=node.private_ips[0], name=node.name)

        if user_option == "2":
            input = str(request.form.get('instance2'))
            print(input)
            id, name, ram, disk, price, bandwidth, driver, extra = format_input(input)
            os = request.form.get('os2')
            provider = driver

            if driver == 'Amazon':
                driver = get_driver(Provider.EC2)
            else:
                driver = get_driver(Provider.GCE)

            if price == "None":
                instance2 = NodeSize(id=id, name=name, ram=int(ram), disk=int(disk), bandwidth=bandwidth, price=None,
                                    driver=driver, extra=None)
                print(instance2)
            else:
                instance2 = NodeSize(id=id, name=name, ram=int(ram), disk=int(disk), bandwidth=bandwidth,
                                    price=float(price), driver=driver, extra=None)
                print(instance2)

            thread = DeploymentThread(instance2, os)
            node = thread.run()
            return render_template('deployment.html', title='Deploy', node=node.id, provider=provider,
                                   ip_address=node.private_ips[0], name=node.name)

        if user_option == "3":
            input = str(request.form.get('instance3'))
            id, name, ram, disk, price, bandwidth, driver, extra = format_input(input)
            os = request.form.get('os3')
            provider = driver

            if driver == 'Amazon':
                driver = get_driver(Provider.EC2)
            else:
                driver = get_driver(Provider.GCE)

            if price is "None":
                instance3 = NodeSize(id=id, name=name, ram=int(ram), disk=int(disk), bandwidth=bandwidth, price=None, driver=driver, extra=None)
                print(instance3)

            else:
                instance3 = NodeSize(id=id, name=name, ram=int(ram), disk=int(disk), bandwidth=bandwidth, price=float(price), driver=driver, extra=None)
                print(instance3)

            thread = DeploymentThread(instance3, os)
            node = thread.run()
            return render_template('deployment.html', title='Deploy', node=node.id, provider=provider,
                                   ip_address=node.private_ips[0], name=node.name)

    return render_template('custom.html', title='User-based', form=form)



@app.route('/progress/<node>/<provider>', methods=['GET', 'POST'])
def progress(node,provider):
    print("-------progress----------")
    print(node)
    print(provider)

    def generate():
        x = 1
        while x == 1:
            yield "data:" + str(x) + "\n\n"
            user_node = get_node(provider, node)
            print(user_node[0].state)
            if user_node[0].state != 'pending':
                print("Node ready")
                x = 2
                yield "data:" + str(x) + "\n\n"
            time.sleep(0.5)

    return Response(generate(), mimetype='text/event-stream')


def format_input(input):
    list = input.split(",")
    print(list)

    #Parse for id
    id = list[0].split("=")[1]
    print("ID: " + id)

    #Parse for name
    name = list[1].split("=")[1]
    print("Name: " + name)

    #Parse for ram
    ram_parse = list[2]
    ram = ram_parse.split("ram=")[1].split(" ")[0]
    print("Ram: " + ram)

    disk_parse = list[2]
    disk = disk_parse.split("disk=")[1].split(" ")[0]
    print("Disk: " + disk)

    price_parse = list[2]
    price = price_parse.split("price=")[1].split(" ")[0]
    print("Price: " + price)
    #Price

    #Bandwidth
    bwidth_parse = list[2]
    bandwidth = bwidth_parse.split("bandwidth=")[1].split(" ")[0]
    print("Bandwidth: " + bandwidth)

    #Extra

    driver = None
    #Driver
    if list[2].find('Amazon') != -1:
        driver = "Amazon"
    else:
        driver ="Google"

    return [id, name, ram, disk, price, bandwidth, driver, None]



