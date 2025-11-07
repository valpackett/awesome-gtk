# Contributing

- You can suggest apps both via GitHub issues and pull requests, doesn't matter.
- When making a pull request: follow the existing structure, use similar formatting, use tags and keep entries sorted alphabetically by title.
- Don't add GTK 2 applications that don't have a working GTK 3 version in development
- Don't add terrible applications
- [Don't be an ass](https://www.contributor-covenant.org/version/1/4/code-of-conduct.html)

## Tags

- Programming language tags: `#c`, `#python`, `#rust`
- GTK version: `#gtk3` or `#gtk4`
- `#gnome` means it's an official GNOME app (note: not everything that has a GNOME wiki page is official)
- `#granite` means it's using elementary's `granite` library / elementary SDK (but not necessarily is an official elementary app)
- `#libunity` means it has a HARD dependency on `libunity`
- New tags must be added to the linter [`TAGS` list](./lint.py)
