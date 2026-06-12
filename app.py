import streamlit as st
from intents import *
from utils import *

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="IntelliBot AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# ----------------------------------
# CUSTOM CSS
# ----------------------------------

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #0f172a,
        #111827,
        #1e293b
    );
}

.main-title{
    text-align:center;
    color:#38bdf8;
    font-size:3rem;
    font-weight:bold;
}

.sub-title{
    text-align:center;
    color:#cbd5e1;
    margin-bottom:25px;
}

.chat-container{
    border-radius:15px;
}

[data-testid="stMetric"]{
    background:#1e293b;
    padding:15px;
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------
# SESSION STATE
# ----------------------------------

defaults = {
    "history": [],
    "user_name": None,
    "messages": 0,
    "known": 0,
    "unknown": 0,
    "personality": "Friendly"
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ----------------------------------
# RESPONSE STYLE
# ----------------------------------

def style_response(text):

    mode = st.session_state.personality

    if mode == "Professional":
        return f"📌 {text}"

    if mode == "Funny":
        return f"😎 {text}"

    return text

# ----------------------------------
# CHATBOT ENGINE
# ----------------------------------

def chatbot_response(user_input):

    st.session_state.messages += 1

    if user_input in GREETINGS:
        st.session_state.known += 1
        return GREETINGS[user_input]

    if user_input in FAREWELLS:
        st.session_state.known += 1
        return FAREWELLS[user_input]

    if user_input in IDENTITY:
        st.session_state.known += 1
        return IDENTITY[user_input]

    if user_input == "time":
        st.session_state.known += 1
        return get_time()

    if user_input == "date":
        st.session_state.known += 1
        return get_date()

    if user_input == "day":
        st.session_state.known += 1
        return get_day()

    if user_input in ["quote", "motivate me"]:
        st.session_state.known += 1
        return get_quote()

    if user_input in ["tell joke", "joke"]:
        st.session_state.known += 1
        return get_joke()

    if "my name is" in user_input:

        name = extract_name(user_input)

        if name:
            st.session_state.user_name = name.title()
            st.session_state.known += 1

            return f"Nice to meet you {name.title()}"

    if user_input == "what is my name":

        st.session_state.known += 1

        if st.session_state.user_name:
            return f"Your name is {st.session_state.user_name}"

        return "I don't know your name yet."

    for mood in MOODS:

        if mood in user_input:
            st.session_state.known += 1
            return MOODS[mood]

    if user_input.startswith("calculate"):

        expression = user_input.replace(
            "calculate",
            ""
        ).strip()

        st.session_state.known += 1

        return calculate_expression(expression)

    st.session_state.unknown += 1

    return (
        "Sorry, I don't understand that. "
        "Type 'help' to see available commands."
    )

# ----------------------------------
# SIDEBAR
# ----------------------------------

with st.sidebar:

    st.title("🤖 IntelliBot")

    st.success("Decode Labs Project 1")

    st.markdown("---")

    st.subheader("Personality")

    st.session_state.personality = st.selectbox(
        "Mode",
        [
            "Friendly",
            "Professional",
            "Funny"
        ]
    )

    st.markdown("---")

    st.subheader("Quick Commands")

    st.code("""
hello
time
date
quote
tell joke
calculate 10+20
my name is John
""")

    st.markdown("---")

    if st.button("🗑 Clear Chat"):

        st.session_state.history = []
        st.rerun()

# ----------------------------------
# HEADER
# ----------------------------------

st.markdown(
    """
    <div class="main-title">
    🤖 IntelliBot AI Assistant
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="sub-title">
    Advanced Rule-Based AI Chatbot
    </div>
    """,
    unsafe_allow_html=True
)

# ----------------------------------
# DASHBOARD METRICS
# ----------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Messages",
        st.session_state.messages
    )

with col2:
    st.metric(
        "Known",
        st.session_state.known
    )

with col3:
    st.metric(
        "Unknown",
        st.session_state.unknown
    )

st.divider()

# ----------------------------------
# CHAT HISTORY
# ----------------------------------

for role, message in st.session_state.history:

    with st.chat_message(role):
        st.markdown(message)

# ----------------------------------
# CHAT INPUT
# ----------------------------------

prompt = st.chat_input(
    "Ask me anything..."
)

if prompt:

    clean_text = sanitize_input(prompt)

    bot_response = chatbot_response(
        clean_text
    )

    bot_response = style_response(
        bot_response
    )

    st.session_state.history.append(
        ("user", prompt)
    )

    st.session_state.history.append(
        ("assistant", bot_response)
    )

    st.rerun()

# ----------------------------------
# DOWNLOAD CHAT
# ----------------------------------

if st.session_state.history:

    chat_log = "\n".join(
        [
            f"{role}: {msg}"
            for role, msg
            in st.session_state.history
        ]
    )

    st.download_button(
        label="📥 Download Chat",
        data=chat_log,
        file_name="chat_history.txt",
        mime="text/plain"
    )