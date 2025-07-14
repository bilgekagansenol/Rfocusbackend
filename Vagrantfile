Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"

  config.vm.network "forwarded_port", guest: 8000, host: 8000  # Django için
  config.vm.network "private_network", ip: "192.168.56.10"     # Kritik kısım bu
  config.vm.network "forwarded_port", guest: 11434, host: 11500

  config.vm.synced_folder ".", "/vagrant", type: "virtualbox"

  config.vm.provision "shell", inline: <<-SHELL
  apt-get update
  apt-get install -y software-properties-common curl
  add-apt-repository -y ppa:deadsnakes/ppa
  apt-get update
  apt-get install -y python3.10 python3.10-venv python3.10-dev python3.10-distutils
  curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10
  SHELL
end
