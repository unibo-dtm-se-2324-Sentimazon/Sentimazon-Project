import matplotlib.pyplot as plt


def plot_top_noun_keywords(noun_counts):
    plt.figure(figsize=(12, 6))
    noun_counts.plot(kind='bar')
    plt.xlabel('Keywords')
    plt.ylabel('Frequency')
    plt.title('Top 20 Noun Keywords')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_top_product_aspects(noun_counts):
    plt.figure(figsize=(10, 6))
    noun_counts.sort_values().plot(kind='barh')
    plt.title('Top Product Aspects Mentioned in Reviews')
    plt.xlabel('Frequency')
    plt.ylabel('Aspects')
    plt.tight_layout()
    plt.show()

    import matplotlib.pyplot as plt


def plot_top_noun_keywords(noun_counts):
    plt.figure(figsize=(12, 6))
    noun_counts.plot(kind='bar')
    plt.xlabel('Keywords')
    plt.ylabel('Frequency')
    plt.title('Top 20 Noun Keywords')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_top_product_aspects(noun_counts):
    plt.figure(figsize=(10, 6))
    noun_counts.sort_values().plot(kind='barh')
    plt.title('Top Product Aspects Mentioned in Reviews')
    plt.xlabel('Frequency')
    plt.ylabel('Aspects')
    plt.tight_layout()
    plt.show()


def plot_model_performance(results_table):
    results_table.set_index('Model').plot(kind='bar')
    plt.title("Performance Comparison")
    plt.ylabel("Score")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()