import streamlit as st

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="My Smart Planner",
    page_icon="📅",
    layout="centered"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #FFF8EC;
    }

    h1, h2, h3 {
        color: #2F5D3A;
    }

    /* Input box */
    .stTextInput input,
    .stTimeInput input {
        background-color: white;
        border-radius: 10px;
    }

    /* Button */
    div.stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 8px 18px;
        font-weight: bold;
    }

    div.stButton > button:hover {
        background-color: #3D8B40;
        color: white;
    }

    /* Activity Card */
    .activity-card {
        background-color: white;
        border: 1px solid #DDDDDD;
        border-radius: 12px;
        padding: 14px;
        margin-bottom: 10px;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.05);
    }

    /* Summary Cards */
    .summary-card {
        border-radius: 14px;
        padding: 18px;
        text-align: center;
        font-weight: bold;
    }

    .total-card {
        background-color: #E8F2FF;
    }

    .completed-card {
        background-color: #E6F4E6;
    }

    .todo-card {
        background-color: #FFF2D7;
    }

    .progress-card {
        background-color: #F1E8FF;
    }

    .summary-number {
        font-size: 30px;
        margin-top: 5px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# SESSION DATA
# =========================

if "activities" not in st.session_state:
    st.session_state.activities = []

# =========================
# TITLE
# =========================

st.title("MY SMART PLANNER")
st.write("Plan Today, Achieve Tomorrow!")

# =========================
# INPUT
# =========================

time = st.time_input("Time")

activity_name = st.text_input("Activity")

if st.button("+ ADD ACTIVITY"):

    if activity_name.strip() == "":
        st.warning("Please enter an activity.")

    else:
        st.session_state.activities.append(
            {
                "time": time.strftime("%H:%M"),
                "name": activity_name,
                "status": "TODO"
            }
        )

        st.success("Activity added! ⭐")
        st.rerun()

# =========================
# TODAY'S PLAN
# =========================

st.subheader("TODAY'S PLAN")

for index, activity in enumerate(st.session_state.activities):

    with st.container():

        st.markdown(
            '<div class="activity-card">',
            unsafe_allow_html=True
        )

        col1, col2, col3, col4 = st.columns(
            [1, 2, 5, 2]
        )

        with col1:

            done = st.checkbox(
                "",
                value=activity["status"] == "DONE",
                key=f"check_{index}"
            )

            if done:
                activity["status"] = "DONE"
            else:
                activity["status"] = "TODO"

        with col2:

            st.markdown(
                f"**{activity['time']}**"
            )

        with col3:

            st.write(
                activity["name"]
            )

        with col4:

            if st.button(
                "Delete",
                key=f"delete_{index}"
            ):

                st.session_state.activities.pop(index)

                st.rerun()

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

# =========================
# SUMMARY
# =========================

total = len(st.session_state.activities)

completed = sum(
    1
    for activity in st.session_state.activities
    if activity["status"] == "DONE"
)

not_completed = total - completed

if total > 0:
    progress = int(
        completed / total * 100
    )
else:
    progress = 0

st.subheader("TODAY'S SUMMARY")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        f"""
        <div class="summary-card total-card">
            Total
            <div class="summary-number">{total}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="summary-card completed-card">
            Completed
            <div class="summary-number">{completed}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div class="summary-card todo-card">
            Not Completed
            <div class="summary-number">{not_completed}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        f"""
        <div class="summary-card progress-card">
            Progress
            <div class="summary-number">{progress}%</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")

st.progress(progress / 100)