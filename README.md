![TREZOR Core](docs/logo.png)

* [Documentation](docs/)

##Build instructions for emulator

###Linux

####Debian/Ubuntu

```
sudo apt-get install libsdl2-dev:i386
make build_unix
```

####Fedora

```
sudo yum install SDL2-devel.i686
make build_unix
```

####openSUSE

```
sudo zypper install libSDL2-devel-32bit
make build_unix
```

###OS X

```
brew install --universal sdl2
make build_unix
```

### Windows

Not supported yet ...

##Build instructions for ARM

###Linux

For flashing firmware to blank device (without bootloader) by ```make flash```, please install https://github.com/texane/stlink

####Debian/Ubuntu

```
sudo apt-get install gcc-arm-none-eabi libnewlib-arm-none-eabi
make build_strmhal_frozen
```
