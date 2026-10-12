
import torch
import gradio as gr
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_ID = "Qwen/Qwen2.5-1.5B-Instruct"

print(f"Loading {MODEL_ID}. The first launch may take several minutes...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float32,
    low_cpu_mem_usage=True,
)
model.eval()

print("Model loaded successfully!")


def respond(message, history):
    if not message or not message.strip():
        return "Please enter a question."

    messages = [
        {
            "role": "system",
            "content": (
                "You are HCI Study Buddy, an educational assistant "
                "specializing in Human-Computer Interaction, usability, "
                "user interface design, accessibility, and artificial "
                "intelligence. Explain concepts clearly, give practical "
                "examples when useful, and acknowledge uncertainty. "
                "Remind students to verify important information."
            ),
        }
    ]

    # Include recent conversation turns for follow-up questions.
    for item in (history or [])[-6:]:
        if isinstance(item, dict):
            role = item.get("role")
            content = item.get("content", "")
            if role in ("user", "assistant") and isinstance(content, str):
                messages.append({"role": role, "content": content})
        elif isinstance(item, (list, tuple)) and len(item) == 2:
            user_text, assistant_text = item
            if isinstance(user_text, str):
                messages.append({"role": "user", "content": user_text})
            if isinstance(assistant_text, str):
                messages.append({"role": "assistant", "content": assistant_text})

    messages.append({"role": "user", "content": message.strip()})

    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )

    inputs = tokenizer(prompt, return_tensors="pt")

    with torch.inference_mode():
        outputs = model.generate(
            **inputs,
            max_new_tokens=220,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            pad_token_id=tokenizer.eos_token_id,
        )

    new_tokens = outputs[0][inputs["input_ids"].shape[1]:]
    answer = tokenizer.decode(new_tokens, skip_special_tokens=True).strip()

    return answer or "I couldn't generate a response. Please try again."


with gr.Blocks(title="HCI Study Buddy") as demo:
    gr.Markdown("# HCI Study Buddy")
    gr.Markdown(
        "An LLM-powered learning assistant for Human-Computer Interaction. "
        "Responses may contain errors; verify important information."
    )

    gr.ChatInterface(
        fn=respond,
        title="Ask an HCI question",
        description="Ask about usability, accessibility, interface design, or AI.",
    )

if __name__ == "__main__":
    demo.launch()
