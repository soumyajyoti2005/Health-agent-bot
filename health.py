import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")


def get_health_advice(user_message):
    """
    Get conversational health advice from AI based on user's message
    """
    
    # System prompt to guide the AI's behavior
    system_instruction = """
You are a friendly, knowledgeable, and professional Health Coach AI assistant. Your role is to provide helpful, accurate, and personalized health, nutrition, fitness, and wellness advice in a conversational manner.

CORE CAPABILITIES:
- Provide expert advice on fitness, exercise, and workout routines
- Offer nutrition guidance, meal planning, and dietary recommendations
- Give sleep optimization tips and sleep hygiene advice
- Calculate and analyze BMI, caloric needs, and other health metrics
- Suggest lifestyle improvements for overall wellness
- Provide motivation and encouragement for health goals
- Answer questions about specific health conditions (informational only, not diagnosis)
- Offer stress management and mental wellness tips

IMPORTANT GUIDELINES:
1. Be conversational, friendly, and supportive - like a real health coach
2. Ask clarifying questions when you need more information
3. Provide specific, actionable advice with real numbers and examples
4. Use formatting (headers, bullet points, numbered lists) for clarity
5. Include relevant emojis to make responses engaging
6. NEVER provide medical diagnosis or replace professional medical advice
7. Always remind users to consult healthcare professionals for serious concerns
8. Be encouraging and positive while being honest about health realities
9. Adapt your response length to the question - brief for simple queries, detailed for complex ones
10. Reference scientific principles when relevant, but keep it accessible

TONE: Professional yet warm, knowledgeable yet approachable, motivating yet realistic

When users ask about their health metrics (height, weight, sleep, steps, etc.), engage naturally and offer to calculate or analyze the information they provide.
"""

    try:
        # Configure generation for conversational responses
        generation_config = {
            "temperature": 0.8,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
        }

        # Create chat session with system instruction
        chat = model.start_chat(history=[])
        
        # Combine system instruction with user message
        full_prompt = f"{system_instruction}\n\nUser: {user_message}\n\nHealth Coach AI:"
        
        # Generate response
        response = chat.send_message(
            full_prompt,
            generation_config=generation_config
        )
        
        return response.text
        
    except Exception as e:
        print(f"Error generating AI response: {str(e)}")
        return f"I apologize, but I encountered an error processing your request. Please try rephrasing your question or ask something else. Error details: {str(e)}"


# Optional: Add a function for multi-turn conversations with history
def get_health_advice_with_history(user_message, conversation_history=None):
    """
    Get health advice while maintaining conversation context
    conversation_history: list of dicts with 'role' and 'content' keys
    """
    
    system_instruction = """
You are a friendly, knowledgeable, and professional Health Coach AI assistant providing conversational health advice.

Remember the conversation context and build upon previous exchanges naturally. If the user references something from earlier in the conversation, acknowledge it and provide relevant follow-up advice.
"""

    try:
        generation_config = {
            "temperature": 0.8,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
        }

        # Start chat with history if provided
        if conversation_history:
            chat = model.start_chat(history=conversation_history)
        else:
            chat = model.start_chat(history=[])
        
        # Send message with system instruction
        full_prompt = f"{system_instruction}\n\nUser: {user_message}"
        
        response = chat.send_message(
            full_prompt,
            generation_config=generation_config
        )
        
        return response.text
        
    except Exception as e:
        print(f"Error generating AI response: {str(e)}")
        return "I apologize, but I encountered an error. Please try again."


if __name__ == "__main__":
    print("=" * 60)
    print("🏥 HEALTH COACH AI - Interactive Chat Mode")
    print("=" * 60)
    print("Type your health questions below. Type 'quit' or 'exit' to stop.\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
            print("\n👋 Thanks for chatting! Stay healthy!")
            break
        
        if not user_input:
            continue
        
        print("\n🤖 Health Coach AI: ", end="", flush=True)
        response = get_health_advice(user_input)
        print(response)
        print("\n" + "-" * 60 + "\n")
