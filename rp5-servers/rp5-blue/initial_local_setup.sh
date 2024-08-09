# Disable WIFI
rfkill block wifi

# Configure server specific MotD
cat >> /etc/motd << EOF
         ██████  ██████  ███████       ██████  ██      ██    ██ ███████         
         ██   ██ ██   ██ ██            ██   ██ ██      ██    ██ ██              
         ██████  ██████  ███████ █████ ██████  ██      ██    ██ █████           
         ██   ██ ██           ██       ██   ██ ██      ██    ██ ██              
         ██   ██ ██      ███████       ██████  ███████  ██████  ███████         
Welcome to the rp5-blue server! 3 out of 4 servers in a Raspberry Pi 5 Cluster.
EOF

# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update