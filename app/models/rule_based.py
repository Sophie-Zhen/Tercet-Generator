import random
import os
from typing import List, Dict, Optional

class RuleBasedGenerator:
    def __init__(self, data_dir: str = None):
        if data_dir is None:
            data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data')
        
        self.data_dir = data_dir
        self.templates = self._load_templates()
        self.word_bank = self._load_word_bank()

    def _load_templates(self) -> List[str]:
        """Load tercet templates from the templates file."""
        template_path = os.path.join(self.data_dir, 'templates', 'basic_templates.txt')
        try:
            with open(template_path, 'r') as f:
                # Split on double newlines to separate tercets
                templates = f.read().strip().split('\n\n')
            return templates
        except FileNotFoundError:
            print(f"Warning: Template file not found at {template_path}")
            return [
                "{adjective} {noun} {verb}\n{adjective} {noun} {adverb}\n{adjective} {noun} {verb}"
            ]

    def _load_word_bank(self) -> Dict[str, List[str]]:
        """Load word categories from the knowledge base."""
        word_bank = {}
        categories = ['adjectives', 'nouns', 'verbs', 'adverbs']
        
        for category in categories:
            singular = category[:-1]  # Remove 's' to get singular form
            file_path = os.path.join(self.data_dir, 'poetry_kb', f'{category}.txt')
            try:
                with open(file_path, 'r') as f:
                    words = [line.strip() for line in f if line.strip()]
                word_bank[singular] = words
            except FileNotFoundError:
                print(f"Warning: Word bank file not found at {file_path}")
                word_bank[singular] = ["default"]
        
        return word_bank

    def generate_tercet(self, theme: Optional[str] = None) -> str:
        """Generate a tercet using templates and word bank."""
        template = random.choice(self.templates)
        
        # Fill in the template with random words from appropriate categories
        filled_template = template
        for category in self.word_bank:
            while "{" + category + "}" in filled_template:
                word = random.choice(self.word_bank[category])
                filled_template = filled_template.replace(
                    "{" + category + "}", word, 1
                )
        
        return filled_template

    def add_template(self, template: str) -> None:
        """Add a new template to the generator."""
        if all(tag in template for tag in ["{noun}", "{verb}"]):
            self.templates.append(template)

    def add_words(self, category: str, words: List[str]) -> None:
        """Add new words to a category in the word bank."""
        if category in self.word_bank:
            self.word_bank[category].extend(words)