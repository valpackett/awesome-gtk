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
  - [Chat and VoIP](#chat-and-voip)
  - [Email](#email)
  - [File Sharing](#file-sharing)
  - [Network Monitoring](#network-monitoring)
  - [News/Feed Readers](#newsfeed-readers)
  - [Social Media Clients](#social-media-clients)
  - [Specialized Web Browsers / Wrappers](#specialized-web-browsers--wrappers)
  - [Web Browsers](#web-browsers)
- [Office](#office)
  - [Book Readers](#book-readers)
  - [Calculators & Math](#calculators--math)
  - [Calendar](#calendar)
  - [Document Managers](#document-managers)
  - [Document Viewers](#document-viewers)
  - [Note-taking](#note-taking)
  - [OCR](#ocr)
  - [PDF Tools](#pdf-tools)
  - [Presentation](#presentation)
- [Productivity](#productivity)
  - [Desktop Productivity](#desktop-productivity)
  - [Mind-mapping](#mind-mapping)
  - [Project Management](#project-management)
  - [Timers / Time Tracking](#timers--time-tracking)
  - [To-do Lists](#to-do-lists)
- [Design](#design)
- [Finance](#finance)
  - [Budget and Accounting Managers](#budget-and-accounting-managers)
  - [Exchange Rate Viewers](#exchange-rate-viewers)

## Apps for GNOME

You can find the most up-to-date info on the most well-supported GNOME apps at [Apps for GNOME](https://apps.gnome.org/);
this list aims to be broader and include apps from various other ecosystems in various states of maintenance.

## Audio

### Audio Players

#### Music Players

- [Lollypop](https://gitlab.gnome.org/World/lollypop) - Lightweight modern music player designed to work excellently on the GNOME desktop environment with party mode, metadata fetching, MTP device sync and scrobbling `#python` `#libhandy`.
- [Melody](http://anufrij.org/melody) - Music player designed for elementary OS with metadata fetching, online radio and MTP device sync `#vala` `#granite`.
- [elementary Music](https://github.com/elementary/music) - Official music player for elementary OS `#vala` `#granite`.
- [GNOME Music](https://wiki.gnome.org/Apps/Music) - Official GNOME desktop music player `#python` `#libadwaita` `#gnome`.
- [Rhythmbox](https://wiki.gnome.org/Apps/Rhythmbox/) - Music management application designed to work well under the GNOME desktop supporting network shares, podcasts, online radio, portable devices (including iPhones) and internet music services such as Last.fm and Magnatune `#c` `#gnome`.
- [Amberol](https://gitlab.gnome.org/ebassi/amberol) - Simple music player well integrated with GNOME `#rust` `#libadwaita`.
- [G4Music](https://github.com/neithern/g4music) - Light-weight music player focusing on high performance supporting ReplayGain, pipewire audio sink and MPRIS control `#vala` `#libadwaita`.

#### Audio Streaming Service Clients

- [Spot](https://github.com/xou816/spot) - Spotify (premium) client for the GNOME desktop with MPRIS integration based on [librespot](https://github.com/librespot-org/librespot) `#rust` `#libadwaita`.
- [Sublime Music](https://sublimemusic.app) - Client for Subsonic-compatible (Subsonic, Airsonic, Revel, Gonic, Navidrome, Ampache, *sonic) personal streaming servers `#python`.

#### MPD Clients

- [Sonata](https://github.com/multani/sonata) - MPD client with tag editor and audio scrobbling support, currently looking for a new maintainer `#python`.
- [Mpdevil](https://github.com/SoongNoonien/mpdevil) - MPD music browser with MPRIS interface `#python`.

#### Podcasts

- [GNOME Podcasts](https://gitlab.gnome.org/World/podcasts) - (ex Hammond) Official GNOME Podcast client `#rust` `#libadwaita` `#gnome`.
- [Vocal](https://vocalproject.net/https://github.com/needle-and-thread/vocal) - Podcast application with iTunes Store integration and smart library management `#vala` `#granite`.

#### Audiobooks

- [Cozy](https://cozy.sh) - Audiobook player with offline library management and MPRIS integration `#python`.

#### Radio

- [Shortwave](https://gitlab.gnome.org/World/Shortwave) - Internet radio player providing access to the community radio station database [radio-browser.info](http://www.radio-browser.info) `#rust` `#libadwaita`.
- [Goodvibes](https://gitlab.com/goodvibes/goodvibes) - Simple light-weight internet radio player `#c`.
- [radiotray-lite](https://github.com/thekvs/radiotray-lite) - Online radio player with minimal interface that runs on the system tray `#c++`.
- [Pithos](https://pithos.github.io/) - Pandora Radio client `#python`.

#### Transcription

- [Parlatype](https://gkarsay.github.io/parlatype) - Minimal audio player for manual speech transcription `#c`.

#### Ambient Sounds

- [Blanket](https://github.com/rafaelmardojai/blanket) - Ambient sound player/mixer with preset management and MPRIS integration `#python` `#libadwaita`.

#### Soundboards

- [Zap](https://gitlab.com/rmnvgr/zap) - Sound effects soundboard and collection manager `#gjs` `#libadwaita`.

### Audio Workstations (DAWs)

- [zrythm](https://github.com/zrythm/zrythm) - DAW offering streamlined editing workflows with automation capabilities, chord assistance and support for plugins `#c++` `#libadwaita`.

### Audio Tools

- [Lyrebird](https://github.com/lyrebird-voice-changer/lyrebird) - Voice changer based on SoX `#python`.
- [Tagger](https://github.com/nlogozzo/NickvisionTagger) - Music tag (metadata) editor `#c++` `#libadwaita`.
- [EasyEffects](https://github.com/wwmm/easyeffects) - Audio effects manager (limiter, convolver, equalizer, autovolume and more) for PipeWire applications `#c++` `#libadwaita`.
- [Myxer](https://github.com/VixenUtils/Myxer) - PulseAudio volume mixer `#rust`.
- [Reco](https://github.com/ryonakano/reco) - Audio recorder `#vala` `#granite`.
- [Mousai](https://github.com/SeaDve/Mousai) - Song identifier based on [AudD](https://audd.io/) `#rust` `#libadwaita`.
- [Ear Tag](https://github.com/knuxify/eartag) - Tag editor designed to edit singular files `#python` `#libadwaita`.
- [Asunder](https://gitlab.gnome.org/Salamandar/asunder) - CD ripper and encoder `#c`.
- [Cavalier](https://github.com/fsobolev/cavalier) - Audio visualizer based on [CAVA](https://github.com/karlstav/cava) `#python` `#libadwaita`.

## Video

### Video Players

- [Celluloid](https://github.com/celluloid-player/celluloid) - (ex GNOME MPV) frontend for MPV `#c` `#libadwaita`.
- [Clapper](https://github.com/Rafostar/clapper) - Media player powered by GStreamer with OpenGL rendering `#gjs` `#c`.
- [Movie Monad](https://lettier.github.io/movie-monad/) - Simple video player powered by GStreamer `#haskell`.
- [GNOME Videos](https://wiki.gnome.org/Apps/Videos) - Official GNOME desktop video player, also known as Totem `#c` `#gnome`.
- [Glide](https://github.com/philn/glide) - Simple video player powered by GStreamer `#rust`.

### Live Stream Viewers

- [GNOME Twitch](https://gnome-twitch.vinszent.com) - Twitch client supporting multiple video backends and with subscription management `#c`.

### Video Editors

- [Pitivi](http://www.pitivi.org) - Video editor based on GStreamer Editor Services `#python`.
- [Video Trimmer](https://gitlab.gnome.org/YaLTeR/video-trimmer) - Application to cut out fragments of a video without re-encoding and reducing video quality `#rust` `#libadwaita`.

### Subtitle Editors

- [Gaupol](https://otsaloma.io/gaupol) - Editor for text-based subtitle files with built-in video player `#python`.
- [Subtitle Editor](https://kitone.github.io/subtitleeditor/) - Subtitle editor with built-in video player and text correction features `#c++`.

### Screen Recorders

- [Kooha](https://github.com/SeaDve/Kooha) - Distraction-free screen recorder `#rust` `#libadwaita`.
- [RecApp](https://github.com/amikha1lov/RecApp) - (archived) Simple screencasting application based on GStreamer `#python`.

### Video Tools

- [Identity](https://gitlab.gnome.org/YaLTeR/identity) - Program for comparing multiple versions of an image or video `#rust` `#libadwaita`.
- [media-toc](https://github.com/fengalin/media-toc) - Application to build a table of contents from a media or to split a media file into chapters `#rust`.

## Graphics

### 3D Graphics

- [Shady](https://github.com/misterdanb/shady) - [Shadertoy](https://github.com/misterdanb/shady/blob/master/Shadertoy.com) compatible GLSL shader live editor `#vala`.

### Image Viewers

- [Image Roll](https://github.com/weclaw1/image-roll) - Simple and fast image viewer with basic image manipulation tools `#rust`.
- [Loupe](https://gitlab.gnome.org/BrainBlasted/loupe) - Simple image viewer `#rust` `#libadwaita`.
- [vipsdisp](https://github.com/jcupitt/vipsdisp) - Image viewer based on [`libvips`](https://github.com/libvips/libvips) supporting many scientific and technical image formats `#c`.

### Raster Graphics

#### Converters

- [Converter](https://gitlab.com/adhami3310/Converter) - [ImageMagick](https://imagemagick.org) frontend `#python` `#libadwaita`.

#### Drawing & Editing

- [Drawing](https://github.com/maoschanz/drawing) - Simple image editor similar to Microsoft paint designed for the GNOME desktop `#python`.
- [Effector](https://notabug.org/grindhold/effector) - GEGL filter app with a flow graph UI `#vala`.
- [GIMP](https://www.gimp.or/) - Raster graphics editor used for image manipulation, image editing, free-form drawing and more specialized stask `#c`.
- [MyPaint](http://mypaint.org) - Simple drawing and painting program with support for Wacom-style graphics tablets `#python`.
- [Obfuscate](https://gitlab.gnome.org/World/obfuscate) - Private information censoring tool `#rust` `#libadwaita`.
- [Swappy](https://github.com/jtheoof/swappy) - Wayland native screenshot editing tool `#c`.

#### GIF

- [Gifcurry](https://lettier.github.io/gifcurry) - GIF editor and video-to-GIF converter application `#haskell`.
- [Gifup](https://github.com/BharatKalluri/Gifup) - Video-to-GIF converter `#vala` `#granite`.

#### Optimizers/Compressors

- [Curtail](https://github.com/Huluti/Curtail) - Image compressor with support for PNG, JPEG and WebP images `#python`.
- [Refract](https://github.com/Blobfolio/refract) - *Guided* image optimization for JPEGs and PNGs producing WebP, AVIF and JPEG XL clones `#rust`.

#### Photography

- [Darktable](https://www.darktable.org) - Photography workflow application and raw developer `#c`.
- [RawTherapee](http://rawtherapee.com) - Raw image processing program `#c++`.
- [Shotwell](https://wiki.gnome.org/Apps/Shotwell) - Personal photo manager with editing features `#vala` `#gnome`.

#### Upscalers

- [Upscaler](https://gitlab.com/TheEvilSkeleton/Upscaler) - Image upscaler based on [Real-ESRGAN ncnn Vulkan](https://github.com/xinntao/Real-ESRGAN-ncnn-vulkan) `#python` `#libadwaita`.

### Technical Graphics

- [Design](https://github.com/dubstar-04/Design) - 2D CAD application with DXF format support `#gjs` `#libadwaita`.
- [Focus Annotator](https://github.com/13hannes11/focus_annotator) - Tool to annotate the focus plane of z-stacked images `#rust` `#libadwaita`.
- [Gaphor](https://gaphor.org) - UML/SysML modeling application `#python`.
- [Horizon](https://github.com/horizon-eda/horizon) - EDA package supporting an integrated end-to-end workflow for printed circuit design `#c++` `#gl`.
- [SolveSpace](http://solvespace.com/index.pl) - Parametric 2D/3D CAD tool `#c++` `#gl`.

### Vector & Fonts

- [Birdfont](https://github.com/johanmattssonm/birdfont) - Font editor for creating fonts in TTF, EOT, SVG and BIRDFONT formats `#vala`.
- [Font Downloader](https://github.com/GustavoPeredo/font-downloader) - Download utility for Google Fonts `#python` `#libhandy`.
- [Inkscape](https://inkscape.org) - General vector graphics editor using GTK since version 1.0 `#c++`.
- [Pizzara](https://pizarra.categulario.xyz/en) - Digital, vectorial and infinite chalkboard for free-hand drawing `#libadwaita`.
- [Webfont Kit Generator](https://github.com/rafaelmardojai/webfont-kit-generator) - Utility to create web font-face kits `#python` `#libadwaita`.

## Multimedia

### Media Downloaders

- [Gydl](https://github.com/JannikHv/gydl) - GUI wrapper around [youtube-dl](https://youtube-dl.org) `#python`.
- [Tube Converter](https://github.com/nlogozzo/NickvisionTubeConverter) - [yt-dlp](https://github.com/yt-dlp/yt-dlp) graphical fronted `#c++`  `#libadwaita`.

### Media Encoders

- [Selene](https://github.com/teejee2008/selene) - Audio/video converter for audio and videos files that can encode them to popular output formats like MKV and MP4 `#vala`.

### Media Servers

- [Girens](https://gitlab.gnome.org/tijder/girens) - Plex media player client with responsive layout and function to download media items `#python` `#libadwaita`.

## Internet and Networking

### Chat and VoIP

- [Dino](https://dino.im) - Modern XMPP/Jabber chat client `#vala` `#libadwaita`.
- [Discover](https://github.com/trigg/Discover) - Discord overlay with X11 and wlroots support `#python`.
- [Flare](https://gitlab.com/Schmiddiii/flare) - Signal client `#rust` `#libadwaita`.
- [Fractal](https://gitlab.gnome.org/GNOME/fractal) - Matrix client for the GNOME desktop `#rust` `#libadwaita`.
- [Gajim](https://gajim.org) - Fully-featured XMPP client `#python`.
- [gtkcord4](https://github.com/diamondburned/gtkcord4) - Discord client written in `#go`.
- [Meeting Point](https://gitlab.gnome.org/lwildberg/meeting-point) - BigBlueButton client `#vala` `#libadwaita`.
- [Mirdorph](https://gitlab.gnome.org/ranchester/mirdorph) - Crappy low feature Discord client `#python` `#libadwaita`.
- [Polari](https://wiki.gnome.org/Apps/Polari) - IRC client `#gjs` `#gnome`.
- [Telegrand](https://github.com/melix99/telegrand) - Telegram client for the GNOME desktop `#rust` `#libadwaita`.
- [Srain](https://srain.silverrainz.me) - Modern IRC client `#c`.

### Email

- [Astroid](https://astroidmail.github.io) - Lightweight and fast Mail User Agent that provides a GUI to searching, displaying and composing email using [notmuch](https://notmuchmail.org) as backend `#c++`.
- [Geary](https://wiki.gnome.org/Apps/Geary) - Email application for the GNOME desktop build around conversations `#vala` `#gnome` `#libhandy`.
- [Evolution](https://wiki.gnome.org/Apps/Evolution) - Personal information management application that provides integrated mail, calendaring and address book functionality `#c` `#gnome`.

### File Sharing

- [Deluge](https://deluge-torrent.org) - BitTorrent client available for Linux, macOS and Windows `#python`.
- [Fragments](https://gitlab.gnome.org/World/Fragments) - BitTorrent client built on top of Transmission `#rust` `#libadwaita`.
- [Nicotine+](https://nicotine-plus.org) - Graphical client for the [Soulseek](https://www.slsknet.org) peer-to-peer network `#python`.
- [Teleport](https://gitlab.gnome.org/jsparber/teleport) - Network file sharing application based on Avahi (mDNS) `#c`.
- [Transmission](https://transmissionbt.com) - BitTorrent client for macOS, Windows and Linux `#c`.
- [Transporter](https://github.com/bleakgrey/Transporter) - (archived) [magic-wormhole] client for elementary OS `#vala` `#granite`.
- [Warp](https://gitlab.gnome.org/World/warp) based on [magic-wormhole] #rust #libadwaita
- [Torrential](https://github.com/davidmhewitt/torrential) alternative GUI on top of Transmission #vala #granite #libunity

[magic-wormhole]: https://github.com/warner/magic-wormhole

### Network Monitoring

- [Hotwire](https://github.com/emmanueltouzery/hotwire) - GUI that leverages the wireshark and tshark infrastructure to capture traffic and explore the contents of tcpdump files `#rust`.

### News/Feed Readers

- [Coffee](https://nick92.github.io/coffee) - News and weather reader for sources provided by News API and DarkSky `#vala`.
- [Feeds](https://gfeeds.gabmus.org) - News reader for the GNOME desktop `#python` `#libadwaita`.
- [Liferea](https://lzone.de/liferea) - News reader with a GUI similar to desktop mail client and with an embedded web browser `#c`.
- [NewsFlash](https://gitlab.com/news-flash/news_flash_gtk) - News reader designed to complement an already existing web-based RSS reader account `#rust` `#libadwaita`.

### Social Media Clients

- [Cawbird](https://github.com/IBBoard/cawbird) - (archived) Fork of the [Corebird](https://github.com/baedert/corebird) client for Twitter discontinued from January 2023 `#vala`.
- [Giara](https://gitlab.gnome.org/World/giara) - Reddit fronted created with Linux in mind `#python` `#libadwaita`.
- [Headlines](https://gitlab.com/caveman250/Headlines) - Reddit client `#c++` `#libadwaita`.
- [NewCaw](https://github.com/CodedOre/NewCaw) - Rewrite of Cawbird as a Mastodon client `#vala` `#libadwaita`.
- [Social](https://gitlab.gnome.org/World/Social) - Mastodon and Pleroma client `#rust`.
- [Tootle](https://gitlab.gnome.org/World/tootle) - Mastodon client `#vala` `#libadwaita`.
- [Tooth](https://github.com/GeopJr/Tooth) - Mastodon client fork of Tootle `#vala` `#libadwaita`.

### Specialized Web Browsers / Wrappers

- [Geopard](https://ranfdev.com/projects/geopard) - Gemini web browser `#rust` `#libadwaita`.
- [HackUp](https://github.com/mdh34/hackup) - [Hacker News](https://news.ycombinator.com) client `#vala` `#granite`.
- [Lobjur](https://github.com/ranfdev/Lobjur) - [lobste.rs](https://lobste.rs) client `#gjs` `#libadwaita`.
- [Tally](https://github.com/cassidyjames/Tally) - Plausible Analytics (Google Analytics alternative) client `#vala` `#libadwaita`.
- [Tangram](https://github.com/sonnyp/Tangram) - Browser for your pinned tabs `#gjs` `#libadwaita`.
- [Wike](https://hugolabe.github.io/Wike) - Wikipedia client `#python`.

### Web Browsers

- [Eolie](https://wiki.gnome.org/Apps/Eolie) - Web browser for the GNOME desktop with Firefox Sync support `#python` `#libhandy`.
- [GNOME Web (Epiphany)](https://wiki.gnome.org/Apps/Web) - Web browser for the GNOME desktop based on the [WebKit] endering engine `#c` `#gnome` `#libadwaita`.
- [luakit](https://luakit.github.io) - Highly configurable browser based on the [WebKit] engine and extensible with Lua `#c` `#lua`.

[webkit]: https://webkit.org

## Office

### Book Readers

- [Bookworm](https://babluboy.github.io/bookworm) - Simple eBook reader for elementary OS `#vala` `#granite`.
- [Foliate](https://github.com/johnfactotum/foliate) - Simple and modern eBook reader based on [Epub.js](https://github.com/futurepress/epub.js) `#gjs` `#libhandy`.
- [Komikku](https://valos.gitlab.io/Komikku) - Manga reader for the GNOME desktop with online and offline reading `#python` `#libadwaita`.

### Calculators & Math

- [balistica](https://github.com/fusilero/balistica) - Exterior ballistics calculator `#vala`.
- [Dippi](https://github.com/cassidyjames/dippi) - Display DPI calculator `#vala` `#libadwaita`.
- [Graphs](https://github.com/SjoerdB93/Graphs) - Plotting and data manipulation tool for the GNOME desktop `#python` `#libadwaita`.
- [NaSC](http://parnold-x.github.io/nasc) - Dual pane text based calculator `#vala`.
- [Plots](https://github.com/alexhuntley/Plots) - Graph plotting app for the GNOME desktop `#python` `#opengl`.
- [Qalculate! GTK+](https://qalculate.github.io) - Multi-purpose cross-platform desktop calculator `#c++`.
- [Gnumeric](http://www.gnumeric.org) - Spreadsheet editor `#c`.

### Calendar

- [GNOME Calendar](https://wiki.gnome.org/Apps/Calendar) - Simple calendar for the GNOME desktop `#c` `#libadwaita` `#gnome`.

### Document Managers

- [GNOME Documents](https://wiki.gnome.org/Apps/Documents) - (archived) Document manager for the GNOME desktop with collection features `#gjs`.
- [Paperwork](https://openpaper.work) - Document manager with scan features `#python`.

### Document Viewers

- [Xreader](https://github.com/linuxmint/xreader) - Generic document viewer with support for PDF, Postscript, djvu, comics and more `#c` `#xapps`.
- [Evince](https://wiki.gnome.org/Apps/Evince) - Document viewer for the GNOME desktop with support for PDF, Postscript, djvu, comics etc. and SyncTex support with gedit `#c` `#libhandy` `#gnome`.

### Note-taking

- [GNOME Notes](https://wiki.gnome.org/Apps/Notes) - Simple note editor for the GNOME desktop, also known as Bijiben `#c` `#gnome`.
- [Gnote](https://wiki.gnome.org/Apps/Gnote) - Note-taking application for the GNOME desktop started as a Tomboy port `#c++` `#gnome`.
- [Iridium](https://github.com/matze/iridium) - [Standard Notes](https://standardnotes.org) local-first client `#rust`.
- [Notejot](https://github.com/lainsce/notejot) - Stupidly simple notes application `#vala` `#granite`.
- [Notekit](https://github.com/blackhole89/notekit) - Hierarchical Markdown note-taking application with tablet support `#c++`.
- [Notes](https://github.com/Blquinn/notes) - Note-taking application for the GNOME desktop with notebook based categorization, trash and dark theme `#vala` `#libadwaita`.
- [Notes-Up](https://github.com/Philip-Scott/Notes-up) - Markdown note manager for elementary OS `#vala` `#granite`.
- [Noteworthy](https://github.com/SeaDve/Noteworthy) - Modern, fast, and version-controlled Markdown notes application `#rust` `#libadwaita`.
- [Notorious](https://gitlab.gnome.org/GabMus/notorious) - Keyboard-centric notes application `#python` `#libhandy`.
- [RedNotebook](https://rednotebook.sourceforge.io) - Desktop journal application that lets you format, tag and search your entries `#python`.
- [Rnote](https://github.com/flxzt/rnote) - Vector-based drawing app for sketching, handwritten notes and to annotate documents and pictures with pressure-sensitive stylus input support `#rust` `#libadwaita`.
- [Xournal++](https://xournalpp.github.io) - Cross-platform handwriting note-taking software with PDF annotation support and support for pen input form devices such as Wacom tablets `#c++`.
- [Zim](https://github.com/zim-desktop-wiki/zim-desktop-wiki) - Text editor used to maintain a collection of wiki pages `#python`.

### OCR

- [Frog](https://tenderowl.com/work/frog) - Intuitive text extraction tool for the GNOME desktop.
- [gImageView](https://github.com/manisandro/gImageReader) - GTK/Qt front-end to [Tesseract] `#c++`.
- [TextSnatcher](https://github.com/RajSolai/TextSnatcher) - Easy to use OCR application based on [Tesseract] `#vala` `#granite`.

[tesseract]: https://github.com/tesseract-ocr/tesseract

### PDF Tools

- [PDF Arranger](https://github.com/pdfarranger/pdfarranger) - PDF editor with merging, splitting, rotating, cropping and rearranging based on [pikepdf](https://github.com/pikepdf/pikepdf) `#python`.
- [PDF Slicer](https://junrrein.github.io/pdfslicer) - Simple application to extract, merge, rotate and reorder pages of PDF documents with undo/redo support `#c++`.

### Presentation

- [pdfpc](https://pdfpc.github.io) - Presentation console with multi-monitor support for PDF files `#vala`.
- [Pympress](https://github.com/Cimbali/pympress) - Presentation tool designed for dual-screen setups such as presentations and public talks `#python`.
- [Spice-up](https://github.com/Philip-Scott/Spice-up) - Web presentation editor `#vala` `#granite`.

## Productivity

### Desktop Productivity

- [Boatswain](https://gitlab.gnome.org/World/boatswain) - Elgato Stream Deck controller `#c` `#libadwaita`.
- [Cigale](https://github.com/emmanueltouzery/cigale) - Timesheet for your activities with support for emails, Git, GitLab and Stack Exchange `#rust`.
- [GNOME Characters](https://apps.gnome.org/app/org.gnome.Characters) emoji picker #gnome #c #libadwaita
- [Random](https://random.amongtech.cc) - Randomization made easy with advanced functions `#vala` `#libadwaita`.
- [Workspaces](https://github.com/DevAlien/workspaces) - Desktop workpaces for elementaryOS `#vala` `#granite`.

### Mind-mapping

- [Minder](https://github.com/phase1geo/Minder) - Mind-mapping application for elementaryOS `#vala` `#granite`.

### Project Management

- [Planner](https://useplanner.com) - Project and task manager with Todoist support `#vala` `#granite`.

### Timers / Time Tracking

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
- [Yishu](https://github.com/lainsce/yishu) - (archived) Simple [todo.txt] client `#vala` `#granite` `#libhandy`.

[todo.txt]: https://github.com/todotxt/todo.txt

## Finance

### Budget and Accounting Managers

- [Denaro](https://github.com/nlogozzo/NickvisionMoney) - Cross-platform personal finance manager `#c++` `#libadwaita`.
- [Envelope](https://github.com/cjfloss/envelope) - Personal finance manager for elementaryOS `#vala` `#granite`.
- [Grisbi](http://grisbi.org) - 20 years old accounting application `#c`.

### Exchange Rate Viewers

- [Crypto](https://gitlab.com/ErikWallstrom/Crypto) - Cryptocyrreny watcher `#c`.
- [Markets](https://github.com/bitstower/markets) - Stock, currency and cryptocurrency tracker `#vala` `#libhandy`.

## Design

- [Emulsion](https://github.com/lainsce/emulsion) - Color palette manager `#vala` `#libadwaita`.
- [Eyedropper](https://github.com/FineFindus/eyedropper) - Color picker and formatter `#rust` `#libadwaita`.
- [Harvey](https://github.com/danrabbit/harvey) - Color contrast calculator `#vala`.
- [Icon Library](https://gitlab.gnome.org/World/design/icon-library) - System icon browser `#rust` `libadwaita`.
- [Icon Preview](https://gitlab.gnome.org/World/design/app-icon-preview) - Application icon previewer for designing application icons `#vala`.
- [LookBook](https://github.com/danrabbit/lookbook) - System icon browser `#vala` `#granite`.
- [Paleta](https://github.com/nate-xyz/paleta) - Image dominant color extractor `#python` `#libadwaita`.
- [Symbolic Preview](https://gitlab.gnome.org/World/design/symbolic-preview) - Symbolic icon previwer `#rust` `#libadwaita`.

## TODO

### Web Service Clients

#### Translation

- [Dialect](https://github.com/gi-lom/dialect) (Google Translate) #python #libadwaita

### File Synchronization

- [Syncthing-GTK](https://github.com/syncthing/syncthing-gtk) UI for [Syncthing](https://syncthing.net/) #python

### Remote File Access

- [Taxi](https://github.com/Alecaddd/taxi) FTP, SFTP, WebDAV, AFP #vala #granite

### File Management

- [Polo](https://github.com/teejee2008/polo) multi-pane & tab file manager #vala
- [Organizer](https://gitlab.gnome.org/aviwad/organizer) #python
- [Portofolio](https://github.com/tchx84/Portfolio) file manager for mobile devices #libhandy

### Backup

- [Pika Backup](https://gitlab.gnome.org/World/pika-backup) UI for [borg](https://github.com/borgbackup/borg) #rust #libadwaita
- ~~[Bups](https://github.com/emersion/bups) UI for [bup](https://github.com/bup/bup) #python~~ (note: [python2](https://github.com/emersion/bups/issues/34)!)
- [Timeshift](https://github.com/linuxmint/timeshift) #vala
- [Déjà Dup Backups](https://wiki.gnome.org/Apps/DejaDup) #vala #libadwaita
- [Butter](https://github.com/zhangyuannie/butter) Btrfs snapshot manager #rust #libadwaita

### Terminals

- [Galacritty](https://github.com/myfreeweb/galacritty) (shameless plug :D) GTK version of [Alacritty](https://github.com/jwilm/alacritty) (not really maintained for now sorry) #rust
- [Guake](https://github.com/Guake/guake) dropdown terminal #python #vte
- [Tilix](https://github.com/gnunn1/tilix) tiling and dropdown terminal #d #vte
- [GNOME Console](https://gitlab.gnome.org/GNOME/console) #c #vte #gnome
- [GNOME Terminal](https://gitlab.gnome.org/GNOME/gnome-terminal) #c #vte #gnome
- [Black Box](https://gitlab.gnome.org/raggesilver/blackbox) #vala #libdwaita #vte

### Code

#### NeoVim GUIs

- [gnvim](https://github.com/vhakulinen/gnvim) #rust
- [neovim-gtk](https://github.com/daa84/neovim-gtk) #rust
  - [maintained fork](https://github.com/Lyude/neovim-gtk)
- [nvim-pygtk3](https://github.com/rliang/nvim-pygtk3) #python

#### Xi GUIs

- [Tau (ex gxi)](https://gitlab.gnome.org/World/Tau) #rust
- [xi-gtk](https://github.com/eyelash/xi-gtk) #vala

#### Simple editors and Light IDEs

- [gedit](https://wiki.gnome.org/Apps/Gedit) #c #gnome
- [Geany](https://www.geany.org/) #c
- [Vulcan](https://github.com/zesterer/vulcan) #vala
- [elementary IDE](https://github.com/donadigo/elementary-ide) not official elementary #vala #granite
- [elementary Code](https://github.com/elementary/code) #vala #granite
- [NEd](https://github.com/ngtk3/NEd) #nim
- [Xed](https://github.com/linuxmint/xed) #c #xapps
- [GNOME Text Editor](https://gitlab.gnome.org/GNOME/gnome-text-editor) #c #gnome
- [Norka](https://tenderowl.com/work/norka) #python #granite

#### Larger IDEs

- [GNOME Builder](https://wiki.gnome.org/Apps/Builder) #c #gnome
- [Anjuta](https://wiki.gnome.org/Apps/Anjuta) #c #gnome
- [Valama](https://github.com/Valama/valama) #vala
- [GtkIDE.jl](https://github.com/jonathanBieler/GtkIDE.jl) #julia
- [Workbench](https://github.com/sonnyp/Workbench) #gjs #libadwaita
- [Playhouse](https://github.com/sonnyp/Playhouse) Playground for HTML/CSS/JavaScript #gjs #libadwaita

### UI Design

- [Glade](https://glade.gnome.org/) #c #gnome
- [Cambalache](https://gitlab.gnome.org/jpu/cambalache) Glade's successor #python
- [Gradience](https://github.com/GradienceTeam/Gradience) Libadwaita apps customizer #python #libadwaita

### Version Control and Diffs

- [gitg](https://wiki.gnome.org/Apps/Gitg) Git GUI client #vala #gnome
- [Meld](https://gitlab.gnome.org/GNOME/meld) visual diff and merge tool #python #gnome
- [Gnomit](https://github.com/small-tech/gnomit) Git commit message editor #gjs
- [Commit](https://github.com/sonnyp/Commit) Commit message editor for Git and Mercurial #gjs #libadwaita
- [Diffuse](https://github.com/MightyCreak/diffuse) text file comparing/merging tool #python

### Documentation

- [DevDocs Desktop](https://github.com/hardpixel/devdocs-desktop) #python
- [quickDocs](https://github.com/mdh34/quickDocs) #vala #granite

### Markdown

- [Marker](https://github.com/fabiocolacio/Marker) #c
- [Showdown](https://github.com/craigbarnes/showdown) #vala
- [Apostrophe](https://gitlab.gnome.org/World/apostrophe) #python #libhandy
- [markdown-rs](https://github.com/nilgradisnik/markdown-rs) #rust
- [Quilter](https://github.com/lainsce/quilter) #vala #libhandy
- [Paper](https://posidon.io/paper) #vala #libadwaita

### LaTeX

- [Gummi](https://github.com/alexandervdm/gummi) #c
- [GNOME LaTeX (LaTeXila)](https://wiki.gnome.org/Apps/GNOME-LaTeX) #vala #gnome
- [Setzer](https://github.com/cvfosammmm/Setzer) #python
- [Citations](https://gitlab.gnome.org/World/citations) BibTex bibliography manager #rust #libadwaita

### Graphviz

- [xdot.py](https://github.com/jrfonseca/xdot.py) #python
- [GraphUI](https://github.com/artemanufrij/graphui) #vala #granite

### Regular Expression

- [RegexTester](https://github.com/artemanufrij/regextester) #vala #granite

### Text Processing

- [Text Pieces](https://github.com/liferooter/textpieces) #vala #libadwaita
- [KonbuCase](https://github.com/ryonakano/konbucase) case converting app #vala #granite
- [Black Fennec](https://gitlab.ost.ch/blackfennec/blackfennec) visual semi-structured data (JSON) editor #python #libadwaita

### Hex Editors

- [GHex](https://wiki.gnome.org/Apps/Ghex) #c #libadwaita #gnome

### Remote Desktop

- [Connections](https://gitlab.gnome.org/GNOME/connections) RDP, VNC #vala #gnome
- [Remmina](https://github.com/FreeRDP/Remmina) RDP, VNC, etc (plugin system) #c
- [Vinagre](https://wiki.gnome.org/Apps/Vinagre) RDP, VNC, SPICE #c #gnome

### SSH

- [EasySSH](https://github.com/muriloventuroso/easyssh) connection manager #vala

### Database Clients

- [Sequeler](https://github.com/Alecaddd/sequeler) #vala #granite
- [Daty](https://gitlab.gnome.org/World/Daty) for Wikidata (which is kind of a database?) #python #libhandy

### Disk Imaging

- [Imageburner](https://github.com/artemanufrij/imageburner) for SD/USB #vala #granite
- [Popsicle](https://github.com/pop-os/popsicle) for SD/USB #rust
- [GNOME MultiWriter](https://wiki.gnome.org/Apps/MultiWriter) for SD/USB #c #gnome
- [Brasero](https://wiki.gnome.org/Apps/Brasero) for CD/DVD #c #gnome

### File Renaming

- [Szyszka](https://github.com/qarmin/szyszka) #rust
- [tv-renamer](https://github.com/mmstick/tv-renamer) #rust

### Security and Privacy

- [Metadata Cleaner](https://gitlab.com/rmnvgr/metadata-cleaner) based on MAT2 #python #libadwaita
- [MAT (Metadata Anonymization Toolkit)](https://0xacab.org/mat/mat) #python
- [Collision](https://github.com/GeopJr/Collision) #crystal #libadwaita
- [GtkHash](https://github.com/tristanheaven/gtkhash) #c
- [Malcontent](https://gitlab.freedesktop.org/pwithnall/malcontent) parental controls client #c #libadwaita
- [Raider](https://github.com/ADBeveridge/raider) file shredder #c #libadwaita
- [krb5-auth-dialog](https://gitlab.gnome.org/GNOME/krb5-auth-dialog) Kerberos tickets monitoring #c #libadwaita

#### Password Management

- [Secrets](https://gitlab.gnome.org/World/secrets) KeePass v4 format based #python #libadwaita
- [Passbook](https://gitlab.gnome.org/gnumdk/passbook) #python
- [Gonepass](https://github.com/jbreams/gonepass) 1Password vault *viewer* #c++
- [Obliviate](https://github.com/elfenware/obliviate) password manager that does not store passwords #vala

#### One-Time Password

- [Authenticator](https://gitlab.gnome.org/World/Authenticator) #rust #libdawaita
- [OTPClient](https://github.com/paolostivanin/OTPClient) #c

### System and File Cleaning

- [BleachBit](https://www.bleachbit.org/) #python
- [Czkawka](https://github.com/qarmin/czkawka) #rust

### System Monitoring and Info

- [GNOME Usage](https://wiki.gnome.org/Apps/Usage) #vala #gnome
- [CPU-X](https://x0rg.github.io/CPU-X/) similar to CPU-Z #c
- [sysctlview](https://gitlab.com/alfix/sysctlview) FreeBSD sysctl MIB tree explorer #c++
- [GreenWithEnvy](https://gitlab.com/leinardi/gwe) NVIDIA card monitoring and fan/OC controlling #python
- [GNOME Logs](https://wiki.gnome.org/Apps/Logs) systemd logs viewer #gnome #c #libadwaita

#### Disk Usage Explorers

- [GNOME Disk Usage Analyzer (Baobab)](https://wiki.gnome.org/Apps/DiskUsageAnalyzer) DaisyDisk style circle chart #vala #gnome

### System Configuration

- [pulse-flow](https://github.com/benwaffle/pulse-flow) PulseAudio config tool with a flow graph UI #vala
- [doppler](https://github.com/spacekookie/doppler) Redshift (f.lux / night light style screen color filter thingy) UI #rust
- [Flatseal](https://github.com/tchx84/Flatseal) Flatpak permission manager #gjs #libandy
- [Login Manager Settings](https://realmazharhussain.github.io/gdm-settings/) GDM settings manager #python #libadwaita
- [Shell Configurator](https://gitlab.com/adeswantaTechs/shell-configurator) GNOME Shell configuration utility #gjs #libadwaita
- [NixOS Configuration Editor](https://github.com/vlinkz/nixos-conf-editor) #rust #libadwaita
- [Dynamic Wallpaper](https://github.com/dusansimic/dynamic-wallpaper) #libadwaita #python

### Installation

- [Parceldude](https://notabug.org/grindhold/parceldude) batch installer for Windows MSI packages #vala
- [Turtle](https://tenderowl.com/work/turtle) `.deskop` files creation tool #python #granite
- [mlinstall](https://petabyt.github.io/mlinstall) Magic Lantern installer #python
- [Pin It!](https://github.com/ryonakano/pinit) portable apps shortcut creator #vala #libadwaita
- [Extension Manager](https://github.com/mjakeman/extension-manager) for GNOME Shell #c #libadwaita
- [Nix Software Center](https://github.com/vlinkz/nix-software-center) #rust #libadwaita
- [ProtonPlus](https://github.com/Vysp3r/ProtonPlus) Proton version manager #vala #libadwaita
- [AdwSteamGtk](https://github.com/Foldex/AdwSteamGtk) [Adwaita for Steam](https://github.com/tkashkin/Adwaita-for-Steam) skin installer #python #libadwaita

### Weather Viewers

- [Meteo](https://gitlab.com/bitseater/meteo) #vala
- [bitseater/Weather](https://github.com/bitseater/weather) #vala
- [GNOME Weather](https://wiki.gnome.org/Apps/Weather) #gjs #gnome
- [Nimbus](https://github.com/danrabbit/nimbus) #vala

### Health & Fitness

- [Health](https://gitlab.gnome.org/World/Health) currently supports Google Fit #rust #libadwaita

### Containers

- [Pods](https://github.com/marhkb/pods) Podman GUI #rust #libadwaita
- [Atoms](https://github.com/AtomsDevs/Atoms) chroot environments manager #python #libadwaita
- [Bottles](https://github.com/bottlesdevs/Bottles) wineprefix environments manager #python #libadwaita
- [Toolbx Tuner](https://github.com/13hannes11/toolbx-tuner) toolbx containers manager #rust #libadwaita

### Task scheduling

- [Time Switch](https://github.com/fsobolev/timeswitch) computer shutdown timer #python #libadwaita

### Map Viewers

- [Atlas](https://github.com/ryonakano/atlas) #vala #libhandy #granite

### Game Launchers

- [Lutris](https://lutris.net) launcher covering most gaming systems #python
