# Stream Chat Bot Extensions
This extension contains tools for streamers to add more interesting commands to their chat bots.



## Supported Bot Modules

### Coin Toss
 - [flip](https://stream-chat-bot-extensions-functionapp.azurewebsites.net/api/cointoss/flip) - Flips a coin and chooses `"heads"` or `"tails"`
 - [custom flip](https://stream-chat-bot-extensions-functionapp.azurewebsites.net/api/cointoss/customflip?heads=yes&tails=no) - Fed up of using heads and tails? Replace them with your own phrases! (e.g. `"yes"` or `"no"`)

### Dice
 - [roll](https://stream-chat-bot-extensions-functionapp.azurewebsites.net/api/dice/roll) - Rolls a standard six-sided dice.

### Rock Paper Scissors
 - [rules](https://stream-chat-bot-extensions-functionapp.azurewebsites.net/api/rockpaperscissors/rules) - Prints the rules for the standard version of "Rock, Paper, Scissors!"
 - [play](https://stream-chat-bot-extensions-functionapp.azurewebsites.net/api/rockpaperscissors/play) - Plays a game of "Rock, Paper, Scissors!" and prints the result.
 - [play (advanced version)](https://stream-chat-bot-extensions-functionapp.azurewebsites.net/api/rockpaperscissorslizardspock/play) - Fed up of the standard version? Why not give "Rock, Paper, Scissors, Lizard, Spock!" a try...

### Famous Quotes
 - [show categories](https://stream-chat-bot-extensions-functionapp.azurewebsites.net/api/famousquotes/showcategories) - Shows avaiable categories to use for getting famous quotes.
 - [get](https://stream-chat-bot-extensions-functionapp.azurewebsites.net/api/famousquotes/get) - Gets a famous quote.



## How to Install

N.B. Currently I've only got command text setup for SE as that's the only bot syntax I know how to use, if anyone knows how to get the same result via Nightbot / Streamlabs feel free to fork the repo, chuck up a pull request, and I'll take a look.

Simply chuck the appropriate text into a new command based on the table of examples below, for the bot you use:

| Example                 | Description                                                                    | Nightbot | StreamElements                                                                                                                    | Streamlabs |
|-------------------------|--------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------|------------|
| !flipacoin              | Flips a coin and chooses `"heads"` or `"tails"`                                | TODO     | `${customapi.https://stream-chat-bot-extensions-functionapp.azurewebsites.net/api/cointoss/flip}`                                 | TODO       |
| !yesorno                | Flips a coin and chooses `"yes"` or `"no"`                                     | TODO     | `${customapi.https://stream-chat-bot-extensions-functionapp.azurewebsites.net/api/cointoss/customflip?heads=yes&tails=no}`        | TODO       |
| !rolldice               | Rolls a standard six-sided dice.                                               | TODO     | `${customapi.https://stream-chat-bot-extensions-functionapp.azurewebsites.net/api/dice/roll}`                                     | TODO       |
| !rolld20                | Rolls a D20 dice from DnD.                                                     | TODO     | `${customapi.https://stream-chat-bot-extensions-functionapp.azurewebsites.net/api/dice/roll?min=1&max=20}`                        | TODO       |
| !roll10die              | Rolls a standard six-sided dice, 10 times.                                     | TODO     | `${customapi.https://stream-chat-bot-extensions-functionapp.azurewebsites.net/api/dice/roll?amount_to_roll=10}`                   | TODO       |
| !rps paper              | Plays a game of "Rock, Paper, Scissors!" and prints the result.                | TODO     | `${customapi.https://stream-chat-bot-extensions-functionapp.azurewebsites.net/api/rockpaperscissors/play?choice=${1}}`            | TODO       |
| !rpsls lizard           | Plays a game of "Rock, Paper, Scissors, Lizard, Spock!" and prints the result. | TODO     | `${customapi.https://stream-chat-bot-extensions-functionapp.azurewebsites.net/api/rockpaperscissorslizardspock/play?choice=${1}}` | TODO       |
| !famousquote leadership | Prints a famous quote from history, based on a specific category.              | TODO     | `${customapi.https://stream-chat-bot-extensions-functionapp.azurewebsites.net/api/famousquotes/get?category=leadership}`          | TODO       |