plt.xlabel("Monthly Charges")
    plt.ylabel("Number of Customers")
    plt.tight_layout()
    plt.show()


# -----------------------------------------
# 10. Tenure vs Churn
# -----------------------------------------

if "Tenure" in df.columns and "Churn" in df.columns:

    df.groupby("Churn")["Tenure"].mean().plot(
        kind="bar",
        title="Average Tenure by Churn Status"
    )

    plt.xlabel("Churn Status")
    plt.ylabel("Average Tenure")
    plt.tight_layout()
    plt.show()


# -----------------------------------------
# 11. Monthly Charges vs Churn
# -----------------------------------------

if "MonthlyCharges" in df.columns and "Churn" in df.columns:

    df.groupby("Churn")["MonthlyCharges"].mean().plot(
        kind="bar",
        title="Average Monthly Charges by Churn Status"
    )

    plt.xlabel("Churn Status")
    plt.ylabel("Average Monthly Charges")
    plt.tight_layout()
    plt.show()


# -----------------------------------------
# 12. Correlation Analysis
# -----------------------------------------

numeric_data = df.select_dtypes(include=np.number)

print("\nCorrelation Matrix:")
print(numeric_data.corr())
