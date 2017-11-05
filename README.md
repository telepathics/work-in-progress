# WORK IN PROGRESS
Template files for starting a new web project.  This includes a basic styled web page (HTML/CSS/JS), empty python server template, and SQLITE3 initialised functions.py.

## Documentation
* `index.html` Work in progress placeholder page with linked CSS and JS.
* `style.css` Styled to work with JS and HTML.
* `script.js` Temporary JS to show a terminal-esque typer for HTML.

* `server.py` Empty python server template.  Does not include overwritten REST methods, but does have CORS support, 404 handling, endpoints path checker, and the ability to serve forever.
* `functions.py` Empty SQLITE3 database template.  Overwrites row_factory with dict_factory and connects to `database.db` (which does not exist in these templates).
