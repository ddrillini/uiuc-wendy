from flask import Flask, render_template
from subprocess import run, PIPE
from os import linesep

# TODO: RELIES ON ~/song BEING SYMLINKED TO THE STEPMANIA SONGS DIR

# see learning.py for me figuring things out
app = Flask(__name__) # flask object

# TODO: features
# 1) call out to OS to run various scripts in the uiuc-wendy scripts dir
# 2) run "tree" and.... parse it into a songlist? idk what's the best way to get a songlist
#    run "tree" and just make a page for it lol
# 3) impl usb backup button, start up cron service ?

### PAGES ###

ERROR_HTML = 'error.html'
SONG_LIST_HTML = 'song-list-output.html'
BASE_HTML = 'index.html'

### HTTP ERROR HANDLERS ###

# 404 page
@app.errorhandler(404)
def page_not_found(e):
    official_error_message = 'uwu owwwhhh nu! the sewvice made an oopsie woopsie! ewwow: 404 Nawt Fownd'
    return render_template(ERROR_HTML, error=official_error_message)

### ROUTES ###

# default landing page
@app.route('/', methods=['GET'])
def main():
    return render_template(BASE_HTML)

# Display packs
@app.route('/display-packs', methods=['GET'])
def display_packs():
    out = run(['ls', '/home/wendy/songs'], stdout=PIPE, stderr=PIPE)
    
    if out.returncode != 0:
        stderr_str = out.stderr.decode('utf-8')
        return render_template(ERROR_HTML, error=stderr_str)

    stdout_str = out.stdout.decode('utf-8')
    song_list = stdout_str.split(os.linesep)
    return render_template(SONG_LIST_HTML, output=song_list)

# TODO: Reboot machine
@app.route('/reboot-machine', methods=['POST'])
def reboot_machine():
    # this one requires sudo so it might actually be impossible unless we run the webapp as root which we shouldn't do
    return render_template(ERROR_HTML, error='Not yet implemented!')

# TODO: Restart stepmania
@app.route('/restart-stepmania', methods=['POST'])
def restart_stepmania():
    return render_template(ERROR_HTML, error='Not yet implemented!')

# TODO: Switch to 3.95 (couples)
@app.route('/switch-3.95', methods=['POST'])
def switch_395():
    # find the script called openitg-swap.sh and call it
    return render_template(ERROR_HTML, error='Not yet implemented!')

# TODO: Switch to SM5 (back from couples)
@app.route('/switch-5', methods=['POST'])
def switch_5():
    # find the script called stepmania-swap.sh and call it
    return render_template(ERROR_HTML, error='Not yet implemented!')

# TODO: Add simfiles
# this starts getting trickier. you'll need to allow the end user to do file
# uploads. file uploads in webapps are tricky - probably we'll need
# flask-specific code. there's some risk here -- someone could accidentally
# wipe all of the songs, by overwriting a directory or something.
# we could like, do user accounts, i guess? and bind each user account to a
# dir? then just store the PINs (do not use return passwords) in a sqlite db
@app.route('/add-simfiles', methods=['POST'])
def add_simfiles():
    return render_template(ERROR_HTML, error='Not yet implemented!')

# TODO: Remove simfiles
# this gets even more complex. i think probably "ever user gets their own dir"
# and "admins get their own dir" is useful here.
@app.route('/rm-simfiles', methods=['POST'])
def rm_simfiles():
    return render_template(ERROR_HTML, error='Not yet implemented!')

if __name__ == '__main__':
    app.run() # host = 0.0.0.0? idk
