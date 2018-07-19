sudo apt update
sudo apt upgrade -y

# remote administration
sudo apt install -y git rsync ssh openssh-server tmux vim

# SM specific dependencies
sudo apt install -y mesa-common-dev libglu1-mesa-dev libglew-dev libxtst-dev libxrandr-dev libpng12-dev libjpeg8-dev libjpeg62-dev zlib1g-dev libbz2-dev libogg-dev libvorbis-dev libc6-dev yasm libasound2-dev libmad0-dev libgtk2.0-dev libva-dev

# build tools
sudo apt install -y cmake g++ build-essential
