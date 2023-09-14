![](/documentation/images/viking-quiz-navbar.png)
---
# *The Winter Survival Exercise*

The Winter Survival Exercise is a Python-based programme based on a groupwork exercise normally used for team-building. It involves a scenario where surviviors of a plane crash in Northern Canada have to prioritise a set of items in order of importance for their survival. The Winter Survival Exercise is a one-person adaptation of the groupwork exercise, where the user, as a lone survivor, has to choose five items from a list of twelve according to how important they consider them for their survival.

Having been developed by a US Army survival expert, the items have been ranked by the expert. The aim of the exercise is to choose items that match the expert's choices, and the game is scored by how differently the user prioritises items compared with the expert. After the user has chosen their items they can choose to see the expert's evaluation of the usefulness of the items they chose.

As in all aspects of survival, the expert's items are not the be-all and end-all, as in a real-world situation the user's ability to use the items and other decisions made by the user would have a major impact on their ability to survive. But nonetheless, the expert's rankings are indicative of the priorities that would provide the best odds of survival.

The Winter Survival Exercise is designed to be educational, teaching the user about prioritisation in a cold-weather survival scenario, testing the user's knowledge of survival and the science behind the items' usefulness, and also to be fun to play.

Whilst the current game is focused on the winter survival scenario, its format and code lend themselves to being expanded and changed to cover different scenarios, as well as to adding further interactive content through a day-by-day decision log.
 
