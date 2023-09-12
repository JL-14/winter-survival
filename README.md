![The Viking Kings Quiz](/documentation/images/viking-quiz-navbar.png)
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
- 

- The general background is a cartoon image of a Viking ship in a bay.

- The background image is fixed, so that the sections appear to scroll over the image.

- On the Home Page there is a cover text box with a semi-transparent background.

![Front Page](/documentation/images/viking-quiz-front-page.png)

#### Introduction

- The introduction sets out a little of the history of the Vikings and how their histories were recorded, and introduces the game.

#### Start Button

- There is a clearly coloured yellow start button, which starts the game.

#### Footer

- The Footer is at the base of each page, in a fixed position.

- The Footer has links to the Home Page, Social Media, the creator's GitHub home page, and Copyright information.

- The links have animations in the form of a colour change and a bottom line under the relevant link when hovered over.

---

### Game Page

- The Game page, which is a modal activated by the Start Button on the Home Page, has the same navbar, background image, and footer as the Home Page.

![Game Page](/documentation/images/viking-quiz-game-page.png)

- The page consists of a biography of one of five Viking kings, a question relating to that king, a grid of nine possible answers, and a score box with a quit button.

#### Viking Biographies

![Viking Biography](/documentation/images/rollo-biography.png)

- Each Viking biography shows the name and date of birth and death of the Viking, an image of the Viking from historical or artistic sources, and a short description of the main achievements of the Viking.

- The Viking biography changes to the next Viking when the Next Question button is clicked.

- There are five questions in total.

#### Question

![Question](/documentation/images/question-screenshot.png)

- Each Viking biography is accompanied by a question relating to the text in the biography.

- The question changes when the Next Question button is clicked, in tandem with the Viking biography changing.

#### Answer Grid

![Answer Grid](/documentation/images/answer-grid.png)

- On the right hand side of the screen there is a grid of 9 tiles, each with a possible answer to the question.

- In this version of the game the tiles are static, and do not change as the Vikings and Questions change. A different tile has the correct answer for each Viking.

- On clicking on a tile, a modal/ popup appears with either feedback that the answer is correct or incorrect.

#### Answer Feedback popups

![Correct Answer](/documentation/images/correct-answer-popup.png)

- The modal consists of feedback that the answer was correct, an animated gif image of a Viking giving the thumbs up, a button for Next Question and a Quit Button.

![Incorrect Answer](/documentation/images/incorrect-answer-popup.png)

- As for the Correct Answers, the modal consists of feedback that the answer was incorrect, an animated gif image of a Viking being hit by lightning, a button for Next Question and a Quit Button.

- Clicking on Next Question opens up a new question window with a new Viking, a new Question, and the same options.

- Clicking on the Quit button brings up a confirmation popup asking the user to confirm that they want to quit the game. If they confirm they are returned to the front page, and if they cancel they are returned to the modal, where they can click Next Question to continue.

![Quit confirmation](/documentation/images/quit-confirmation.png)

- The final, fifth, question brings up a slightly different modal both for the correct and incorrect answers.

![Final Correct Answer](/documentation/images/final-correct-answer.png)

![Final Incorrect Answer](/documentation/images/final-incorrect-answer.png)

- The final modals inform the user that it was the final question, and provides a Finish button which takes the user to the final score page. There is also a button to quit.

#### Score Area

![Score Area](/documentation/images/score-area.png)

- The Score Area consists of a tally of right answers, wrong answers, and a Quit button.

- The scores are updated dynamically when answers are clicked, according to whether the answer is correct or incorrect.

- Correct answers are displayed in green, wrong answers in red.

#### Final Score Screens

- After the final answer has been answered and the user clicks on the Finish button, a final result modal appears with the final score and feedback and an animated git image depending on whether they were successful in the game or not.

- The score threshold set in this game is 3 out of 5 to be successful, so scores between 3 and 5 gives a success final screen whilst scores between 0 and 2 gives the unsuccessful final screen.

![Final Screen -Success](/documentation/images/final-screen-success.png)

![Final Screen -Fail](/documentation/images/final-screen-fail.png)

- From the final screen there is a button to Return to Main Page, returning to the front page where the user can start a new game if they so wish.

---

