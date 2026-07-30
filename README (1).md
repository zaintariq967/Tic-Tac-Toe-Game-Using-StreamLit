# ❌⭕ Tic Tac Toe — Streamlit Edition

A fully-featured Tic Tac Toe game built with Python and Streamlit. It includes an interactive web UI, real-time win and draw detection, highlighted winning lines, persistent score tracking across rounds, a detailed move history log, and a one-click round reset, all wrapped in a clean, responsive, lightweight design that's simple to run anywhere.

---

## 📸 Preview

> Run the app locally and play directly in your browser — no installation of a game engine required, just Python and Streamlit.

---

## ✨ Features

- 🎮 **Two-player local gameplay** (X vs O) on the same device
- 🏆 **Automatic win detection** for all rows, columns, and diagonals
- 🟩 **Winning line highlight** — the winning combination is visually marked
- 🤝 **Draw detection** when the board fills up with no winner
- 📊 **Persistent scoreboard** that tracks X wins, O wins, and draws across rounds
- 📜 **Move history log** showing every move made during the current round
- 🔄 **New Round** button to reset the board while keeping scores
- 🗑️ **Reset Scores** button to clear the scoreboard completely
- 🖥️ **Clean, responsive UI** built entirely with Streamlit — no extra frontend framework needed

---

## 🗂️ Project Structure

```
tictactoe-streamlit/
│
├── tictactoe.py         # Main application (game logic + Streamlit UI)
├── requirements.txt      # Python dependencies
└── README.md              # Project documentation
```

---

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **Framework:** [Streamlit](https://streamlit.io/)
- **IDE:** PyCharm

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/tictactoe-streamlit.git
cd tictactoe-streamlit
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run tictactoe.py
```

Streamlit will open the game automatically in your default browser at `http://localhost:8501`.

> ⚠️ **Note (PyCharm users):** Don't run `tictactoe.py` with the normal ▶ Run button — Streamlit apps must be launched with the `streamlit run` command above. You can also set this up as a custom PyCharm run configuration using "Module name: streamlit" with parameters `run tictactoe.py`.

---

## 🎮 How to Play

1. Player **X** always goes first.
2. Click any empty cell on the 3×3 grid to place your mark.
3. Players alternate turns automatically.
4. The game announces a winner as soon as three matching marks line up (row, column, or diagonal) and highlights the winning cells.
5. If all 9 cells fill up with no winner, the game declares a draw.
6. Click **New Round** to play again (scores are kept).
7. Click **Reset Scores** to clear the scoreboard and start fresh.

---

## 🧩 Code Overview

| Component | Description |
|---|---|
| `check_winner(board)` | Checks all win combinations and returns the winner (or draw) |
| `make_move(index)` | Handles a player's move, updates state, and checks for a winner |
| `new_round()` | Resets the board for a new round while keeping the scoreboard |
| `reset_scores()` | Resets both the board and the scoreboard |
| `st.session_state` | Used to persist game state (board, scores, history) across reruns |

---

## 📦 Requirements

```
streamlit>=1.32.0
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 🗺️ Roadmap / Ideas for Future Improvements

- [ ] Add a single-player mode with an AI opponent (Minimax algorithm)
- [ ] Add sound effects for moves and wins
- [ ] Add player name customization
- [ ] Add dark mode / theme toggle
- [ ] Deploy live on Streamlit Community Cloud

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to fork this repo and submit a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License — feel free to use, modify, and distribute it.

```
MIT License

Copyright (c) 2026 <Your Name>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions...
```

---

## 👤 Author

**Your Name**  
Built with ❤️ using Python & Streamlit in PyCharm.

- GitHub: [@your-username](https://github.com/your-username)
- LinkedIn: [Your Name](https://linkedin.com/in/your-profile)

---

## ⭐ Show Your Support

If you liked this project, give it a ⭐ on GitHub — it helps a lot!
