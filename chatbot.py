class StudyBot:
    def __init__(self):
        # Initialiser le pipeline de questions-réponses
        self.qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
        self.faqs = self.load_faqs()
        self.current_context = ""

    def load_faqs(self) -> Dict[str, str]:
        try:
            # Charger les FAQ (questions fréquemment posées) à partir d'un fichier JSON
            with open('faqs.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            # Si le fichier n'existe pas, retourner un dictionnaire vide
            return {}

    def answer_from_faq(self, question: str) -> str:
        # Recherche simple de mots-clés dans les FAQ
        question = question.lower()
        for q, a in self.faqs.items():
            if any(keyword in question for keyword in q.lower().split()):
                return a
        return None

    def answer_from_context(self, question: str) -> str:
        if not self.current_context:
            # Si aucun contexte n'a été fourni, demander d'abord de téléverser un document
            return "Veuillez d'abord téléverser un document pour répondre aux questions basées sur le contenu."
        
        # Utiliser le pipeline pour répondre à la question en fonction du contexte
        result = self.qa_pipeline(
            question=question,
            context=self.current_context
        )
        return result['answer']

    def set_context(self, text: str):
        # Définir le contexte pour répondre aux questions spécifiques
        self.current_context = text

    def get_answer(self, question: str) -> str:
        # Essayer d'abord de trouver une réponse dans les FAQ
        faq_answer = self.answer_from_faq(question)
        if faq_answer:
            return faq_answer
        
        # Si aucune correspondance dans les FAQ, essayer de répondre en fonction du contexte
        return self.answer_from_context(question)
