import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="🏦 Simple Banking System", layout="centered")

# --- Title ---
st.title("🏦 Simple Banking System")
st.markdown("Manage your virtual wallet with a sleek dark interface. 💳💸")
# st.markdown("""
#     <style>
#         .stApp {
#             background-image: url("https://assets.smatechnologies.com/production/assets/images/financial_200721_124432.svg?dm=1595335473");
#             background-size: cover;
#             background-repeat: no-repeat;
#             background-attachment: fixed;
#         }
#     </style>
# """, unsafe_allow_html=True)

# --- Initialize Session State ---
if "balance" not in st.session_state:
    st.session_state.balance = 0.0

# --- Styling ---
st.markdown(
    """
    <style>
        .stApp {
            background-color: #1E1E1E;
        }
        .balance-box {
            background-color: #2C2C2C;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .balance {
            font-size: 28px;
            font-weight: bold;
            color: #00C49A;
        }
        .section-title {
            color: #F9A825;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Sidebar ---
# st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=90)
st.sidebar.image("bank.svg", width=190)
st.sidebar.header("💡 Banking Tips")
st.sidebar.markdown("- Always track your spending.")
st.sidebar.markdown("- Save regularly, even small amounts. 💰")
st.sidebar.markdown("- Don’t withdraw more than your balance! 🚫")
st.sidebar.markdown("---")

# 📬 Contact Section
st.sidebar.markdown("### 📬 Contact")
st.sidebar.write("📧 [Email Us](mailto:ismailahmedshahpk@gmail.com)")
st.sidebar.write("🔗 [Connect on LinkedIn](https://www.linkedin.com/in/ismail-ahmed-shah-2455b01ba/)")
st.sidebar.write("💬 [Chat on WhatsApp](https://wa.me/923322241405)")
st.sidebar.markdown("---")
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135716.png", width=90, use_container_width=True)
st.sidebar.markdown("<p style='text-align: center; color: grey;'>Build with ❤️ By Ismail Ahmed Shah</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

# --- Show Balance ---
balance_html = f"""
<div class="balance-box">
    <p class="section-title">💰 Current Balance</p>
    <p class="balance">${st.session_state.balance:,.2f}</p>
</div>
"""

st.markdown(balance_html, unsafe_allow_html=True)


# --- Deposit Section ---
st.markdown('<p class="section-title">➕ Deposit Money</p>', unsafe_allow_html=True)
deposit_amount = st.number_input("Enter amount to deposit:", min_value=0.0, format="%.2f", step=1.0, key="deposit")
if st.button("Deposit", type="primary"):
    if deposit_amount > 0:
        st.session_state.balance += deposit_amount
        st.success(f"✅ ${deposit_amount:.2f} deposited successfully!")
    else:
        st.warning("⚠️ Please enter a valid amount to deposit.")

st.markdown("---")

# --- Withdraw Section ---
st.markdown('<p class="section-title">➖ Withdraw Money</p>', unsafe_allow_html=True)
withdraw_amount = st.number_input("Enter amount to withdraw:", min_value=0.0, format="%.2f", step=1.0, key="withdraw")
if st.button("Withdraw"):
    if withdraw_amount <= 0:
        st.warning("⚠️ Please enter a valid amount to withdraw.")
    elif withdraw_amount > st.session_state.balance:
        st.error("❌ Insufficient funds. Try a smaller amount.")
    else:
        st.session_state.balance -= withdraw_amount
        st.success(f"✅ ${withdraw_amount:.2f} withdrawn successfully!")

# --- Footer Message ---
st.markdown("---")
st.info("🔐 This is a demo banking app. All data is session-based and will reset on refresh.")

st.image("gitbank-bg.png", width=700, use_container_width=True)