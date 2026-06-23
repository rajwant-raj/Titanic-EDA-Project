import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for all plots
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

def main():
    print("Starting Titanic EDA visualization generator...")
    
    # 1. Create outputs directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    outputs_dir = os.path.join(script_dir, "outputs")
    os.makedirs(outputs_dir, exist_ok=True)
    print(f"Saving outputs to: {outputs_dir}")
    
    # 2. Load dataset
    print("Loading Titanic dataset...")
    try:
        df = sns.load_dataset('titanic')
    except Exception as e:
        print(f"Error loading via seaborn, attempting fallback: {e}")
        # Fallback online URL if seaborn fails
        url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
        df = pd.read_csv(url)
    
    print(f"Dataset successfully loaded. Shape: {df.shape}")
    
    # 3. Create distributions
    
    # a. Age distribution
    print("Generating age_distribution.png...")
    plt.figure()
    sns.histplot(data=df, x='age', kde=True, color='skyblue', bins=30)
    plt.title('Distribution of Passenger Ages on the Titanic')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(os.path.join(outputs_dir, 'age_distribution.png'), dpi=300)
    plt.close()
    
    # b. Gender distribution
    print("Generating gender_distribution.png...")
    plt.figure()
    sns.countplot(data=df, x='sex', palette='pastel')
    plt.title('Gender Distribution of Passengers')
    plt.xlabel('Sex')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(os.path.join(outputs_dir, 'gender_distribution.png'), dpi=300)
    plt.close()
    
    # c. Survival distribution
    print("Generating survival_distribution.png...")
    plt.figure()
    # Map survival to readable categories if numeric
    if df['survived'].dtype in [np.int64, np.int32, int]:
        survival_data = df['survived'].map({0: 'No', 1: 'Yes'})
    else:
        survival_data = df['survived']
    sns.countplot(
    x=survival_data,
    hue=survival_data,
    palette='Set2',
    legend=False
)
    plt.title('Overall Survival Count')
    plt.xlabel('Survived')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(os.path.join(outputs_dir, 'survival_distribution.png'), dpi=300)
    plt.close()
    
    # d. Survival by gender
    print("Generating survival_by_gender.png...")
    plt.figure()
    sns.countplot(
    data=df,
    x='sex',
    hue='sex',
    palette='pastel',
    legend=False
)

    plt.title('Survival Breakdown by Gender')
    plt.xlabel('Sex')
    plt.ylabel('Count')
    plt.legend(title='Survived', labels=['No', 'Yes'] if df['survived'].dtype in [np.int64, np.int32, int] else None)
    plt.tight_layout()
    plt.savefig(os.path.join(outputs_dir, 'survival_by_gender.png'), dpi=300)
    plt.close()
    
    # e. Survival by class
    print("Generating survival_by_class.png...")
    plt.figure()
    # Handle both seaborn dataset (which has 'class' and 'pclass') and standard CSV (which has 'Pclass')
    class_col = 'class' if 'class' in df.columns else 'Pclass'
    sns.countplot(data=df, x=class_col, hue='survived', palette='viridis')
    plt.title('Survival Breakdown by Passenger Class')
    plt.xlabel('Passenger Class')
    plt.ylabel('Count')
    plt.legend(title='Survived', labels=['No', 'Yes'] if df['survived'].dtype in [np.int64, np.int32, int] else None)
    plt.tight_layout()
    plt.savefig(os.path.join(outputs_dir, 'survival_by_class.png'), dpi=300)
    plt.close()
    
    # f. Correlation heatmap
    print("Generating correlation_heatmap.png...")
    plt.figure()
    # Select only numeric columns for correlation matrix
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    corr_matrix = df[numeric_cols].corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Correlation Heatmap of Numerical Features')
    plt.tight_layout()
    plt.savefig(os.path.join(outputs_dir, 'correlation_heatmap.png'), dpi=300)
    plt.close()
    
    print("All visualizations successfully generated and saved to 'outputs/'!")

if __name__ == '__main__':
    main()
