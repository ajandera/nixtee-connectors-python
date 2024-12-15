from nixtee_client.client import NixteeClient

client = NixteeClient()

try:
    # Authenticate and get token
    token = client.authorize("user@example.com", "password123")
    print("Token:", token)

    # Example of using the train function
    train_response = client.train({"data": "your training data here"})
    print("Train response:", train_response)

    # Other functions can be used similarly
    # client.save("model_id", {"param": "value"})
    # client.load("model_id")
    # client.predict("model_id", {"input": "data"})
    # client.classify("model_id", {"input": "data"})

except Exception as e:
    print("Error:", e)