## Technologies Used

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) was used as the foundation of the site.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/css) - was used for the formatting and layout of the site.
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - was used to programme interactive elements of the site.
- [Balsamiq](https://balsamiq.com/) was used to make wireframes for the website.
- [Gitpod](https://gitpod.io/) was used as a backup IDE tool for writing code and editing.
- [Git](https://git-scm.com/) was used for the version control of the website.
- [GitHub](https://github.com/) was used to host the code of the website.
- [GitHub Pages](https://pages.github.com/) was used to deploy the website on the internet.
- [iStock](https://www.istockphoto.com/) was used to source the images on the website.
- [Adobe Photoshop](https://www.adobe.com/uk/products/photoshop.html) was used to edit and size images on the website.

---

## Design

### Colour Scheme

![Color Palette](/documentation/images/colour-palette.png)

- A darker red colour (Engineering Orange) was chosen as the main background colour, as psychologically it is associated with excitement and strength, and fit with the theme of the game (around Viking kings and their exploits). The colour matches the theme and the background for the website and is used both in full and with 0.9 opaqueness.

- An off-white colour (Antique White) was used for the fonts, both in the header and in the body of the site. The colour provides good contrast against the red background, and is gentler than pure white.

- A bright yellow colour was used for the Start, Next Question, and Finish buttons as it provides excellent contrast against the background colours, and draws the user's attention to it, making it the natural next button to press.

- A medium brown colour was used for borders around modals/ popups and buttons, as it provides good contrast with the red, off-white, and yellow background colours used for buttons. Brown also fits the theme of the website in being associated with nature and ruggedness.

- Black was used for fonts on modals/ popups and for the Viking biographies, as it provides the highest level of contrast against the off-white backgrounds used here, and is highly legible.

### Typography

![Main Font](/documentation/images/typography.png)

- Acme was used as the main font for the website as it provides good readability and has a Nordic appearance (with sharper edges than most other fonts). The font is legible and goes well with the theme of the website.

### Wireframe

![Wireframe for website](/documentation/images/balsamiq-wireframes-viking-quiz-1.png)

![Wireframe for website](/documentation/images/balsamiq-wireframes-viking-quiz-2.png)

- The wireframe for the website was greated using the Balsamiq wireframe tool, creating an initial outline of the website. The initial design was further developed as the website was realised, but the core concept and design remains consistent.

- The full wireframe document can be found [here](/documentation/images/balsamiq-wireframes-viking-kings-quiz.pdf)
---

## Testing

In order to confirm the functionality, responsiveness and presentation of the website, it was tested on a range of screen types and screen sizes, across Chrome, Firefox, and Edge browsers.

The website displays correctly across the different browsers, and also across different screen sizes. The responsiveness of the website was tested on several screens (different width monitors, iPhone 14 Max, and other displays used by other users), and also through the [Responsive Viewer add-in](https://responsiveviewer.org/) on Google Chrome:

![Responsive Viewer](/documentation/images/responsive-viewer.png)

### Manual testing

| feature | action | expected result | tested | passed | comments |
| --- | --- | --- | --- | --- | --- |
| Navbar | | | | | |
| Home | Click on the "Home" link | The user is redirected to the main page | Yes | Yes | - |
| Instructions | Click on the "Instructions" link | The user is shown the Instructions popup | Yes | Yes | - |
| Close Instructions button | Click on the Close Instructions button | Instruction popup is closed and user returned to home or game page | Yes | Yes | - |
| E-mail Us! | Click on the "E-mail Us!" link | The user is redirected to their preferred e-mail client | Yes | Yes | - |
| Footer | | | | | |
| Home | Click on the "Home" link | The user is redirected to the main page | Yes | Yes | - | 
| Facebook link in the footer | Click on the Facebook link | The user is redirected to the Facebook page | Yes | Yes | - |
| Twitter/ X link in the footer | Click on the Twitter/ X link | The user is redirected to the Twitter/ X page | Yes | Yes | - |
| Instagram link in the footer | Click on the Instagram link | The user is redirected to the Instagram page | Yes | Yes | - |
| GitHub Home Page link in the footer | Click on the GitHub link | The user is redirected to the creator's GitHub page | Yes | Yes | - |
| Home page | | | | | |
| Start button | Click on the Start button | The game starts and the game page displays | Yes | Yes | - |
| Game page | | | | | |
| Correct Answer button | Click on the correct answer | The correct answer popup shows for all 5 questions | Yes | Yes | - |
| Incorrect Answer buttons | Click on an incorrect answer | The Incorrect answer popup shows for all 8 incorrect options | Yes | Yes | - |
| Correct Final Answer button | Click on the correct answer for final question | The correct final answer popup appears for all 5 questions | Yes | Yes | - |
| Incorrect Final Answer button | Click on an incorrect answer for final question | The incorrect final answer popup appears for all 5 questions | Yes | Yes | - |
| Finish button on Correct Final Answer popup | Click on the Finish button on the Correct Final Answer popup | The Result screen appears | Yes | Yes | - |
| Finish button on Incorrect Final Answer popup | Click on the Finish button on the Inorrect Final Answer popup | The Result screen appears | Yes | Yes | - |
| Final Score screen -Successful game | Click on the Finish button on the Final answer screens | When score is 3 or higher the Successful Result screen appears with correct score (N out of 5) | Yes | Yes | - |
| Final Score screen -Failed game | Click on the Finish button on the Final answer screens | When score is 2 or lower the Failed Result screen appears with correct score (N out of 5) | Yes | Yes | On some screen sizes the Failed Game popup appears low on the page, hiding the Return to Main Page button |
| Return to Main Page button | Click on Return to Main Page button on Final Score screen | Returns to the Home Page | Yes | Yes | - |
| Score counters | Click on correct and incorrect answer buttons | The score counters for both correct and incorrect answers update correctly | Yes | Yes | - |
| Quit button in Score box | Click on Quit button | Popup appears asking user to confirm they want to quit | Yes | Yes | - |
| Quit button in Correct and Incorrect Answer popup | Click on Quit button | Popup appears asking user to confirm they want to quit | Yes | Yes | - |
| Quit confirmation popup -Yes | Click on 'OK' to quit game | Returns to Home Page | Yes | Yes | - |
| Quit confirmation popup -No | Click on 'Cancel' to stay in game | Returns to game screen | Yes | Yes | - |
---

### Validator Testing

### HTML
- No errors or warnings were found when W3C Validator was employed.

![Home Page HTML Validator](/documentation/images/validator-html.png)

### CSS

- No errors were found when the W3C CSS Validator was employed.

![CSS Page Validator](/documentation/images/validator-css.png)

- There were 9 warnings when the W3C CSS Validator was run, all relating to external content in the Google Fonts link.

### JavaScript

![JavaScript Validator](/documentation/images/validator-js.png)

- The JS Validator (https://jshint.com/) found 1 warning and no errors. The warning relates to the use of 'answerIndex[i]' in code matching tiles to question, but it does not appear to affect the user experience.

---

### Performance
- Using Lighthouse in DevTools on the Chrome browser I checked the performance of the website, which was very good across the board. The only flagged area was linked to the use of gif images which are resource intensive, hence the lower performance score of 87. Alternative image formats will be explored in future versions of the site.

![Website Lighthouse](/documentation/images/lighthouse-viking-kings-quiz.png)

---

### Accessibility Testing

- The accessibility of the website for visitors with assistive technologies or other impairments was tested using the Google WAVE extension. 

- After making some adjustments to increase contrast, there were no accessibility errors, with some warnings about the length of some ARIA-label descriptions linked to text links (the descriptions being on the long side) which do not impair the accessibility of the website.

![Website WAVE](/documentation/images/validator-wave.png)

---

## Deployment

- The website was deployed to GitHub Pages.

- In order to deploy, the following process was followed:
    1. Select the [GitHub repository](https://github.com/JL-14/famous-vikings-game) and go to Settings.
    2. Select the **Main Branch** from the Source Dropdown menu, and click Save.
    3. The page will be refreshed automatically with a detailed report showing successful deployment.

- The live link can be found [here](https://jl-14.github.io/viking-experience-uk/)

## Local Deployment

- The Viking Kings Quiz website can be cloned in your IDE, creating a local copy. The following command will create the clone:

- `git clone https://github.com/JL-14/famous-vikings-game'

- In Gitpod you can open the workspace [here](https://gitpod.io/#https://github.com/JL-14/famous-vikings-game)

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