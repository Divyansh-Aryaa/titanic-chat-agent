import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

from data_loader import load_data

df = load_data()

def text_answer(question: str):

    q = question.lower()

    # Percentage male
    if "percentage" in q and "male" in q:
        male_percent = (df["Sex"] == "male").mean() * 100
        return f"{male_percent:.2f}% of the passengers were male.", None
    
    # Average fare
    if "average ticket fare" in q or "average fare" in q:
        avg_fare = df["Fare"].mean()
        return f"The average ticket fare was {avg_fare:.2f}.", None
    
    # Overall Survival rate
    if "survival rate" in q and "gender" not in q:
        rate = df["Survived"].mean() * 100
        return f"Overall, the survival rate was {rate:.2f}%.", None
    

    # Survival by gender
    if "survival" in q and "gender" in q:
        data = df.groupby("Sex")["Survived"].mean() * 100
        plt.figure(figsize = (6,4))
        data.plot(kind="bar")
        plt.title("Survival Rate by Gender")
        #plt.close()
        return data.round(2).to_string(), plot_to_base64()
    
    # Survival by class
    if "survival" in q and "class" in q:
        data = df.groupby("Pclass")["Survived"].mean() * 100
        plt.figure(figsize=(6,4))
        data.plot(kind="bar")
        plt.title("Survival Rate by Class")
        #plt.close()
        return data.round(2).to_string(), plot_to_base64()

    # Gender Count
    if "gender count" in q:
        counts = df["Sex"].value_counts()
        plt.figure(figsize=(5,3))
        counts.plot(kind="bar")
        plt.title("Gender Distribution")
        #plt.close()
        return counts.to_string(), plot_to_base64()
    
    # Histogram age
    if "histogram" in q and "age" in q:
        plt.figure(figsize=(8,5))
        sns.histplot(df["Age"].dropna(), bins=300)
        #plt.close()
        return "Here is the age distribution.", plot_to_base64()
        
    
    # Embarked Count
    if "embarked" in q:
        counts = df["Embarked"].value_counts()
        plt.figure(figsize=(6,4))
        counts.plot(kind="bar")
        plt.title("Passenger by Embarkation Port")
        #plt.close()
        return str(counts.to_dict()), plot_to_base64()
    
    return "Sorry, I don't understand that question yet.", None

def plot_to_base64():
    buffer = io.BytesIO()
    plt.savefig(buffer,format="png")
    buffer.seek(0)
    image_png =buffer.getvalue()
    buffer.close()
    return base64.b64encode(image_png).decode()

    
 
        
       
