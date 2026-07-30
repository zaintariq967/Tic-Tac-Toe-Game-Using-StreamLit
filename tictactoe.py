"""
Tic Tac Toe - Streamlit App
----------------------------
A fully featured Tic Tac Toe game built with Streamlit.

Features:
- Two player mode (X vs O) on the same device
- Win detection (rows, columns, diagonals)
- Draw detection
- Winning line highlighted
- Score tracker (persists across rounds using session_state)
- Restart current round / Reset scores
- Turn indicator
- Move history

Run with:
    streamlit run tictactoe.py
"""

import streamlit as st

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------
st.set_page_config(page_title="Tic Tac Toe", page_icon="❌⭕", layout="centered")

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
WIN_COMBOS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
    (0, 4, 8), (2, 4, 6),              # diagonals
]

EMPTY_BOARD = [""] * 9

# ---------------------------------------------------------------------------
# Session state initialization
# ---------------------------------------------------------------------------
def init_state():
    defaults = {
        "board": EMPTY_BOARD.copy(),
        "current_player": "X",
        "winner": None,          # "X", "O", "Draw", or None
        "winning_combo": None,
        "scores": {"X": 0, "O": 0, "Draw": 0},
        "history": [],           # list of move strings
        "move_count": 0,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


init_state()


# ---------------------------------------------------------------------------
# Game logic helpers
# ---------------------------------------------------------------------------
def check_winner(board):
    """Return (winner, combo) if there's a winner, else (None, None)."""
    for combo in WIN_COMBOS:
        a, b, c = combo
        if board[a] and board[a] == board[b] == board[c]:
            return board[a], combo
    if all(cell != "" for cell in board):
        return "Draw", None
    return None, None


def make_move(index):
    if st.session_state.winner is not None:
        return
    if st.session_state.board[index] != "":
        return

    player = st.session_state.current_player
    st.session_state.board[index] = player
    st.session_state.move_count += 1
    row, col = divmod(index, 3)
    st.session_state.history.append(f"Move {st.session_state.move_count}: {player} -> row {row+1}, col {col+1}")

    winner, combo = check_winner(st.session_state.board)
    if winner:
        st.session_state.winner = winner
        st.session_state.winning_combo = combo
        st.session_state.scores[winner] += 1
    else:
        st.session_state.current_player = "O" if player == "X" else "X"


def new_round():
    st.session_state.board = EMPTY_BOARD.copy()
    st.session_state.current_player = "X"
    st.session_state.winner = None
    st.session_state.winning_combo = None
    st.session_state.history = []
    st.session_state.move_count = 0


def reset_scores():
    st.session_state.scores = {"X": 0, "O": 0, "Draw": 0}
    new_round()


# ---------------------------------------------------------------------------
# Styling
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>
    div.stButton > button {
        height: 90px;
        width: 100%;
        font-size: 36px;
        font-weight: bold;
        border-radius: 10px;
    }
    .win-cell button {
        background-color: #90EE90 !important;
        color: black !important;
    }
    .score-box {
        text-align: center;
        padding: 10px;
        border-radius: 8px;
        background-color: #f0f2f6;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
st.title("❌⭕ Tic Tac Toe")
st.caption("Two-player local game built with Streamlit")

# ---------------------------------------------------------------------------
# Scoreboard
# ---------------------------------------------------------------------------
score_col1, score_col2, score_col3 = st.columns(3)
with score_col1:
    st.markdown(
        f"<div class='score-box'><h4>❌ X</h4><h2>{st.session_state.scores['X']}</h2></div>",
        unsafe_allow_html=True,
    )
with score_col2:
    st.markdown(
        f"<div class='score-box'><h4>🤝 Draws</h4><h2>{st.session_state.scores['Draw']}</h2></div>",
        unsafe_allow_html=True,
    )
with score_col3:
    st.markdown(
        f"<div class='score-box'><h4>⭕ O</h4><h2>{st.session_state.scores['O']}</h2></div>",
        unsafe_allow_html=True,
    )

st.write("")

# ---------------------------------------------------------------------------
# Status message
# ---------------------------------------------------------------------------
if st.session_state.winner == "Draw":
    st.info("It's a draw! 🤝")
elif st.session_state.winner:
    st.success(f"Player {st.session_state.winner} wins! 🎉")
else:
    st.info(f"Player **{st.session_state.current_player}**'s turn")

# ---------------------------------------------------------------------------
# Board
# ---------------------------------------------------------------------------
winning_cells = set(st.session_state.winning_combo) if st.session_state.winning_combo else set()

for row in range(3):
    cols = st.columns(3, gap="small")
    for col in range(3):
        idx = row * 3 + col
        cell_value = st.session_state.board[idx]
        label = cell_value if cell_value else " "
        disabled = cell_value != "" or st.session_state.winner is not None

        with cols[col]:
            st.button(
                label,
                key=f"cell_{idx}",
                on_click=make_move,
                args=(idx,),
                disabled=disabled,
                type="primary" if idx in winning_cells else "secondary",
            )

st.write("")

# ---------------------------------------------------------------------------
# Controls
# ---------------------------------------------------------------------------
control_col1, control_col2 = st.columns(2)
with control_col1:
    st.button("🔄 New Round", on_click=new_round, use_container_width=True)
with control_col2:
    st.button("🗑️ Reset Scores", on_click=reset_scores, use_container_width=True)

# ---------------------------------------------------------------------------
# Move history (optional expander)
# ---------------------------------------------------------------------------
with st.expander("📜 Move History"):
    if st.session_state.history:
        for move in st.session_state.history:
            st.write(move)
    else:
        st.write("No moves yet.")

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.markdown("---")
st.caption("Built with Python & Streamlit")