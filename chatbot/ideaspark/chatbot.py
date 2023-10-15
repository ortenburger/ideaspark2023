import gradio as gr
import query

css='''
body {
    --block-background-fill: #49507E;
    --neutral-200: #F5F5FA;
    --neutral-500: #30B099;
    --neutral-700: #49507E;
    --button-secondary-background-fill: var(--neutral-500);
    --input-background-fill: var(--neutral-700);
    --border-color-primary: var(--neutral-500);
    --input-border-color: var(--neutral-500);
    --input-border-color-focus: var(--neutral-500);
    --background-fill-primary: var(--body-background-fill);
    --input-placeholder-color: grey;
    --block-title-text-color: #f3f4f6;
}

body:not(.dark) .form input {
    --body-text-color: #f3f4f6;
}

body.dark {
    --body-background-fill: #232952;
    --block-background-fill: #49507E;
    --neutral-200: #F5F5FA;
    --neutral-500: #30B099;
    --neutral-700: #49507E;
    --button-secondary-background-fill: var(--neutral-500);
    --input-background-fill: var(--neutral-700);
    --border-color-primary: var(--neutral-500);
    --input-border-color: var(--neutral-500);
    --input-border-color-focus: var(--neutral-500);
    --background-fill-primary: var(--body-background-fill);
    --input-placeholder-color: grey;
}
'''

examples=[
        ['Ist meine Drohne mitversichert?', 'Haftpflicht'],
        ['Zahlt meine Versicherung wenn meine Katze das Handy eines Besuchers vom Tisch stößt?', 'Tierhalterhaftpflicht'],
        ['Was passiert wenn mein Pferd vor einer Apotheke kotzt und darin ausrutscht?', 'Tierhalterhaftpflicht'],
        ['Was kann ich tun wenn ich in Thailand schlimmen Durchfall bekomme?', 'Auslandsreisekrankenversicherung'],
        ['Bekomme ich meinen Fernseher nach einem Flutschaden ersetzt?', 'Hausratversicherung'],
        ['Bekomme ich ein Ersatzgerät wenn ich mein Handy nach meinem Freund werfe?', 'Mobilgeraeteschutz'],
        ['Wie hoch ist die Deckung wenn ich in Dubai verklagt werde?', 'Rechtsschutz'],
        ['Was soll ich machen wenn ich beim Skifahren mein Bein breche?', 'Sorglos leben'],
        ['Durch einen Trojaner wurde mir mein Konto leergeräumt. Was soll ich tun?', 'Internetschutz']
]

def chatbot(input, policy):
    if input:
        return query.answer_query(input+('' if input.strip()[-1]=='?' else '?') +" Antworte auf deutsch.", f"ask_sv_police_{policy.lower().replace(' ', '-')}")["answer"]

#for collection_name,title, description, examples in [
#    ("ask_sv_haftpflicht_docs", "Haftpflicht Police", "Frag mich etwas ueber die SV Haftpflicht", [["Ist meine Drohne versichert", "Haftpflicht"],["Was passiert, wenn ich den Autoschluessel von meinem Freund verliere", "Haftpflicht"]])]:
#    policies=query.get_policies()
#    sv_demo = gr.ChatInterface(
#                fn=chatbot, examples=examples, title=title,
#                description="", additional_inputs=[
#                    gr.Dropdown(choices=policies, label='Police', value='Haftpflicht')
#                ])
#    print(title + ": {}\n".format(sv_demo.launch(debug=False, share=True)))

with gr.Blocks(title='inzure bot', css=css) as chatapp:
    gr.Markdown('''
    # inzure bot
    Stell mir eine Frage zu Deiner Versicherungspolice
    ''')
    policies=query.get_policies()
    policy=gr.Dropdown(choices=policies, label='Police', value='Haftpflicht')
    question=gr.Textbox(placeholder='Deine Frage', label='Anfrage')
    answer=gr.Textbox(lines=8, max_lines=50, label='Ergebnis Deiner Anfrage')
    btn=gr.Button('Senden')
    btn.click(fn=chatbot, inputs=[question, policy], outputs=answer)

    with gr.Row() as row:
        ex=gr.Examples(label='Beispiele', inputs=[question, policy], examples=examples)

chatapp.launch()
