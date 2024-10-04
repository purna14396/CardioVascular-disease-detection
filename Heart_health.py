import streamlit as st
from PIL import Image
import pandas as pd


def create_sidebar():
    # Sidebar: Add logo
    logo = Image.open('D:/Downloads/Artificial_Intelligence/PROJECTS____/Cardio Vascular Disease Detection Project/heart_beat.png')  # Path to your logo
    logo = logo.resize((500, 500))
    st.sidebar.image(logo, use_column_width=True)
    
    # Sidebar: Add text
    st.sidebar.markdown("# Welcome to Heart Health App")
    st.sidebar.markdown("""
    Your comprehensive guide to understanding heart diseases, prevention, and maintenance of a healthy heart.
    """)

# Page configuration
st.set_page_config(
    page_title="Heart_health",
    page_icon="D:/Downloads/Artificial_Intelligence/PROJECTS____/Cardio Vascular Disease Detection Project/heart_beat.png",  # Path to your favicon file
    layout="wide"
)

# Create the sidebar
create_sidebar()




# Set the title and header
st.title("Understanding Heart Diseases and How to Maintain a Healthy Heart")
st.subheader("An Introduction to Cardiovascular Health")

# Add a banner image (optional)
image = Image.open('D:/Downloads/Artificial_Intelligence/PROJECTS____/Cardio Vascular Disease Detection Project/Heart_health_banner.jpg')  # Replace with the path to your image
st.image(image, use_column_width=True)

# Brief introduction to heart health
st.write("""
### Introduction to Heart Health
Maintaining heart health is essential for overall well-being. A healthy heart ensures proper blood circulation, which delivers oxygen and nutrients to the body's tissues and organs. By adopting a healthy lifestyle and being aware of heart diseases, you can significantly reduce your risk of developing cardiovascular issues.
""")

# What are Heart Diseases?
st.header("What are Heart Diseases?")
st.write("""
Heart diseases, or cardiovascular diseases, encompass a range of disorders that affect the heart and blood vessels. They are a leading cause of death worldwide. Common factors that contribute to heart diseases include high blood pressure, high cholesterol, smoking, obesity, and physical inactivity. The good news is that many types of heart disease can be prevented or managed with the right lifestyle choices.
""")

# Set the title and header
st.title("Understanding Heart Diseases")

# Small header and detailed descriptions for each type of heart disease
st.header("Types of Heart Diseases")

# List of heart diseases with explanations
diseases = {
    "1. Coronary Artery Disease (CAD)": "Occurs when the blood vessels that supply oxygen and blood to the heart become narrowed or blocked, often due to cholesterol buildup.",
    "2. Heart Attack (Myocardial Infarction)": "Happens when the blood flow to a part of the heart is blocked for a long enough time that part of the heart muscle is damaged or dies.",
    "3. Arrhythmia": "Refers to an irregular heartbeat, which can be too fast (tachycardia), too slow (bradycardia), or erratic.",
    "4. Heart Failure": "A condition in which the heart is unable to pump blood effectively, leading to fatigue and fluid retention.",
    "5. Hypertension": "High blood pressure that increases the risk of heart disease and stroke, often referred to as a 'silent killer.'",
    "6. Cardiomyopathy": "A disease of the heart muscle that makes it harder for the heart to pump blood and can lead to heart failure.",
    "7. Peripheral Artery Disease (PAD)": "A condition in which narrowed arteries reduce blood flow to the limbs, often causing pain.",
    "8. Valvular Heart Disease": "Involves damage to one or more of the heart valves, affecting blood flow through the heart.",
    "9. Congenital Heart Defects": "Heart structural problems present at birth that can affect normal blood flow.",
    "10. Stroke": "A condition where blood supply to the brain is interrupted, leading to brain damage."
}

# Display each disease with a small heading and its description

for disease, description in diseases.items():

    st.subheader(disease)
    st.write(description)



# Main content for the Dos and Don'ts page
st.header("Dos and Don'ts for a Healthy Heart")

# Create a table for Dos
st.subheader("Dos for Heart Health")
dos_data = [
    ["🥗 Eat a balanced diet", "Rich in fruits, vegetables, whole grains, and lean proteins."],
    ["🚶 Stay physically active", "Aiming for at least 150 minutes of moderate aerobic exercise per week."],
    ["🩺 Regular check-ups", "Monitor blood pressure, cholesterol, and blood sugar levels."],
    ["🚭 Quit smoking", "Avoid exposure to secondhand smoke."],
    ["😌 Manage stress", "Use techniques like meditation, yoga, or deep breathing exercises."],
    ["💧 Stay hydrated", "Drink plenty of water throughout the day."],
    ["⚖️ Maintain a healthy weight", "Through diet and exercise."],
    ["💤 Get adequate sleep", "Aiming for 7-9 hours per night."],
    ["🍏 Incorporate healthy fats", "Found in avocados and nuts."],
    ["🌱 Limit processed foods", "And added sugars in your diet."],
    ["🥑 Eat omega-3 fatty acids", "Found in fatty fish like salmon and walnuts."],
    ["🍷 Consume alcohol in moderation", "Up to one drink per day for women and two for men."],
    ["🤝 Stay socially connected", "Support mental and emotional health."],
    ["📖 Educate yourself", "Stay informed about heart health and risk factors."],
    ["🍊 Increase fiber intake", "Through whole grains, fruits, and vegetables to lower cholesterol levels."]
]

# Create DataFrame for Dos
dos_df = pd.DataFrame(dos_data, columns=["Activity", "Reason"])
st.table(dos_df)

# Create a table for Don'ts
st.subheader("Don'ts for Heart Health")
donts_data = [
    ["❌ Avoid processed and high-sugar foods", "Contributes to weight gain and poor heart health."],
    ["❌ Don't smoke or use tobacco", "Significantly increases the risk of heart disease."],
    ["❌ Limit alcohol consumption", "No more than one drink per day for women and two for men."],
    ["❌ Avoid a sedentary lifestyle", "Too much sitting negatively impacts your heart."],
    ["❌ Avoid excess salt", "Can lead to high blood pressure."],
    ["❌ Don't ignore symptoms", "Of heart disease, such as chest pain or shortness of breath."],
    ["❌ Avoid eating large portions", "Can lead to overeating and weight gain."],
    ["❌ Don't skip meals", "Can lead to unhealthy snacking and blood sugar spikes."],
    ["❌ Limit caffeine intake", "Especially if sensitive to it, as it can increase heart rate."],
    ["❌ Don't let stress go unmanaged", "Chronic stress can lead to heart problems."]
]

# Create DataFrame for Don'ts
donts_df = pd.DataFrame(donts_data, columns=["Activity", "Reason"])
st.table(donts_df)