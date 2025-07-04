import gradio as gr

def evaluate_output(user_query, retrieved_context, final_answer, answer_found):
    evaluation = ""
    rationale = ""

    if answer_found.lower() == "true":
        if retrieved_context.strip() in final_answer:
            evaluation = "Correct"
            rationale = "Answer is faithful to retrieved context and matches the query."
        else:
            evaluation = "Partially Correct"
            rationale = "Answer is relevant but doesn't fully use the retrieved context."
    else:
        if any(keyword in retrieved_context for keyword in user_query.split()):
            evaluation = "Partially Correct"
            rationale = "answerFound is false but context has relevant info."
        else:
            evaluation = "Correct"
            rationale = "answerFound is false and context lacks necessary info."

    return {
        "evaluation": evaluation,
        "rationale": rationale
    }

demo = gr.Interface(
    fn=evaluate_output,
    inputs=[
        gr.Textbox(label="User Query"),
        gr.Textbox(label="Retrieved Context"),
        gr.Textbox(label="Model Output (finalAnswer)"),
        gr.Textbox(label="Answer Found (true/false)"),
    ],
    outputs="json",
    title="LLM Output Evaluator",
    description="Evaluate LLM responses based on context, query, and output quality."
)

if __name__ == "__main__":
    demo.launch()
