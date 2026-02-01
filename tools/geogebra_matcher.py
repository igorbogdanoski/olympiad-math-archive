"""
GeoGebra Auto-Matcher - AI-powered matching of problems to GeoGebra applets
Uses Google Gemini to analyze problem text and suggest appropriate visualizations
"""

import os
import json
import re
from pathlib import Path
from typing import Dict, List, Optional
import google.generativeai as genai

class GeoGebraAutoMatcher:
    def __init__(self, api_key: Optional[str] = None):
        """Initialize matcher with Gemini API"""
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-1.5-pro')
        
        # Load GeoGebra library
        self.library = self._load_library()
        print(f"✅ Loaded {len(self.library)} GeoGebra materials")
    
    def _load_library(self) -> List[Dict]:
        """Load GeoGebra materials library"""
        library_path = Path(__file__).parent / "geogebra_library.json"
        
        if not library_path.exists():
            print(f"⚠️  Library not found at {library_path}")
            return []
        
        with open(library_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _extract_topics_from_text(self, text: str) -> List[str]:
        """Extract mathematical topics from problem text"""
        topics = []
        
        # Geometry keywords
        geometry_keywords = {
            'триаголник': 'triangles',
            'кружница': 'circle',
            'агол': 'angles',
            'паралелограм': 'parallelogram',
            'трапез': 'trapezoid',
            'ромб': 'rhombus',
            'квадрат': 'square',
            'правоаголник': 'rectangle',
            'височина': 'altitude',
            'медијана': 'median',
            'биссектриса': 'bisector',
            'тангент': 'tangent',
            'хорда': 'chord'
        }
        
        # Algebra keywords
        algebra_keywords = {
            'функција': 'functions',
            'равенка': 'equations',
            'систем': 'systems',
            'квадратна': 'quadratic',
            'линеарна': 'linear',
            'параблола': 'parabola',
            'график': 'graph'
        }
        
        text_lower = text.lower()
        
        # Check geometry
        for mk_word, eng_topic in geometry_keywords.items():
            if mk_word in text_lower:
                topics.append(eng_topic)
                if 'geometry' not in topics:
                    topics.append('geometry')
        
        # Check algebra
        for mk_word, eng_topic in algebra_keywords.items():
            if mk_word in text_lower:
                topics.append(eng_topic)
                if 'algebra' not in topics:
                    topics.append('algebra')
        
        return list(set(topics))
    
    def _format_library_for_prompt(self, topics: List[str] = None) -> str:
        """Format library materials for AI prompt"""
        materials = self.library
        
        # Filter by topics if provided
        if topics:
            materials = [
                m for m in materials 
                if any(t in m.get('topics', []) for t in topics)
            ]
        
        if not materials:
            return "Нема достапни GeoGebra материјали за овие теми."
        
        formatted = []
        for mat in materials:
            formatted.append(f"""
ID: {mat['id']}
Наслов: {mat['title_mk']}
Теми: {', '.join(mat['topics'])}
Одделение: {mat['grade_range'][0]}-{mat['grade_range'][1]}
Опис: {mat['description']}
БРО Стандарди: {', '.join(mat.get('bro_codes', []))}
---""")
        
        return '\n'.join(formatted)
    
    def match_problem(self, problem_text: str, metadata: Dict) -> Dict:
        """
        Match a problem to the best GeoGebra applet using AI
        
        Args:
            problem_text: Full problem statement in Macedonian
            metadata: Dict with grade, topic, difficulty, bro_standard
        
        Returns:
            {
                "material_id": str or None,
                "confidence": float (0.0-1.0),
                "reason": str,
                "alternatives": List[str]
            }
        """
        # Extract topics from text
        detected_topics = self._extract_topics_from_text(problem_text)
        
        # Build AI prompt
        prompt = f"""Ти си експерт за GeoGebra и македонска математичка едукација.

## ЗАДАЧА ЗА МАПИРАЊЕ:
Текст: {problem_text[:500]}...  # First 500 chars
Одделение: {metadata.get('grade', 'Непознато')}
Тема: {metadata.get('topic', 'Непознато')}
Тежина: {metadata.get('difficulty', 'Непознато')}
БРО Стандард: {metadata.get('bro_standard', 'Непознато')}

## ДЕТЕКТИРАНИ ТЕМИ:
{', '.join(detected_topics) if detected_topics else 'Непознато'}

## ДОСТАПНИ GEOGEBRA МАТЕРИЈАЛИ:
{self._format_library_for_prompt(detected_topics)}

## ТВОЈА ЗАДАЧА:
Најди го НАЈДОБРИОТ GeoGebra аплет за оваа задача.

Критериуми:
1. Совпаѓање на тема (геометрија, алгебра, итн.)
2. Соодветност за одделение
3. Ниво на интерактивност
4. Поддршка за македонски јазик
5. Alignment со БРО стандарди

Врати JSON одговор во следниов формат:
{{
  "material_id": "ID од погоре" или null,
  "confidence": 0.0-1.0,
  "reason": "Зошто е ова добар избор (на македонски)",
  "alternatives": ["id1", "id2"] # Алтернативни опции
}}

Ако НЕМА добар match, врати:
{{
  "material_id": null,
  "confidence": 0.0,
  "reason": "Зошто нема добар match",
  "custom_suggestion": "Што треба да содржи custom аплет"
}}

ВАЖНО: Врати САМО JSON, без дополнителен текст.
"""
        
        try:
            # Call Gemini API
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.3,
                    top_p=0.8,
                    top_k=40,
                    max_output_tokens=1024,
                )
            )
            
            # Parse JSON response
            response_text = response.text.strip()
            
            # Remove markdown code blocks if present
            if response_text.startswith('```'):
                response_text = re.sub(r'```json\n?|```\n?', '', response_text)
            
            result = json.loads(response_text)
            
            # Validate result
            if 'material_id' not in result:
                result['material_id'] = None
            if 'confidence' not in result:
                result['confidence'] = 0.0
            if 'reason' not in result:
                result['reason'] = "Непознато"
            if 'alternatives' not in result:
                result['alternatives'] = []
            
            return result
            
        except json.JSONDecodeError as e:
            print(f"❌ JSON parse error: {e}")
            print(f"Response: {response.text}")
            return {
                "material_id": None,
                "confidence": 0.0,
                "reason": "Грешка при обработка на AI одговор",
                "alternatives": [],
                "error": str(e)
            }
        except Exception as e:
            print(f"❌ Error: {e}")
            return {
                "material_id": None,
                "confidence": 0.0,
                "reason": f"Грешка: {str(e)}",
                "alternatives": [],
                "error": str(e)
            }
    
    def batch_process(self, problems: List[Dict], output_file: str = "geogebra_matches.json"):
        """
        Batch process multiple problems
        
        Args:
            problems: List of problem dicts from problems.json
            output_file: Where to save results
        """
        results = []
        
        for i, problem in enumerate(problems, 1):
            print(f"\n[{i}/{len(problems)}] Processing: {problem.get('meta', {}).get('problem_id', 'Unknown')}")
            
            # Extract text and metadata
            problem_text = problem.get('body', '')
            metadata = {
                'grade': problem.get('grade', ''),
                'topic': problem.get('meta', {}).get('topic', ''),
                'difficulty': problem.get('difficulty', ''),
                'bro_standard': problem.get('meta', {}).get('bro_standard', '')
            }
            
            # Match
            match_result = self.match_problem(problem_text, metadata)
            
            # Store result
            results.append({
                "problem_id": problem.get('meta', {}).get('problem_id', ''),
                "filename": problem.get('filename', ''),
                "match": match_result
            })
            
            # Print result
            if match_result['material_id']:
                print(f"  ✅ Match: {match_result['material_id']} (Confidence: {match_result['confidence']:.2f})")
                print(f"  📝 {match_result['reason']}")
            else:
                print(f"  ⚠️  No match found")
                print(f"  📝 {match_result['reason']}")
        
        # Save results
        output_path = Path(__file__).parent / output_file
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ Results saved to: {output_path}")
        
        # Statistics
        matched = sum(1 for r in results if r['match']['material_id'])
        high_confidence = sum(1 for r in results if r['match']['confidence'] >= 0.7)
        
        print(f"\n📊 Statistics:")
        print(f"  Total processed: {len(results)}")
        print(f"  Matched: {matched} ({matched/len(results)*100:.1f}%)")
        print(f"  High confidence (≥0.7): {high_confidence} ({high_confidence/len(results)*100:.1f}%)")
        
        return results


if __name__ == "__main__":
    # Test with sample problems
    matcher = GeoGebraAutoMatcher()
    
    # Sample test problem
    test_problem = {
        'body': """Во триаголник ABC, височините AD, BE и CF се сечат во точката H.
        Докажете дека AH · HD = BH · HE = CH · HF.""",
        'meta': {
            'problem_id': 'test_001',
            'topic': 'geometry',
            'bro_standard': 'МАТ.8.Г.2'
        },
        'grade': '8',
        'difficulty': 'hard'
    }
    
    print("🧪 Test matching:")
    result = matcher.match_problem(test_problem['body'], {
        'grade': test_problem['grade'],
        'topic': test_problem['meta']['topic'],
        'difficulty': test_problem['difficulty'],
        'bro_standard': test_problem['meta']['bro_standard']
    })
    
    print(f"\n✅ Result: {json.dumps(result, ensure_ascii=False, indent=2)}")
