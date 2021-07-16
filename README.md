# WIKI

For minor programming we have to make a wikipedia-like online encyclopedia.

## Requirements

* Entry Page: Visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry, should render a page that displays the contents of that encyclopedia entry.
    * The view should get the content of the encyclopedia entry by calling the appropriate util function.
    * If an entry is requested that does not exist, the user should be presented with an error page indicating that their requested page was not found.
    * If the entry does exist, the user should be presented with a page that displays the content of the entry. The title of the page should include the name of the entry.
* Index Page: Update index.html such that, instead of merely listing the names of all pages in the encyclopedia, user can click on any entry name to be taken directly to that entry page.
* Search: Allow the user to type a query into the search box in the sidebar to search for an encyclopedia entry.
    * If the query matches the name of an encyclopedia entry, the user should be redirected to that entry’s page.
    * If the query does not match the name of an encyclopedia entry, the user should instead be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring. For example, if the search query were Py, then Python should appear in the search results.
    * Clicking on any of the entry names on the search results page should take the user to that entry’s page.
* New Page: Clicking “Create New Page” in the sidebar should take the user to a page where they can create a new encyclopedia entry.
    * Users should be able to enter a title for the page and, in a textarea, should be able to enter the Markdown content for the page.
    * Users should be able to click a button to save their new page.
    * When the page is saved, if an encyclopedia entry already exists with the provided title, the user should be presented with an error message.
    * Otherwise, the encyclopedia entry should be saved to disk, and the user should be taken to the new entry’s page.
* Edit Page (extra): On each entry page, the user should be able to click a link to be taken to a page where the user can edit that entry’s Markdown content in a textarea.
    * The textarea should be pre-populated with the existing Markdown content of the page. (i.e., the existing content should be the initial value of the textarea).
    * The user should be able to click a button to save the changes made to the entry.
    * Once the entry is saved, the user should be redirected back to that entry’s page.

## Design document pages

### Index page

The user can click on any entry name to be taken directly to that entry page. Hovering the mouse pointer over an item name changes the color of that name, informing the user that they can click it.
<img src = design-images/index.png>
<img src = design-images/index-hover.png>

### Search results page

The user can enter what he is looking for in the search form, the results will be shown in this page. Hovering the mouse pointer over an item name changes the color of that name, informing the user that they can click it.
<img src = design-images/search-results.png>
<img src = design-images/search-results-hover.png>

### Entry page

Page with content about the chosen entry.
<img src = design-images/entrypage.png>

### Create new page

Page where the user can create a new encyclopedia entry
<img src = design-images/new-page.png>

### Error pages

If the user searches for a page that does not exist, or if the user creates a page that already exists, an error will appear.
<img src = design-images/error-page.not.found.png>
<img src = design-images/error-page.already.exist.png>

## Design document routes
<img src = design-images/buttons.png>


## Getting Started

1. install python and pip
2. clone the repository (in terminal) or download it as a zip file (click the green button at the top right):
```
$ git clone https://github.com/uva-webapps/wiki-Susanne-Becker.git
```
3. run in terminal:
```
$ python3 -m pip install Django
```
4. run in terminal:
```
$ pip3 install markdown2
```
5. run in terminal: 
```
$ python3 manage.py runserver
```
