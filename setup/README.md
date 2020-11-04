# Stanford CTC Website Toolkit
This directory is a toolkit to easily update project and team information.
*NOTE:* This toolkit is designed for Unix systems.

## Adding your profile picture
To add a person, update `src/data/people.json` JSON object with the following fields:
- *name_id*: a unique identifier for you (usually firstlast, no spaces)
    - *imageSrc*: `./assets/<profie_photo.jpg>`. Make sure you put `<profie_photo.jpg>`in `public/assets/`. Also make
    sure that the image is square and <300 KB.
    - *links*: (optional - add only what you're comfortable being public)
        - *email*: your email address
        - *github*: Github profile link
        - *linkedin*: your Linkedn profile link
    - *leadership*: false
    - *name*: your full name, usually "First Last".
    - *role*: Usually "Developer"

Finally, go to `projects.json` and add the `name_id` in the `team` list.

To preview these changes, run `yarn && yarn serve`.

## Updating Project Information
Make sure you have Python 3 and Pip installed as well as pipenv.
Installation instructions for Python3/Pip are [here](https://pip.pypa.io/en/stable/installing/) and installation instructions for pipenv are [here](https://docs.pipenv.org/en/latest/install/#pragmatic-installation-of-pipenv).
Next, automatically get the correct environment by running `pipenv shell` within the `setup` directory.

### A Quick Overview of `projects.json`
All the project UI is loaded from one JSON array: `src/data/projects.json`.
For each project is a JSON objcet with the following structure:
- background: The main iconography for the project. It should be a file path to an image within the `public/assets` folder.
- bullets: A JSON string array that summarizes the work in a couple bullet points. This will be displayed in the profile listing in the top card.
- featured: a boolean that determines whether this project will be displayed.
- name: A string representing the project name (i.e. "Oppia")
- narrative: Raw, unstyled HTML that will be the primary content of the project listing. To be elaborated in the [Narrative](#Narrative) section.
- organization: A brief, <= 2 sentence description of your partner org that will be displayed in italics at the top of the project listing.
- summary: 1 sentence description that will be displayed on the content cards.
- team: a list of references to team members to be displayed on the people page.
- wip: a boolean representing whether the project is in progress.
- year: the the latest year the project was running.

### The Cumbersome Fields
Most of these fields will be easies to directly modify in the JSON. Some fields, however, are too cumbersome to modify directly: `narrative`, and `assets`. Here is how to modify them.

### Narrative
Create an HTML file with `<div id="narrative">` tag and include the HTML content you would like within that tag. The basic styling, such as the fonts, sizes, colors, etc. will be based on the site's global styling, so you do not have to worry about that kind of styling. If you do want your own, custom styling, you must include it inline via the `style=""` attribute. Recommended HTML content items include headers, text, and links. If you have an image you want to include from the web, feel free to add the image within this html content. Otherwise, if you want to locally import an image, please include it as described in the [Assets](#Assets) section. An example HTML file is `setup/example.html`.
Next, run these commands.
```
cd setup
pipenv shell
python parse_and_stringify_html.py [name] [path to html file]
```
The `[name]` field should correspond to the same `name` field in the project JSON object (described above).

### Assets
Local images will be added at the bottom of the project listing. Add the imagea follows:
```
cd setup
pipenv shell
python add_images_to_project.py [name] [path_to_image_file] [caption]
```
The `[name]` field should correspond to the same field in the JSON object described above, and the `[caption]` field should be the string that you want to be displayed under the image to give it context.

If you have any questions, feel free to contact [drewgreg@stanford.edu]
