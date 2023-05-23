<!DOCTYPE html>
<html>
<head>
    <title>Tour Registration</title>
    <style>
        .passenger {
            margin-bottom: 10px;
        }
    </style>
    <script>
        function calculateTotalFare() {
            var farePerPerson = 900;
            var passengerCount = document.getElementsByClassName('passenger').length;
            var totalFare = farePerPerson * passengerCount;
            document.getElementById('total-fare').innerText = totalFare;
        }

        function addPassenger() {
            var passengerContainer = document.getElementById('passenger-container');

            var passengerDiv = document.createElement('div');
            passengerDiv.classList.add('passenger');

            var passengerIndex = passengerContainer.childElementCount + 1;

            var nameLabel = document.createElement('label');
            nameLabel.innerText = 'Name:';
            var nameInput = document.createElement('input');
            nameInput.type = 'text';
            nameInput.name = 'name' + passengerIndex;
            nameLabel.appendChild(nameInput);

            var emailLabel = document.createElement('label');
            emailLabel.innerText = 'Email:';
            var emailInput = document.createElement('input');
            emailInput.type = 'email';
            emailInput.name = 'email' + passengerIndex;
            emailLabel.appendChild(emailInput);

            var mobileLabel = document.createElement('label');
            mobileLabel.innerText = 'Mobile:';
            var mobileInput = document.createElement('input');
            mobileInput.type = 'tel';
            mobileInput.name = 'mobile' + passengerIndex;
            mobileLabel.appendChild(mobileInput);

            var ageLabel = document.createElement('label');
            ageLabel.innerText = 'Age:';
            var ageInput = document.createElement('input');
            ageInput.type = 'number';
            ageInput.name = 'age' + passengerIndex;
            ageLabel.appendChild(ageInput);

            var genderLabel = document.createElement('label');
            genderLabel.innerText = 'Gender:';
            var genderSelect = document.createElement('select');
            genderSelect.name = 'gender' + passengerIndex;
            var maleOption = document.createElement('option');
            maleOption.value = 'male';
            maleOption.innerText = 'Male';
            var femaleOption = document.createElement('option');
            femaleOption.value = 'female';
            femaleOption.innerText = 'Female';
            genderSelect.appendChild(maleOption);
            genderSelect.appendChild(femaleOption);
            genderLabel.appendChild(genderSelect);

            var deleteButton = document.createElement('button');
            deleteButton.type = 'button';
            deleteButton.innerText = '-';
            deleteButton.onclick = function() {
                passengerContainer.removeChild(passengerDiv);
                calculateTotalFare();
            };

            passengerDiv.appendChild(nameLabel);
            passengerDiv.appendChild(emailLabel);
            passengerDiv.appendChild(mobileLabel);
            passengerDiv.appendChild(ageLabel);
            passengerDiv.appendChild(genderLabel);
            passengerDiv.appendChild(deleteButton);

            passengerContainer.appendChild(passengerDiv);
            calculateTotalFare();
        }

        function init() {
            var addButton = document.getElementById('add-passenger');
            addButton.onclick = addPassenger;
        }

        window.onload = init;
    </script>
</head>
<body>
    <h1>Tour Registration</h1>
    <form>
        <div id="passenger-container">
            <div class="passenger">
                <label for="name1">Name:</label>
                <input type="text" id="name1" name="name1" required>

                <label for="email1">Email
                :</label>
                <input type="email" id="email1" name="email1" required>

                <label for="mobile1">Mobile:</label>
                <input type="tel" id="mobile1" name="mobile1" required>

                <label for="age1">Age:</label>
                <input type="number" id="age1" name="age1" required>

                <label for="gender1">Gender:</label>
                    <option value="male">Male</option>
                    <option value="female">Female</option>
                </select>
            </div>
        </div>
        <button type="button" id="add-passenger">+</button>

        <div>
            <strong>Total Fare:</strong> $<span id="total-fare">900</span>
        </div>

        <button type="submit">Register</button>
    </form>
</body>
</html>


""
Tic-Tac-Toe players using inheritance implementation by Kylie YIng
YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

import math
import random


class Player():
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'

        # first we want to check if the previous move is a winner
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move

            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best
