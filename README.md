# python-templates
Some template python programs. Mostly just examples for now. 

The python files in the root directory shows the convention I like best for python programs. 
There are two distinct types of python programs (although sometimes they can be a combination):
- Scripts
- Modules

---

Scripts are what are most familiar to beginners of python. They can be called in the command line as follows

```sh
python script.py
```

If functions or classes are made in a script, they are most likely also used within the script. 
Importing a script is analogous to just calling the script. 

---

Modules are what allow complex libraries to be developed. It allows modularity (hence the name), so that there can 
be fine control over what the user of the module has access to. 

If functions or classes are made in a module, they won't be run when calling in the command line most of the time. 

If you do call the module in the command line, it is common practice to make a "main function" that looks like this:

```python
if __name__ == "__main__":
  # do stuff here that would be run in the command line...
```

---

All the examples in the examples folder follow this convention. If the file is a script, it is names script_NAME.py, 
and if it is a module it is named mod_NAME.py. 

Templates are also good examples, but I will probably separate when I make the templates for the things I want. 
This is the roadmap for what templates I would like to add:

- [ ] Flask initialization (with perhaps some design patterns) for initial web pages
- [ ] BeautifulSoup/Requests initialization pattern for web scraping
- [ ] Selenium initialization with as many different browsers as possible (chrome, firefox, etc.)
- [ ] pynput/pyautogui for operating system automation control
