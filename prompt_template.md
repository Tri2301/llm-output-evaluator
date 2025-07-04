# LLM Output Evaluator – Prompt Template

## 🎯 Goal
To evaluate model outputs based on:
- User Query
- Retrieved Context
- Final Answer
- AnswerFound (true/false)

## 📌 Evaluation Rules
- If answerFound = true → Output must be fully supported by the retrieved context.
- If answerFound = false → Output should reflect missing info in context.

## ✅ Output Format

```json
{
  "evaluation": "Correct | Partially Correct | Incorrect",
  "rationale": "Why the score was given"
}
