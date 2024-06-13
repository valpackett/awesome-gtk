<!-- lint ignore awesome-toc-->

<img src="https://www.gtk.org/assets/img/logo-gtk-sm.png" align="right" width="144"/>

# Awesome GTK [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) [![Distros: Please do not theme any apps](https://stopthemingmy.app/badge.svg)](https://stopthemingmy.app)

> Collections of awesome native open-source [GTK](https://en.wikipedia.org/wiki/GTK%2B) (4 and 3) applications.

## Contents

- [Apps for GNOME](#apps-for-gnome)
- [Audio](#audio)
  - [Audio Players](#audio-players)
    - [Music Players](#music-players)
    - [Audio Streaming Service Clients](#audio-streaming-service-clients)
    - [MPD Clients](#mpd-clients)
    - [Podcasts](#podcasts)
    - [Audiobooks](#audiobooks)
    - [Radio](#radio)
    - [Transcription](#transcription)
    - [Ambient Sounds](#ambient-sounds)
  - [Audio Workstations (DAWs)](#audio-workstations-daws)
  - [Audio Tools](#audio-tools)
- [Video](#video)
  - [Video Players](#video-players)
  - [Live Stream Viewers](#live-stream-viewers)
  - [Video Editors](#video-editors)
  - [Subtitle Editors](#subtitle-editors)
  - [Screen Recorders](#screen-recorders)
  - [Video Tools](#video-tools)
- [Graphics](#graphics)
  - [3D Graphics](#3d-graphics)
  - [ASCII/Pixel Art](#asciipixel-art)
  - [Image Viewers](#image-viewers)
  - [Raster Graphics](#raster-graphics)
    - [Drawing & Editing](#drawing--editing)
    - [Photography](#photography)
    - [Optimizers/Compressors](#optimizerscompressors)
    - [Upscalers](#upscalers)
  - [Technical Graphics](#technical-graphics)
  - [Vector & Fonts](#vector--fonts)
- [Multimedia](#multimedia)
  - [Media Downloaders](#media-downloaders)
  - [Media Encoders](#media-encoders)
  - [Media Servers](#media-servers)
- [Internet and Networking](#internet-and-networking)
  - [Bluetooth](#bluetooth)
  - [Chat and VoIP](#chat-and-voip)
  - [Email](#email)
  - [File Sharing](#file-sharing)
  - [Network Monitoring](#network-monitoring)
  - [News/Feed Readers](#newsfeed-readers)
  - [Remote Desktop](#remote-desktop)
  - [Social Media Clients](#social-media-clients)
    - [Social Graveyard](#social-graveyard)
  - [Specialized Web Browsers / Wrappers](#specialized-web-browsers--wrappers)
  - [Web Browsers](#web-browsers)
  - [WiFi](#wifi)
  - [Proxy](#proxy)
- [Office](#office)
  - [Book Readers](#book-readers)
  - [Calculators & Math](#calculators--math)
  - [Calendar](#calendar)
  - [Document Managers](#document-managers)
  - [Document Viewers](#document-viewers)
  - [Note-taking](#note-taking)
  - [Journaling](#journaling)
  - [OCR](#ocr)
  - [PDF Tools](#pdf-tools)
  - [Presentation](#presentation)
  - [Translation](#translation)
- [Productivity](#productivity)
  - [Desktop Productivity](#desktop-productivity)
  - [Mind-mapping](#mind-mapping)
  - [Project Management](#project-management)
  - [Timers / Time Tracking](#timers--time-tracking)
  - [To-do Lists](#to-do-lists)
  - [Inventory](#inventory)
- [Security and Privacy](#security-and-privacy)
  - [Password Management](#password-management)
- [Digital Forensics](#digital-forensics)
- [Finance](#finance)
  - [Budget and Accounting Managers](#budget-and-accounting-managers)
  - [Exchange Rate Viewers](#exchange-rate-viewers)
- [Development](#development)
  - [Containers](#containers)
  - [Documentation](#documentation)
  - [Hex Editors](#hex-editors)
  - [IDEs](#ides)
    - [Featureful IDEs](#featureful-ides)
    - [Neovim GUIs](#neovim-guis)
    - [Simple Editors and Light IDEs](#simple-editors-and-light-ides)
    - [Xi GUIs](#xi-guis)
  - [Markdown](#markdown)
  - [LaTeX](#latex)
  - [Terminals](#terminals)
  - [Text Processing](#text-processing)
  - [Toolboxes](#toolboxes)
  - [UI Design](#ui-design)
  - [Version Control and Diffs](#version-control-and-diffs)
- [Design](#design)
- [File and Data Management](#file-and-data-management)
  - [Backup](#backup)
  - [Database Clients](#database-clients)
  - [Disk Imaging](#disk-imaging)
  - [File Management](#file-management)
  - [File Synchronisation](#file-synchronisation)
  - [Remote File Access](#remote-file-access)
- [System Management](#system-management)
  - [Software Installation](#software-installation)
  - [System and File Cleaning](#system-and-file-cleaning)
  - [System Configuration](#system-configuration)
  - [System Monitoring and Info](#system-monitoring-and-info)
  - [Task Scheduling](#task-scheduling)
- [Gaming](#gaming)
  - [Board Games](#board-games)
  - [Puzzles](#puzzles)
- [Health and Fitness](#health-and-fitness)
- [Map Viewers](#map-viewers)
- [Public Transports](#public-transports)
- [Weather Viewers](#weather-viewers)

## Apps for GNOME

You can find the most up-to-date info on the most well-supported GNOME apps at [Apps for GNOME](https://apps.gnome.org/);
this list aims to be broader and include apps from various other ecosystems in various states of maintenance.

## Audio

### Audio Players

#### Music Players

- [Lollypop](https://gitlab.gnome.org/World/lollypop) - Lightweight modern music player designed to work excellently on the GNOME desktop environment with party mode, metadata fetching, MTP device sync and scrobbling `#python` `#libhandy`.
- [Melody](http://anufrij.org/melody) - Music player designed for elementary OS with metadata fetching, online radio and MTP device sync `#vala` `#granite`.
- [Muzika](https://github.com/vixalien/muzika) - Music player with customizable home screen and Google Music integration `#gjs` `#libadwaita`.
- [elementary Music](https://github.com/elementary/music) - Official music player for elementary OS `#vala` `#granite`.
- [GNOME Music](https://apps.gnome.org/Music) - Official GNOME desktop music player `#python` `#libadwaita` `#gnome`.
- [Rhythmbox](https://gitlab.gnome.org/GNOME/rhythmbox) - Music management application designed to work well under the GNOME desktop supporting network shares, podcasts, online radio, portable devices (including iPhones) and internet music services such as Last.fm and Magnatune `#c` `#gnome`.
- [Amberol](https://gitlab.gnome.org/ebassi/amberol) - Simple music player well integrated with GNOME `#rust` `#libadwaita`.
- [G4Music](https://github.com/neithern/g4music) - Light-weight music player focusing on high performance supporting ReplayGain, pipewire audio sink and MPRIS control `#vala` `#libadwaita`.
- [HBud](https://github.com/swanux/hbud) - Audio and video player with karaoke features `#python` `#libadwaita`.
- [Resonance](https://github.com/nate-xyz/resonance) - Music player with MPRIS support, Discord Rich presence and Last.fm scrobbling `#rust` `#python` `#libadwaita`.
- [Monophony](https://gitlab.com/zehkira/monophony) - Application for streaming music from YouTube `#python` `#libadwaita`.
- [netease-cloud-music-gtk](https://github.com/gmg137/netease-cloud-music-gtk) - Audio player for the Netease Cloud Music `#rust` `#libadwaita`.
- [Decibels](https://github.com/vixalien/decibels) - Audio player with waveform view `#gjs` `#libadwaita`.

#### Audio Streaming Service Clients

- [Spot](https://github.com/xou816/spot) - Spotify (premium) client for the GNOME desktop with MPRIS integration based on [librespot](https://github.com/librespot-org/librespot) `#rust` `#libadwaita`.
- [Sublime Music](https://sublimemusic.app) - Client for Subsonic-compatible (Subsonic, Airsonic, Revel, Gonic, Navidrome, Ampache, \*sonic) personal streaming servers `#python`.
- [High Tide](https://github.com/Nokse22/high-tide) - Tidal streaming client `#python` `#libadwaita`.

#### MPD Clients

- [Sonata](https://github.com/multani/sonata) - MPD client with tag editor and audio scrobbling support, currently looking for a new maintainer `#python`.
- [Mpdevil](https://github.com/SoongNoonien/mpdevil) - MPD music browser with MPRIS interface `#python`.

#### Podcasts

- [GNOME Podcasts](https://gitlab.gnome.org/World/podcasts) - (ex Hammond) Official GNOME Podcast client `#rust` `#libadwaita` `#gnome`.
- [Vocal](https://vocalproject.net) - Podcast application with iTunes Store integration and smart library management `#vala` `#granite`.

#### Audiobooks

- [Cozy](https://cozy.sh) - Audiobook player with offline library management and MPRIS integration `#python` `#libadwaita`.

#### Radio

- [Shortwave](https://gitlab.gnome.org/World/Shortwave) - Internet radio player providing access to the community radio station database [radio-browser.info](http://www.radio-browser.info) `#rust` `#libadwaita`.
- [Goodvibes](https://gitlab.com/goodvibes/goodvibes) - Simple light-weight internet radio player `#c`.
- [radiotray-lite](https://github.com/thekvs/radiotray-lite) - Online radio player with minimal interface that runs on the system tray `#c++`.
- [Pithos](https://pithos.github.io/) - Pandora Radio client `#python`.

#### Transcription

- [Parlatype](https://github.com/gkarsay/parlatype) - Minimal audio player for manual speech transcription `#c`.

#### Ambient Sounds

- [Blanket](https://github.com/rafaelmardojai/blanket) - Ambient sound player/mixer with preset management and MPRIS integration `#python` `#libadwaita`.

#### Soundboards

- [Zap](https://gitlab.com/rmnvgr/zap) - Sound effects soundboard and collection manager `#gjs` `#libadwaita`.

### Audio Workstations (DAWs)

- [zrythm](https://github.com/zrythm/zrythm) - DAW offering streamlined editing workflows with automation capabilities, chord assistance and support for plugins `#c++` `#libadwaita`.

### Audio Tools

- [Chromatic](https://github.com/nate-xyz/chromatic) - Instruments tuner `#rust` `#libadwaita`.
- [Lyrebird](https://github.com/lyrebird-voice-changer/lyrebird) - Voice changer based on SoX `#python`.
- [Tagger](https://github.com/NickvisionApps/Tagger) - Music tag (metadata) editor `#csharp` `#libadwaita`.
- [EasyEffects](https://github.com/wwmm/easyeffects) - Audio effects manager (limiter, convolver, equalizer, autovolume and more) for PipeWire applications `#c++` `#libadwaita`.
- [Myxer](https://github.com/VixenUtils/Myxer) - PulseAudio volume mixer `#rust`.
- [Reco](https://github.com/ryonakano/reco) - Audio recorder `#vala` `#granite`.
- [Mousai](https://github.com/SeaDve/Mousai) - Song identifier based on [AudD](https://audd.io/) with MPRIS support `#rust` `#libadwaita`.
- [Ear Tag](https://github.com/knuxify/eartag) - Tag editor designed to edit singular files `#python` `#libadwaita`.
- [Asunder](https://gitlab.gnome.org/Salamandar/asunder) - CD ripper and encoder `#c`.
- [Cavalier](https://github.com/NickvisionApps/Cavalier) - Audio visualizer based on [CAVA](https://github.com/karlstav/cava) `#csharp` `#libadwaita`.
- [pwvucontrol](https://github.com/saivert/pwvucontrol) - PipeWire volume mixer `#rust` `#libadwaita`.
- [Simple Wireplumber GUI](https://github.com/dyegoaurelio/simple-wireplumber-gui) - WirePlumber (PipeWire session manager) GUI to rename devices and show properties.
- [SoundConverter](https://soundconverter.org) - Multithreaded sound converter with compatibility with everything that GStreamer reads and automatic renaming `#python`.
- [Audio Sharing](https://gitlab.gnome.org/World/AudioSharing) - Application to share audio playback in the form of an RTSP stream `#rust` `#libadwaita`.

## Video

### Video Players

- [Celluloid](https://github.com/celluloid-player/celluloid) - (ex GNOME MPV) frontend for MPV `#c` `#libadwaita`.
- [Clapper](https://github.com/Rafostar/clapper) - Media player powered by GStreamer with OpenGL rendering `#gjs` `#c`.
- [Delfin](https://codeberg.org/avery42/delfin) - Application to stream movies/TV shows from Jellyfin `#rust` `#libadwaita`.
- [Movie Monad](https://lettier.github.io/movie-monad/) - Simple video player powered by GStreamer `#haskell`.
- [GNOME Videos](https://apps.gnome.org/Totem) - Official GNOME desktop video player, also known as Totem `#c` `#gnome`.
- [Glide](https://github.com/philn/glide) - Simple video player powered by GStreamer `#rust` `#libadwaita`.

### Live Stream Viewers

- [Multiplex](https://github.com/pojntfx/multiplex) - Application to stream and watch torrents together, providing an experience similar to Apple's SharePlay and Amazon's Prime Video Watch Party `#go` `#libadwaita`.

### Video Editors

- [Footage](https://gitlab.com/adhami3310/Footage) - Application to trim, flip, rotate and crop individual clips `#rust` `#libadwaita`.
- [Pitivi](http://www.pitivi.org) - Video editor based on GStreamer Editor Services `#python`.
- [Video Trimmer](https://gitlab.gnome.org/YaLTeR/video-trimmer) - Application to cut out fragments of a video without re-encoding and reducing video quality `#rust` `#libadwaita`.

### Subtitle Editors

- [Gaupol](https://otsaloma.io/gaupol) - Editor for text-based subtitle files with built-in video player `#python`.
- [Subtitle Editor](https://kitone.github.io/subtitleeditor/) - Subtitle editor with built-in video player and text correction features `#c++`.

### Screen Recorders

- [Kooha](https://github.com/SeaDve/Kooha) - Distraction-free screen recorder `#rust` `#libadwaita`.
- [RecApp](https://github.com/amikha1lov/RecApp) - (archived) Simple screencasting application based on GStreamer `#python`.

### Video Tools

- [Aviator](https://github.com/gianni-rosato/aviator) - Utility for encoding with SVT-AV1 & Opus `#python` `#libadwaita`.
- [Identity](https://gitlab.gnome.org/YaLTeR/identity) - Program for comparing multiple versions of an image or video `#rust` `#libadwaita`.
- [media-toc](https://github.com/fengalin/media-toc) - Application to build a table of contents from a media or to split a media file into chapters `#rust`.

## Graphics

### 3D Graphics

- [Shady](https://github.com/misterdanb/shady) - [Shadertoy](https://www.shadertoy.com) compatible GLSL shader live editor `#vala`.

### ASCII/Pixel Art

- [ASCII Draw](https://github.com/Nokse22/ascii-draw) - App to draw diagrams or anything using only ASCII `#python` `#libadwaita`.
- [Calligraphy](https://gitlab.com/gregorni/Calligraphy) - Text to ASCII banners converter `#python` `#libadwaita`.
- [Letterpress](https://gitlab.com/gregorni/Letterpress) - Image to ASCII art converter using [jp2a](https://github.com/Talinx/jp2a) `#python` `#libadwaita`.
- [Halftone](https://github.com/tfuxu/Halftone) - Image to pixel art converter `#python` `#libadwaita`.

### Image Viewers

- [Geeqie](https://www.geeqie.org/) - Cross-platform image viewer and organizer `#c++`.
- [Image Roll](https://github.com/weclaw1/image-roll) - Simple and fast image viewer with basic image manipulation tools `#rust`.
- [Loupe](https://gitlab.gnome.org/BrainBlasted/loupe) - Simple image viewer `#rust` `#libadwaita`.
- [Memento](https://github.com/SelfRef/memento) - Meme browser, search and tagger with OCR tagging `#python` `#libadwaita`.
- [vipsdisp](https://github.com/jcupitt/vipsdisp) - Image viewer based on [`libvips`](https://github.com/libvips/libvips) supporting many scientific and technical image formats `#c`.

### Raster Graphics

#### Converters

- [Switcheroo](https://gitlab.com/adhami3310/Switcheroo) - Image converter and manipulator ([ImageMagick] frontend) `#python` `#libadwaita`.

#### Drawing & Editing

- [Annotator](https://github.com/phase1geo/annotator) - Image annotation application designed for elementary OS `#vala` `#granite`.
- [Conjure](https://github.com/nate-xyz/conjure) - Image enhancer based on [ImageMagick] `#python` `#libadwaita`.
- [Drawing](https://github.com/maoschanz/drawing) - Simple image editor similar to Microsoft paint designed for the GNOME desktop `#python`.
- [Effector](https://notabug.org/grindhold/effector) - GEGL filter app with a flow graph UI `#vala`.
- [GIMP](https://www.gimp.org/) - Raster graphics editor used for image manipulation, image editing, free-form drawing and more specialized stask `#c`.
- [MyPaint](http://mypaint.org) - Simple drawing and painting program with support for Wacom-style graphics tablets `#python`.
- [Obfuscate](https://gitlab.gnome.org/World/obfuscate) - Private information censoring tool `#rust` `#libadwaita`.
- [Swappy](https://github.com/jtheoof/swappy) - Wayland native screenshot editing tool `#c`.

[imagemagick]: https://imagemagick.org

#### GIF

- [Gifcurry](https://lettier.github.io/gifcurry) - GIF editor and video-to-GIF converter application `#haskell`.
- [Gifup](https://github.com/BharatKalluri/Gifup) - Video-to-GIF converter `#vala` `#granite`.

#### Optimizers/Compressors

- [Curtail](https://github.com/Huluti/Curtail) - Image compressor with support for PNG, JPEG, WebP and SVG images `#python` `#libadwaita`.
- [Refract](https://github.com/Blobfolio/refract) - _Guided_ image optimization for JPEGs and PNGs producing WebP, AVIF and JPEG XL clones `#rust`.

#### Photography

- [Darktable](https://www.darktable.org) - Photography workflow application and raw developer `#c`.
- [RawTherapee](http://rawtherapee.com) - Raw image processing program `#c++`.
- [Shotwell](https://gitlab.gnome.org/GNOME/shotwell) - Personal photo manager with editing features `#vala` `#gnome`.

#### Upscalers

- [Upscaler](https://gitlab.com/TheEvilSkeleton/Upscaler) - Image upscaler based on [Real-ESRGAN ncnn Vulkan](https://github.com/xinntao/Real-ESRGAN-ncnn-vulkan) `#python` `#libadwaita`.

### Technical Graphics

- [Dagger](https://github.com/SeaDve/dagger) - [Graphviz] DOT graphs viewer and editor `#rust` `#libadwaita`.
- [Design](https://github.com/dubstar-04/Design) - 2D CAD application with DXF format support `#gjs` `#libadwaita`.
- [Exhibit](https://flathub.org/apps/io.github.nokse22.Exhibit) - 3D model previewer based on the F3D library that supports many formats `#python` `#libadwaita`.
- [Focus Annotator](https://github.com/13hannes11/focus_annotator) - Tool to annotate the focus plane of z-stacked images `#rust` `#libadwaita`.
- [Gaphor](https://gaphor.org) - UML/SysML modeling application `#python`.
- [GraphUI](https://github.com/artemanufrij/graphui) - Graph visualization based on [Graphviz] `#vala` `#granite`.
- [Horizon](https://github.com/horizon-eda/horizon) - EDA package supporting an integrated end-to-end workflow for printed circuit design `#c++` `#gl`.
- [Photometric Viewer](https://github.com/dlippok/photometric-viewer) - IES and EULUMDAT photometric files viewer `#python` `#libadwaita`.
- [SolveSpace](http://solvespace.com/index.pl) - Parametric 2D/3D CAD tool `#c++` `#gl`.
- [xdot.py](https://github.com/jrfonseca/xdot.py) - Interactive viewer for graphs written in [Graphviz] `#python`.
- [Dune 3D](https://dune3d.org/) - Parametric 3D CAD tool based on OpenCASCADE+SolveSpace from the author of Horizon EDA `#c`.

[graphviz]: https://www.graphviz.org

### Vector & Fonts

- [Birdfont](https://github.com/johanmattssonm/birdfont) - Font editor for creating fonts in TTF, EOT, SVG and BIRDFONT formats `#vala`.
- [Font Downloader](https://github.com/GustavoPeredo/font-downloader) - Download utility for Google Fonts `#python` `#libhandy`.
- [Inkscape](https://inkscape.org) - General vector graphics editor using GTK since version 1.0 `#c++`.
- [Pizzara](https://pizarra.categulario.xyz/en) - Digital, vectorial and infinite chalkboard for free-hand drawing `#libadwaita`.
- [Webfont Kit Generator](https://github.com/rafaelmardojai/webfont-kit-generator) - Utility to create web font-face kits `#python` `#libadwaita`.
- [Mingle](https://github.com/halfmexican/mingle) - Application to combine emojis using Google's Emoji Kitchen `#vala` `#libadwaita`.

## Multimedia

### Media Downloaders

- [Gydl](https://github.com/JannikHv/gydl) - GUI wrapper around [youtube-dl](https://github.com/ytdl-org/youtube-dl) `#python`.
- [Parabolic](https://github.com/NickvisionApps/Parabolic) - [yt-dlp](https://github.com/yt-dlp/yt-dlp) graphical fronted `#csharp` `#libadwaita`.

### Media Encoders

- [Selene](https://github.com/teejee2008/selene) - Audio/video converter for audio and videos files that can encode them to popular output formats like MKV and MP4 `#vala`.

### Media Servers

- [Girens](https://gitlab.gnome.org/tijder/girens) - Plex media player client with responsive layout and function to download media items `#python` `#libadwaita`.
- [Playlifin](https://gitlab.com/Krafting/playlifin-gtk) - Tool to convert YouTube playlists to Jellyfin playlists `#python` `#libadwaita`.

## Internet and Networking

### Bluetooth

- [IP Lookup](https://github.com/Bytezz/IPLookup-gtk) - Simple application to find information about an IP address `#python` `#libadwaita`.
- [Overskride](https://github.com/kaii-lb/overskride) - Bluetooth and Obex client/device manager `#rust` `#libadwaita`.

### Chat and VoIP

- [Dino](https://dino.im) - Modern XMPP/Jabber chat client `#vala` `#libadwaita`.
- [Discover](https://github.com/trigg/Discover) - Discord overlay with X11 and wlroots support `#python`.
- [Flare](https://gitlab.com/schmiddi-on-mobile/flare) - Signal client `#rust` `#libadwaita`.
- [Fractal](https://gitlab.gnome.org/GNOME/fractal) - Matrix client for the GNOME desktop `#rust` `#libadwaita`.
- [Gajim](https://gajim.org) - Fully-featured XMPP client `#python`.
- [Dissent](https://github.com/diamondburned/dissent) - Discord client `#go` `#libadwait`.
- [Meeting Point](https://gitlab.gnome.org/lwildberg/meeting-point) - BigBlueButton client `#vala` `#libadwaita`.
- [Mirdorph](https://gitlab.gnome.org/ranchester/mirdorph) - Crappy low feature Discord client `#python` `#libadwaita`.
- [Polari](https://apps.gnome.org/Polari) - IRC client `#gjs` `#gnome`.
- [Paper Plane](https://github.com/paper-plane-developers/paper-plane) - Telegram client for the GNOME desktop `#rust` `#libadwaita`.
- [Srain](https://srain.silverrainz.me) - Modern IRC client `#c`.

### Email

- [Astroid](https://astroidmail.github.io) - Lightweight and fast Mail User Agent that provides a GUI to searching, displaying and composing email using [notmuch](https://notmuchmail.org) as backend `#c++`.
- [Geary](https://gitlab.gnome.org/GNOME/geary) - Email application for the GNOME desktop build around conversations `#vala` `#gnome` `#libhandy`.
- [Evolution](https://gitlab.gnome.org/GNOME/evolution) - Personal information management application that provides integrated mail, calendaring and address book functionality `#c` `#gnome`.

### File Sharing

- [Deluge](https://deluge-torrent.org) - BitTorrent client available for Linux, macOS and Windows `#python`.
- [Fragments](https://gitlab.gnome.org/World/Fragments) - BitTorrent client built on top of Transmission `#rust` `#libadwaita`.
- [Gabut Download Manager](https://github.com/gabutakut/gabutdm) - Download manager supporting torrents and direct download with Firefox integration  `#vala`.
- [Nicotine+](https://nicotine-plus.org) - Graphical client for the [Soulseek](https://www.slsknet.org) peer-to-peer network `#python`.
- [Teleport](https://gitlab.gnome.org/jsparber/teleport) - Network file sharing application based on Avahi (mDNS) `#c`.
- [Transmission](https://transmissionbt.com) - BitTorrent client for macOS, Windows and Linux `#c`.
- [Transporter](https://github.com/bleakgrey/Transporter) - (archived) [magic-wormhole] client for elementary OS `#vala` `#granite`.
- [Torrential](https://github.com/davidmhewitt/torrential) - Alternative GUI on top of the Transmission BitTorrent client `#vala` `#granite`.
- [Varia](https://github.com/giantpinkrobots/varia) - Download manager based on [aria2](https://github.com/aria2/aria2) `#python` `#libadwaita`.
- [Warp](https://apps.gnome.org/app/app.drey.Warp) - [magic-wormhole] client `#rust` `#libadwaita`.
- [Warpinator](https://github.com/linuxmint/warpinator) - Linux Mint's LAN file sharing program `#c++`.

[magic-wormhole]: https://github.com/warner/magic-wormhole

### Network Monitoring

- [Hotwire](https://github.com/emmanueltouzery/hotwire) - GUI that leverages the wireshark and tshark infrastructure to capture traffic and explore the contents of tcpdump files `#rust`.

### News/Feed Readers

- [Coffee](https://nick92.github.io/coffee) - News and weather reader for sources provided by News API and DarkSky `#vala`.
- [Feeds](https://gfeeds.gabmus.org) - News reader for the GNOME desktop `#python` `#libadwaita`.
- [Liferea](https://lzone.de/liferea) - News reader with a GUI similar to desktop mail client and with an embedded web browser `#c`.
- [NewsFlash](https://gitlab.com/news-flash/news_flash_gtk) - News reader designed to complement an already existing web-based RSS reader account `#rust` `#libadwaita`.

### Remote Desktop

- [Connections](https://gitlab.gnome.org/GNOME/connections) - Remote desktop client for the GNOME desktop with RDP and VNC support `#vala` `#gnome`.
- [Remmina](https://gitlab.com/Remmina/Remmina) - Remote desktop client with plugin system and RDP, VNC, SPICE, X2GO, HTTP and SSH support `#c`.
- [Vinagre](https://gitlab.gnome.org/Archive/vinagre) - (archive) Remote desktop viewer for the GNOME desktop with RDP, VNC, SPICE support `#c` `#gnome`.

### Social Media Clients

- [Tuba](https://tuba.geopjr.dev) - Mastodon client, fork of Tootle `#vala` `#libadwaita`.
- [Social](https://gitlab.gnome.org/World/Social) - Mastodon and Pleroma client `#rust`.

#### Social Graveyard

Clients for commercial social platforms that had their API access cut off in a wave of [enshittification](https://pluralistic.net/2023/01/21/potemkin-ai/).

- Corebird / [Cawbird](https://github.com/IBBoard/cawbird) / [NewCaw](https://github.com/CodedOre/NewCaw) - Used to be a Twitter client, rewrite to Mastodon API abandoned `#vala`.
- [Headlines](https://gitlab.com/caveman250/Headlines) - Used to be a Reddit client `#c++` `#libadwaita`.
- [Giara](https://gitlab.gnome.org/World/giara) - Used to be a Reddit client (not officially deprecated yet) `#python` `#libadwaita`.

### Specialized Web Browsers / Wrappers

- [Bavarder](https://github.com/Bavarder/Bavarder) - AI chatbot (ChatGPT, CatGPT, BAI Chat, Open-Assistant SFT-1 12B Model) interface `#python` `#libadwaita`.
- [Geopard](https://ranfdev.com/projects/geopard) - Gemini web browser `#rust` `#libadwaita`.
- [HackUp](https://github.com/mdh34/hackup) - [Hacker News](https://news.ycombinator.com) client `#vala` `#granite`.
- [Imaginer](https://github.com/ImaginerApp/Imaginer) - AI image generator (DALL·E 2, Portrait Plus, Stable Diffusion, Custom Provider) interface `#python` `#libadwaita`.
- [Lobjur](https://github.com/ranfdev/Lobjur) - [lobste.rs](https://lobste.rs) client `#gjs` `#libadwaita`.
- [Tally](https://github.com/cassidyjames/Tally) - Plausible Analytics (Google Analytics alternative) client `#vala` `#libadwaita`.
- [Tangram](https://github.com/sonnyp/Tangram) - Browser for your pinned tabs `#gjs` `#libadwaita`.
- [Wike](https://hugolabe.github.io/Wike) - Wikipedia client `#python` `#libadwaita`.

### Web Browsers

- [Eolie](https://gitlab.gnome.org/World/eolie) - Web browser for the GNOME desktop with Firefox Sync support `#python` `#libhandy`.
- [GNOME Web (Epiphany)](https://apps.gnome.org/Epiphany) - Web browser for the GNOME desktop based on the [WebKit] endering engine `#c` `#gnome` `#libadwaita`.
- [luakit](https://luakit.github.io) - Highly configurable browser based on the [WebKit] engine and extensible with Lua `#c` `#lua`.

[webkit]: https://webkit.org

### WiFi

- [Linux Wifi Hotspot](https://github.com/lakinduakash/linux-wifi-hotspot) - Feature-rich wifi hotspot creator for Linux which provides both GUI and command-line interface `#c`.

### Proxy

- [Carburetor](https://tractor.frama.io/carburetor) - Graphical setting app to easily set up a TOR proxy on your session, without getting your hands dirty with system configs `#python` `#libadwaita`.
- [Haguichi](https://haguichi.net) - Graphical fronted for Hamachi `#vala`.

## Office

### Book Readers

- [Bookworm](https://babluboy.github.io/bookworm) - Simple eBook reader for elementary OS `#vala` `#granite`.
- [Foliate](https://github.com/johnfactotum/foliate) - Simple and modern eBook reader based on [Epub.js](https://github.com/futurepress/epub.js) `#gjs` `#libadwaita`.
- [Komikku](https://valos.gitlab.io/Komikku) - Manga reader for the GNOME desktop with online and offline reading `#python` `#libadwaita`.

### Calculators & Math

- [balistica](https://github.com/fusilero/balistica) - Exterior ballistics calculator `#vala`.
- [Dippi](https://github.com/cassidyjames/dippi) - Display DPI calculator `#vala` `#libadwaita`.
- [Graphs](https://github.com/SjoerdB93/Graphs) - Plotting and data manipulation tool for the GNOME desktop `#python` `#libadwaita`.
- [NaSC](https://github.com/parnoldx/nasc) - Dual pane text based calculator `#vala`.
- [Plots](https://github.com/alexhuntley/Plots) - Graph plotting app for the GNOME desktop `#python` `#opengl`.
- [Qalculate! GTK+](https://qalculate.github.io) - Multi-purpose cross-platform desktop calculator `#c++`.
- [Gnumeric](http://www.gnumeric.org) - Spreadsheet editor `#c`.
- [LogicRs](https://github.com/Spydr06/logicrs) - Logical circuits simulator/editor `#rust` `#libadwaita`.
- [Binary](https://github.com/fizzyizzy05/binary) - Small application to convert numbers to different bases `#python` `#libadwaita`.

### Calendar

- [GNOME Calendar](https://apps.gnome.org/Calendar) - Simple calendar for the GNOME desktop `#c` `#libadwaita` `#gnome`.

### Document Managers

- [GNOME Documents](https://gitlab.gnome.org/Archive/gnome-documents) - (archived) Document manager for the GNOME desktop with collection features `#gjs`.
- [Paperwork](https://openpaper.work) - Document manager with scan features `#python`.

### Document Viewers

- [Xreader](https://github.com/linuxmint/xreader) - Generic document viewer with support for PDF, Postscript, djvu, comics and more `#c` `#xapps`.
- [Evince](https://apps.gnome.org/Evince) - Document viewer for the GNOME desktop with support for PDF, Postscript, DjVu, comics etc. and SyncTex support with gedit `#c` `#libhandy` `#gnome`.
- [Papers](https://apps.gnome.org/en/Papers) - Document viewer for the GNOME desktop (GTK 4 fork of Evince) with support for PDF, Postscript, DjVu, EPS, XPS and comics archives `#c` `#libadwaita` `#gnome`.

### Note-taking

- [GNOME Notes](https://gitlab.gnome.org/GNOME/gnome-notes) - Simple note editor for the GNOME desktop, also known as Bijiben `#c` `#gnome`.
- [Gnote](https://gitlab.gnome.org/GNOME/gnote) - Note-taking application for the GNOME desktop started as a Tomboy port `#c++` `#gnome`.
- [Iridium](https://github.com/matze/iridium) - [Standard Notes](https://standardnotes.org) local-first client `#rust`.
- [Notejot](https://github.com/lainsce/notejot) - Stupidly simple notes application `#vala` `#granite`.
- [Notekit](https://github.com/blackhole89/notekit) - Hierarchical Markdown note-taking application with tablet support `#c++`.
- [Notes](https://github.com/Blquinn/notes) - Note-taking application for the GNOME desktop with notebook based categorization, trash and dark theme `#vala` `#libadwaita`.
- [Notes-Up](https://github.com/Philip-Scott/Notes-up) - Markdown note manager for elementary OS `#vala` `#granite`.
- [Noteworthy](https://github.com/SeaDve/Noteworthy) - Modern, fast, and version-controlled Markdown notes application `#rust` `#libadwaita`.
- [Notorious](https://gitlab.gnome.org/GabMus/notorious) - Keyboard-centric notes application `#python` `#libhandy`.
- [Outliner](https://github.com/phase1geo/outliner) - Outlining application for elementary OS `#vala` `#granite`.
- [Paper](https://gitlab.com/posidon_software/paper) - Markdown note-taking application with GNOME desktop integration `#vala` `#libadwaita`.
- [Iotas](https://gitlab.gnome.org/World/iotas) - Simple Markdown note-taking application with Nextcloud Notes integration `#python` `#libadwaita`.
- [Rnote](https://github.com/flxzt/rnote) - Vector-based drawing app for sketching, handwritten notes and to annotate documents and pictures with pressure-sensitive stylus input support `#rust` `#libadwaita`.
- [Xournal++](https://xournalpp.github.io) - Cross-platform handwriting note-taking software with PDF annotation support and support for pen input form devices such as Wacom tablets `#c++`.
- [Zim](https://github.com/zim-desktop-wiki/zim-desktop-wiki) - Text editor used to maintain a collection of wiki pages `#python`.
- [Folio](https://github.com/toolstack/Folio) - Markdown note-taking application with GNOME desktop integration (Paper fork with additional features) `#vala` `#libadwaita`.

### Journaling

- [Journaler](https://github.com/phase1geo/journaler) - Journaling application for elementary OS `#vala` `#granite`.
- [RedNotebook](https://rednotebook.sourceforge.io) - Desktop journal application that lets you format, tag and search your entries `#python`.

### OCR

- [Frog](https://tenderowl.com/work/frog) - Intuitive text extraction tool for the GNOME desktop.
- [gImageView](https://github.com/manisandro/gImageReader) - GTK/Qt front-end to [Tesseract] `#c++`.
- [TextSnatcher](https://github.com/RajSolai/TextSnatcher) - Easy to use OCR application based on [Tesseract] `#vala` `#granite`.

[tesseract]: https://github.com/tesseract-ocr/tesseract

### PDF Tools

- [Paper Clip](https://github.com/Diego-Ivan/Paper-Clip) - PDF metadata editor `#vala` `#libadwaita`.
- [PDF Arranger](https://github.com/pdfarranger/pdfarranger) - PDF editor with merging, splitting, rotating, cropping and rearranging based on [pikepdf](https://github.com/pikepdf/pikepdf) `#python`.
- [PDF Slicer](https://junrrein.github.io/pdfslicer) - Simple application to extract, merge, rotate and reorder pages of PDF documents with undo/redo support `#c++`.

### Presentation

- [pdfpc](https://pdfpc.github.io) - Presentation console with multi-monitor support for PDF files `#vala`.
- [Pympress](https://github.com/Cimbali/pympress) - Presentation tool designed for dual-screen setups such as presentations and public talks `#python`.
- [Spice-up](https://github.com/Philip-Scott/Spice-up) - Web presentation editor `#vala` `#granite`.
- [Teleprompter](https://github.com/Nokse22/teleprompter) - Simple application to read scrolling text from your screen `#python` `#libadwaita`.

### Translation

- [Dialect](https://github.com/gi-lom/dialect) - Translation based on Google Translate, LibreTranslate and the free DeepL API `#python` `#libadwaita`.

## Productivity

### Desktop Productivity

- [Actioneer](https://github.com/phase1geo/actioneer) - Tool to automate actions on file changes `#vala` `#granite`.
- [Boatswain](https://gitlab.gnome.org/World/boatswain) - Elgato Stream Deck controller `#c` `#libadwaita`.
- [StreamController](https://github.com/StreamController/StreamController) - Elgato Stream Deck controller with support for plugins `#python` `#libadwaita`.
- [Cigale](https://github.com/emmanueltouzery/cigale) - Timesheet for your activities with support for emails, Git, GitLab and Stack Exchange `#rust`.
- [Collector](https://mijorus.it/projects/collector) - Dropover utility that allows to drag files/images/text into a collection window and drop them anywhere `#python` `#libadwaita`.
- [GNOME Characters](https://apps.gnome.org/app/org.gnome.Characters) - Emoji picker `#c` `#libadwaita` `#gnome`.
- [Morphosis](https://flathub.org/apps/garden.jamie.Morphosis) - Document converter (using Pandoc) supporting PDF, Markdown, RST, LaTeX, HTML, Microsoft Word, Open/Libre Office and EPUB formats `#python` `#libadwaita`. 
- [Notify](https://github.com/ranfdev/Notify) - Client for ntfy `#rust` `#libadwaita`.
- [Random](https://codeberg.org/foreverxml/random) - Randomization made easy with advanced functions `#vala` `#libadwaita`.
- [Szyszka](https://github.com/qarmin/szyszka) - Fast bulk file renamer `#rust`.
- [Ticket Booth](https://github.com/aleiepure/ticketbooth) - Application to keep track of TV series/movies with TMDB's API `#python` `#libadwaita`.
- [TV Series Renamer](https://github.com/mmstick/tv-renamer) - TV series renaming application that support adding titles to episodes `#rust`.
- [Workspaces](https://github.com/DevAlien/workspaces) - Desktop workpaces for elementaryOS `#vala` `#granite`.

### Mind-mapping

- [Minder](https://github.com/phase1geo/Minder) - Mind-mapping application for elementaryOS `#vala` `#granite`.

### Project Management

- [Planify](https://github.com/alainm23/planify) - Project and task manager with Todoist support `#vala` `#libadwaita`.

### Timers / Time Tracking

- [Chess Clock](https://apps.gnome.org/app/com.clarahobbs.chessclock) - Over-the-board chess time control `#python` `#libadwaita`.
- [Exercise Timer](https://github.com/mfep/exercise-timer) - Interval training timer `#rust` `#libadwaita`.
- [Flowtime](https://github.com/Diego-Ivan/Flowtime) - Pomodoro timer with statistics `#vala` `#libadwaita`.
- [Furtherance](https://github.com/lakoliu/Furtherance) - Cross-platform time tracker `#rust` `#libadwaita`.
- [hamster-gtk](https://github.com/projecthamster/hamster-gtk) - Time tracker provided by `hamster-lib` `#python`.
- [Hourglass](https://github.com/sgpthomas/hourglass) - Simple time keeping application for elementaryOS `#vala` `#granite`.
- [Khronos](https://github.com/lainsce/khronos) - Task time logger `#vala` `#libadwaita`.
- [Retro](https://github.com/sonnyp/Retro) - Customizable digital clock `#gjs` `#libadwaita`.
- [Solanum](https://gitlab.gnome.org/World/Solanum) - Pomodoro timer for the GNOME desktop `#rust` `#libadwaita`.
- [Timetrack](https://gitlab.gnome.org/danigm/timetrack) - Simple time trakcer for the GNOME desktop `#python`.
- [Tomato](https://github.com/luizaugustomm/tomato) - Pomodoro timer for elementaryOS `#vala` `#granite`.
- [Timer](https://github.com/vikdevelop/timer) - Simple countdown timer `#python` `#libadwaita`.

### To-do Lists

- [Agenda](https://github.com/dahenson/agenda) - Simple to-do application for elementaryOS `#vala` `#granite`.
- [Done](https://done.edfloreshz.dev) - To-do application that allows you to consolidate your existing task providers into a single place `#rust` `#libadwaita`.
- [Endeavour](https://gitlab.gnome.org/World/Endeavour) - Personal tasks manager with complete integration with the GNOME desktop `#c` `#libadwaita`.
- [Effitask](https://github.com/sanpii/effitask) - [todo.txt] client with due, flag, future note and schedule addons `#rust`.
- [Getting Things GNOME](https://github.com/getting-things-gnome/gtg) - Personal task organizer for the GNOME desktop inspired by [Getting Things Done](https://gettingthingsdone.com/what-is-gtd) `#python` `#gnome`.
- [Remembrance](https://github.com/dgsasha/remembrance) - Simple reminder app `#python` `#libadwaita`.
- [Yishu](https://github.com/lainsce/yishu) - (archived) Simple [todo.txt] client `#vala` `#granite` `#libhandy`.
- [List](https://github.com/mrvladus/List) - Simple todo application for those who prefer simplicity `#c` `#libadwaita`.
- [IPlan](https://github.com/iman-salmani/iplan) - Personal task manager with project-based task grouping, task timers and drag and drop arranging `#rust` `#libadwaita`.
- [Errands](https://github.com/mrvladus/Errands) - Simple to-do application with subtasks, accent colors and drag & drop support `#python` `#libadwaita`.

[todo.txt]: https://github.com/todotxt/todo.txt

### Inventory

- [Jellybean](https://codeberg.org/turtle/jellybean) - Inventory manager with refill functions and a handy low-stock indicator `#vala` `#libadwaita`.

## Security and Privacy

- [Collision](https://collision.geopjr.dev) - Tool to generate, compare and verify hashes `#crystal` `#libadwaita`.
- [GtkHash](https://gtkhash.org) - Desktop utility for computing message digests or checksums `#c`.
- [Key Rack](https://gitlab.gnome.org/sophie-h/key-rack) - Tool that allows to view and edit keys, like passwords or tokens, stored by apps `#rust` `#libadwaita`.
- [krb5-auth-dialog](https://gitlab.gnome.org/GNOME/krb5-auth-dialog) - Kerberos tickets monitoring `#c` `#libadwaita`.
- [Malcontent](https://gitlab.freedesktop.org/pwithnall/malcontent) - Parental control client `#c` `#libadwaita`.
- [Metadata Cleaner](https://metadatacleaner.romainvigier.fr) - File metadata cleanre based on MAT2 `#python` `#libadwaita`.
- [Raider](https://github.com/ADBeveridge/raider) - Application to securely delete your files for the GNOME desktop `#c` `#libadwaita`.

### Password Management

- [Authenticator](https://gitlab.gnome.org/World/Authenticator) - Two-factor authentication codes generator `#rust` `#libadwaita`.
- [Gonepass](https://github.com/jbreams/gonepass) - 1Password vault reader `#c++`.
- [Obliviate](https://github.com/elfenware/obliviate) - Password manager that does not store passwords for elementaryOS `#vala`.
- [OTPClient](https://github.com/paolostivanin/OTPClient) - One Time Password application that supports both TOTP and HOTP `#c`.
- [Passbook](https://gitlab.gnome.org/gnumdk/passbook) - Password manager `#python`.
- [Secrets](https://gitlab.gnome.org/World/secrets) - Password manager for the GNOME desktop with support for KeePass safes `#python` `#libadwaita`.

## Digital Forensics

- [Hashes](https://github.com/zefr0x/hashes) - Identify hashing algorithms `#python` `#libadwaita`.

## Finance

### Budget and Accounting Managers

- [Denaro](https://github.com/NickvisionApps/Denaro) - Personal finance manager for GNOME `#csharp` `#libadwaita`.
- [Envelope](https://github.com/cjfloss/envelope) - Personal finance manager for elementaryOS `#vala` `#granite`.
- [Grisbi](http://grisbi.org) - 20 years old accounting application `#c`.

### Exchange Rate Viewers

- [Crypto](https://gitlab.com/ErikWallstrom/Crypto) - Cryptocyrreny watcher `#c`.
- [Markets](https://github.com/bitstower/markets) - Stock, currency and cryptocurrency tracker `#vala` `#libhandy`.

## Development

### Containers

- [Atoms](https://github.com/AtomsDevs/Atoms) - Linux Chroot environments manager `#python` `#libadwaita`.
- [Bottles](https://github.com/bottlesdevs/Bottles) - Wine environments manager `#python` `#libadwaita`.
- [BoxBuddy](https://github.com/Dvlv/BoxBuddyRS) - Graphical interface for Distrobox `#rust` `#libadwaita`.
- [Pods](https://github.com/marhkb/pods) - Podman containers manager `#rust` `#libadwaita`.
- [Toolbx Tuner](https://github.com/13hannes11/toolbx-tuner) - [toolbx](https://containertoolbx.org) containers manager `#rust` `#libadwaita`.

### Documentation

- [Biblioteca](https://github.com/workbenchdev/Biblioteca) - GNOME/Libadwaita documentation browser and viewer `#gjs` `#libadwaita`.
- [DevDocs Desktop](https://github.com/hardpixel/devdocs-desktop) - [DevDocs] browser and viewer `#python`.
- [quickDocs](https://github.com/mdh34/quickDocs) - Documentation browser for [DevDocs] and Valadoc `#vala` `#granite`.

[devdocs]: https://devdocs.io

### Hex Editors

- [GHex](https://gitlab.gnome.org/GNOME/ghex) - Tool to load data from any file, view and edit it in either hex or ASCII `#c` `#libadwaita` `#gnome`.

### IDEs

#### Featureful IDEs

- [Anjuta](https://gitlab.gnome.org/Archive/anjuta) - (archived) IDE with a GUI designer for the GNOME desktop `#c` `#gnome`.
- [GNOME Builder](https://apps.gnome.org/Builder) - Tool to help you write and contribute to great GNOME-based applications `#c` `#libadwaita` `#gnome`.
- [GtkIDE.jl](https://github.com/jonathanBieler/GtkIDE.jl) - GTK-based IDE for Julia `#julia`.
- [Playhouse](https://github.com/sonnyp/Playhouse) - Playground for HTML/CSS/JavaScript `#gjs` `#libadwaita`.
- [Valama](https://github.com/Valama/valama) - Vala IDE `#vala`.
- [Workbench](https://apps.gnome.org/app/re.sonny.Workbench) - Tool to experiment with GNOME technologies `#gjs` `#libadwaita`.

#### Neovim GUIs

- [GNvim](https://github.com/vhakulinen/gnvim) - GUI for Neovim without any web bloat `#rust`.
- [neovim-gtk](https://github.com/Lyude/neovim-gtk) - GUI for Neovim with ligatures support `#rust`.
- [nvim-pygtk3](https://github.com/rliang/nvim-pygtk3) - PyGTK3 frontend to Neovim with some visual GUI elements `#python`.

#### Simple Editors and Light IDEs

- [elementary Code](https://github.com/elementary/code) - Code editor designed for elementaryOS `#vala` `#granite`.
- [elementary IDE](https://github.com/donadigo/elementary-ide) - Unofficial elementaryOS-oriented IDE `#vala` `#granite`.
- [Geany](https://www.geany.org) - Cross-platform ext editor that provides tons of useful features `#c`.
- [gedit](https://gitlab.gnome.org/GNOME/gedit) - Easy-to-use and general-purpose text editor for the GNOME desktop `#c` `#gnome`.
- [GNOME Text Editor](https://gitlab.gnome.org/GNOME/gnome-text-editor) - Simple text editor that focuses on session management `#c` `#gnome`.
- [Norka](https://tenderowl.com/work/norka) - Continuous text editor for the GNOME desktop and elementaryOS `#python` `#granite`.
- [SciTE](https://www.scintilla.org/SciTE.html) - Lightweight cross-platform code editor `#c++`.
- [Scripter](https://github.com/david-swift/Scripter) - Simple application to write and execute small Python scripts `#swift` `#libadwaita`.
- [Vulcan](https://github.com/zesterer/vulcan) - Minimalistic text editor designed for both ordinary use and software development `#vala`.
- [Xed](https://github.com/linuxmint/xed) - Small and lightweight text editor `#c` `#xapps`.

#### Xi GUIs

- [Tau](https://gitlab.gnome.org/World/Tau) - GTK frontend for Xi, previously called gxi `#rust`.
- [xi-gtk](https://github.com/eyelash/xi-gtk) - GTK fronted for the Xi `#vala`.

### Markdown

- [Apostrophe](https://gitlab.gnome.org/World/apostrophe) - Distraction-free Markdown editor `#python` `#libadwaita`.
- [markdown-rs](https://github.com/nilgradisnik/markdown-rs) - Distraction-free Markdown editor `#rust`.
- [Marker](https://github.com/fabiocolacio/Marker) - Markdown editor with HTML and LaTeX conversion with [scidown](https://github.com/Mandarancio/scidown) `#c`.
- [Quilter](https://github.com/lainsce/quilter) - Distraction-free Markdown editor `#vala` `#libadwaita`.
- [Showdown](https://gitlab.com/craigbarnes/showdown) - Simple markdown viewer `#vala`.

### LaTeX

- [Citations](https://gitlab.gnome.org/World/citations) - BibTex bibliography manager `#rust` `#libadwaita`.
- [Gummi](https://gummi.app) - Simple LaTeX editor `#c`.
- [GNOME LaTeX (LaTeXila)](https://gitlab.gnome.org/swilmet/gnome-latex) - LaTeX editor with Latexmk support for the GNOME desktop `#vala` `#gnome`.
- [Hieroglyphic](https://github.com/FineFindus/Hieroglyphic) - Application to search for LaTeX symbols by sketching, fork of TeX Match `#rust` `#libadwaita`.
- [Setzer](https://www.cvfosammmm.org/setzer) - Simple yet full-featured LaTeX editor `#python`.
- [TeX Match](https://github.com/zoeyfyi/TeX-Match) - Application to search for LaTeX symbols by sketching `#rust`.

### Terminals

- [Black Box](https://gitlab.gnome.org/raggesilver/blackbox) - Terminal with customizable UI `#vala` `#libadwaita` `#vte`.
- [GNOME Console](https://gitlab.gnome.org/GNOME/console) - Minimal terminal for the GNOME desktop `#c` `#vte` `#gnome`.
- [GNOME Terminal](https://gitlab.gnome.org/GNOME/gnome-terminal) - Terminal for the GNOME desktop `#c` `#vte` `#gnome`.
- [Guake](https://github.com/Guake/guake) - Dropdown terminal for the GNOME desktop `#python` `#vte`.
- [Prompt](https://gitlab.gnome.org/chergert/prompt) - Terminal with first-class support for containers `#c` `#vte`.
- [Tilix](https://gnunn1.github.io/tilix-web) - Tiling and dropdown terminal for the GNOME desktop `#d` `#vte`.

### Text Processing

- [Black Fennec](https://gitlab.ost.ch/blackfennec/blackfennec) - Visual semi-structured data (JSON) editor `#python` `#libadwaita`.
- [KonbuCase](https://github.com/ryonakano/konbucase) - Case converting application `#vala` `#granite`.
- [Wildcard](https://gitlab.gnome.org/World/Wildcard) - Regex tester `#rust` `#libadwaita`.
- [RegexTester](https://github.com/artemanufrij/regextester) - Regex tester for elementaryOS `#vala` `#granite`.
- [Snoop](https://gitlab.gnome.org/philippun1/snoop) - Tool to search through your files and providing a Nautilus extension `#vala` `#libadwaita`.
- [Text Pieces](https://github.com/liferooter/textpieces) - Swiss knife of text processing `#vala` `#libadwaita`.
- [TextShine](https://github.com/phase1geo/textshine) - Text conversion utility `#vala` `#granite`.

### Toolboxes

- [Dev Toolbox](https://github.com/aleiepure/devtoolbox) - Developer toolbox with JSON to YAML converter, CRON expressions parser, language formatter, hash generators, regex tester, Markdown preview, image converters and more `#python` `#libadwaita`.
- [Escambo](https://github.com/CleoMenezesJr/escambo) - HTTP-based APIs test application `#python` `#libadwaita`.
- [Aurea](https://flathub.org/apps/io.github.cleomenezesjr.aurea) - Simple preview banner made to read metainfo files from Flatpak apps and represent them as they would on Flathub `#python` `#libadwaita`.
 
### UI Design

- [Glade](https://glade.gnome.org) - RAD tool to enable quick & easy development of user interfaces for the GTK toolkit and the GNOME desktop `#c` `#gnome`.
- [Cambalache](https://gitlab.gnome.org/jpu/cambalache) - RAD tool for Gtk 4 and 3 with a clear MVC design and data model first philosophy `#python`.
- [Gradience](https://github.com/GradienceTeam/Gradience) - Libadwaita applications customizer `#python` `#libadwaita`.

### Version Control and Diffs

- [Commit](https://github.com/sonnyp/Commit) - Commit message editor for Git and Mercurial `#gjs` `#libadwaita`.
- [Diffuse](https://github.com/MightyCreak/diffuse) - Text file comparing/merging tool `#python`.
- [Forge Sparks](https://github.com/rafaelmardojai/forge-sparks) - Git forge (GitHub, Gitea, Forgejo) notification application `#gjs` `#libadwaita`.
- [gitg](https://gitlab.gnome.org/GNOME/gitg) - Git GUI client `#vala` `#gnome`.
- [Gnomit](https://github.com/small-tech/gnomit) - (archived) Git commit message editor for the GNOME desktop `#gjs`.
- [Meld](https://gitlab.gnome.org/GNOME/meld) - Visual diff and merge tool `#python` `#gnome`.
- [Turtle](https://gitlab.gnome.org/philippun1/turtle) - Tool to manage Git repositories within Nautilus by providing emblems, context menus and specific dialogues for complex operations `#python` `#libadwaita`.

## Design

- [Contrast](https://gitlab.gnome.org/World/design/contrast) - Tool to check whether the contrast between two colors meet the [WCAG](https://www.w3.org/WAI/standards-guidelines/wcag) requirements `#rust` `#libadwaita`.
- [Emulsion](https://github.com/lainsce/emulsion) - Color palette manager `#vala` `#libadwaita`.
- [Eyedropper](https://github.com/FineFindus/eyedropper) - Color picker and formatter `#rust` `#libadwaita`.
- [Harvey](https://github.com/danrabbit/harvey) - Color contrast calculator `#vala`.
- [Icon Library](https://gitlab.gnome.org/World/design/icon-library) - System icon browser `#rust` `libadwaita`.
- [Icon Preview](https://gitlab.gnome.org/World/design/app-icon-preview) - Application icon previewer for designing application icons `#vala`.
- [LookBook](https://github.com/danrabbit/lookbook) - System icon browser `#vala` `#granite`.
- [Paleta](https://github.com/nate-xyz/paleta) - Image dominant color extractor `#rust` `#libadwaita`.
- [Symbolic Preview](https://gitlab.gnome.org/World/design/symbolic-preview) - Symbolic icon previwer `#rust` `#libadwaita`.

## File and Data Management

### Backup

- [Butter](https://github.com/zhangyuannie/butter) - Btrfs snapshot manager `#rust` `#libadwaita`.
- [Déjà Dup Backups](https://apps.gnome.org/DejaDup/) - Simple backup tool for the GNOME desktop `#vala` `#libadwaita`.
- [Pika Backup](https://gitlab.gnome.org/World/pika-backup) - Backup application based on [BorgBackup](https://www.borgbackup.org/support/fund.html) with remote, scheduling and encryption features `#rust` `#libadwaita`.
- [Timeshift](https://github.com/linuxmint/timeshift) - System restore tool for Linux that creates filesystem snapshots using rsync or Btrfs snapshots `#vala`.

### Database Clients

- [Daty](https://gitlab.gnome.org/World/Daty) - Cross-platform advanced Wikidata editor `#python` `#libhandy`.
- [Sequeler](https://github.com/Alecaddd/sequeler) - SQL client with support for PostgreSQL, MariaDB and SQLite `#vala` `#granite`.

### Disk Imaging

- [Brasero](https://gitlab.gnome.org/GNOME/brasero) - Application to burn CD/DVD designed to be as simple as possible `#c` `#gnome`.
- [GNOME MultiWriter](https://gitlab.gnome.org/GNOME/gnome-multi-writer) - Utility to write an ISO file to multiple USB devices at once `#c` `#gnome`.
- [Imageburner](https://github.com/artemanufrij/imageburner) - Simple imageburner for SD/USB designed for elementaryOS `#vala` `#granite`.
- [Popsicle](https://github.com/pop-os/popsicle) - Utility for flashing multiple USB devices in parallel `#rust`.

### File Management

- [Hyperplane](https://github.com/kra-mo/hyperplane) - Non-hierarchical file manager `#python` `#libadwaita`.
- [Organizer](https://gitlab.gnome.org/aviwad/organizer) - Application to organize your files into categories `#python`.
- [Polo](https://github.com/teejee2008/polo) - Multi-pane and tabbed file manager `#vala`.
- [Portofolio](https://github.com/tchx84/Portfolio) - File manager for mobile devices `#libhandy`.
- [Snoop](https://flathub.org/apps/de.philippun1.Snoop) - Application (with Nautilus extension) to search through file contents in a given folder `#vala` `#libadwaita`.

### File Synchronisation

- [Celeste](https://github.com/hwittenborn/celeste) - File synchronization client that can sync with any cloud provider `#rust` `#libadwaita`.
- [Syncthing-GTK](https://github.com/syncthing/syncthing-gtk) - UI for [Syncthing](https://syncthing.net) with the same features as the Web UI `#python`.

### Remote File Access

- [Taxi](https://github.com/Alecaddd/taxi) - FTP client that also supports SFTP, WebDAV and AFP `#vala` `#granite`.

## System Management

### Software Installation

- [AdwSteamGtk](https://github.com/Foldex/AdwSteamGtk) - [Adwaita for Steam](https://github.com/tkashkin/Adwaita-for-Steam) skin installer `#python` `#libadwaita`.
- [Extension Manager](https://github.com/mjakeman/extension-manager) - Utility for browsing and installing GNOME Shell Extensions `#c` `#libadwaita`.
- [mlinstall](https://petabyt.github.io/mlinstall) - USB Magic Lantern installer `#python`.
- [Parceldude](https://notabug.org/grindhold/parceldude) - Batch installer for Windows MSI packages `#vala`.
- [PinApp](https://github.com/fabrialberio/PinApp) - `.desktop` files creator/editor `#python` `#libadwaita`.
- [Pin It!](https://github.com/ryonakano/pinit) - Portable applications shortcut creator `#vala` `#libadwaita`.
- [ProtonPlus](https://github.com/Vysp3r/ProtonPlus) - Proton version manager `#vala` `#libadwaita`.
- [turtle](https://tenderowl.com/work/turtle) - `.desktop` files creation tool `#python` `#granite`.
- [Nix Software Center](https://github.com/snowfallorg/nix-software-center) - Software center to easity install and manage Nix packages `#rust` `#libadwaita`.
- [Icicle](https://github.com/snowfallorg/icicle) - Graphical installer for NixOS based distributions `#rust` `#libadwaita`.
- [Impression](https://gitlab.com/adhami3310/Impression) - Straight-forward and modern application to create bootable drives `#rust` `#libadwaita`.
- [SimpleSteamTinker](https://github.com/JordanViknar/SimpleSteamTinker) - Simple, and modern Adwaita alternative to SteamTinkerLaunch `#lua` `#libadwaita`.

### System and File Cleaning

- [Czkawka](https://github.com/qarmin/czkawka) - Cross-platform, simple and fast application to remove unnecessary files from your computer `#rust`.
- [BleachBit](https://www.bleachbit.org) - Cross-platform Disk space cleaner and system optimizer `#python`.

### System Configuration

- [Damask](https://gitlab.gnome.org/subpop/damask) - Application that automatically sets wallpaper from a variety or sources (local folder, Wallhaven, Bing Wallpaper, NASA Astronomy, etc) `#vala` `#libadwaita`.
- [doppler](https://github.com/spacekookie/doppler) - Fronted for Redshift allowing to configure different display temperatures for each time of day `#rust`.
- [Dynamic Wallpaper](https://github.com/dusansimic/dynamic-wallpaper) - Dynamic wallpaper creator for GNOME 42 `#python` `#libadwaita`.
- [Nostalgia](https://gitlab.gnome.org/bertob/nostalgia) - Application to set historic GNOME wallpapers `#vala` `#libadwaita`.
- [Lan Mouse](https://github.com/feschber/lan-mouse) - Mouse and keyboard sharing software (software KVM switch) designed for Wayland `#rust` `#libadwaita`.
- [EasySSH](https://github.com/muriloventuroso/easyssh) - SSH connection manager `#vala`.
- [Flatseal](https://github.com/tchx84/Flatseal) - Flatpak permission manager `#gjs` `#libadwaita`.
- [Login Manager Settings](https://gdm-settings.github.io/) - GNOME's Login Manager (GDM) settings manager `#python` `#libadwaita`.
- [NixOS Configuration Editor](https://github.com/vlinkz/nixos-conf-editor) - Application for editing NixOS configurations `#rust` `#libadwaita`.
- [pulse-flow](https://github.com/benwaffle/pulse-flow) - PulseAudio configuration tool with a flow graph UI `#vala`.
- [Shell Configurator](https://gitlab.com/adeswantaTechs/shell-configurator) - GNOME Shell configuration utility with advanced settings `#gjs` `#libadwaita`.
- [ReGreet](https://github.com/rharish101/ReGreet) - GTK-based [greetd](https://git.sr.ht/~kennylevinsen/greetd) greeter `#rust` `#relm4`.
- [SaveDesktop](https://github.com/vikdevelop/SaveDesktop) - Plasma, Xfce and GNOME-based DE configuration saver (icons, fonts, themes, settings, background, GNOME extensions, Flatpak permissions and more) `#python` `#libadwaita`.
- [Warehouse](https://github.com/flattool/warehouse) - Versatile toolbox for viewing flatpak info, managing user data, and batch managing installed flatpaks `#python` `#libadwaita`.

### System Monitoring and Info

- [Bustle](https://flathub.org/apps/org.freedesktop.Bustle) - D-Bus activity viewer that draws diagram sequences `#rust` `#libadwaita`.
- [CPU-X](https://thetumultuousunicornofdarkness.github.io/CPU-X) - System profiling and monitoring application (similar to CPU-Z for Windows) `#c`.
- [GNOME Disk Usage Analyzer](https://apps.gnome.org/Baobab) - Disk usage analyzer, also known as Baobab, with DaisyDisk style circle chart `#vala` `#gnome`.
- [GNOME Logs](https://apps.gnome.org/Logs/) - systemd logs viewer `#c` `#gnome` `#libadwaita`.
- [GNOME Usage](https://gitlab.gnome.org/GNOME/gnome-usage) - System resources monitoring for the GNOME desktop `#vala` `#gnome`.
- [GreenWithEnvy](https://gitlab.com/leinardi/gwe) - NVIDIA card monitoring and fan/OC controlling application `#python`.
- [Inspector](https://flathub.org/apps/io.github.nokse22.inspector) - Application to view system information such as USB/disk/PCIE/networks devices and motherboard/CPU information `#python` `#libadwaita`.
- [Mission Center](https://missioncenter.io) - CPU, memory, disk, network and GPU usage monitor `#rust` `#libadwaita`.
- [Monitorets](https://github.com/jorchube/monitorets) - CPU, memory, disk, network and GPU usage monitor widget `#python` `#libadwaita`.
- [Resources](https://github.com/nokyan/resources) - CPU, memory, GPUs, network interfaces and block devices usage monitor `#rust` `#libadwaita`.
- [Snowglobe](https://gitlab.gnome.org/bilelmoussaoui/snowglobe) - Virtualization viewer using QEMU over DBus `#c` `#libadwaita`.
- [sysctlview](https://gitlab.com/alfix/sysctlview) - FreeBSD sysctl MIB tree explorer `#c++`.
- [Monitor](https://github.com/stsdc/monitor) - Manage processes and monitor system resources `#vala` `#elementaryos`.

### Task Scheduling

- [Time Switch](https://github.com/fsobolev/timeswitch) - Computer shutdown timer `#python` `#libadwaita`.

## Gaming

- [An Anime Game launcher](https://github.com/an-anime-team/an-anime-game-launcher) - Genshin Impact launcher for Linux with telemetry disabling `#rust` `#libadwaita`.
- [Cartridges](https://github.com/kra-mo/cartridges) - Game launcher with Steam, Lutris, Heroic, Legendary, Bottles, itch and RetroArch library import `#python` `#libadwaita`.
- [Lutris](https://lutris.net) - Game launcher covering most gaming systems `#python`.
- [Gameeky](https://github.com/tchx84/gameeky) - Application to create and play games without any code for young learners and educators `#python` `#libadwaita`.
- [Keypunch](https://github.com/bragefuglseth/keypunch) - Keyboard typing test like monkeytype `#rust` `#libadwaita`.

### Board Games

- [Chess Clock](https://flathub.org/apps/com.clarahobbs.chessclock) - Timer for over-the-board chess games `#python` `#libadwaita`.
- [Crosswords](https://flathub.org/apps/org.gnome.Crosswords) - Game of crosswords with squpport for shaped and colors crosswords and `.ipuz`, `.jpuz`, `.xd`, and `.puz` files `#c` `#libadwaita`.
- [Mahjongg](https://gitlab.gnome.org/GNOME/gnome-mahjongg) - Solitaire (one player) version of the classic Eastern tile game, Mahjongg `#gnome` `#vala` `#libadwaita`.
- [Ultimate Tic Tac Toe](https://github.com/Nokse22/ultimate-tic-tac-toe) - [Ultimate Tic Tac Toe](https://en.wikipedia.org/wiki/Ultimate_tic-tac-toe) to play with friends or against an AI `#python` `#libadwaita`.

### Puzzles

- [Multiplication Puzzle](https://gitlab.gnome.org/mterry/gmult) - Simple game inspired by the multiplication game from emacs.
- [SemantiK](https://gitlab.com/Krafting/semantik-gtk) - Word-game where you need to find a secret word.

## Health and Fitness

- [Health](https://gitlab.gnome.org/World/Health) - Fitness goals tracker `#rust` `#libadwaita`.
- [Dosage](https://github.com/diegopvlk/Dosage) - Medication tracker `#gjs` `#libadwaita`.

## Map Viewers

- [Atlas](https://github.com/ryonakano/atlas) - Map viewer designed for elementaryOS `#vala` `#granite` `#libhandy`.

## Public Transports

- [Railway](https://gitlab.com/schmiddi-on-mobile/railway) - Application to look up information about (german) train journeys in one place `#rust` `#libadwaita`.  

## Weather Viewers

- [GNOME Weather](https://apps.gnome.org/Weather) - Weather application for the GNOME desktop `#gjs` `#gnome`.
- [Nimbus](https://github.com/danrabbit/nimbus) - Minimal weather applet `#vala` `#libhandy`.
- [Meteo](https://gitlab.com/bitseater/meteo) - Forecast application using OpenWeatherMap API `#vala`.
- [Mousam](https://github.com/amit9838/mousam) - Lightweight weather application with dynamically changing gradient-based background according to current weather condition `#python` `#libadwaita`.
