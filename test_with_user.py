from mf_knn_recommender import MF_KNN_Recommender

# Initialize the recommender system
recommender = MF_KNN_Recommender(
    latent_factors=100,  # Optimize number of latent factors
    steps=250,           # Number of training steps
    k=5,                 # Default number of recommendations
    alpha=0.001,         # Learning rate
    beta=0.01            # Regularization parameter
)

# Load an existing model or train a new one
if not recommender.load_model():
    print("Training a new model...")
    recommender.train('segment_dataset.csv')
    print("Training completed!")

# List of user IDs to generate recommendations for
target_users = [
    'e1feae9083c4c2895ddf6dc80526a85d', 
    'afddf43a03a9941624ed42c0b2c17280', 
    '64ee476500a01beb94df40f97a108c50'
]

print("\n===== PRODUCT RECOMMENDATIONS FOR SPECIFIC USERS =====")
for i, user_id in enumerate(target_users):
    print(f"\n{i+1}. User {user_id}:")
    print("   Standard recommendations:")
    recs = recommender.recommend_items_for_user(user_id, top_k=5, show_scores=True)
    
    print("\n   Diversified recommendations (lambda=0.7):")
    diverse_recs = recommender.diversify_recommendations(user_id, top_k=5, lambda_diversity=0.7)
    for item in diverse_recs:
        print(f"   - {item}")

print("\n===== COMPARISON OF RECOMMENDATION TYPES =====")
comparison = {}

for user_id in target_users:
    regular_recs = recommender.recommend_items_for_user(user_id, top_k=5, show_scores=False)
    diverse_recs = recommender.diversify_recommendations(user_id, top_k=5, lambda_diversity=0.7)
    
    # Count the number of different items between the two recommendation types
    differences = set(diverse_recs) - set(regular_recs)
    
    comparison[user_id] = {
        'regular': regular_recs,
        'diverse': diverse_recs,
        'num_different': len(differences),
        'different_items': list(differences)
    }

# Print comparison results
print("\nComparison of standard vs. diversified recommendations:")
for user_id, data in comparison.items():
    print(f"\nUser: {user_id}")
    print(f"  Standard: {', '.join(data['regular'])}")
    print(f"  Diversified: {', '.join(data['diverse'])}")
    print(f"  Number of different items: {data['num_different']}")
    if data['num_different'] > 0:
        print(f"  New items: {', '.join(data['different_items'])}")

# Deeper analysis for the first user in the list
focus_user = target_users[0]
print(f"\n===== DETAILED ANALYSIS FOR USER {focus_user} =====")

# Generate product embedding visualization
print("Generating product embedding plot...")
recommender.plot_item_embeddings(top_n=30, save_path=f"product_embeddings_{focus_user}.png")
print(f"Plot saved at: product_embeddings_{focus_user}.png")

# Explore the effect of different diversity parameters
print("\nEffect of diversity parameter:")
lambda_values = [0.0, 0.3, 0.5, 0.7, 1.0]

for lambda_val in lambda_values:
    recs = recommender.diversify_recommendations(focus_user, top_k=5, lambda_diversity=lambda_val)
    print(f"  Lambda = {lambda_val:.1f}: {', '.join(recs)}")
