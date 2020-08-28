import flask
from flask import request, jsonify, render_template
import subprocess

# RELIES ON ~/song BEING SYMLINKED TO THE STEPMANIA SONGS DIR

# see learning.py for me figuring things out

app = flask.Flask(__name__) # flask object
app.config["DEBUG"] = True

# TODO: features
# call out to OS to run various scripts in the uiuc-wendy scripts dir
# run "tree" and.... parse it into a songlist? idk what's the best way to get a songlist
# run "tree" and just make a page for it lol

### HTTP ERROR HANDLERS ###

# 404 page
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>uwu oh no! the service made an oopsie woopsie!</p>", 404

### ROUTES ###
# TODO make actual html in a template file instead of just inline html as strings

# default landing page
@app.route('/', methods=['GET'])
def main():
    return render_template("index.html")

# Display packs
@app.route('/display-packs', methods=['POST'])
def display_packs():
    # run os command
    out = subprocess.Popen(['ls', '/home/wendy/songs'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = out.communicate()

    # convert bytestring to string so it doesn't print a b''
    s = lambda e: str(e, 'utf-8')
    foo = list(map(s, stdout.split()))

    return render_template('command-output.html', output=foo)

# TODO: Reboot machine
@app.route('/reboot-machine', methods=['POST'])
def reboot_machine():
    # this one requires sudo so it might actually be impossible unless we run the webapp as root which we shouldn't do
    return render_template('command-output.html', output=['Not yet implemented!'])

# TODO: Restart stepmania
@app.route('/restart-stepmania', methods=['POST'])
def restart_stepmania():
    return render_template('command-output.html', output=['Not yet implemented!'])

# TODO: Switch to 3.95 (couples)
@app.route('/switch-3.95', methods=['POST'])
def switch_395():
    # find the script called openitg-swap.sh and call it
    return render_template('command-output.html', output=['Not yet implemented!'])

# TODO: Switch to SM5 (back from couples)
@app.route('/switch-5', methods=['POST'])
def switch_5():
    # find the script called stepmania-swap.sh and call it
    return render_template('command-output.html', output=['Not yet implemented!'])

# TODO: Add simfiles
# this starts getting trickier. you'll need to allow the end user to do file
# uploads. file uploads in webapps are tricky - probably we'll need
# flask-specific code. there's some risk here -- someone could accidentally
# wipe all of the songs, by overwriting a directory or something.
# we could like, do user accounts, i guess? and bind each user account to a
# dir? then just store the PINs (do not use return passwords) in a sqlite db
@app.route('/add-simfiles', methods=['POST'])
def add_simfiles():
    return render_template('command-output.html', output=['Not yet implemented!'])

# TODO: Remove simfiles
# this gets even more complex. i think probably "ever user gets their own dir"
# and "admins get their own dir" is useful here.
@app.route('/rm-simfiles', methods=['POST'])
def rm_simfiles():
    return render_template('command-output.html', output=['Not yet implemented!'])

if __name__ == '__main__':
    app.run() # host = 0.0.0.0? idk