The Winter Survival Exercise can be accessed [here](https://jl-14.github.io/famous-vikings-game/).

![Responsive Mockup](/documentation/images/viking-kings-quiz-mockup.png)

---
## User Stories

### First Time Visitor Goals

* On my first visit, I want to easily find out what the Winter Survival Exercise is about.
* On my first visit, I want to be able to easily find instructions on how to complete the exercise.
* On my first visit, I want to easily be able to complete the exercise, understanding the flow of the programme.
* On my first visit, I want to see and understand my score after completing the game.

### Returning Visitor Goals

* On my return visit, I want to be able to easily start a new game.
* On my return visit, I want to be able to complete the exercise to see if I can get a better score than on my last visit.

### Frequent Visitor Goals

* As a frequent visitor to the site, I want to see whether there is new content and new scenarios to complete.
* As a frequent visitor, I want to complete the exercise again to see if I can get an even better score.
* As a frequent visitor, I want to see the expert's feedback for all the different items, and to fully understand how all the possible items might be helpful (or not) for the purposes of survival.

---

## Features

### Throughout the programme

- The font colours indicate the nature of the information:
    * White font is the narrative of the exercise
    * Yellow font indicates that user input is required
    * Green font indicates that the text represents input from the expert
    * Red font indicates that the user input is incorrect 

### Introduction to the exercise

- The exercise starts with a short introduction welcoming the user, asking the user to press Enter when they are ready to begin.
- The user is also informed that they can exit the exercise at any time by pressing the Esc button on their keyboard.

![Intro](/documentation/images/viking-quiz-header.png)

### Scenario section

- The user is then taken through the scenario for the exercise, as well as given some details about likely priorities and how the exercise is scored. 
- The user is then invited to press Enter to see the twelve items and begin to choose their five items in order of priority. 

![Scenario](/documentation/images/scenario-section.png)

### Items list and user choices

- The twelve items from which the user has to choose five is then presented in table format.
- Under the table the user is asked to choose one of the twelve items as their highest priority item for survival in the given environment, repeated for each of the user's five items.
- When the user has chosen five items, the items are listed back to the user and they are asked to confirm that they are happy with their selection.
- If they are not happy with what they chose the table of items will be displayed again, and they will be given a second opportunity to select items
- If they make an incorrect entry (a non-numerical entry, an entry outside the range 1-12, an empty entry, or a duplicate entry of an item already chosen), an error will appear and they can choose again.

### Score and feedback

- Once the user has made their choices the score is calculated in accordance with the scoring information presented at the start of the game, and presented as a number with an accompanying statement (Excellent, Very Good, OK, or Poor) depending on their score.

### Expert feedback on items chosen

- After they have been presented with the score, the user is invited to see the expert's feedback (a paragraph of text) for each of the items they chose, which includes and benefits and potential dangers associated with each item.
- The user will only be able to see feedback for the items they chose, so that if they wish to play again they can do so without having it spoiled.
- The feedback is in green font to indicate that it represents the expert's views.

### Final step

- After the expert's feedback on the chosen items, the user can choose to try again, see the full list of expert ratings, or to quit the game.
    * Try again: Restarts the game from the beginning.
    * Expert's rankings: Displays a table (in green) showing how the expert ranked the twelve items, from the most important to the least important.
    * Quit: Takes the user to the option to clean the terminal at the end of the exercise.

### Clean the terminal

- At the end of the exercise the user is asked whether they want to clean the terminal (unless they have chosen to start again, in which case the terminal is automatically cleaned).
- If they select yes, the terminal is cleaned and left empty, whilst if they choose no, the exercise will finish, leaving the information from the exercise in the terminal (so that the user can revisit the expert's advice, their choices, etc).

## Flowchart

- The following flowchart shows the logic of the application:
![Flowchart](/documentation/images/flowchart.png)

## Technologies used

### Languages:

- [Python 3.11.4](https://www.python.org/downloads/release/python-3114/): used to anchor the project and direct all application behavior

- [JavaScript](https://www.javascript.com/): used to provide the start script needed to run the Code Institute mock terminal in the browser

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) used to construct the elements involved in building the mock terminal in the browser

### Frameworks/Libraries, Programmes and Tools:
#### Python modules/packages:

##### Standard library imports:

- [os](https://docs.python.org/3/library/os.html ) was used to clear the terminal before running the program.

##### Third-party imports:

- [Tabulate Package](https://pypi.org/project/tabulate/) was used to create tables for items and expert rankings.
- [Colorama](https://pypi.org/project/colorama/) was used to add colors and styles to the project.

#### Other tools:

- [VSCode](https://code.visualstudio.com/) was used as the main tool to write and edit code.
- [Git](https://git-scm.com/) was used for the version control of the website.
- [GitHub](https://github.com/) was used to host the code of the website.
- [Adobe Photoshop](https://www.adobe.com/uk/products/photoshop.html) was used to make and resize images for the README file.
- [Lucid](https://www.lucidchart.com/pages/examples/flowchart-maker) was used to make a flowchart for the README file.
- [Heroku](https://dashboard.heroku.com/apps) was used to deploy the project.

---

## Design

- As this is a text-based exercise displaying in a terminal-environment, there was little design involved.
- Colorama was used to add colours to the exercise, providing clarity about the nature of the different sections for the user:
    * White font for the narrative of the exercise
    * Yellow font where user input is required
    * Green font where the text represents input from the expert
    * Red font where there is an error/ the user input is incorrect 
- Tabulate was used to structure the items list and expert rankings in table formats, to make the content more user friendly.

---

## Testing

In order to confirm the functionality, responsiveness and presentation of the programme, it was tested on a range of screen types and screen sizes, across Chrome, Firefox, and Edge browsers, and in various developer environments, including VS Code, GitPod, and Heroku (with the purpose-built app for the project).

The website displays correctly across the different browsers, and also across different screen sizes.

### Manual testing

| feature | action | expected result | tested | passed | comments |
| --- | --- | --- | --- | --- | --- |
| Navbar | | | | | |
| Introduction | Click on the "Home" link | The user is redirected to the main page | Yes | Yes | - |
| Scenario | Click on the "Instructions" link | The user is shown the Instructions popup | Yes | Yes | - |
| Start exercise | Click on the Close Instructions button | Instruction popup is closed and user returned to home or game page | Yes | Yes | - |
| Choose items | Click on the "E-mail Us!" link | The user is redirected to their preferred e-mail client | Yes | Yes | - |
| Correct number entries | | | | | |
| Display choices made | | | | | |
| Incorrect entry -No entry | Click on the "Home" link | The user is redirected to the main page | Yes | Yes | - | 
| Incorrect entry - Number outside range | Click on the Facebook link | The user is redirected to the Facebook page | Yes | Yes | - |
| Incorrect entry - Non-number entry | Click on the Twitter/ X link | The user is redirected to the Twitter/ X page | Yes | Yes | - |
| Incorrect entry - Duplicate entry | Click on the Instagram link | The user is redirected to the Instagram page | Yes | Yes | - |
| Confirm selection -Yes | Click on the GitHub link | The user is redirected to the creator's GitHub page | Yes | Yes | - |
| Confirm selection -No | | | | | |
| Second attempt Correct number entries| Click on the Start button | The game starts and the game page displays | Yes | Yes | - |
| Second attempt Incorrect entry -No entry | | | | | |
| Second attempt Incorrect entry - Number outside range | Click on the correct answer | The correct answer popup shows for all 5 questions | Yes | Yes | - |
| Second attempt Incorrect entry - Non-number entry | Click on an incorrect answer | The Incorrect answer popup shows for all 8 incorrect options | Yes | Yes | - |
| Second attempt Incorrect entry - Duplicate entry | Click on the correct answer for final question | The correct final answer popup appears for all 5 questions | Yes | Yes | - |
| Second attempt confirmation | Click on an incorrect answer for final question | The incorrect final answer popup appears for all 5 questions | Yes | Yes | - |
| Second attempt Display choices made | | | | | | 
| Display score | Click on the Finish button on the Inorrect Final Answer popup | The Result screen appears | Yes | Yes | - |
| Display score statement | Click on the Finish button on the Final answer screens | When score is 3 or higher the Successful Result screen appears with correct score (N out of 5) | Yes | Yes | - |
| See expert feedback -Yes | Click on the Finish button on the Final answer screens | When score is 2 or lower the Failed Result screen appears with correct score (N out of 5) | Yes | Yes | On some screen sizes the Failed Game popup appears low on the page, hiding the Return to Main Page button |
| See expert feedback -No | Click on Return to Main Page button on Final Score screen | Returns to the Home Page | Yes | Yes | - |
| See expert feedback -Non-valid | Click on correct and incorrect answer buttons | The score counters for both correct and incorrect answers update correctly | Yes | Yes | - |
| Try again/ expert's rankings/ quit options -'t' to try again | Click on Quit button | Popup appears asking user to confirm they want to quit | Yes | Yes | - |
| Try again/ expert's rankings/ quit options -'e' to see expert's rankings | Click on Quit button | Popup appears asking user to confirm they want to quit | Yes | Yes | - |
| Try again/ expert's rankings/ quit options -'q' to quit | Click on Quit button | Popup appears asking user to confirm they want to quit | Yes | Yes | - |
| Quit -Clean terminal -Yes | Click on 'Cancel' to stay in game | Returns to game screen | Yes | Yes | - |
| Quit -Clean terminal -No | Click on 'Cancel' to stay in game | Returns to game screen | Yes | Yes | - |
| Quit -Clean terminal -Non-valid entry | Click on 'Cancel' to stay in game | Returns to game screen | Yes | Yes | - |
| Try again/ expert's rankings/ quit options Incorrect entry -No entry | Click on Quit button | Popup appears asking user to confirm they want to quit | Yes | Yes | - |
| Try again/ expert's rankings/ quit options Incorrect entry -Non-valid entry | Click on 'OK' to quit game | Returns to Home Page | Yes | Yes | - |
| Clean terminal -Yes | Click on 'Cancel' to stay in game | Returns to game screen | Yes | Yes | - |
| Clean terminal -No | Click on 'Cancel' to stay in game | Returns to game screen | Yes | Yes | - |
| Clean terminal -Non-valid entry | Click on 'Cancel' to stay in game | Returns to game screen | Yes | Yes | - |


---

### Validator testing



---

## Deployment

- The program was deployed to [Heroku](https://dashboard.heroku.com).
- The program can be reached by the [link](https://the-maddest-madlib.onrender.com/)

### To deploy the project as an application that can be **run locally**:

*Note:*
  1. This project requires you to have Python installed on your local PC:
  - `sudo apt install python3`

  1. You will also need pip installed to allow the installation of modules the application uses.
  - `sudo apt install python3-pip`

Create a local copy of the GitHub repository by following one of the two processes below:

- Download ZIP file:
  1. Go to the [GitHub Repo page](https://github.com/IuliiaKonovalova/madlib_with_python).
  1. Click the Code button and download the ZIP file containing the project.
  1. Extract the ZIP file to a location on your PC.

- Clone the repository:
  1. Open a folder on your computer with the terminal.
  1. Run the following command
  - `git clone https://github.com/IuliiaKonovalova/madlib_with_python.git`

- Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

  [![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/IuliiaKonovalova/madlib_with_python)

  1. Install Python module dependencies:
     
      1. Navigate to the folder madlib_with_python by executing the command:
      - `cd madlib_with_python`
      1. Run the command pip install -r requirements.txt
        - `pip3 install -r requirements.txt`
      1. *Note:* If you are located in China ![China](https://www.countryflags.io/cn/flat/32.png) or any other country with restricted internet access, you may need to add the following code in order to be able to use the nltk package.
      
       - For example:

        ```python
        nltk.set_proxy('127.0.0.1:41091')
        ```
      - To set the proxy, you need to open setting in preferred VPN, find Server address and HTTP/HTTPS Proxy Port joining them by colons as it is shown in the example above:
      ![Settings VPN](documentation/deployment/settings_vpn.png)


### To deploy the project to Heroku so it can be run as a remote web application:
- Clone the repository:
  1. Open a folder on your computer with the terminal.
  1. Run the following command
  - `git clone https://github.com/IuliiaKonovalova/madlib_with_python.git`

  1. Create your own GitHub repository to host the code.
  1. Run the command `git remote set-url origin <Your GitHub Repo Path>` to set the remote repository location to your repository.

  1. Push the files to your repository with the following command:
  `git push`
  1. Create a Heroku account if you don't already have one here [Heroku](https://dashboard.heroku.com).
  1. Create a new Heroku application on the following page here [New Heroku App](https://dashboard.heroku.com/apps):

      - ![New Heroku App](documentation/deployment/new_heroku_app.png)

  1. Go to the Deploy tab:

      - ![Deploy Tab](documentation/deployment/deploy_tab.png)

      - ![Deployment Method](documentation/deployment/deployment_method.png)

  1. Link your GitHub account and connect the application to the repository you created.

      - ![Link GitHub account](documentation/deployment/link_to_github.png)

  1. Go to the Settings tab:
  
      - ![Settings Tab](documentation/deployment/settings_tab.png)

  1. Click "Add buildpack":

      - ![Add Buildpack](documentation/deployment/add_buildpack.png)

  1. Add the Python and Node.js buildpacks in the following order:

      - ![Add Python and Node.js](documentation/deployment/add_python_and_node_js.png)

  1. Click "Reveal Config Vars."

      - ![Reveal Config Vars](documentation/deployment/reveal_config_vars.png)

  1. Add 1 new Config Vars:
      - Key: PORT Value: 8000
      - *This Config was provided by [CODE INSTITUTE](https://codeinstitute.net/)*.

  1. Go back to the Deploy tab:

      - ![Deploy Tab](documentation/deployment/deploy_tab.png)

  1. Click "Deploy Branch":

      - ![Deploy Branch](documentation/deployment/deploy_branch.png)

      - Wait for the completion of the deployment.

      - ![Deploying Branch](documentation/deployment/deploying_branch.png)

  1. Click "Open app" to launch the application inside a web page.

      - ![View Button](documentation/deployment/view_app.png)

---

## Bugs

### Existing Bugs

1. There are two warnings in DevTools on Chrome and Firefox browsers stating that: 

"DevTools failed to load source map: Could not load content for chrome-extension://fheoggkfdfchfphceeifdbepaooicaho/sourceMap/chrome/scripts/content_autoplay_detection.js.map: System error: net::ERR_BLOCKED_BY_CLIENT"

The warning relates to the embedded Google Map in the Location section on the Home Page, and does not affect performance.

2. The W3C CSS Validator returned 9 warnings relating to external third-party content in the code, none of which affect the user experience.

3. On some screen sizes the Failed Game result screen appears low down, cutting off the bottom of the box (including the Return to Main Page button). 

4. The overlay behind popup boxes does not stretch below the bottom of the screen, so when scrolling down the lower portion of the screen appears without the overlay.

5. On smaller screen sizes the answer grid moves from 3x3 to 4x2 and a single tile at the bottom, and eventually to 9x1 for the smallest screens. The preference would be to keep the 3x3 format and then moving to 9x1.

6. At the smallest screen sizes (<270px) the text in the Viking biography section becomes too big for the containing box and overflows.

### Solved Bugs
- A number of bugs were solved throughout the design of the website, on a running basis. The key tools for finding and addressing bugs were DevTools in Chrome, and the use of commenting out code (ctrl + /) to examine the impact of particular sections of code.

- The most significant bug related to the switch from one Viking to the next (lines 165-179 in the current script.js), where there was duplication of a loop causing the progression of Viking biographies to halt after three iterations. The bug was removed by restructuring the code and moving the vikingIndex++ command to the end of the section.

- A second significant bug was around matching the correct answers on the answer tiles to the question displaying. The issue of matching the question and answer was solved through applying data-labels to the variables and matching the labels rather than innerHTML content.

- The final significant bug related to quitting the game returning to the home page but not resetting the game, so on pressing start the previous game would resume. This was solved through adding code to the event listener to intialise the game.

- There were also bugs related to the use of fixed heights affecting the responsivity of the website, solved through replacing with relative values through the use of the [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln) extension showing overlapping containers, as well as DevTools.

---

## Future Improvements
* add Favicon with [Favicon Generator](https://realfavicongenerator.net/)
* further refine responsive design elements to improve appearance on the smallest screens (especially small mobiles)
* refine the images used, both in terms of file-types and placement on the Packages page
* randomise the answer tiles in the answer grid each time the next question button is clicked to make for a more engaging game
* add a custom quit confirmation popup
* add more questions and Viking biographies to the game
* add a custom 404 Error page
* add feedback functionality in addition to the e-mail function

---

## Credits

+ #### Content

- The idea, concept, and content for the website came from me (Jorgen Lovbakke).

- The outline of the README document has been taken from my earlier README.md from the Viking Experience website, published through GitHub Pages.

- In developing the idea and concept, I consulted "The Children of Ash and Elm -A History of the Vikings" by Neil Price, published in 2022 by Penguin Books, and the Heimskringla -Snorre's sagas of the Viking kings, the version consulted was published in Norwegian in 1998 by Gyldendal Publishers. 

- Inspiration for the use of a fixed background image came from the Code Institute's 'Love Running' project.

+ #### Media

- The background image on the website was downloaded from [iStock](https://www.istockphoto.com/).

- The animated gif images were published by http://www.animated-gifs.fr/. (The site is currently unavailable.)
- The animated gif of the correct answer Viking (thumbs up) is from https://waterford.fyi/.

- The images of the Viking Kings were from:
* Rollo of Normandy: Anonymous, historical image available on Wikipedia.
* Olav Haraldsson: By Rabax63 -CC BY-SA 4.0, image available on https://www.warhistoryonline.com/.
* Leif Erikson: available on WikiMedia Commons, https://commons.wikimedia.org/wiki/File:Leif_Erikson_Discovers_America_Hans_Dahl.jpg.
* Harald Hardrada: public domain, via Wikimedia Commons.
* Canute the Great: image from https://vikinghistorytales.blogspot.com/.


+ #### Tools

- [coolors](https//:coolors.co) was used to create the colour palette
- [Am I Responsive](https://ui.dev/amiresponsive) was used to create the multi-screen mockup for the README.md document
- [WAVE Accessibility evaluator](https://wave.webaim.org/) was used to test the accessibility of the website

---

## Acknowledgements

- [Juliia Konovalova](https://github.com/IuliiaKonovalova) for her support as Code Institute mentor for the project, for her invaluable insights and suggestions.
- [Code Institute](https://codeinstitute.net/) and Slack community members for the teaching, tutor support, and resources for the project.
- My wife, Joanne, for her patience with me whilst doing the project and her invaluable talent for graphics formatting. 
- My sons, Samuel and Christopher, for user testing of the website.
- Coders across the world offering their time and support on forums such as [Stack Overflow](https://stackoverflow.com/) and [Reddit](https://www.reddit.com/r/programming/).