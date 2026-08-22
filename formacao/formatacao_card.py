import streamlit as st


def card_kpi(
    titulo,
    valor,
    delta=None,
    icone="📊",
    positivo=True
):

    cor_delta = "#16A34A" if positivo else "#DC2626"

    html = f"""
    <div style="
        background-color: white;
        border: 1px solid #E5E7EB;
        border-radius: 18px;
        padding: 20px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
        height: 140px;
        margin-bottom: 10px;
    ">

        <div style="
            display: flex;
            justify-content: space-between;
            align-items: center;
        ">

            <span style="
                font-size: 14px;
                color: #6B7280;
                font-weight: 600;
            ">
                {titulo}
            </span>

            <span style="
                font-size: 24px;
            ">
                {icone}
            </span>

        </div>

        <div style="
            font-size: 28px;
            font-weight: 700;
            color: #111827;
            margin-top: 15px;
        ">
            {valor}
        </div>

        <div style="
            font-size: 13px;
            color: {cor_delta};
            margin-top: 8px;
            font-weight: 600;
        ">
            {delta if delta else ""}
        </div>

    </div>
    """

    st.markdown(html, unsafe_allow_html=True)