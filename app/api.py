from flask import Blueprint, jsonify, request
from .models.rule_based import RuleBasedGenerator

bp = Blueprint('api', __name__)

# Initialize generators
rule_based_generator = RuleBasedGenerator()

@bp.route('/generate', methods=['POST'])
def generate_tercet():
    """Generate a tercet based on the specified method and parameters."""
    data = request.get_json()
    method = data.get('method', 'rule_based')
    theme = data.get('theme')
    
    try:
        if method == 'rule_based':
            tercet = rule_based_generator.generate_tercet(theme=theme)
        else:
            return jsonify({'error': 'Invalid generation method'}), 400
            
        return jsonify({
            'tercet': tercet,
            'method': method
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/health', methods=['GET'])
def health_check():
    """Simple health check endpoint."""
    return jsonify({'status': 'healthy'})