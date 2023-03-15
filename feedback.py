def get_user_feedback(input_sentence, predicted_intent):
    # This function prompts the user for feedback on the accuracy of the predicted intent
    print(f"The system predicted the following intent for your input: {predicted_intent}")
    feedback = input("Did the system accurately capture your intent? (yes/no): ")
    if feedback.lower() == "yes":
        return True
    elif feedback.lower() == "no":
        # If the user indicates that the system made an incorrect prediction, ask for the correct intent
        correct_intent = input("What was your intended intent? ")
        # Return a tuple with the corrected intent and a flag indicating that the prediction was incorrect
        return (correct_intent, False)
    else:
        # If the user provides an invalid response, prompt again
        print("Invalid response. Please enter 'yes' or 'no'")
        return get_user_feedback(input_sentence, predicted_intent)

def update_model_with_feedback(input_sentence, predicted_intent, feedback):
    if feedback is True:
        # If the user confirms that the prediction was correct, do nothing
        return
    else:
        # If the user indicates that the prediction was incorrect, update the model's training data with the corrected intent
        corrected_intent, incorrect = feedback
        # Add the corrected intent to the training data
        intents.append({"tag": corrected_intent, "patterns": [input_sentence], "responses": []})
        # If the incorrect flag is set, prompt the user to confirm that the corrected intent is accurate
        if incorrect:
            print("Thank you for your feedback. Please confirm the corrected intent:")
            new_feedback = get_user_feedback(input_sentence, corrected_intent)
            update_model_with_feedback(input_sentence, corrected_intent, new_feedback)
        else:
            print("Thank you for your feedback. The model has been updated.")

update_model_with_feedback("hi","hello",-1)