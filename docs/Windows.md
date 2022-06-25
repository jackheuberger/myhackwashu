# Windows Dev Environment

This doc is going to go into getting set up with (imo) the best Windows dev environment.

1. Get a Windows Education Key from this WUSTL-specific [link](https://wustl.onthehub.com) (it's free).
2. Open Windows search and look up "product key". This should take you to a settings page where you can swap out your license key.
    - If your license doesn't activate, wait 30 minutes and try again. If it still doesn't work, click the "Get Help" button and get on the phone with Microsoft. I had to do this once and it was super quick, about 15 minutes total including hold time.
3. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
4. Install [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install)
5. Once WSL is set up and you've created a user account, open Docker Desktop on Windows, click the settings gear at the top, click Resources -> WSL Integration -> Enable the distro that you installed, then click Apply & Restart at the bottom
6. Download the updated [Windows Terminal](https://www.microsoft.com/store/productId/9N0DX20HK701) from the Microsoft Store. (I also changed my default environment in the settings to Ubuntu)
7. Try running `sudo docker run hello-world` in WSL
8. Run `sudo groupadd docker && sudo usermod -ag docker $USER`, and then type `logout`
9. Open a new terminal and try running `docker run hello-world`. You hopefully will not get a permissions error!
10. Install [Visual Studio Code](https://code.visualstudio.com/)
11. Once installed, install the [WSL extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl)
12. See the [general setup steps](docs/General.md)!
