#!/usr/bin/env python3
"""
Freelance Proposal Generator
Generates customized freelance proposals for zero-capital income platforms
"""

PROPOSAL_TEMPLATES = {
    "writing": {
        "title": "Professional Content Writer | AI + Crypto + Tech",
        "rate": "$0.05/word or $25/article",
        "description": """I'm an AI-powered content writer specializing in:
• Cryptocurrency & blockchain analysis
• AI agent automation tutorials
• DeFi protocol reviews
• Technical documentation

What I deliver:
✅ SEO-optimized articles (1000-3000 words)
✅ Original research & analysis
✅ Fast turnaround (24-48h)
✅ Unlimited revisions

I use AI to research and draft, then refine for quality and accuracy. This means faster delivery and lower costs for you.""",
        "portfolio": "https://github.com/a918124259a/ai-agent-income-kit"
    },
    "data_entry": {
        "title": "Data Entry & Research Specialist",
        "rate": "$15/hour",
        "description": """Fast, accurate data entry and research services:
• Web research & data collection
• Spreadsheet organization
• Lead generation
• Market analysis

AI-assisted for speed and accuracy.""",
    },
    "ai_prompts": {
        "title": "AI Prompt Engineer | Custom Prompt Packs",
        "rate": "$19-49/pack",
        "description": """Custom AI prompt packs for businesses:
• ChatGPT/Claude/Gemini prompts
• Industry-specific templates
• Workflow automation prompts
• Marketing copy prompts

Each pack includes 50+ tested prompts with instructions.""",
    }
}

def generate_proposal(platform, category, client_needs):
    """Generate a customized proposal"""
    template = PROPOSAL_TEMPLATES.get(category, PROPOSAL_TEMPLATES["writing"])
    
    proposal = f"""Hi there!

I saw your project and I'd love to help. Here's what I bring:

{template['description']}

**My rate:** {template['rate']}

**Portfolio:** {template.get('portfolio', 'N/A')}

I can start immediately and deliver high-quality work on time.

Looking forward to working with you!

Best,
Hermes AI Agent"""
    
    return proposal

if __name__ == "__main__":
    import sys
    category = sys.argv[1] if len(sys.argv) > 1 else "writing"
    print(generate_proposal("fiverr", category, ""))
