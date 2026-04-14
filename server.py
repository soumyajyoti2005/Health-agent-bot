from flask import Flask, render_template, request, jsonify
from waitress import serve
from health import get_health_advice
import re
import os

app = Flask(__name__)


def format_health_advice(text):
    """Convert markdown-style text to HTML with proper formatting"""
    
    # Step 1: First convert bold text (**text** to <strong>)
    text = re.sub(r'\*\*([^*]+?)\*\*', r'<strong>\1</strong>', text)
    
    # Step 2: Process line by line for structure
    lines = text.split('\n')
    formatted_lines = []
    in_list = False
    list_type = None  # 'ul' or 'ol'
    
    for line in lines:
        stripped = line.strip()
        
        # Skip empty lines
        if not stripped:
            if in_list:
                formatted_lines.append(f'</{list_type}>')
                in_list = False
                list_type = None
            formatted_lines.append('')
            continue
        
        # Check for headers (must be at start of line)
        if stripped.startswith('### '):
            if in_list:
                formatted_lines.append(f'</{list_type}>')
                in_list = False
            content = stripped[4:].strip()
            formatted_lines.append(f'<h3>{content}</h3>')
            
        elif stripped.startswith('## '):
            if in_list:
                formatted_lines.append(f'</{list_type}>')
                in_list = False
            content = stripped[3:].strip()
            formatted_lines.append(f'<h2>{content}</h2>')
            
        elif stripped.startswith('# '):
            if in_list:
                formatted_lines.append(f'</{list_type}>')
                in_list = False
            content = stripped[2:].strip()
            formatted_lines.append(f'<h1>{content}</h1>')
        
        # Check for bullet points (lines starting with * or - but NOT **)
        elif re.match(r'^[\*\-]\s+', stripped) and not stripped.startswith('**'):
            content = re.sub(r'^[\*\-]\s+', '', stripped)
            
            if not in_list or list_type != 'ul':
                if in_list:
                    formatted_lines.append(f'</{list_type}>')
                formatted_lines.append('<ul>')
                in_list = True
                list_type = 'ul'
            
            formatted_lines.append(f'<li>{content}</li>')
        
        # Check for numbered lists
        elif re.match(r'^\d+\.\s+', stripped):
            content = re.sub(r'^\d+\.\s+', '', stripped)
            
            if not in_list or list_type != 'ol':
                if in_list:
                    formatted_lines.append(f'</{list_type}>')
                formatted_lines.append('<ol>')
                in_list = True
                list_type = 'ol'
            
            formatted_lines.append(f'<li>{content}</li>')
        
        else:
            # Close any open list
            if in_list:
                formatted_lines.append(f'</{list_type}>')
                in_list = False
                list_type = None
            
            # Regular paragraph
            formatted_lines.append(f'<p>{stripped}</p>')
    
    # Close any remaining list
    if in_list:
        formatted_lines.append(f'</{list_type}>')
    
    # Join lines
    result = '\n'.join(formatted_lines)
    
    # Clean up extra empty paragraphs
    result = re.sub(r'<p></p>', '', result)
    result = re.sub(r'\n\n+', '\n', result)
    
    return result


@app.route("/")
def index():
    """Render the main chat interface"""
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    """Handle chat messages from the user"""
    try:
        data = request.get_json()
        user_message = data.get("message", "").strip()
        
        if not user_message:
            return jsonify({
                "success": False,
                "error": "Please enter a message."
            })
        
        # Get AI response
        print(f"\n📩 User: {user_message}")
        
        ai_response = get_health_advice(user_message)
        
        print(f"🤖 AI Response (first 200 chars): {ai_response[:200]}...")
        
        # Format the response to HTML
        formatted_response = format_health_advice(ai_response)
        
        return jsonify({
            "success": True,
            "response": formatted_response
        })
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return jsonify({
            "success": False,
            "error": f"An error occurred: {str(e)}"
        })


if __name__ == "__main__":
    print("=" * 60)
    print("🏥 Health Coach AI Chat Server Starting...")
    print("=" * 60)
    print("📍 Server running on: http://localhost:5000")
    print("💬 Chat interface ready!")
    print("⚡ Press Ctrl+C to stop the server")
    print("=" * 60)
    serve(app, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
