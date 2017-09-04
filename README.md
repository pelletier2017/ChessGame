[![Build Status](https://travis-ci.org/pelletier2017/ChessGame.svg?branch=master)](https://travis-ci.org/pelletier2017/ChessGame) 
[![Coverage Status](https://coveralls.io/repos/github/pelletier2017/ChessGame/badge.svg?branch=master)](https://coveralls.io/github/pelletier2017/ChessGame?branch=master)
[![Code Health](https://landscape.io/github/pelletier2017/ChessGame/master/landscape.svg?style=flat)](https://landscape.io/github/pelletier2017/ChessGame/master)

# ChessGame

Library for running chess simulations. Allows customizable AI including random choice and minimax (with variable depth).

## Getting Started

To work with project, clone repo using git.

```
$git clone https://github.com/pelletier2017/ChessGame.git
```

Example Usage

```
import chess.player as player
from chess.game import ChessGame

p1 = player.RandomComputer()
p2 = player.BasicMinimax()
game = ChessGame(p1, p2)
game.play()
```

### Prerequisites

Dependencies are found in requirements.txt

```
$pip install -r requirements.txt
```

## Running the tests

Run test runner here

```
$cd tests
$python test_all.py
```

Travis CI will run tests automatically when changes are pushed to github.

[travis-ci.org/pelletier2017/ChessGame](https://travis-ci.org/pelletier2017/ChessGame)

### And coding style tests

Landscape evaluates code quality including code style. Project goal is to stay above 95%.

[landscape.io/github/pelletier2017/ChessGame](https://landscape.io/github/pelletier2017/ChessGame)

Coveralls evaluates code coverage. Project goal is to stay above 80%.

[coveralls.io/github/pelletier2017/ChessGame](https://coveralls.io/github/pelletier2017/ChessGame)

## Deployment

No deployment implemented yet, will come with flask update

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [Travis CI](https://travis-ci.org/) - Continuous Integration
* [Coveralls](https://coveralls.io/) - Used to test code coverage

## Contributing

Contributing guide coming later.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
