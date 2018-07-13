# WORK IN PROGRESS
Template files for starting a new web project.  This includes a basic styled web page (HTML/CSS/JS), empty python server template, and SQLITE3 initialised functions.py.  This is mostly in an attempt to automate my work flow a little.

## File Structure
* `index.html` Work in progress placeholder page with linked CSS and JS.
* `assets` A folder of more folders.
	* `css` Folder for all cascading style sheets.
		* `style.css` Styled to work with JS and HTML.
	* `imgs` Folder to store all images.  It currently has one surprise image in it so git will track it.
	* `js` Folder for front-end javascript stuff.
		* `script.js` Temporary JS to show a terminal-esque typer for HTML.
	* `node-server` Folder with boilerplate nodejs server.
	* `python-server` Folder with boilerplate python server.
		* `server.py` Empty python server template.  Does not include overwritten REST methods, but does have CORS support, 404 handling, endpoints path checker, and the ability to serve forever.
		* `functions.py` Empty SQLITE3 database template.  Overwrites row_factory with dict_factory and connects to database (which does not exist in these templates).

## Dependencies
* ??? a computer

## How to use me
* please be gentle.

## To Do
- [ ] Node server boilerplate
- [ ] Finish writing the README
