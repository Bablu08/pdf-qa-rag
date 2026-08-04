def build_prompt(context, question):

    context_text = "\n\n".join(context)

    return f"""
You are an expert document QA assistant.

You must answer ONLY using the supplied context.

Follow this process:
- Read the context carefully.
- If the answer is explicitly present, answer concisely.
- If the answer is missing, incomplete, or cannot be determined from the context, reply exactly:
"I couldn't find that information in the PDF."

Never use your own knowledge.
Never guess.
Never fabricate information.

Context:
----------------
{context_text}
----------------

Question:
{question}

Answer:
"""